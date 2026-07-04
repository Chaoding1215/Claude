# PPT Style Specification — v10 (consolidated)

**Consolidates v2–v9 into one current, non-redundant reference.** No new samples this round — this is an editorial pass only, per the `writing-great-skills` information hierarchy (actionable rules first, supporting reference next, raw material last) and its failure-mode checklist (duplication, sediment, sprawl). Per-version changelogs are collapsed into a single Decision Log (§8); repeated "unchanged from vN" restatements and superseded framings (e.g. `C00000` presented as *the* rule, corrected in v8) are removed rather than carried forward. v2–v9 stay on disk unmodified as the audit trail for future Reconcile passes — nothing here deletes them.

**Corpus**: 7 files — 6 content samples + 1 canonical template.

| Sample | File | Genre | Format | Authoring tool |
|---|---|---|---|---|
| A | `Telefonica B2B Insight 20260703.pptx` | Data-insight briefing, 13 slides | pptx | Google Slides export |
| B | `华为SD-WAN高层主打胶片-Template.pptx` | Pitch/product deck, 20 slides | pptx | Google Slides export |
| C | `华为BLM模型管理：从战略到执行落地-Template.pptx` | Framework-teaching, 24 slides | pptx | Google Slides export |
| D | `高层交流风格.pdf` | Senior-leadership style guide, 24 pages | pdf | Native PowerPoint |
| E | `中基层交流风格.pdf` | Mid/junior style guide, 27 pages | pdf | Native PowerPoint |
| F | `技术风格.pdf` | Technical style guide, 17 pages | pdf | Native PowerPoint |
| Template | `PPT模板-浅色版16-9.pptx` | Canonical template (5 demo slides, 4 masters) | pptx | Native PowerPoint |

The template doesn't vote on content-genre rules — it supplies ground truth the other 6 are checked against (§4).

---

## 1. Mandatory rules (≥5/6 content samples)

