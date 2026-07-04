#!/usr/bin/env python3
"""Batch-extract structural profiles from .pptx files.

Usage:
    extract_pptx.py <samples-dir> [--cache-dir .distill-cache/raw]

For each .pptx under <samples-dir>, computes a content hash and skips
extraction if a matching cache file already exists — this is what makes
distill-slide-style step 1 incremental across repeated runs. Writes one
JSON file per sample.
"""
import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE, PP_PLACEHOLDER

TITLE_PLACEHOLDER_TYPES = (PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE)

LAYOUT_KEYWORDS = {
    "toc": ("agenda", "contents", "目录", "议程"),
    "closing": ("thank you", "谢谢", "q&a", "questions"),
}

CITATION_KEYWORDS = (
    "数据来源", "资料来源", "图片来源", "来源：", "来源:", "引用自", "参考来源",
    "source:", "source :",
)

BRANDING_KEYWORDS = (
    "机密", "保密", "版权所有", "confidential", "copyright", "proprietary",
)

DIAGRAM_SHAPE_TYPES = (
    MSO_SHAPE_TYPE.AUTO_SHAPE, MSO_SHAPE_TYPE.PICTURE, MSO_SHAPE_TYPE.FREEFORM,
)
# GROUP is deliberately excluded: flatten_shapes() already descends into a
# group's children individually, so counting the group's own bounding box
# too would double-count the same visual content at two granularities.


def flatten_shapes(shapes, transform=None):
    """Yield (shape, abs_left, abs_top, abs_width, abs_height) for every shape,
    recursing into GROUP shapes.

    A shape's own .left/.top/.width/.height are in its immediate parent's
    coordinate space, not the slide's -- for a top-level shape that's the
    same thing, but for a shape nested inside a GROUP it's relative to the
    group's child coordinate space (<a:chOff>/<a:chExt>), which can be
    offset and scaled arbitrarily relative to the group's own on-slide
    position/size. Trusting a nested shape's raw .left/.top silently
    misreports its real position (or, worse, silently drops all content
    inside groups if callers only ever look at slide.shapes directly --
    groups are common in decks with copy-pasted/precomposed graphics).
    transform is (offset_x, offset_y, scale_x, scale_y) composed from all
    enclosing groups; None means top-level (identity).
    """
    for shape in shapes:
        if shape.left is None:
            continue
        if transform is None:
            abs_left, abs_top, abs_width, abs_height = shape.left, shape.top, shape.width, shape.height
        else:
            off_x, off_y, sx, sy = transform
            abs_left = off_x + shape.left * sx
            abs_top = off_y + shape.top * sy
            abs_width = shape.width * sx
            abs_height = shape.height * sy
        yield shape, abs_left, abs_top, abs_width, abs_height
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            xfrm = shape._element.grpSpPr.xfrm
            ch_ext_cx = xfrm.chExt.cx or 1
            ch_ext_cy = xfrm.chExt.cy or 1
            child_scale_x = abs_width / ch_ext_cx
            child_scale_y = abs_height / ch_ext_cy
            child_offset_x = abs_left - xfrm.chOff.x * child_scale_x
            child_offset_y = abs_top - xfrm.chOff.y * child_scale_y
            yield from flatten_shapes(shape.shapes, (child_offset_x, child_offset_y, child_scale_x, child_scale_y))


def authoring_tool(path: Path) -> str:
    """PowerPoint writes docProps/app.xml with an <Application> tag; exporters
    from other tools (Google Slides, Keynote, ...) typically omit it and use
    generic shape names instead -- both are useful, independent signals."""
    with zipfile.ZipFile(path) as z:
        if "docProps/app.xml" in z.namelist():
            app_xml = z.read("docProps/app.xml").decode("utf-8", "ignore")
            if "<Application>" in app_xml:
                start = app_xml.index("<Application>") + len("<Application>")
                end = app_xml.index("</Application>", start)
                return app_xml[start:end]
    return "unknown (no docProps/app.xml — likely exported from a non-PowerPoint tool)"


def cluster(values: list, tolerance: float) -> list:
    values = sorted(values)
    clusters = []
    for v in values:
        if clusters and abs(v - clusters[-1][-1]) < tolerance:
            clusters[-1].append(v)
        else:
            clusters.append([v])
    return clusters


