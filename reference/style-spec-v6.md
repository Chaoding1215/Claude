# PPT Style Specification — v6

**Sample size: 7 files** (4 pptx, 3 pdf) — the new 7th sample, `PPT模板-浅色版16-9.pptx`, is qualitatively different from the other 6: it's a near-empty canonical template (5 demo slides, 4 masters), not a real content deck. It doesn't vote on content-genre rules (density, logic flow) the way the other 6 do — instead it supplies **ground truth** that the other 6 can be checked against. This version adds that ground-truth layer; no changes to the density profile (v4) or image/citation findings (v5).

## 0. Ground truth vs empirical drift (new — read this before trusting rules 1.1 and 2.5)

`scripts/extract_theme.py` reads each file's slide-master theme XML directly (color scheme, and the CJK/Hans-script font, which lives in a per-script fallback entry the generic `<a:ea>` slot doesn't carry) instead of inferring conventions from what authors typed. Cross-checking this against the theme actually embedded in each of the 3 pptx content samples:

| Sample | Theme match to canonical template | Own theme's declared accent1 | Own theme's declared Hans font | What authors actually did |
|---|---|---|---|---|
| B (SD-WAN) | **Exact** — 8 of 13 embedded themes match the template's `C7000A/E9002F/F4A100` exactly; 2 match its other variant (`C7000A/C8102E/EA594F`); 1 stray slide carries an untouched default-Office theme | `C7000A` | 宋体 (SimSun) | Used `C00000` (not `C7000A`) as the empirical accent; used Microsoft Yahei (not 宋体) for CJK text |
| C (BLM) | **None** — its single theme (`BBE0E3/333399/FFFFFF`, pale cyan) shares no color with the template at all | `BBE0E3` | 宋体 (SimSun) | Used `C00000` — which doesn't match its *own* theme's accent1 either. Every color and font in this deck is a manual override with no theme backing. |
| A (Telefonica) | **Patchwork** — only 1 of 11 embedded themes matches the template exactly; most carry a related-but-distinct red (`E9002F` as accent1, not `C7000A`) or an untouched default-Office theme | varies by slide | 宋体 (SimSun) on every embedded theme | Used `000000`/`1D1D1A` dominant, `C00000` as accent — again not matching any of its own embedded themes precisely |

Two confirmed drift patterns, now settled (see `SKILL.md`):

1. **Font**: every sample's own theme declares 宋体 (SimSun, PowerPoint's plain default) as the CJK font — none declare Yahei. Authors override to Microsoft Yahei on nearly every run regardless. The theme's font scheme is vestigial in actual practice; **Yahei is a manual-override convention, not a theme-inherited one.**
2. **Color**: the empirically-dominant `C00000` across this whole corpus (rules 1.1/2.1 in prior versions) is **not** the org's actual theme accent1 (`C7000A`) — it's PowerPoint's built-in "Dark Red" standard-palette swatch, 7–10 RGB units off from the real brand red, close enough to be invisible on screen but not the linked, rebrand-safe color. **Rule 1.1 (accent color) should be read as "authors consistently reach for standard-palette Dark Red, which approximates but does not equal the true brand accent1 `C7000A`"** — worth stating both values if this spec is ever used to configure a drafting tool, since `C7000A` is the correct one to actually use.

Theme identity is also a compliance signal in its own right: B was clearly built from the shared template (exact theme match), C was authored completely outside it (unrelated theme, colors matching neither), A is a patchwork of multiple sources (consistent with slides copy-pasted across decks/authors over time). This explains A's earlier-noted oddities (short-label titles instead of headline-as-conclusion, heavier native-table usage) — A was never built from a single consistent template to begin with.

## 1. Official palette, fonts, and composition grid (new — from the canonical template)

