# PPT Style Specification — v5

**Sample size: 6 decks** (3 pptx, 3 pdf) — unchanged from v4. This version adds two previously-uncovered dimensions: image treatment and citation style, closing gaps identified against the original extraction spec. No new samples this round.

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
4. **External-source citation is rare-to-absent, and where present is audience-tier dependent.** B, C, F carry zero citation markers; A carries exactly one (its headline external financial figure); E carries one internal-spec disclosure but no "Source: X"-style external attribution. 5 of 6 samples (83%) show either zero or one incidental citation. *Exception: D* — the sole sample with systematic external-source citation (4 instances, all `Source: X` format: Huawei financial report, Roland Berger ×2, 2024 Omdia). D is also the sole gold-palette / senior-leadership sample (same outlier as Mandatory rule 1) — citation discipline appears to scale with audience seniority, not with genre or format.

## 2. Preferential rules (majority, with exceptions)

1. **Black/near-black (`000000`/`1D1D1A`) as the dominant text color.** Clearly dominant in A, B, E, F (4/6). *Exceptions*: C has near-black present but secondary to `C00000`; D has no black/near-black in its top colors at all (same outlier as Mandatory rule 1).
2. **Visual data is carried by images/diagrams rather than native charts, with tables as a secondary carrier.** B and C use near-zero tables (0/20, 2/24) and lean entirely on images. A uses tables heavily (7/13) alongside its one chart. D, E, F show high table-detection rates (71%, 56%, 29%), read cautiously per the pdfplumber caveat below. Images dominate everywhere regardless (17/17 to 26/27 pages/slides across all 6 samples).
3. **Body/label text clusters 10–14pt.** A:11.0pt · B:14.0pt · C:14.0pt · D:12.0pt · E:10.0pt · F:12.0pt — a shared band, no single majority value.
4. **Headline-as-conclusion titles, scoped to pptx sources.** Confirmed strongly in B and C (nearly every slide is a full declarative sentence). A is the pptx exception (mostly short section labels). Settled scope: pptx-only, permanently.
5. **Font family is scenario-conditioned, not a single cross-format rule.** Internal-use/pptx (A, B, C) → Microsoft Yahei + Arial. External-use/PDF (D, E, F) → ArialMT + Calibri family (expected PDF font-substitution artifact, not a real design difference).
6. **Images function as labeled diagram/icon elements, not standalone captioned photographs — and full-bleed photographic treatment is rare in pptx, more common in PDF.** All 6 samples show a substantial share of images with an adjacent text label (25–59%), but spot-checking the actual label text (e.g. B: "云化\n2020年，85%企业业务上云"; F: "HCS Installed"; C: brand-name lists under a framework diagram) shows these are diagram annotations/data callouts, not editorial photo captions — this corpus has no evidence of traditional "figure + caption" treatment at all. Full-bleed images are near-absent in the pptx sources (A: 0/14, B: 2/44, C: 0/51) but appear as a real pattern in PDF source D (20/477, a full-page-background-graphic style) — *treat D's full-bleed rate cautiously*, since it's also the sample most affected by the raster-object-count inflation noted below.

## 3. Prohibitions (never observed in any sample)

1. **No chart types beyond pie**, and only once (A, slide 1) across all 6 samples / 125 total pages+slides.
2. **No traditional editorial photo captions** (a standalone photograph with a descriptive caption beneath it) in any sample — every detected "caption" resolves to a diagram/icon label on closer inspection (see Preferential rule 2.6).

## 4. Reference examples

