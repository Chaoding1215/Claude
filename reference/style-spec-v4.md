# PPT Style Specification — v4

**Sample size: 6 decks** (3 pptx, 3 pdf) — unchanged from v3. This version adds the Information density profile, now a standing required section (see `SKILL.md`), with a full role- and genre-segmented breakdown plus a remediation policy. No new samples this round.

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
4. **Headline-as-conclusion titles, scoped to pptx sources.** Confirmed strongly in B and C (nearly every slide is a full declarative sentence, e.g. C-slide-9 "战略：包括市场洞察、战略意图、创新焦点、业务设计"). A is the pptx exception (mostly short section labels: "WAN," "LAN"). Settled scope: pptx-only, permanently (see `SKILL.md`).
5. **Font family is scenario-conditioned, not a single cross-format rule.**
   - *Internal-use / working-file scenario* (pptx sources A, B, C): CJK text renders as **Microsoft Yahei**, paired with **Arial** for Latin characters/numerals.
   - *External-use / distributed scenario* (PDF sources D, E, F): fonts surface as **ArialMT + Calibri family** even on CJK-text pages — the expected signature of PDF font re-encoding/subsetting, not a real design difference.

## 3. Prohibitions (never observed in any sample)

1. **No chart types beyond pie**, and only once (A, slide 1) across all 6 samples / 125 total pages+slides.

## 4. Reference examples

| Rule | Sample : slide/page | Evidence |
|---|---|---|
| Accent `C00000` (exception: D) | A, B, C, E, F top colors; D's top-6 has none | raw profile color-frequency counts |
| Title 24pt cluster | B:0, C:21, D (1373 occ.), E (1331), F (568) | title-placeholder / most-frequent large size |
| No native charts | A:1 (`chart_type: "PIE (5)"`), all others 0 | `has_chart` field, all 6 raw profiles |
| Black/near-black dominant (exception: C, D) | A, B, E, F top-2 colors; C's C00000 leads; D has none | raw profile color-frequency counts |
| Table-vs-image split | A:7/13, B:0/20, C:2/24, D:17/24, E:15/27, F:5/17 | `has_table` counts, PDF caveat applies |
| Body 10–14pt band | A:11.0(n=332), B:14.0(n=65), C:14.0(n=55), D:12.0(n=3227), E:10.0(n=3768), F:12.0(n=2942) | most-frequent font_sizes per raw profile |
| Headline-as-title, pptx scope | B:7 ("技术积累带来好的市场表现...主创新"), C:9 ("战略：包括市场洞察...") | title_text, pptx samples only |
| Headline-as-title counter-example | A:5, A:6 | title_text is a bare label ("WAN", "LAN") |
| Internal-use font (Yahei+Arial) | A, B, C font lists | Microsoft Yahei dominant/co-dominant in all 3 pptx raw profiles |
| External-use font (ArialMT/Calibri) | D, E, F font lists | ArialMT + Calibri-family entries dominate |

## 5. Information density profile

Density is reported per **role** first — pooling role and content together into one number hides that most "low density" in this corpus is deliberate, not deficient.

### 5.1 By-design roles (never flag these as under-dense)

| Role | n | Char range | Median | Samples |
|---|---|---|---|---|
| `cover`/`title` | 3 | 5–26 | 19 | A:3 ("Telefonica B2B"), C:21, D:0 |
| `divider` (short transitional slide) | 9 | 14–45 | 33 | B:0,1,5,17 (14–45); A:10,11 (26,39); C:8,9 (21,24) |
| `toc` | 3 | 95 | 95 | D:0–2 (all three TOC pages identical length — likely a template placeholder pattern) |
| `closing` | 1 | 10 | 10 | E:26 |

These four roles are *supposed* to be terse. A cover with 19 characters or a divider with 33 is the pattern working correctly — never route these through the remediation policy below.

### 5.2 `content`-role density, by genre (not by file format)

File format alone doesn't predict content density — two pptx samples (B, C) differ by as much as the pptx-vs-PDF split does. Genre is the real driver:

