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
from pathlib import Path

from pptx import Presentation

LAYOUT_KEYWORDS = {
    "toc": ("agenda", "contents", "目录", "议程"),
    "closing": ("thank you", "谢谢", "q&a", "questions"),
}


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


def extract_slide(slide) -> dict:
    shapes = list(slide.shapes)
    colors, fonts, font_sizes, texts = [], [], [], []
    has_chart = has_table = has_picture = False
    chart_type = None

    for shape in shapes:
        if getattr(shape, "has_chart", False):
            has_chart = True
            try:
                chart_type = str(shape.chart.chart_type)
            except Exception:
                pass
        if getattr(shape, "has_table", False):
            has_table = True
        if shape.shape_type == 13:  # MSO_SHAPE_TYPE.PICTURE
            has_picture = True
        try:
            fill_color = rgb_hex(shape.fill.fore_color)
            if fill_color:
                colors.append(fill_color)
        except (AttributeError, ValueError):
            pass
        if getattr(shape, "has_text_frame", False):
            for para in shape.text_frame.paragraphs:
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

    text = " ".join(texts).strip()
    return {
        "shape_count": len(shapes),
        "has_chart": has_chart,
        "chart_type": chart_type,
        "has_table": has_table,
        "has_picture": has_picture,
        "colors": colors,
        "fonts": fonts,
        "font_sizes": font_sizes,
        "word_count": len(text),
        "layout_type": classify_slide(len(shapes), text, has_chart, has_table),
    }


def extract_profile(path: Path) -> dict:
    prs = Presentation(str(path))
    slides = [extract_slide(s) for s in prs.slides]
    return {"source": path.name, "slide_count": len(slides), "slides": slides}


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