1. **Accent color target is `C7000A`** (the template's true `accent1`), **not** the empirically-common `C00000`. Authors across the corpus consistently reach for `C00000` — PowerPoint's standard-palette "Dark Red" swatch — as a close but incorrect approximation (top-3-frequency color in A, B, C, E, F — 5/6). *Exception: D* uses a gold/amber family (`FFC000` in practice) instead — this is **not an anomaly**: it's the template's own `accent3` (`F4A100`), the designated senior-audience secondary accent (see §4). Apply `F4A100` by analogy if that scenario recurs, but don't generalize it further pre-emptively.
2. **Title size sits at 20–24pt, clustering at 24pt.** A:20.0pt · B/C/D/E/F: 24.0pt (5/6 exactly at 24pt).
3. **Native charts are essentially absent; visuals are image- or table-driven instead.** Only 1 native chart across all 6 content samples (A's single pie chart); every other sample has zero.
4. **External-source citation is rare-to-absent, and where present is audience-tier dependent.** B, C, F carry zero citation markers; A carries one (its headline external financial figure); E carries one internal-spec disclosure, not external attribution. 5/6 samples show zero or one incidental citation. *Exception: D* is the sole sample with systematic `Source: X` citation (4 instances: Huawei financial report, Roland Berger ×2, Omdia 2024) — the same senior-audience outlier as rule 1, suggesting citation discipline scales with audience seniority, not genre or format.

## 2. Preferential rules (majority, with exceptions)

1. **Black/near-black (`000000`/`1D1D1A`) as the dominant text color.** Dominant in A, B, E, F (4/6). *Exceptions*: C has it present but secondary to `C00000`; D has none in its top colors (same outlier as rule 1.1 — `1D1D1A` is in fact the template's own `dk1/lt1`, so D's absence is real, not noise).
2. **Visual data is carried by images/diagrams, with tables as a secondary carrier.** B and C use near-zero tables (0/20, 2/24) and lean on images; A uses tables heavily (7/13) alongside its one chart; D/E/F show high table-detection rates (71/56/29%) but read cautiously — pdfplumber's table detector false-positives on aligned text blocks (§7). Images dominate everywhere regardless (17/17 to 26/27 pages/slides).
3. **Body/label text clusters 10–14pt** (a shared band, no single majority value): A:11.0 · B:14.0 · C:14.0 · D:12.0 · E:10.0 · F:12.0.
4. **Headline-as-conclusion titles — settled scope, pptx-only.** Confirmed strongly in B and C (nearly every title is a full declarative sentence, e.g. C-slide-9 "战略：包括市场洞察、战略意图、创新焦点、业务设计"). A is the pptx exception (short labels like "WAN," "LAN"). PDF sources have no title-placeholder structure to check this against — that's a permanent extraction boundary, not an open gap.
5. **Font family is scenario-conditioned, kept as the empirical (not theme-nominal) target:**
   - *Internal/pptx* (A, B, C): CJK → **Microsoft Yahei**, Latin → **Arial**. This is a manual-override convention, not theme-inherited — every sample's own embedded theme actually declares 宋体/SimSun (§4) — but it's real, repeated author practice and is kept as the apply-skill's target rather than "corrected" to the nominal default (§8 decision).
   - *External/PDF* (D, E, F): **ArialMT + Calibri family**, even on CJK pages, with only a trace `DengXian` in E. This is the expected signature of PDF font re-encoding/subsetting, not a real design difference from the pptx scenario.
6. **Images function as labeled diagram/icon elements, not captioned photographs.** All 6 samples show images with an adjacent text label (25–59%), but the labels are diagram annotations/data callouts (e.g. B: "云化\n2020年，85%企业业务上云"), never editorial photo captions. Full-bleed images are near-absent in pptx (A:0/14, B:2/44, C:0/51) but appear as a real pattern in PDF sample D (20/477, full-page-background style) — read D's rate cautiously (§7 raster-inflation caveat).

## 3. Prohibitions (never observed in any sample)

1. **No chart types beyond pie**, and only once (A, slide 1) across 125 total pages+slides.
2. **No traditional editorial photo captions** anywhere — every detected "caption" resolves to a diagram/icon label on inspection (rule 2.6).

## 4. Ground truth vs. empirical drift (template cross-check)

`extract_theme.py` reads each file's slide-master theme XML directly rather than inferring conventions from usage. Cross-checked against the 3 pptx content samples:

| Sample | Theme match to template | Own theme's accent1 / Hans font | What authors actually did |
|---|---|---|---|
| B (SD-WAN) | Exact (8/13 embedded themes) or its other variant (2/13); 1 stray default-Office theme | `C7000A` / 宋体 | Used `C00000` (not `C7000A`); Yahei (not 宋体) |
| C (BLM) | None — own theme (`BBE0E3/333399/FFFFFF`) shares nothing with the template | `BBE0E3` / 宋体 | Used `C00000`, matching neither template nor its own theme — every color/font here is a manual override |
| A (Telefonica) | Patchwork — only 1/11 embedded themes matches exactly; most carry a related-but-distinct red (`E9002F`) or default-Office | varies / 宋体 on every embedded theme | Used `000000`/`1D1D1A` + `C00000`, matching none of its own embedded themes precisely |

Two settled drift patterns: **font** — no sample's theme declares Yahei, yet authors use it almost universally (theme font is vestigial); **color** — the corpus-wide empirical `C00000` is not the org's real `accent1` (`C7000A`), it's PowerPoint's standard "Dark Red" swatch, close enough to be invisible on screen but not the linked, rebrand-safe value.

Theme identity is also a compliance signal: B was clearly built from the shared template (exact theme match), C was authored entirely outside it, A is a patchwork consistent with slides copy-pasted across sources over time — explaining A's other oddities (short-label titles, heavier native-table use).

**Official palette** (template has two active accent families, not one):
- Variant α (theme1/3): `accent1=C7000A` · `accent2=E9002F` · `accent3=F4A100` (gold)
- Variant β (theme2): `accent1=C7000A` · `accent2=C8102E` · `accent3=EA594F`
- `dk1/lt1=1D1D1A` · `dk2/lt2=FFFFFF`

**Official composition grid** (4 named layouts — documented for reference; see §5 for why it is *not* the apply-skill's default target):

| Layout | Placeholders | Composition |
|---|---|---|
| 4 cover skins (探索/智能/攀登/灯塔) | CENTER_TITLE (0.07,0.13,0.54×0.10) + BODY (0.08,0.28,0.54×0.09) | Left ~55%/upper-third title block; right ~45% reserved for full-height art. 4 skins share one geometry, differ only in background art. |
| Contents page | one BODY (0.08,0.27,0.83×0.44) | Wide single zone for a TOC list; no title placeholder. |
| Content page | SUBTITLE (0.06,0.07,0.88×0.14) + OBJECT (0.06,0.22,0.88×0.68) | Thin 14%-height header strip + one large 68%-height free canvas. |
| End page | none | Pure background art / free-floating text. |

**Cover metadata + footer**: the template's own cover carries `部门：/作者：/日期：` as a fill-in body block, plus a bottom-left `Security Level:` footer at (0.08,0.91,0.21×0.02), ~10pt.

**Chart/table color convention** (from the template's own labeled demo page): clustered-column charts default every bar to `accent1`, with exactly **one** data point manually recolored to `accent2` — "all bars one color, highlight the one key figure," not a categorical multi-color palette. Competitor-capability matrices use **no cell fill** — presence/absence is a bullet character (`•`) vs. a blank cell, not a heatmap.

## 5. Composition-grid compliance is the exception, not the rule

Cross-validating the template's declared grid (§4) against where the 3 real pptx samples actually place shapes:

| Sample | Slides | Zero-placeholder (freeform) | TITLE placeholder | ...matching content-page title zone | ...matching cover title zone |
|---|---|---|---|---|---|
| B (SD-WAN) | 20 | 9 (45%) | 8 (40%) | 6 (30%) | 0 |
| A (Telefonica) | 13 | 12 (92%) | 1 (8%) | 1 (8%) | 0 |
| C (BLM) | 24 | 23 (96%) | 0 | 0 | 0 |

B's theme (colors) matched the template exactly, yet its composition matches the generic content grid on only 30% of slides, and 0% on covers (its cover placeholders sit at an entirely different position than any official cover skin). **Brand-palette compliance and brand-grid compliance are independent axes** — a sample can pass one and fail the other.

A confound applies here specifically: all 3 pptx content samples are Google Slides exports, not native PowerPoint (generic `Google Shape` names, no `docProps/app.xml`), while the template and all 3 PDFs are native PowerPoint. This confounds the grid-compliance numbers above — can't fully separate "authors ignore the grid" from "the export pipeline drops placeholder typing regardless of original fidelity." It does **not** confound the color/font habit findings (§1.1, §2.5), which are corroborated identically in the native-PowerPoint PDF samples.

**Resolution — descriptive fidelity by default, color is the one prescriptive override** (§8): the grid in §4 is the org's *declared* template, not how real decks are laid out. Kept here as brand reference only; the apply-skill should not use it by default.

## 6. Argument structure & diagram convention (pptx-only)

**Argument structure** — median content-points/slide by genre, cross-validating the §7.2 density-by-genre finding:

| Sample | Genre | Median points/slide | Shape |
|---|---|---|---|
| B (SD-WAN) | Pitch deck | 18 | Flat — one point per slide, similar depth |
| A (Telefonica) | Data-insight briefing | 32 (likely inflated by dashboard-style text-box labels) | Flat-high |
| C (BLM) | Framework-teaching | 6 (bimodal) | Sharp split — most slides 2–4 navigation points, a minority 16–40 in dense explanation slides |

**Diagram geometry** — non-text shapes clustered into rows/columns: 80% of B's slides, 54% of C's, 69% of A's have ≥3 shapes arranged as a 2D grid (both rows *and* columns). **Zero slides anywhere in the corpus** show a single-row/column linear arrangement — no evidence for funnel/timeline/process-arrow diagrams in this corpus. Caveat: this geometry heuristic only distinguishes "grid" from "not a grid" — it cannot tell a real data matrix from an unstructured icon scatter, or detect pyramid tapering; confirming the real semantic type needs visual/textual judgment at the profiling step.

**Footer/branding** — genre-specific, not corpus-wide: F carries `"{page} Huawei Confidential"` on every one of 17 pages (clean, universal); C has one inline mid-sentence `保密` mention (a content annotation, not a page marker); A, B, D, E have none. D and F are both native-PowerPoint PDF exports with completely different footer discipline — don't generalize any single sample's footer convention to the rest of the corpus.

## 7. Information density profile

Density is reported by role first — pooling role and content together hides that most "low density" here is deliberate, not deficient.

### 7.1 By-design roles (never flag these as under-dense)

| Role | n | Char range | Median |
|---|---|---|---|
| `cover`/`title` | 3 | 5–26 | 19 |
| `divider` | 9 | 14–45 | 33 |
| `toc` | 3 | 95 | 95 |
| `closing` | 1 | 10 | 10 |

### 7.2 `content`-role density, by genre (not by file format)

Genre predicts density far better than format — two pptx samples (B, C) differ by ~2x; all-PDF D/E/F still span 775–948 median.

| Genre | Samples | Content median | Range | Shape |
|---|---|---|---|---|
| Pitch/product deck | B | 198 | 84–370 | Flat — every slide argues one point at similar length |
| Data-insight briefing | A | 580 | 92–794 | Flat-dense — built for data-heavy tables |
| Framework-teaching | C | 105 | 57–505 | Bimodal — short navigation slides (57–135, majority) alternate with dense explanation slides (236–505) |
| Reference/style-guide | D, E, F | 936 / 775 / 948 | 615–1462 / 196–1584 / 170–1677 | Consistently dense — reads standalone, closer to a printed report than a presented deck |

Pick the density floor from the row matching the target's genre, never a corpus-wide average — the pooled median (~625) would wrongly flag every pitch-deck and most framework-navigation slides as under-dense.

### 7.3 Density remediation policy

Applies only to `content`-role slides notably below their genre's own floor (never to cover/divider/toc/closing). Try in order, stop at the first that resolves the gap:

1. **Consolidate** — merge 2+ adjacent thin source units onto one slide if they cover one coherent idea.
2. **Web search** — fill a specific factual/public-data gap; always flag web-sourced content for user verification.
3. **Ask the user** — for proprietary data or a judgment call only they can make.

Never pad with filler, restated bullets, or invented specifics just to hit a genre's number.

## 8. Decision log (compact — supersedes the per-version changelogs in v2–v9)

- **Descriptive fidelity by default; color is the sole prescriptive override.** The apply-skill should reproduce what authors actually, repeatedly do (freeform layout, empirical Yahei) — except accent color, which is corrected to the template's true `accent1` (`C7000A`, not the habitual `C00000`), and the gold slot by analogy (`F4A100`, not `FFC000`) if that scenario recurs. Rationale: color's true value is both known precisely (theme XML) and cosmetically almost invisible to override; font/grid corrections would visibly "templatize" a look that's supposed to match real decks.
- **Font stays empirical** (Yahei), not corrected to the theme's nominal 宋体/SimSun default — same logic, opposite conclusion, because the correction here *would* be visually obvious.
- **Grid stays empirical** (freeform placement), not corrected to the template's official 4-layout system — composition-grid compliance was rare even in the color-compliant sample (B, 30% best case, 0% on covers). The official grid is retained in §4 as brand reference only, explicitly out of scope as a default apply-skill target.
- **pptx-only fields, permanently, not open gaps**: `logic_flow`/headline-as-title (§2.4), `argument_structure` and `diagram_convention` (§6). PDF sources have no title-placeholder or paragraph/shape-typing equivalent to check these against — this is a structural extraction boundary, not something a future sample can close.
- **D's gold palette and citation discipline are one linked, explained finding**, not two anomalies: D is the corpus's only senior-leadership-audience sample, and its accent (`F4A100`, the template's real `accent3`) plus its systematic `Source: X` citations both trace to that audience tier. Still n=1 on the audience-tier axis — confirm with another senior-audience sample before treating it as a general audience-conditioned rule rather than a single sample's convention.
- **Google Slides authoring-tool confound is scoped to grid findings only** — it does not extend to color/font habit findings, which hold identically in the native-PowerPoint PDF samples.

## 9. Data quality caveats

- pdfplumber's `has_table` detector can false-positive on aligned text blocks — D/E/F's table percentages are weaker signals than A/B/C's (which read the actual pptx shape type).
- Font-family and color findings are not directly comparable across pptx vs. PDF sources — PDF export commonly re-encodes/subsets fonts and can't carry theme links.
- PDF `image_count` runs 10–20x higher than pptx picture counts for a visually comparable deck (pdfplumber enumerates every embedded raster XObject, not just user-placed photos) — compare placement-zone/captioning patterns within a format, not raw counts across formats.
- `classify_diagram_geometry` only reports row/column clustering — it cannot distinguish a real matrix from an icon scatter, or detect pyramid tapering.
- `layout_type` misclassifies at least one mid-deck section-divider as `title` in sample C (slide 21) — structural claims there rely on `title_text` and slide position, not `layout_type`.

## 10. Open follow-ups (not yet resolved)

- Diagram-geometry's "grid" label needs visual/semantic confirmation (matrix vs. icon-wall vs. something else) — geometry alone isn't enough.
- `argument_structure` and `diagram_convention` have no PDF equivalent yet; closing that gap needs PDF text-line clustering for paragraph segmentation and `rects`/`curves`-based shape detection for diagrams.
- Freeform (non-placeholder) shape positions still aren't captured at the per-shape level — only typed placeholders are. A true empirical grid (where authors actually put things, not just whether they used a placeholder) would need shape-position capture extended to text boxes generally, keyed by role via the same font-size/position heuristics as `title_text`.
- D's audience-tier-conditioned gold accent + citation discipline is a single-sample finding — needs a second senior-audience sample before promotion to a settled rule.

## External reference

- This corpus's full decision trail, superseded framings, and per-version evidence: `reference/style-spec-v2.md` through `style-spec-v9.md` (kept on disk for the Reconcile step — not duplicated here).
- Per-sample profiles: `reference/profiles/` (`gaoceng.json`=D, `zhongjiceng.json`=E, `jishu.json`=F, hashed filenames=A/B/C, `index.json`).
- Theme ground truth: `reference/theme_profile.json`.
- Extraction scripts and prompts: see `distill-slide-style` SKILL.md's own External reference section — not re-listed here to avoid duplication.
