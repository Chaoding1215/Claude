---
template_id: financial_briefing_dense
kind: layout
category: scenario
summary: Dense financial/account-strategy briefing deck structure — dark-ground register with a full-width three-panel KPI band and an asymmetric narrow-chart/wide-initiatives content split; derived from a live Orange Group FY2025 financial-briefing project (2026-07-14)
keywords: [financial, briefing, kpi-band, dense, consulting, dashboard, segment-analysis]
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
placeholders:
  01_chapter_speaker: ["{{CHAPTER_TITLE}}", "{{SPEAKER_NAME}}", "{{SPEAKER_ROLE}}"]
  02_content_case_shell: ["{{PAGE_TITLE}}", "{{KPI_1_LABEL}}", "{{KPI_1_VALUE}}", "{{KPI_1_DETAIL_1}}", "{{KPI_1_DETAIL_2}}", "{{KPI_2_LABEL}}", "{{KPI_2_VALUE}}", "{{KPI_2_DETAIL_1}}", "{{KPI_2_DETAIL_2}}", "{{KPI_3_LABEL}}", "{{KPI_3_VALUE}}", "{{KPI_3_DETAIL_1}}", "{{KPI_3_DETAIL_2}}", "{{CHART_CAPTION}}", "{{CHART_AREA}}", "{{KEY_INITIATIVES_ITEM_N}}", "{{SOURCE_FOOTNOTE}}"]
  03_content_agenda_pills: ["{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_3_TITLE}}"]
  04_content_divider: ["{{DIVIDER_TITLE}}"]
  05_content_process_framework: ["{{PAGE_TITLE}}", "{{PHASE_N_LABEL}}", "{{PHASE_N_DESC}}"]
  06_ending: ["{{CLOSING_MESSAGE}}", "{{QUADRANT_N_LABEL}}"]
---

# Financial Briefing (Dense) — Design Specification

> Structure-only layout template. `01_chapter_speaker`, `03_content_agenda_pills`, `04_content_divider`, `05_content_process_framework`, `06_ending` are carried over unchanged (structurally) from `omea_b2b_summit` — only their default font-family was normalized to Arial-only (see §III). `02_content_case_shell` is a full replacement: it distills a live redesign iterated across a real financial-briefing project rather than any single source deck, and is documented here as the reusable pattern. Colors below are this template's own default rendering, not a locked brand — override freely per the "structure not skin" rule.

## I. Template Overview

Dense, KPI-forward register for financial/account-strategy briefings: every `02_content_case_shell` content page opens with a single-line title (never wrapped to two lines — see §III) followed by a **full-width three-panel KPI band** (no side gutter, no navigation chrome competing for canvas width), then an asymmetric content split below — a **narrower chart/table column** (~460px, favors portrait-oriented bars to minimize horizontal footprint) paired with a **wider "Key Initiatives" text column** (~728px) that pairs each headline metric with the concrete action that drove it. This template exists specifically to eliminate two recurring failure modes seen in earlier dense-deck templates: (a) decorative chrome (e.g. a segment-nav strip) that eats canvas width without adding information, and (b) charts sized to fill available space rather than sized to the data, leaving the rest of the page under-used.

## II. Color Scheme

Default rendering (override freely per project brand):

| Role | HEX | Usage |
|---|---|---|
| background (dark ground) | `#1D1D1A` | Page background throughout |
| panel fill | `#262626` | KPI panel / content-column fills |
| accent (primary emphasis) | `#FFC000` | Headline keywords, positive/neutral KPI figures, chart "current period" series |
| accent (secondary) | `#F4A100` | Sparing use — isolated KPI highlight, alternate chart series |
| decline / warning | `#C0392B` | Negative YoY figures, declining KPI figures |
| growth / success | `#4E9B4E` | Positive YoY figures, growing KPI figures |
| body text | `#FFFFFF` | Standard paragraph / label text on dark ground |
| secondary text | `#DDDDDD` | Captions, sub-labels |
| tertiary text | `#666666` | Footnotes, "prior period" chart series, disabled/unavailable-data notes |
| structural line | `#A6A6A6` | Panel borders, data-block frames, chart baselines |
| divider ground | `#000000` or same as background | Full-bleed background on the pure divider variant |