def classify_diagram_geometry(flat_shapes, slide_w, slide_h):
    """Rough geometric descriptor for non-text decorative shapes (icons,
    autoshapes, freeform diagram parts) -- reports row/column clustering,
    not a semantic diagram type. Step 2 profiling should interpret this
    alongside the slide's title/text to name the actual diagram convention
    (matrix, process, pyramid, ...) -- this heuristic can't distinguish a
    pyramid's tapering from a plain grid on its own. flat_shapes entries
    are (shape, abs_left, abs_top, abs_width, abs_height)."""
    candidates = [f for f in flat_shapes if f[0].shape_type in DIAGRAM_SHAPE_TYPES]
    if len(candidates) < 3:
        return None
    lefts = [left / slide_w for _, left, _, _, _ in candidates]
    tops = [top / slide_h for _, _, top, _, _ in candidates]
    n_cols = len(cluster(lefts, 0.05))
    n_rows = len(cluster(tops, 0.05))
    if n_rows == 1 and n_cols > 1:
        arrangement = "horizontal-sequence"
    elif n_cols == 1 and n_rows > 1:
        arrangement = "vertical-stack"
    elif n_rows > 1 and n_cols > 1:
        arrangement = "grid"
    else:
        arrangement = "cluster"
    return {"shape_count": len(candidates), "rows": n_rows, "cols": n_cols, "arrangement": arrangement}


def classify_image_position(left, top, width, height, slide_w, slide_h) -> dict:
    coverage = (width * height) / (slide_w * slide_h)
    if coverage > 0.8:
        return {"zone": "full-bleed", "coverage": round(coverage, 2)}
    cx = (left + width / 2) / slide_w
    cy = (top + height / 2) / slide_h
    horiz = "left" if cx < 0.33 else ("right" if cx > 0.67 else "center")
    vert = "top" if cy < 0.33 else ("bottom" if cy > 0.67 else "middle")
    return {"zone": f"{vert}-{horiz}", "coverage": round(coverage, 2)}


def find_caption(pic_left, pic_top, pic_width, pic_height, flat_shapes, slide_h) -> str:
    """A text shape directly beneath the picture, within a small margin, counts as a caption."""
    pic_right, pic_bottom = pic_left + pic_width, pic_top + pic_height
    margin = slide_h * 0.05
    for shape, left, top, width, height in flat_shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        text = shape.text_frame.text.strip()
        if not text:
            continue
        horiz_overlap = not (left + width < pic_left or left > pic_right)
        below_picture = pic_bottom <= top <= pic_bottom + margin
        if horiz_overlap and below_picture:
            return text[:80]
    return ""


def find_keyword_hits(shapes, keywords) -> list:
    hits = []
    for shape in shapes:
        if not getattr(shape, "has_text_frame", False):
            continue
        text = shape.text_frame.text
        lowered = text.lower()
        for kw in keywords:
            if kw.lower() in lowered:
                hits.append({"keyword": kw, "snippet": text.strip()[:100]})
                break
    return hits


def classify_slide(shape_count: int, text: str, has_chart: bool, has_table: bool) -> str:
    if has_chart:
        return "chart"
    if has_table:
        return "content"
    lowered = text.lower()
    for label, keywords in LAYOUT_KEYWORDS.items():
        if any(k in lowered for k in keywords):
            return label
    if shape_count <= 2 and len(text) < 40:
        return "title"
    return "content"


def rgb_hex(color_format):
    try:
        if color_format.type is not None:
            return str(color_format.rgb)
    except (AttributeError, TypeError, ValueError):
        pass
    return None


