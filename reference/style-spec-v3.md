# PPT Style Specification — v3

**Sample size: 6 decks** (3 pptx, 3 pdf) — unchanged from v2. This version resolves two items v2 left open for human confirmation; no new samples were added.

Samples:
- **A** — `Telefonica B2B Insight 20260703.pptx` (13 slides, data/insight briefing)
- **B** — `华为SD-WAN高层主打胶片-Template.pptx` (20 slides, product pitch)
- **C** — `华为BLM模型管理：从战略到执行落地-Template.pptx` (24 slides, framework teaching deck)
- **D** — `高层交流风格.pdf` (24 pages, senior-leadership communication style guide)
- **E** — `中基层交流风格.pdf` (27 pages, mid/junior-level communication style guide)
- **F** — `技术风格.pdf` (17 pages, technical style guide)

## 1. Mandatory rules (≥5/6 samples)

1. **Accent color is dark red `C00000`.** Present as a top-3-frequency color in A, B, C, E, F (5/6). *Exception: D* — uses a gold/amber family (`FFC000` etc.) instead; D is also the only senior-leadership-audience sample.
2. **Title size sits at 20–24pt, clustering at 24pt.** A:20.0pt · B/C/D/E/F: 24.0pt (5/6 exactly at 24pt).
3. **Native charts are essentially absent; visuals are image- or table-driven instead.** Only 1 native chart across all 6 samples combined (A's single pie chart). Every other sample has zero native charts.

## 2. Preferential rules (majority, with exceptions)

1. **Black/near-black (`000000`/`1D1D1A`) as the dominant text color.** Clearly dominant in A, B, E, F (4/6). *Exceptions*: C has near-black present but secondary to `C00000`; D has no black/near-black in its top colors at all (same outlier as Mandatory rule 1).
2. **Visual data is carried by images/diagrams rather than native charts, with tables as a secondary carrier.** B and C use near-zero tables (0/20, 2/24) and lean entirely on images. A uses tables heavily (7/13) alongside its one chart. D, E, F show high table-detection rates (71%, 56%, 29%), read cautiously per the pdfplumber caveat below. Images dominate everywhere regardless (17/17 to 26/27 pages/slides across all 6 samples).
3. **Body/label text clusters 10–14pt.** A:11.0pt · B:14.0pt · C:14.0pt · D:12.0pt · E:10.0pt · F:12.0pt — a shared band, no single majority value.
4. **Headline-as-conclusion titles, scoped to pptx sources.** Confirmed strongly in B and C (nearly every slide is a full declarative sentence, e.g. C-slide-9 "战略：包括市场洞察、战略意图、创新焦点、业务设计"). A is the pptx exception (mostly short section labels: "WAN," "LAN"). **Settled scope**: this rule only ever votes on pptx samples — PDF sources have no title-placeholder structure to check it against, and that's a permanent extraction boundary, not a gap to close (see SKILL.md "Settled conventions"). 2 of 3 eligible (pptx) samples confirm it.
5. **Font family is scenario-conditioned, not a single cross-format rule.** Two sub-scenarios, both grounded in the same underlying corpus:
   - *Internal-use / working-file scenario* (pptx sources A, B, C): CJK text renders as **Microsoft Yahei**, paired with **Arial** for Latin characters/numerals. Confirmed in all 3 pptx samples (C is Yahei-dominant with only 2 stray Arial glyphs; A and B pair both fonts).
   - *External-use / distributed scenario* (PDF sources D, E, F): fonts surface as **ArialMT + Calibri family** (including Bold/Italic subset variants) even on CJK-text pages, with only a trace CJK font name (`DengXian`, sample E) appearing at low rank. This is the expected signature of PDF export re-encoding/subsetting fonts for portability, not evidence that the underlying deck design abandons Yahei for these audiences.

## 3. Prohibitions (never observed in any sample)

1. **No chart types beyond pie**, and only once (A, slide 1) across all 6 samples / 125 total pages+slides. Weak signal — 5 of 6 samples show zero native charts of any kind, so this is more "charts are rare" than "pie is preferred."

## 4. Reference examples

| Rule | Sample : slide/page | Evidence |
|---|---|---|
| Accent `C00000` (exception: D) | A, B, C, E, F top colors; D's top-6 has none | raw profile color-frequency counts |
| Title 24pt cluster | B:0, C:21, D (1373 occurrences), E (1331), F (568) | title-placeholder / most-frequent-large-size in raw profile |
| No native charts | A:1 (`chart_type: "PIE (5)"`), all others 0 | `has_chart` field across all 6 raw profiles |
| Black/near-black dominant (exception: C, D) | A, B, E, F top-2 colors; C's C00000 leads; D has none | raw profile color-frequency counts |
| Table-vs-image split | A: 7/13 tables; B: 0/20; C: 2/24; D: 17/24; E: 15/27; F: 5/17 | `has_table` counts per sample, with PDF caveat noted below |
| Body 10-14pt band | A:11.0(n=332), B:14.0(n=65), C:14.0(n=55), D:12.0(n=3227), E:10.0(n=3768), F:12.0(n=2942) | most-frequent font_sizes entry per raw profile |
| Headline-as-title, pptx scope | B:7 ("技术积累带来好的市场表现...主创新"), C:9 ("战略：包括市场洞察...") | title_text field, pptx samples only |
| Headline-as-title counter-example | A:5, A:6 | title_text is a bare label ("WAN", "LAN") |
| Internal-use font (Yahei+Arial) | A, B, C font lists | Microsoft Yahei present as dominant/co-dominant in all 3 pptx raw profiles |
| External-use font (ArialMT/Calibri) | D, E, F font lists | ArialMT + Calibri-family entries dominate; `DengXian` trace only in E |

## Changelog vs v2

- **Resolved**: headline-as-conclusion titles. v2 flagged this as needing a decision between adding PDF title detection or accepting pptx-only evidence. **Decision: accept pptx-only evidence, permanently.** Rule wording updated from "cannot be checked against D/E/F" (open gap) to "settled scope: pptx only" (closed). Encoded in `SKILL.md` under Settled conventions so future reconcile passes don't re-ask this.
- **Resolved**: font-family divergence across formats. v2 treated the pptx-vs-PDF font mismatch as a data-quality caveat to distrust. **Decision: split into two scenario-conditioned sub-rules** (internal-use/pptx → Yahei+Arial; external-use/PDF → ArialMT/Calibri) rather than merging or discarding. Promoted from "Data quality caveats" to a first-class Preferential rule (2.5). Also encoded in `SKILL.md` under Settled conventions.
- **Unchanged**: all three Mandatory rules, and Preferential rules 1–3, held as-is from v2 — no new samples this round.

## Data quality caveats (apply to all rules above)

- `layout_type` mis-classifies at least one mid-deck section-divider as `title` in sample C (slide 21) — structural claims there rely on `title_text` and slide position, not `layout_type`.
- pdfplumber's `has_table` detector can false-positive on aligned text blocks; D/E/F's table percentages are a weaker signal than A/B/C's (which read the actual pptx shape type).
- No slide-master/theme-level extraction yet — everything above is inferred from explicit per-run formatting, not the deck's underlying theme definition.