## III. Typography

**Font**: Arial-only — `"Arial Black", Arial, sans-serif` for titles/emphasis, `Arial, sans-serif` for body. No CJK companion fallback by default (normalized 2026-07-14; add one back explicitly if a project needs CJK body copy).

**Single-line title rule (content pages only)**: `02_content_case_shell` titles must fit one line. Default/ceiling size is 40px (the deck's normal `title` role), but **may shrink for a long title down to a 22px floor** — tighten the wording first, shrink the font second. Never wrap to a second line; a two-line title is what this template's predecessor did and is exactly the "chart fills space, page feels sparse" problem this template corrects.

**KPI hero-number rule**: the big headline number in each KPI panel must **never render larger than that page's own title size** (`hero_number ≤ title_size_on_this_page`, not a flat value). On a page whose title lands at 28px, hero numbers are ≤28px too. This keeps the title visually dominant regardless of how much any one page's title had to shrink to fit.

## IV. Signature Design Elements

- **Full-width three-panel KPI band**: three equal panels (386px each at 1280 canvas width, zero gutter to the canvas edge — `x = 36, 447, 858`), replacing any nav-strip or two-panel chrome. Each panel: small caption label (18px) → hero number (≤ title size, see §III) → 1-2 lines of supporting detail (18px). An icon may sit top-right of a panel if one genuinely fits the metric; never invent an icon assignment just to fill space.
- **Asymmetric chart/initiatives split**: content area below the KPI band divides into a narrow left column (~460px) holding the page's one visualization (table, bar chart, bullet chart — whatever `page_charts` assigns) and a wide right column (~728px) holding a "Key Initiatives" list: 3-5 items, each a small colored square marker + 2-line statement pairing a metric with the action that drove it.
- **Chart sizing discipline**: size the chart to the data, not to the available column — reduce horizontal footprint before reducing vertical, since a narrower chart frees width for more real KPI/initiative content rather than leaving dead space. A two-series comparison (e.g. prior-period vs current-period) should use muted gray (`#666666`) for the prior period and the accent color for the current period, so the reader's eye lands on "what changed."
- **Chart legend placement**: when a chart needs a legend, place it **inside a genuinely sparse region of the chart's own plot area** (e.g. the empty space above a shorter bar group) rather than a dedicated caption row — a dedicated legend row is exactly the kind of space-for-decoration tradeoff this template avoids.
- **No navigation/segment chrome on content pages**: deliberately dropped. If a future project needs to orient the reader to which section/segment a page belongs to, prefer a small text label inside the KPI band or title, not dedicated nav chrome.

## V. Page Roster

| File | Description |
|---|---|
| `01_chapter_speaker.svg` | Dark-ground speaker/session-opener page: large centered bold title + speaker credit block. Unchanged from `omea_b2b_summit`. |
| `02_content_case_shell.svg` | Single-line title bar + full-width three-panel KPI band + narrow chart column (left, ~460px) + wide Key Initiatives column (right, ~728px). This template's core contribution — see §IV. |
| `03_content_agenda_pills.svg` | Three stacked numbered pill rows — table-of-contents / walk-through. Unchanged from `omea_b2b_summit`. |
| `04_content_divider.svg` | Pure dark background, single huge centered section-title wordmark. Unchanged from `omea_b2b_summit`. |
| `05_content_process_framework.svg` | Horizontal numbered arrow/roadmap banner, phase-label pairs above each stop. Unchanged from `omea_b2b_summit` — not exercised by the source project, carried for roster completeness. |
| `06_ending.svg` | Four-quadrant grid, bordered slots + captions. Unchanged from `omea_b2b_summit`. |

## VI. Assets

None bundled. Logo/brand marks are project-specific — a consuming project supplies its own via the brand template, placed per that brand's own asset rules (typically cover-only, `01_chapter_speaker`).
