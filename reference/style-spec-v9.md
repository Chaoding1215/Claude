# PPT Style Specification — v9

Closes the three remaining high-priority gaps from the earlier audit: per-slide argument structure, diagram/framework-type preference, and footer/branding conventions. No new samples this round (still 6 content samples + 1 canonical template); three new profile fields (`argument_structure`, `diagram_convention`, `branding_footer`) added to the schema.

## New finding: all 3 pptx content samples are Google Slides exports, not native PowerPoint

Discovered while adding the `authoring_tool` field: A (Telefonica), B (SD-WAN), and C (BLM) all carry generic `Google Shape` shape names and no `docProps/app.xml` — they were exported from Google Slides. The canonical template and all 3 PDF samples (D, E, F), by contrast, carry genuine `Microsoft® PowerPoint®` metadata. This is now a settled methodological caveat (see `SKILL.md`): it confounds the v7 grid-compliance finding (can't separate "authors ignore the grid" from "Google Slides' export drops placeholder typing regardless of fidelity"), but does *not* confound the color-habit finding, which is corroborated identically in the native-PowerPoint PDFs.

## 1. Argument structure (pptx-only — no PDF equivalent, see Settled conventions)

| Sample | Genre | Median content points/slide | Shape |
|---|---|---|---|
| B (SD-WAN) | Pitch deck | 18 | Flat — each slide develops one point at similar depth |
| A (Telefonica) | Data-insight briefing | 32 (likely inflated) | Flat-high, but caveat: dashboard-style slides built from many small text-box data labels rather than true bullets may overstate this |
| C (BLM) | Framework-teaching | 6 (bimodal) | Sharp split — most slides carry 2-4 navigation points, a minority carry 16-40 in dense explanation slides |

This tracks the same genre pattern as the v4 density profile (pitch < framework-navigation-median but framework has a long dense tail < data-insight), which cross-validates both metrics against each other rather than contradicting.

## 2. Diagram/framework-type preference (pptx-only)

`classify_diagram_geometry` clusters non-text shapes (icons, autoshapes, freeform parts) into rows/columns. Result across the corpus:

- **16/20 (80%) of B's slides, 13/24 (54%) of C's, 9/13 (69%) of A's** have ≥3 such shapes arranged as a 2D grid (multiple distinct rows *and* columns).
- **Zero slides anywhere in the corpus** show a single-row or single-column arrangement — meaning there's no evidence for funnel/timeline/process-arrow-style linear diagrams in this corpus at all. Whatever conceptual diagrams these decks use, they're not sequential.
- Concrete examples: B slide 2 ("商业驱动：更多的企业在转型过程中对网络提出更高诉求", 15 shapes, ~4×6) reads as a market-driver icon grid; C slide 19 ("创新领域...", 29 picture shapes — logos for 星巴克/淘宝/携程/亚马逊/迪斯尼/麦当劳/宜家 — plus grouping boxes) is a categorized logo wall.
- **Caveat, stated plainly**: this geometric heuristic cannot distinguish a genuine data matrix from an unstructured icon scatter, and can't detect pyramid tapering. "Grid" here means "not a single row or column," nothing more precise. Confirming the actual semantic type (matrix vs. icon wall vs. something else) needs visual/textual judgment at the profiling step, not just this geometry descriptor.

## 3. Footer/branding convention — genre-specific, not corpus-wide

No universal convention exists. Presence is inconsistent even within the same file format and authoring tool:

| Sample | Footer/branding marker |
|---|---|
| F (技术风格.pdf) | **`"{page} Huawei Confidential"` on every one of 17 pages** — clean, universal, page-numbered |
| C (BLM) | One inline mid-sentence mention of `保密` (confidential) inside body text (slide 15) — a content annotation about a competitive-analysis method, not a page-level marker |
| A, B, D, E | **Zero** footer, page-number, or confidentiality markers found |

D and F are both native-PowerPoint PDF exports (confirmed via producer metadata) — same tool, same file format, completely different footer discipline. Report this per-sample/per-genre, not as a corpus-wide rule; there isn't one.

## Changelog vs v8

- **New**: argument-structure convention (per-genre content-point medians), cross-validating the v4 density genre bands.
- **New**: diagram-geometry finding — majority of pptx slides use 2D icon/shape grids; zero linear/sequential diagrams found anywhere, ruling out funnel/timeline conventions as common in this corpus. Flagged clearly as a geometry-only signal, not a confirmed semantic diagram type.
- **New**: footer/branding is genre-specific, not corpus-wide — one sample (F) has a universal page+confidentiality footer, the rest have none or only an incidental inline mention.
- **New, corpus-wide methodological finding**: all 3 pptx content samples are Google Slides exports; the template and all 3 PDFs are native PowerPoint. Recorded as a confound for grid-related findings specifically, not for color findings.
- **Schema**: profile fields grow from 8 to 11 (`argument_structure`, `diagram_convention`, `branding_footer`); the first two are pptx-only, permanently, following the same scope-limit pattern as the existing title-pattern rules.

## Remaining follow-ups (not done)

- The diagram-geometry heuristic's "grid" label needs visual confirmation to become a real semantic finding (matrix vs. icon wall vs. something else) — geometry alone isn't enough.
- Argument-structure and diagram-convention have no PDF equivalent yet; if closing that gap becomes a priority, paragraph segmentation would need to come from PDF text-line clustering (no native paragraph structure in PDF), and diagram detection would need pdfplumber's `rects`/`curves` objects rather than shape typing.
