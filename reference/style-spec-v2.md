# PPT Style Specification — v2

**Sample size: 6 decks** (3 pptx, 3 pdf) — up from 3 in v1. The >80%-consistency bar for "mandatory" now admits 5/6 (83%), not just 6/6.

Samples:
- **A** — `Telefonica B2B Insight 20260703.pptx` (13 slides, data/insight briefing)
- **B** — `华为SD-WAN高层主打胶片-Template.pptx` (20 slides, product pitch)
- **C** — `华为BLM模型管理：从战略到执行落地-Template.pptx` (24 slides, framework teaching deck)
- **D** — `高层交流风格.pdf` (24 pages, senior-leadership communication style guide)
- **E** — `中基层交流风格.pdf` (27 pages, mid/junior-level communication style guide)
- **F** — `技术风格.pdf` (17 pages, technical style guide)

## 1. Mandatory rules (≥5/6 samples)

1. **Accent color is dark red `C00000`.** Present as a top-3-frequency color in A, B, C, E, F (5/6). *Exception: D* — uses a gold/amber family (`FFC000` etc.) instead, with no `C00000` in its top 6 colors at all. D is also the only "高层" (senior-leadership) sample, so this may be a deliberate audience-tier distinction rather than noise — worth confirming with another senior-audience sample before either promoting D's palette to its own rule or writing it off as an exception.
2. **Title size sits at 20–24pt, clustering at 24pt.** A:20.0pt · B/C/D/E/F: 24.0pt (5/6 exactly at 24pt).
3. **Native charts are essentially absent; visuals are image- or table-driven instead.** Only 1 native chart across all 6 samples combined (A's single pie chart). Every other sample has zero native charts.

## 2. Preferential rules (majority, with exceptions)

1. **Black/near-black (`000000`/`1D1D1A`) as the dominant text color.** Clearly dominant in A, B, E, F (4/6). *Exceptions*: C has near-black present but secondary to `C00000`; D has no black/near-black in its top colors at all (see Mandatory rule 1 — same outlier).
2. **Visual data is carried by images/diagrams rather than native charts, with tables as a secondary carrier.** B and C use near-zero tables (0/20, 2/24) and lean entirely on images. A uses tables heavily (7/13) alongside its one chart. D, E, F (the PDFs) show high table-detection rates (71%, 56%, 29%) — *but treat these three numbers cautiously*: pdfplumber's table detector is known to false-positive on aligned text blocks, so PDF table counts are a weaker signal than the pptx-derived ones (A, B, C, which read the actual shape type). Net read: images dominate everywhere (17/17 to 26/27 pages/slides across all 6 samples); whether tables are a real secondary pattern or a detection artifact needs a pptx-side sample with heavy tables to cross-check against a PDF export of the same deck.
3. **Body/label text clusters 10–14pt.** A:11.0pt · B:14.0pt · C:14.0pt · D:12.0pt · E:10.0pt · F:12.0pt — all 6 fall within a 10–14pt band, but no single value is shared by a majority, so this stays a band-level rule, not a specific size.
4. **Headline-as-conclusion titles** (full declarative sentence as the title, e.g. C-slide-9 "战略：包括市场洞察、战略意图、创新焦点、业务设计"). Confirmed strongly in B and C (pptx, nearly every slide). *Cannot be checked against D/E/F* — the PDF extraction script doesn't currently capture a title-placeholder equivalent, so this rule's evidence is pptx-only (2/3 pptx samples, with A as the pptx exception using short labels instead). Flagged as an open extraction gap, not resolved by this aggregation — see Data Quality Caveats.

## 3. Prohibitions (never observed in any sample)

1. **No chart types beyond pie**, and only once (A, slide 1) across all 6 samples / 125 total pages+slides. Weak signal — 5 of 6 samples show zero native charts of any kind, so this is more "charts are rare" than "pie is preferred."

## 4. Reference examples

| Rule | Sample : slide/page | Evidence |
|---|---|---|
| Accent `C00000` (exception: D) | A, B, C, E, F top colors; D's top-6 has none | raw profile color-frequency counts |
| Title 24pt cluster | B:0, C:21, D (1373 occurrences), E (1331), F (568) | title-placeholder / most-frequent-large-size in raw profile |
| No native charts | A:1 (`chart_type: "PIE (5)"`), all others 0 | `has_chart` field across all 6 raw profiles |
| Black/near-black dominant (exception: C, D) | A, B, E, F top-2 colors; C's C00000 leads; D has none | raw profile color-frequency counts |
| Table-vs-image split | A: 7/13 tables; B: 0/20; C: 2/24; D: 17/24; E: 15/27; F: 5/17 | `has_table` counts per sample, with PDF caveat noted above |
| Body 10-14pt band | A:11.0(n=332), B:14.0(n=65), C:14.0(n=55), D:12.0(n=3227), E:10.0(n=3768), F:12.0(n=2942) | most-frequent font_sizes entry per raw profile |
| Headline-as-title (pptx only) | B:7 ("技术积累带来好的市场表现...主创新"), C:9 ("战略：包括市场洞察...") | title_text field, pptx samples only |
| Headline-as-title counter-example | A:5, A:6 | title_text is a bare label ("WAN", "LAN") |

## Changelog vs v1

- **Promoted to Mandatory**: "accent color C00000" (was borderline preferential territory implicitly at n=3; now clears 5/6 explicitly, with D's gold palette named as a specific, reasoned exception rather than noise).
- **New Mandatory rule**: "native charts are essentially absent" — v1's Prohibitions section only had a weak "pie-only" observation; with 3 more samples showing zero charts, the stronger and more useful claim is that charts as a category are rare, which is now confidently mandatory.
- **Unchanged**: title-size band (20-24pt) — held at n=3, holds at n=6, now with 5/6 exactly at 24pt rather than a looser band.
- **Weakened, flagged for human review**: "headline-as-conclusion titles" was Preferential in v1 with A as the lone exception (1/3 samples). At n=6 it's still Preferential, but now with an unresolved gap rather than a clean majority — the 3 new PDF samples can't be checked against this rule at all, because the PDF extraction script has no title-placeholder equivalent. **This is a flip that needs your confirmation**: do we (a) add title detection to `extract_pdf.py` before trusting this rule further, or (b) accept pptx-only evidence for title-pattern rules going forward?
- **New caveat, not in v1**: PDF and pptx samples show different font-name distributions for what's presumably the same underlying CJK typeface — pptx samples explicitly report Microsoft Yahei; PDF samples report almost entirely Latin font names (ArialMT, Calibri variants) even on clearly Chinese-text pages, with only a trace CJK font (`DengXian`) appearing at low rank in one sample. This looks like a PDF font-subsetting/embedding quirk (the extractor may be reading a fallback name), not evidence that these decks actually use a different font family. **Do not treat the current font-family findings as comparable across pptx vs PDF sources.**

## Data quality caveats (apply to all rules above)

- `layout_type` mis-classifies at least one mid-deck section-divider as `title` in sample C (slide 21) — structural claims there rely on `title_text` and slide position, not `layout_type`.
- pdfplumber's `has_table` detector can false-positive on aligned text blocks; D/E/F's table percentages are a weaker signal than A/B/C's (which read the actual pptx shape type).
- The PDF extraction script has no title-placeholder equivalent — title-pattern rules (headline-as-conclusion, logic_flow) are currently pptx-only evidence, even though half the corpus is now PDF.
- Font-family comparisons across pptx vs PDF sources are unreliable until the font-subsetting issue above is understood.
- No slide-master/theme-level extraction yet — everything above is inferred from explicit per-run formatting, not the deck's underlying theme definition.