**Color scheme** (4 theme variants exist in the template itself, so there isn't one single official palette — there are two accent families in active use):
- Variant α (theme1, theme3): `accent1=C7000A` (brand red) · `accent2=E9002F` · `accent3=F4A100` (gold)
- Variant β (theme2): `accent1=C7000A` (same red) · `accent2=C8102E` · `accent3=EA594F`
- `dk1/lt1 = 1D1D1A` (near-black, matches the corpus-wide empirical finding exactly) · `dk2/lt2 = FFFFFF`

This resolves the earlier "D is a gold outlier" question definitively: `高层交流风格.pdf`'s gold palette (`FFC000`, close to `F4A100`) is not an anomaly — **it's the template's own accent3**, the designated secondary/senior-audience accent, not a deviation from brand.

**Fonts** (also multi-variant): theme1 pairs Microsoft Yahei (title) with 黑体/Heiti (body); theme2/3 pair 等线 Light/DengXian Light (title) with 等线/DengXian (body); theme4 pairs 黑体 with 黑体. None of the template's own variants is "Yahei for everything," which makes the content samples' actual practice (Yahei used for both title and body uniformly) a simplification authors converged on independently, not a literal reproduction of any single official variant.

**Composition grid** (the named-layout vocabulary — this is the within-slide structure `layout_pattern` never captured before):

| Layout | Master | Placeholders | Composition |
|---|---|---|---|
| 探索 / 智能 / 攀登 / 灯塔 (4 cover variants) | master 0 | CENTER_TITLE at (0.07, 0.13, 0.54×0.10) + BODY at (0.08, 0.28, 0.54×0.09) | Left-aligned title block occupying the left ~55% of the slide, upper third — the right ~45% is reserved for a full-height graphic/photo (not a placeholder, so not captured, but implied by the geometry). The 4 variants share identical placeholder geometry and differ only in background art — i.e. "4 official cover skins, 1 grid." |
| 1_Contents page | master 1 | single BODY at (0.08, 0.27, 0.83×0.44) | One wide content zone for a TOC list — no title placeholder at all (the section name is presumably baked into the body text or a non-placeholder shape). |
| 1_Chinese text page | master 2 | SUBTITLE at (0.06, 0.07, 0.88×0.14) + OBJECT at (0.06, 0.22, 0.88×0.68) | Thin header band (14% of slide height) + one large open content zone (68% of height) — this is the generic "content slide" template: skinny title strip, everything else is free canvas. |
| End page | master 3 | none | No placeholders — closing slide is pure background art / free-floating text boxes. |

**Cover metadata + footer convention** (from the template's own demo slide 0, using layout 探索): the body placeholder directly beneath the title carries `部门：/作者：/日期：` (department/author/date) as a fill-in-the-blank block, and a separate small text box at (0.08, 0.91, 0.21×0.02) — the bottom-left footer, 10pt — carries `Security Level:`. This is the concrete answer to the previously-flagged footer/branding gap: **classification/confidentiality marking belongs bottom-left, ~10pt, on at minimum the cover page.**

**Chart/table color convention** (from the template's own demo slide 3, explicitly labeled "此页为图表配色示意，正式使用时请删除此页" — "this page demos chart coloring, delete before real use"):
- A clustered-column chart's series defaults to `accent1` (theme-linked, the brand red) for every bar, with **one data point manually overridden to `accent2`** — i.e. the official convention is "all bars one color; highlight exactly one bar in the secondary accent to draw the eye to the key figure," not a multi-color categorical palette.
- A competitor-capability matrix table (columns: T-Mobile/Huawei/Orange/China Mobile/China Telecom/China Unicom; rows: capability tiers) uses **no cell fill coloring at all** — presence/absence is marked purely by a bullet character (`•`) vs a blank cell. This is a real, citable answer to the previously-open "framework/diagram type preference" question: competitive benchmarking in this corpus is a **bullet-presence matrix**, not a heatmap or a scored/colored grid.

## Changelog vs v5

- **New sample type**: a canonical template file, treated as ground truth rather than a 7th content-genre vote. Doesn't affect the Mandatory/Preferential/Prohibition rule counts from v5 (still based on the 6 content samples) — it *annotates* them instead.
- **Resolved, not just caveated**: the "D uses a gold palette, exception to the C00000 rule" finding (v2-v5) is now explained, not just flagged — gold is the template's own accent3, an official secondary accent, not an anomaly.
- **Upgraded from inference to ground truth**: the font-family Settled Convention (pptx→Yahei, PDF→Latin-substitute) is now known to be *authors overriding their own file's declared 宋体 default*, not a theme-driven convention — same practical rule, much stronger evidence, and a sharper caveat if this spec is ever used to configure a drafting tool (write Yahei directly; don't rely on inheriting it from a theme, because none of the samples' themes actually declare it).
- **New, previously unaddressed**: composition grid (priority gap #2) and footer/branding convention (priority gap #5) both get a first real answer, sourced from the template's own layouts and demo slides rather than inferred from content decks.
- **Partially addressed**: chart-color-vs-brand-palette (medium-priority gap #8) and framework/diagram-type preference (high-priority gap #4) both get one concrete data point (accent1-default-plus-accent2-highlight bar charts; bullet-presence competitor matrices) — still n=1 for this specific finding since it comes from a single demo page, not yet cross-validated against real chart/table usage in the 6 content samples.

## Open follow-ups (not yet done)

- The composition-grid geometry above comes only from the template's own layouts — it hasn't been cross-validated against where the 3 pptx content samples actually place their title/body shapes, because `extract_pptx.py` doesn't currently record shape position (only `extract_theme.py`'s layout-level extraction does). Closing this fully means adding position capture to the per-slide extraction, then checking whether B/A/C's real title shapes land in the same left-55%-upper-third zone the template declares.
- Only one demo chart and one demo table exist in the whole corpus (both from the template's reference page) — the accent1-plus-highlight and bullet-matrix conventions are single-data-point findings, not yet confirmed against real chart/table usage in content decks.