| Rule | Sample : slide/page | Evidence |
|---|---|---|
| Accent `C00000` (exception: D) | A, B, C, E, F top colors; D's top-6 has none | raw profile color-frequency counts |
| Title 24pt cluster | B:0, C:21, D, E, F | title-placeholder / most-frequent large size |
| No native charts | A:1 (`chart_type: "PIE (5)"`), all others 0 | `has_chart` field, all 6 raw profiles |
| Citation rarity (exception: D) | B, C, F: 0; A:2 ("数据来源：25Q4 Telefonica财报"); E:5 (internal spec, not external cite); D:1,7,many ("Source: Roland Berger" etc.) | `citations` field, all 6 raw profiles |
| Black/near-black dominant (exception: C, D) | A, B, E, F top-2 colors; C's C00000 leads; D has none | raw profile color-frequency counts |
| Table-vs-image split | A:7/13, B:0/20, C:2/24, D:17/24, E:15/27, F:5/17 | `has_table` counts, PDF caveat applies |
| Body 10–14pt band | A:11.0, B:14.0, C:14.0, D:12.0, E:10.0, F:12.0 (most-frequent size per sample) | font_sizes distribution per raw profile |
| Headline-as-title, pptx scope | B:7, C:9 | title_text field, pptx samples only |
| Internal-use font (Yahei+Arial) | A, B, C font lists | Microsoft Yahei dominant/co-dominant, all 3 pptx |
| External-use font (ArialMT/Calibri) | D, E, F font lists | ArialMT + Calibri-family entries dominate |
| Icon-label images, not photo captions | B:2 ("云化\n2020年85%企业业务上云"), C:19 (brand-name list) | `images[].caption` field, all 6 raw profiles |
| Full-bleed rare in pptx, present in D | A:0/14, B:2/44, C:0/51 vs D:20/477 | `images[].zone == "full-bleed"` counts |

## 5. Information density profile

*(unchanged from v4 — see below for full detail; no new samples this round)*

### 5.1 By-design roles (never flag these as under-dense)

| Role | n | Char range | Median |
|---|---|---|---|
| `cover`/`title` | 3 | 5–26 | 19 |
| `divider` | 9 | 14–45 | 33 |
| `toc` | 3 | 95 | 95 |
| `closing` | 1 | 10 | 10 |

### 5.2 `content`-role density, by genre (not by file format)

| Genre | Samples | Content median | Range |
|---|---|---|---|
| Pitch / product deck | B | 198 | 84–370 |
| Data-insight briefing | A | 580 | 92–794 |
| Framework-teaching deck | C | 105 (bimodal) | 57–505 |
| Reference / style-guide | D, E, F | 936 / 775 / 948 | 615–1462 / 196–1584 / 170–1677 |

### 5.3 Density remediation policy

Unchanged from v4: (1) consolidate adjacent thin source units, (2) web search to fill a factual gap (flagged for verification), (3) ask the user for proprietary/judgment-call gaps. Never pad with filler.

## Changelog vs v4

- **New Mandatory rule**: external-source citation is rare-to-absent and audience-tier dependent (rule 1.4). D's systematic "Source: X" citation practice (4 instances) contrasts sharply with the other 5 samples (0-1 incidental citations each). This is the same D outlier already seen in the color-palette Mandatory rule — reinforces that D's senior-leadership audience drives multiple distinguishing conventions, not just color.
- **New Preferential rule**: image treatment (rule 2.6) — images function as labeled diagram/icon elements, never as traditional captioned photographs; full-bleed treatment is rare in pptx, more common in PDF source D specifically.
- **New Prohibition**: no traditional editorial photo captions anywhere in the corpus (prohibition 2).
- **Data-quality note carried from the extraction fix**: PDF `image_count`/`images` runs 10-20x higher than pptx picture counts for a visually comparable deck (pdfplumber enumerates every embedded raster XObject — icons, logo fragments, textures — not just user-placed photos). Raw image counts across formats are not directly comparable; only the zone/caption *pattern* is, and even that should be read as a within-format signal first.
- **Unchanged**: all prior Mandatory/Preferential/Prohibition/Density findings — no new samples this round.

## Data quality caveats (apply to all rules above)

- `layout_type` mis-classifies at least one mid-deck section-divider as `title` in sample C (slide 21).
- pdfplumber's `has_table` detector can false-positive on aligned text blocks; D/E/F's table percentages are a weaker signal than A/B/C's.
- PDF image counts are inflated relative to pptx picture counts by roughly an order of magnitude (see Changelog) — a script-level limitation, not a real design difference.
- The "captioned" detection (text within a small margin below/near an image) reliably catches diagram/icon labels but has no way to distinguish those from a genuine editorial caption — in this corpus that distinction turned out not to matter (no genuine editorial captions were found), but a future corpus with real photo essays could need a stricter heuristic.
- No slide-master/theme-level extraction yet — everything above is inferred from explicit per-run formatting, not the deck's underlying theme definition.
