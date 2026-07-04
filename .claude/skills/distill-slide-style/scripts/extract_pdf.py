#!/usr/bin/env python3
"""Batch-extract structural profiles from .pdf files (pdfplumber).

Usage:
    extract_pdf.py <samples-dir> [--cache-dir .distill-cache/raw]

Mirrors extract_pptx.py: same cache-by-hash behaviour, same raw JSON shape
per page, so distill-slide-style step 2's profiling prompt can treat PPT
and PDF sources uniformly. Chart-vs-picture cannot be distinguished from
PDF structure alone — has_chart is always False here and gets flagged for
manual review in the profile step if a page looks chart-like. has_table
uses pdfplumber's default line-based detector, which is known to
false-positive on pages with aligned text blocks that aren't real tables
— treat table counts as a weaker signal than the pptx script's, which
reads the actual shape type. image_count/images can run 10-20x higher
per page than the pptx script's picture counts for a visually similar
deck — pdfplumber's page.images enumerates every embedded raster XObject
(icons, logo fragments, background textures), not just user-placed
photos/screenshots the way the pptx script's shape_type==13 check does.
Don't compare raw image counts across formats; the position/caption
breakdown is still meaningful within a single format.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

import pdfplumber

LAYOUT_KEYWORDS = {
    "toc": ("agenda", "contents", "目录", "议程"),
    "closing": ("thank you", "谢谢", "q&a", "questions"),
}

CITATION_KEYWORDS = (
    "数据来源", "资料来源", "图片来源", "来源：", "来源:", "引用自", "参考来源",
    "source:", "source :",
)


def classify_image_position(img, page_w, page_h) -> dict:
    coverage = (img["width"] * img["height"]) / (page_w * page_h)
    if coverage > 0.8:
        return {"zone": "full-bleed", "coverage": round(coverage, 2)}
    cx = (img["x0"] + img["x1"]) / 2 / page_w
    cy = (img["top"] + img["bottom"]) / 2 / page_h
    horiz = "left" if cx < 0.33 else ("right" if cx > 0.67 else "center")
    vert = "top" if cy < 0.33 else ("bottom" if cy > 0.67 else "middle")
    return {"zone": f"{vert}-{horiz}", "coverage": round(coverage, 2)}


def find_caption(img, words, page_h) -> str:
    """Words directly beneath the image, within a small margin, count as a caption."""
    margin = page_h * 0.05
    below = [
        w for w in words
        if img["bottom"] <= w["top"] <= img["bottom"] + margin
        and not (w["x1"] < img["x0"] or w["x0"] > img["x1"])
    ]
    if not below:
        return ""
    below.sort(key=lambda w: (w["top"], w["x0"]))
    return " ".join(w["text"] for w in below)[:80]


def find_citations(text: str) -> list:
    lowered = text.lower()
    hits = []
    for kw in CITATION_KEYWORDS:
        idx = lowered.find(kw.lower())
        if idx != -1:
            hits.append({"keyword": kw, "snippet": text[max(0, idx - 10):idx + 90].strip()})
    return hits


def classify_page(text: str, font_sizes: list, shape_count: int) -> str:
    lowered = text.lower()
    for label, keywords in LAYOUT_KEYWORDS.items():
        if any(k in lowered for k in keywords):
            return label
    if shape_count <= 2 and len(text) < 40:
        return "title"
    return "content"


def rgb_hex_from_pdf_color(color):
    # Only handles RGB color space; CMYK/grayscale chars are skipped rather
    # than guessed at.
    if isinstance(color, (list, tuple)) and len(color) == 3:
        r, g, b = (int(round(c * 255)) for c in color)
        return f"{r:02X}{g:02X}{b:02X}"
    return None


def extract_page(page) -> dict:
    chars = page.chars
    font_sizes = [round(c["size"], 1) for c in chars]
    fonts = [c["fontname"] for c in chars]
    colors = [rgb_hex_from_pdf_color(c.get("non_stroking_color")) for c in chars]
    colors = [c for c in colors if c]
    text = page.extract_text() or ""
    images = page.images
    words = page.extract_words()
    image_details = []
    for img in images:
        position = classify_image_position(img, page.width, page.height)
        caption = find_caption(img, words, page.height)
        image_details.append({**position, "captioned": bool(caption), "caption": caption})

    return {
        "shape_count": len(words),
        "has_chart": False,
        "has_table": bool(page.find_tables()),
        "has_picture": len(images) > 0,
        "image_count": len(images),
        "images": image_details,
        "citations": find_citations(text),
        "colors": colors,
        "fonts": fonts,
        "font_sizes": font_sizes,
        "char_count": len(text),
        "layout_type": classify_page(text, font_sizes, len(words)),
    }


def extract_profile(path: Path) -> dict:
    with pdfplumber.open(str(path)) as pdf:
        pages = [extract_page(p) for p in pdf.pages]
    return {"source": path.name, "slide_count": len(pages), "slides": pages}


def content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples_dir", type=Path)
    parser.add_argument("--cache-dir", type=Path, default=Path(".distill-cache/raw"))
    args = parser.parse_args()

    args.cache_dir.mkdir(parents=True, exist_ok=True)
    pdf_files = sorted(args.samples_dir.rglob("*.pdf"))
    if not pdf_files:
        print(f"No .pdf files found under {args.samples_dir}", file=sys.stderr)
        sys.exit(1)

    extracted = skipped = 0
    for path in pdf_files:
        h = content_hash(path)
        out_path = args.cache_dir / f"{h}.json"
        if out_path.exists():
            skipped += 1
            continue
        profile = extract_profile(path)
        profile["hash"] = h
        out_path.write_text(json.dumps(profile, ensure_ascii=False, indent=2))
        extracted += 1

    print(f"Extracted {extracted}, skipped {skipped} (unchanged) of {len(pdf_files)} files.")


if __name__ == "__main__":
    main()
