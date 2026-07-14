#!/usr/bin/env python3
"""Structural fidelity gate for fidelity / mirror template pages.

Compares each generated ``svg_output/`` page against the ``templates/`` SVG it
declares in ``spec_lock.md`` ``page_layouts``, using a **skin-invariant** grid
occupancy metric: it asks "is each region as visually filled as the template
said it should be?" rather than "are the pixels identical?".

Why occupancy and not a raw pixel diff
--------------------------------------
Fidelity templates supply *structure, not skin* (``executor-base.md``): the
Executor legitimately swaps the template's placeholder colors and text for the
deck's own palette and real content. A raw RGB diff would flag that intended
re-skin as a failure. Occupancy is skin-free — a red box and a blue box are
both "inked" — so recoloring passes, while a genuine structural collapse (a
dense framework diagram flattened into a few plain boxes, the "骨架图" failure
this gate exists to catch) shows up as regions that were inked in the template
but are near-empty in the output.

Scope
-----
Only meaningful for ``fidelity`` / ``mirror`` templates, where a real visual
reference exists. ``standard`` templates define only header/footer (content is
free), so this gate does not apply to them. Pages with no ``page_layouts``
entry are free design and are skipped. If no SVG→PNG renderer is available the
gate refuses to run (exit 2) rather than reporting a hollow pass.

Ad-hoc pairwise mode (``--pair``)
---------------------------------
Everything above assumes a whole project with ``spec_lock.md`` / ``page_layouts``.
``--pair`` is a lighter, project-independent mode for the Layout Reference
mechanism (see ``docs/agents/ppt-master-layout-reference.md``): compare one
generated SVG page directly against one user-supplied reference (an image, or
one page of a PDF), optionally restricted to a cropped region of both. It
reuses the same ``compare_page()`` occupancy comparison — no new metric, just
a different way to supply the two sides.

Exit codes: 0 = all compared pages pass · 1 = at least one page fails ·
2 = cannot run (no renderer, or nothing to compare).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ── SVG → PNG renderer detection (same preference order as
#    svg_to_pptx/pptx_package/media.py, inlined here to avoid pulling in the
#    python-pptx dependency of that package) ───────────────────────────────
_PNG_RENDERER: Optional[str] = None
try:
    import cairosvg  # type: ignore
    _PNG_RENDERER = "cairosvg"
except (ImportError, OSError):
    try:
        from svglib.svglib import svg2rlg  # type: ignore
        from reportlab.graphics import renderPM  # type: ignore
        _PNG_RENDERER = "svglib"
    except (ImportError, OSError):
        pass

# PDF page rasterization for --pair mode, same library ppt-master's own
# source_to_md/pdf_to_md.py already depends on — kept optional here too so a
# missing fitz only blocks --pair with a PDF reference, not the whole script.
try:
    import fitz  # type: ignore  # PyMuPDF
    _HAVE_FITZ = True
except ImportError:
    _HAVE_FITZ = False


def _render_svg_to_png(svg_path: Path, png_path: Path, width: int, height: int) -> bool:
    if _PNG_RENDERER == "cairosvg":
        try:
            cairosvg.svg2png(
                url=str(svg_path), write_to=str(png_path),
                output_width=width, output_height=height,
            )
            return True
        except Exception as exc:  # noqa: BLE001
            print(f"  [warn] cairosvg failed on {svg_path.name}: {exc}")
            return False
    if _PNG_RENDERER == "svglib":
        try:
            drawing = svg2rlg(str(svg_path))
            if drawing is None:
                return False
            renderPM.drawToFile(drawing, str(png_path), fmt="PNG")
            return True
        except Exception as exc:  # noqa: BLE001
            print(f"  [warn] svglib failed on {svg_path.name}: {exc}")
            return False
    return False


def _parse_page_layouts(lock_path: Path) -> Dict[str, str]:
    """Return {P<NN>: basename} from spec_lock.md ``## page_layouts``."""
    layouts: Dict[str, str] = {}
    current: Optional[str] = None
    for raw in lock_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            current = line[3:].strip()
            continue
        if current != "page_layouts":
            continue
        m = re.match(r"^-\s+([A-Za-z0-9_]+)\s*:\s*(.+?)\s*$", line)
        if m:
            layouts[m.group(1)] = m.group(2).strip()
    return layouts