def extract_slide(slide, slide_w, slide_h) -> dict:
    top_shapes = list(slide.shapes)
    # Placeholders are only ever meaningful at the top level -- a shape
    # nested inside a GROUP isn't part of the layout's placeholder scheme.
    placeholders = []
    placeholder_title = None
    title_shape = None
    for shape in top_shapes:
        if getattr(shape, "is_placeholder", False):
            entry = {"type": str(shape.placeholder_format.type)}
            if shape.left is not None:
                entry["position"] = {
                    "left": round(shape.left / slide_w, 3),
                    "top": round(shape.top / slide_h, 3),
                    "width": round(shape.width / slide_w, 3),
                    "height": round(shape.height / slide_h, 3),
                }
            placeholders.append(entry)
            if (
                placeholder_title is None
                and shape.placeholder_format.type in TITLE_PLACEHOLDER_TYPES
                and getattr(shape, "has_text_frame", False)
            ):
                placeholder_title = shape.text_frame.text.strip()[:80]
                title_shape = shape

    # Everything else (text, color, images, diagrams, citations) recurses
    # into GROUP shapes -- a deck built from precomposed/copy-pasted
    # graphics can have most or all of its real content nested inside
    # groups, and a flat slide.shapes scan would silently see none of it.
    flat = list(flatten_shapes(top_shapes))

    colors, fonts, font_sizes, texts = [], [], [], []
    sized_texts = []  # (size_pt, text) pairs — fallback title guess if there's no title placeholder
    has_chart = has_table = has_picture = False
    chart_type = None
    images = []
    content_paragraphs = 0

    for shape, left, top, width, height in flat:
        if getattr(shape, "has_chart", False):
            has_chart = True
            try:
                chart_type = str(shape.chart.chart_type)
            except Exception:
                pass
        if getattr(shape, "has_table", False):
            has_table = True
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            has_picture = True
            position = classify_image_position(left, top, width, height, slide_w, slide_h)
            caption = find_caption(left, top, width, height, flat, slide_h)
            images.append({**position, "captioned": bool(caption), "caption": caption})
        try:
            fill_color = rgb_hex(shape.fill.fore_color)
            if fill_color:
                colors.append(fill_color)
        except (AttributeError, TypeError, ValueError):
            pass
        if getattr(shape, "has_text_frame", False):
            for para in shape.text_frame.paragraphs:
                if shape is not title_shape and para.text.strip():
                    content_paragraphs += 1
                for run in para.runs:
                    if run.font.size:
                        font_sizes.append(run.font.size.pt)
                    if run.font.name:
                        fonts.append(run.font.name)
                    color = rgb_hex(run.font.color)
                    if color:
                        colors.append(color)
                    if run.text:
                        texts.append(run.text)
                        size_pt = run.font.size.pt if run.font.size else 0
                        sized_texts.append((size_pt, run.text.strip()))

    text = " ".join(texts).strip()
    if placeholder_title:
        title_text = placeholder_title
    elif sized_texts:
        title_text = max(sized_texts, key=lambda st: st[0])[1][:80]
    else:
        title_text = ""
    all_shapes = [f[0] for f in flat]
    return {
        "shape_count": len(flat),
        "has_chart": has_chart,
        "chart_type": chart_type,
        "has_table": has_table,
        "has_picture": has_picture,
        "images": images,
        "placeholders": placeholders,
        "citations": find_keyword_hits(all_shapes, CITATION_KEYWORDS),
        "branding_markers": find_keyword_hits(all_shapes, BRANDING_KEYWORDS),
        "content_paragraph_count": content_paragraphs,
        "diagram_geometry": classify_diagram_geometry(flat, slide_w, slide_h),
        "colors": colors,
        "fonts": fonts,
        "font_sizes": font_sizes,
        "char_count": len(text),
        "title_text": title_text,
        "layout_type": classify_slide(len(flat), text, has_chart, has_table),
    }


def extract_profile(path: Path) -> dict:
    prs = Presentation(str(path))
    slide_w, slide_h = prs.slide_width, prs.slide_height
    slides = [extract_slide(s, slide_w, slide_h) for s in prs.slides]
    return {
        "source": path.name,
        "authoring_tool": authoring_tool(path),
        "slide_count": len(slides),
        "slides": slides,
    }


def content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples_dir", type=Path)
    parser.add_argument("--cache-dir", type=Path, default=Path(".distill-cache/raw"))
    args = parser.parse_args()

    args.cache_dir.mkdir(parents=True, exist_ok=True)
    pptx_files = sorted(args.samples_dir.rglob("*.pptx"))
    if not pptx_files:
        print(f"No .pptx files found under {args.samples_dir}", file=sys.stderr)
        sys.exit(1)

    extracted = skipped = 0
    for path in pptx_files:
        h = content_hash(path)
        out_path = args.cache_dir / f"{h}.json"
        if out_path.exists():
            skipped += 1
            continue
        profile = extract_profile(path)
        profile["hash"] = h
        out_path.write_text(json.dumps(profile, ensure_ascii=False, indent=2))
        extracted += 1

    print(f"Extracted {extracted}, skipped {skipped} (unchanged) of {len(pptx_files)} files.")


if __name__ == "__main__":
    main()