| Genre | Samples | Content median | Range | Shape |
|---|---|---|---|---|
| Pitch / product deck | B (华为SD-WAN, pptx) | 198 | 84–370 | Fairly flat — every slide argues one point at similar length |
| Data-insight briefing | A (Telefonica, pptx) | 580 | 92–794 | Flat-dense — built to be read with data-heavy tables |
| Framework-teaching deck | C (华为BLM, pptx) | 105 | 57–505 | **Bimodal**: short navigation slides (57–135, majority) alternate with dense explanation slides (236–505) — the low cluster is scaffolding, not thin content |
| Reference / style-guide (printed-report style) | D, E, F (all PDF) | 936 / 775 / 948 | 615–1462 / 196–1584 / 170–1677 | Consistently dense — these read standalone without narration, closer to a printed report than a presented deck |

**Practical use**: when drafting a new `content` slide, pick the floor from the row matching the target's genre, not a corpus-wide average — the corpus-wide median (~625, from the pooled table) would wrongly flag every pitch-deck slide (B) and most framework-navigation slides (C) as under-dense when they're actually on-genre.

### 5.3 Density remediation policy

Applies only to `content`-role slides sitting notably below their genre's own floor (5.2) — never to cover/divider/toc/closing (5.1). Try in order, stop at the first that resolves the gap:

1. **Consolidate** — check whether 2+ adjacent thin source units cover one coherent idea; if so, merge them onto a single slide instead of leaving both thin. Preferred first because it reshapes material the user already owns.
2. **Web search** — if a specific factual/public-data gap is blocking the slide (a date, a public figure, a named standard), search to fill it. Always mark web-sourced content for the user's verification before finalizing — it didn't come from their material.
3. **Ask the user** — if the gap is proprietary data, an internal decision, or a judgment call only the user can make, request supplementary material or a direct answer rather than guessing.

Never pad with filler, restated bullets, or invented specifics just to hit a genre's density number — an honestly-thin slide that says less is better than a padded one that says nothing new per added character.

## Changelog vs v3

- **New standing section**: Information density profile (5). Not present in v1–v3, which only had a loose per-sample `text_density_rule` string. Promoted to a required top-level section in `SKILL.md` because it's now a high-priority deliverable for the eventual apply-skill (step 5), not incidental detail.
- **Key finding, not previously surfaced**: density is genre-driven, not format-driven. B and C are both pptx but differ in median content density by ~2x (198 vs 105); D/E/F are all PDF but span 775–948 median — genre (pitch vs framework-teaching vs reference-guide) predicts density far better than file format does. Prior versions implicitly conflated the two.
- **New finding**: C's content-density distribution is bimodal (short navigation slides + dense explanation slides), not simply "average 105 characters." Treating C's low median as a single target would misrepresent how that deck actually reads.
- **New policy, not in v1–v3**: the density remediation policy (5.3) — consolidate → web search → ask user, in that priority order. Encoded in `SKILL.md` as a durable requirement that must carry into the packaged apply-skill's behavior, not just its reference data.
- **Unchanged**: Mandatory/Preferential/Prohibitions sections — no new samples this round, no reason to revisit them.

## Data quality caveats (apply to all rules above)

- `layout_type` mis-classifies at least one mid-deck section-divider as `title` in sample C (slide 21) — structural claims there rely on `title_text` and slide position, not `layout_type`.
- pdfplumber's `has_table` detector can false-positive on aligned text blocks; D/E/F's table percentages are a weaker signal than A/B/C's (which read the actual pptx shape type).
- The `divider` role classification in 5.1 is a heuristic (any non-cover/toc/closing slide well below its sample's own content median) applied for this analysis, not a field the extraction scripts emit directly — if it proves durably useful, it belongs as a proper `layout_type` value in `extract_pptx.py`/`extract_pdf.py` rather than a one-off aggregation-time heuristic.
- No slide-master/theme-level extraction yet — everything above is inferred from explicit per-run formatting, not the deck's underlying theme definition.