def _detect_replication_mode(project: Path) -> Optional[str]:
    """Read ``replication_mode`` from the template's design_spec.md frontmatter."""
    for candidate in (project / "templates" / "design_spec.md",
                      project / "design_spec.md"):
        if not candidate.is_file():
            continue
        text = candidate.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^replication_mode:\s*([A-Za-z0-9_]+)", text, re.MULTILINE)
        if m:
            return m.group(1).strip().lower()
    return None


def _load_rgb(png_path: Path):
    from PIL import Image  # local import; optional dependency
    import numpy as np
    with Image.open(png_path) as im:
        arr = np.asarray(im.convert("RGB"), dtype=np.int16)
    return arr


def _background_rgb(arr):
    """Estimate the page background as the most common (quantized) color.

    The dominant color of a slide is its background surface. Corner sampling is
    unreliable — a full-width header bar puts the top corners on the header, not
    the background — so use the whole-image mode instead.
    """
    import numpy as np
    q = ((arr // 8) * 8).reshape(-1, 3)
    colors, counts = np.unique(q, axis=0, return_counts=True)
    return colors[counts.argmax()].astype(float)


def _ink_mask(arr, ink_threshold: float):
    """Boolean map of 'inked' pixels = far enough from the page background."""
    import numpy as np
    bg = _background_rgb(arr)
    dist = np.sqrt(((arr - bg) ** 2).sum(axis=2))
    return dist > ink_threshold


def _occupancy_grid(mask, cols: int, rows: int):
    """Per-cell fraction of inked pixels → (rows, cols) float array."""
    import numpy as np
    h, w = mask.shape
    grid = np.zeros((rows, cols), dtype=float)
    for r in range(rows):
        y0, y1 = r * h // rows, (r + 1) * h // rows
        for c in range(cols):
            x0, x1 = c * w // cols, (c + 1) * w // cols
            cell = mask[y0:y1, x0:x1]
            grid[r, c] = float(cell.mean()) if cell.size else 0.0
    return grid


def compare_page(
    template_png: Path,
    generated_png: Path,
    *,
    cols: int,
    rows: int,
    ink_threshold: float,
    tolerance: float,
    min_cell_ink: float,
    mirror: bool,
    mirror_tolerance: float,
) -> Dict:
    """Compare one page. Returns a result dict (see keys below)."""
    import numpy as np
    t_arr = _load_rgb(template_png)
    g_arr = _load_rgb(generated_png)

    t_occ = _occupancy_grid(_ink_mask(t_arr, ink_threshold), cols, rows)
    g_occ = _occupancy_grid(_ink_mask(g_arr, ink_threshold), cols, rows)

    underfilled: List[Dict] = []
    overfilled: List[Dict] = []
    for r in range(rows):
        for c in range(cols):
            t, g = float(t_occ[r, c]), float(g_occ[r, c])
            if t >= min_cell_ink and (t - g) > tolerance:
                underfilled.append({"col": c, "row": r,
                                    "template_occ": round(t, 3),
                                    "render_occ": round(g, 3),
                                    "delta": round(t - g, 3)})
            elif g >= min_cell_ink and (g - t) > tolerance:
                overfilled.append({"col": c, "row": r,
                                   "template_occ": round(t, 3),
                                   "render_occ": round(g, 3),
                                   "delta": round(g - t, 3)})

    underfilled.sort(key=lambda d: d["delta"], reverse=True)
    overfilled.sort(key=lambda d: d["delta"], reverse=True)
    structural_similarity = round(1.0 - float(np.abs(t_occ - g_occ).mean()), 4)

    result = {
        "structural_similarity": structural_similarity,
        "underfilled_cells": underfilled,
        "overfilled_cells": overfilled,
    }

    if mirror:
        # In mirror mode the skin should match verbatim (only text is edited),
        # so a raw RGB difference is meaningful. Text edits still move some
        # pixels, hence a lenient default tolerance.
        raw_diff = round(float(np.abs(t_arr - g_arr).mean()) / 255.0, 4)
        result["raw_rgb_diff"] = raw_diff
        result["mirror_skin_exceeded"] = raw_diff > mirror_tolerance
    return result


def _parse_pdf_page_suffix(source: str) -> Tuple[str, Optional[int]]:
    """Split ``path.pdf#page=12`` into (``path.pdf``, 12); else (source, None)."""
    m = re.match(r"^(.*)#page=(\d+)$", source)
    if m:
        return m.group(1), int(m.group(2))
    return source, None


def _load_reference_to_png(
    source: str, pdf_page: Optional[int], out_png: Path, width: int, height: int,
) -> Tuple[bool, Optional[str]]:
    """Rasterize a --reference input (image or one PDF page) to a WxH PNG.

    Returns (ok, error_message). A PDF reference must resolve a 1-based page
    number from either --pdf-page or an inline ``#page=N`` suffix on the path
    (not both) — this mirrors the layout_references schema in
    docs/agents/ppt-master-layout-reference.md.
    """
    clean_source, inline_page = _parse_pdf_page_suffix(source)
    src_path = Path(clean_source)
    if not src_path.is_file():
        return False, f"reference not found: {src_path}"

    is_pdf = src_path.suffix.lower() == ".pdf"
    if is_pdf:
        if pdf_page is not None and inline_page is not None:
            return False, "supply --pdf-page OR an inline #page=N suffix, not both"
        page_num = pdf_page if pdf_page is not None else inline_page
        if page_num is None:
            return False, "PDF reference requires --pdf-page N or '#page=N' on the path"
        if not _HAVE_FITZ:
            return False, ("PDF reference needs PyMuPDF (`pip install pymupdf`) — "
                           "the same dependency ppt-master's source_to_md/pdf_to_md.py uses")
        try:
            doc = fitz.open(str(src_path))
            if not (1 <= page_num <= doc.page_count):
                return False, f"page {page_num} out of range (PDF has {doc.page_count} pages)"
            page = doc[page_num - 1]
            zoom_x = width / page.rect.width
            zoom_y = height / page.rect.height
            pix = page.get_pixmap(matrix=fitz.Matrix(zoom_x, zoom_y))
            pix.save(str(out_png))
            doc.close()
            return True, None
        except Exception as exc:  # noqa: BLE001
            return False, f"PyMuPDF failed to rasterize page {page_num}: {exc}"

    # Plain raster image: load and letterbox-resize onto the WxH canvas so the
    # occupancy grid compares like-for-like against the rendered generated SVG.
    try:
        from PIL import Image
        with Image.open(src_path) as im:
            im = im.convert("RGB")
            canvas = Image.new("RGB", (width, height), (255, 255, 255))
            scale = min(width / im.width, height / im.height)
            new_w, new_h = max(1, round(im.width * scale)), max(1, round(im.height * scale))
            resized = im.resize((new_w, new_h))
            canvas.paste(resized, ((width - new_w) // 2, (height - new_h) // 2))
            canvas.save(out_png)
        return True, None
    except Exception as exc:  # noqa: BLE001
        return False, f"failed to load reference image: {exc}"


def _crop_region_png(src_png: Path, region_pct: Tuple[float, float, float, float],
                      out_png: Path) -> None:
    """Crop src_png to a percent-of-canvas box (x, y, w, h), each 0-100."""
    from PIL import Image
    x_pct, y_pct, w_pct, h_pct = region_pct
    with Image.open(src_png) as im:
        w, h = im.size
        box = (
            round(w * x_pct / 100), round(h * y_pct / 100),
            round(w * (x_pct + w_pct) / 100), round(h * (y_pct + h_pct) / 100),
        )
        im.crop(box).save(out_png)


def _parse_region(spec: Optional[str]) -> Optional[Tuple[float, float, float, float]]:
    if not spec:
        return None
    parts = [float(p) for p in spec.split(",")]
    if len(parts) != 4:
        raise ValueError("--region expects 4 comma-separated numbers: x,y,w,h (percent)")
    return tuple(parts)  # type: ignore[return-value]


def _run_pair(args: argparse.Namespace) -> int:
    """--pair mode: one generated SVG vs one user-supplied reference image/PDF page."""
    generated_svg = Path(args.generated)
    if not generated_svg.is_file():
        print(f"[ERROR] --generated not found: {generated_svg}")
        return 2
    if _PNG_RENDERER is None:
        print("[ERROR] No SVG→PNG renderer available (need cairosvg, or svglib+reportlab).")
        return 2

    try:
        region = _parse_region(args.region)
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        return 2

    width, height = (int(x) for x in args.size.lower().split("x"))
    cols, rows = (int(x) for x in args.grid.lower().split("x"))
    work_dir = Path(args.work_dir) if args.work_dir else generated_svg.parent / ".layout_reference_check"
    work_dir.mkdir(parents=True, exist_ok=True)

    g_png = work_dir / f"{generated_svg.stem}.render.png"
    if not _render_svg_to_png(generated_svg, g_png, width, height):
        print(f"[ERROR] failed to render {generated_svg}")
        return 2

    ref_png = work_dir / "reference.render.png"
    ok, err = _load_reference_to_png(args.reference, args.pdf_page, ref_png, width, height)
    if not ok:
        print(f"[ERROR] {err}")
        return 2

    compare_g_png, compare_ref_png = g_png, ref_png
    if region is not None:
        cropped_g = work_dir / f"{generated_svg.stem}.render.cropped.png"
        cropped_ref = work_dir / "reference.render.cropped.png"
        _crop_region_png(g_png, region, cropped_g)
        _crop_region_png(ref_png, region, cropped_ref)
        compare_g_png, compare_ref_png = cropped_g, cropped_ref

    res = compare_page(
        compare_ref_png, compare_g_png,
        cols=cols, rows=rows, ink_threshold=args.ink_threshold,
        tolerance=args.tolerance, min_cell_ink=args.min_cell_ink,
        mirror=False, mirror_tolerance=args.mirror_tolerance,
    )
    n_under = len(res["underfilled_cells"])
    page_failed = n_under > args.max_underfill
    res["status"] = "fail" if page_failed else "pass"
    res["generated"] = str(generated_svg)
    res["reference"] = args.reference
    res["region"] = list(region) if region else None

    print("=" * 74)
    print(f"[LAYOUT REFERENCE] grid={cols}x{rows}  region={res['region'] or 'full page'}")
    print("=" * 74)
    tag = "OK  " if res["status"] == "pass" else "FAIL"
    print(f"  [{tag}] {generated_svg.name}  sim={res['structural_similarity']}  "
          f"underfilled={n_under}")
    if page_failed:
        for cell in res["underfilled_cells"][:5]:
            print(f"        collapsed cell (c{cell['col']},r{cell['row']}): "
                  f"reference {cell['template_occ']} → render {cell['render_occ']} "
                  f"(−{cell['delta']})")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(res, indent=2, ensure_ascii=False),
                                       encoding="utf-8")
        print(f"\n[report] {args.json_out}")

    print(f"\n[RESULT] {'passed' if not page_failed else 'FAILED'} structural fidelity "
          f"against layout reference.")
    return 1 if page_failed else 0


def _find_generated(svg_output: Path, page_key: str) -> Optional[Path]:
    m = re.match(r"P?0*(\d+)", page_key)
    if not m:
        return None
    nn = int(m.group(1))
    for cand in sorted(svg_output.glob("*.svg")):
        mm = re.match(r"0*(\d+)", cand.name)
        if mm and int(mm.group(1)) == nn:
            return cand
    return None


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("project", nargs="?", default=None,
                    help="project directory (has spec_lock.md, templates/, svg_output/); "
                         "omit when using --pair")
    ap.add_argument("--pair", action="store_true",
                    help="ad-hoc mode: compare one --generated SVG against one --reference "
                         "image/PDF page, independent of any project/spec_lock.md")
    ap.add_argument("--generated", default=None, help="--pair: path to the generated SVG page")
    ap.add_argument("--reference", default=None,
                    help="--pair: path to a reference image, or a PDF (use --pdf-page or "
                         "'file.pdf#page=N')")
    ap.add_argument("--pdf-page", type=int, default=None,
                    help="--pair: 1-based PDF page number (alternative to '#page=N' on --reference)")
    ap.add_argument("--region", default=None,
                    help="--pair: crop both sides to this box before comparing, as "
                         "'x,y,w,h' percent of the full canvas (e.g. 58,12,40,50)")
    ap.add_argument("--work-dir", default=None,
                    help="--pair: directory for intermediate renders (default: "
                         "<generated's dir>/.layout_reference_check)")
    ap.add_argument("--mode", choices=["auto", "fidelity", "mirror"], default="auto",
                    help="template replication mode; auto reads templates/design_spec.md")
    ap.add_argument("--grid", default="12x8", help="occupancy grid, COLSxROWS (default 12x8)")
    ap.add_argument("--size", default="1280x720", help="render size WxH (default 1280x720)")
    ap.add_argument("--ink-threshold", type=float, default=32.0,
                    help="RGB distance from background to count a pixel as inked (default 32)")
    ap.add_argument("--tolerance", type=float, default=0.15,
                    help="per-cell occupancy delta that counts as a mismatch (default 0.15)")
    ap.add_argument("--min-cell-ink", type=float, default=0.06,
                    help="a cell must be at least this inked in the template to judge underfill (default 0.06)")
    ap.add_argument("--max-underfill", type=int, default=3,
                    help="max underfilled cells before a page fails (default 3)")
    ap.add_argument("--mirror-tolerance", type=float, default=0.12,
                    help="mirror-mode raw RGB diff (0-1) above which skin is flagged (default 0.12)")
    ap.add_argument("--pages", default=None,
                    help="comma-separated page keys to limit to (e.g. P01,P07)")
    ap.add_argument("--json-out", default=None, help="write full report JSON here")
    args = ap.parse_args()

    if args.pair:
        if not args.generated or not args.reference:
            print("[ERROR] --pair requires both --generated and --reference")
            return 2
        return _run_pair(args)

    if args.project is None:
        ap.error("project is required unless --pair is given")

    if _PNG_RENDERER is None:
        print("[ERROR] No SVG→PNG renderer available (need cairosvg, or svglib+reportlab).")
        print("        Install one: pip install cairosvg   (preferred)")
        print("        The gate refuses to report a pass it did not actually verify.")
        return 2

    project = Path(args.project)
    lock_path = project / "spec_lock.md"
    templates_dir = project / "templates"
    svg_output = project / "svg_output"
    if not lock_path.is_file():
        print(f"[ERROR] spec_lock.md not found under {project}")
        return 2
    if not svg_output.is_dir():
        print(f"[ERROR] svg_output/ not found under {project}")
        return 2

    layouts = _parse_page_layouts(lock_path)
    if not layouts:
        print("[INFO] spec_lock.md has no page_layouts entries — nothing to verify "
              "(free-design deck). Fidelity gate does not apply.")
        return 2

    mode = args.mode
    if mode == "auto":
        detected = _detect_replication_mode(project)
        if detected == "standard":
            print("[INFO] template replication_mode=standard — content pages are free "
                  "design; fidelity gate does not apply. Nothing to verify.")
            return 2
        mode = detected if detected in {"fidelity", "mirror"} else "fidelity"
    mirror = mode == "mirror"

    cols, rows = (int(x) for x in args.grid.lower().split("x"))
    width, height = (int(x) for x in args.size.lower().split("x"))
    only = set(args.pages.split(",")) if args.pages else None

    render_dir = project / ".fidelity_render"
    render_dir.mkdir(exist_ok=True)

    report: Dict[str, Dict] = {}
    failed: List[str] = []
    skipped: List[str] = []

    for page_key, basename in sorted(layouts.items()):
        if only and page_key not in only:
            continue
        basename = basename[:-4] if basename.lower().endswith(".svg") else basename
        template_svg = templates_dir / f"{basename}.svg"
        generated_svg = _find_generated(svg_output, page_key)
        if not template_svg.is_file():
            skipped.append(f"{page_key}: template {basename}.svg missing "
                           "(run svg_quality_checker for the binding error)")
            continue
        if generated_svg is None or not generated_svg.is_file():
            skipped.append(f"{page_key}: no generated svg_output page found")
            continue

        t_png = render_dir / f"{basename}.template.png"
        g_png = render_dir / f"{generated_svg.stem}.render.png"
        if not (_render_svg_to_png(template_svg, t_png, width, height)
                and _render_svg_to_png(generated_svg, g_png, width, height)):
            skipped.append(f"{page_key}: render failed")
            continue

        res = compare_page(
            t_png, g_png,
            cols=cols, rows=rows, ink_threshold=args.ink_threshold,
            tolerance=args.tolerance, min_cell_ink=args.min_cell_ink,
            mirror=mirror, mirror_tolerance=args.mirror_tolerance,
        )
        res["template"] = f"{basename}.svg"
        res["generated"] = generated_svg.name
        n_under = len(res["underfilled_cells"])
        page_failed = n_under > args.max_underfill or res.get("mirror_skin_exceeded", False)
        res["status"] = "fail" if page_failed else "pass"
        report[page_key] = res
        if page_failed:
            failed.append(page_key)

    # ── Human summary ──────────────────────────────────────────────────
    print("=" * 74)
    print(f"[FIDELITY] mode={mode}  grid={cols}x{rows}  pages compared={len(report)}")
    print("=" * 74)
    for page_key in sorted(report):
        res = report[page_key]
        tag = "OK  " if res["status"] == "pass" else "FAIL"
        line = (f"  [{tag}] {page_key} {res['generated']} vs {res['template']}  "
                f"sim={res['structural_similarity']}  "
                f"underfilled={len(res['underfilled_cells'])}")
        if mirror:
            line += f"  raw_diff={res.get('raw_rgb_diff')}"
        print(line)
        if res["status"] == "fail":
            for cell in res["underfilled_cells"][:5]:
                print(f"        collapsed cell (c{cell['col']},r{cell['row']}): "
                      f"template {cell['template_occ']} → render {cell['render_occ']} "
                      f"(−{cell['delta']})")
            if res.get("mirror_skin_exceeded"):
                print(f"        mirror skin diff {res.get('raw_rgb_diff')} exceeds "
                      f"{args.mirror_tolerance} — non-text elements drifted from the source")
    for note in skipped:
        print(f"  [skip] {note}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps({
            "mode": mode, "grid": [cols, rows], "size": [width, height],
            "thresholds": {"ink": args.ink_threshold, "tolerance": args.tolerance,
                           "min_cell_ink": args.min_cell_ink,
                           "max_underfill": args.max_underfill,
                           "mirror_tolerance": args.mirror_tolerance},
            "pages": report, "failed": failed, "skipped": skipped,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n[report] {args.json_out}")

    if not report:
        print("\n[INFO] nothing was compared.")
        return 2
    if failed:
        print(f"\n[RESULT] {len(failed)} page(s) failed structural fidelity: "
              f"{', '.join(failed)}")
        return 1
    print("\n[RESULT] all compared pages passed structural fidelity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
