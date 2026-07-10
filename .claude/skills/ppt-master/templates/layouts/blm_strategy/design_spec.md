---
template_id: blm_strategy
kind: layout
category: scenario
summary: BLM (Business Leadership Model) strategy-to-execution training/consulting deck structure — dense analytical diagrams, matrices, and text-heavy content pages
keywords: [blm, strategy, business-leadership-model, training, consulting]
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: fidelity
placeholders:
  03b_content_text_sidebar: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{CONTENT_AREA}}", "{{KEY_MESSAGE}}", "{{SIDEBAR_TITLE}}", "{{SIDEBAR_BODY}}"]
  03c_content_table: ["{{PAGE_TITLE}}", "{{TABLE_HEADER_1}}", "{{TABLE_HEADER_2}}", "{{TABLE_HEADER_3}}", "{{TABLE_HEADER_4}}", "{{TABLE_ROW_N_LABEL}}", "{{TABLE_ROW_N_VALUE}}", "{{KEY_MESSAGE}}"]
  03d_content_comparison_cards: ["{{PAGE_TITLE}}", "{{CARD_1_HEADER}}", "{{CARD_1_BODY}}", "{{CARD_2_HEADER}}", "{{CARD_2_BODY}}", "{{CARD_3_HEADER}}", "{{CARD_3_BODY}}", "{{CARD_4_HEADER}}", "{{CARD_4_BODY}}", "{{CARD_5_HEADER}}", "{{CARD_5_BODY}}", "{{KEY_MESSAGE}}"]
  03e_content_numbered_list_image: ["{{PAGE_TITLE}}", "{{LIST_ITEM_N_TITLE}}", "{{LIST_ITEM_N_DESC}}", "{{IMAGE}}", "{{KEY_MESSAGE}}"]
  03f_content_process_horizontal: ["{{PAGE_TITLE}}", "{{PHASE_N_LABEL}}", "{{PHASE_N_DESC}}", "{{CONTENT_AREA}}", "{{KEY_MESSAGE}}"]
  03g_content_hierarchy_diagram: ["{{PAGE_TITLE}}", "{{GROUP_1_LABEL}}", "{{GROUP_2_LABEL}}", "{{NODE_LABEL}}", "{{GAP_LABEL}}", "{{RESULT_LABEL}}"]
  03h_content_2x2_matrix: ["{{PAGE_TITLE}}", "{{AXIS_X_LABEL}}", "{{AXIS_Y_LABEL}}", "{{QUADRANT_1_LABEL}}", "{{QUADRANT_2_LABEL}}", "{{QUADRANT_3_LABEL}}", "{{QUADRANT_4_LABEL}}", "{{KEY_MESSAGE}}"]
  03i_content_chart: ["{{PAGE_TITLE}}", "{{CHART_AREA}}", "{{KEY_MESSAGE}}"]
  03j_content_icon_grid: ["{{PAGE_TITLE}}", "{{ICON_ITEM_N_LABEL}}", "{{KEY_MESSAGE}}"]
---

# BLM战略执行 (BLM Strategy) — Design Specification

> Structure-only layout template distilled from a 64-page Huawei internal BLM (Business Leadership Model) strategy-to-execution training deck. No identity segment — colors below are the template's own default rendering, not a locked brand; a consuming project may substitute its own palette entirely.

## I. Template Overview

Dense, no-nonsense analytical/consulting register: every content page leads with a bold blue title and closes (where applicable) with a full-width red-on-white or white-on-blue takeaway banner stating the page's one-line conclusion — a McKinsey-style "action title" convention pulled directly from the source deck. Theme mode: light (white background throughout, no dark chrome). The template favors real, drawn structural skeletons (tables, matrices, hierarchy networks, process chevrons) over freeform blank content boxes — a page's shape is part of its argument.

## II. Color Scheme

Default rendering colors carried over from the source deck (not a locked identity — override freely):

| Role | HEX | Usage |
|---|---|---|
| primary (title blue) | `#0070C0` | Page titles, primary structural strokes |
| secondary (deep red) | `#C00000` | Emphasis text, key numbers, alert/highlight labels |
| accent (teal) | `#BBE0E3` | Connector lines, secondary structural fills |
| accent (indigo) | `#333399` | Alternate structural fill (hierarchy diagrams) |
| banner fill | `#0070C0` / `#C00000` | Full-width bottom takeaway banner background (either color, pick per page for variety) |
| banner text | `#FFFFFF` | Takeaway banner text, always bold |
| body text | `#000000` | Standard paragraph / list text |
| light fill | `#D4EAF5` | Table/card header cells, light structural panels |
| background | `#FFFFFF` | Page background throughout |

## III. Typography

Default stack: `Arial, "Microsoft YaHei", sans-serif` (no divergent brand typeface — source hardcodes 微软雅黑 directly on runs rather than through a distinct display font).

## IV. Signature Design Elements

- **Bottom takeaway banner**: full-width bar (`x=0, width=1280, height=48`, `y≈660`) in `#0070C0` or `#C00000`, centered bold white `{{KEY_MESSAGE}}` text (18-22px) — the deck's recurring "one-line conclusion" device, present on the majority of content variants. Treat it as optional per page; omit on variants that are already dense (e.g. `03i_content_chart`) if it would crowd the page.
- **Bold blue page title**: top-left, `#0070C0`, 28-32px, bold — every content page opens the same way regardless of body structure.
- **Structural geometry is load-bearing, not decorative**: unlike a generic blank content box, each `03*` variant below draws its actual distinguishing skeleton (table gridlines, card frames, hierarchy boxes + connectors, chevron/pentagon phase shapes, quadrant axis lines) — this is what fidelity mode is capturing. Strategist fills the drawn slots; it does not need to invent the skeleton.
- **No section-divider or TOC page in source**: `02_chapter` below is synthesized (not literal replication) to complete a usable roster — matching the deck's blue/white register but with no direct source anchor.

## V. Page Roster

| File | Cluster source (slide #) | Description |
|---|---|---|
| `01_cover.svg` | 1 | Full-bleed photo + dark gradient overlay, centered bold title + red subtitle line. Literal fidelity to source geometry. |
| `02_chapter.svg` | *(synthesized — no source anchor)* | Full `#0070C0` background, large white chapter number + title, thin teal accent rule. Built to match the deck's register, not copied from a slide. |
| `03a_content_text.svg` | 19,22,25,31,48,59–63 | Single bordered text block, plain heavy paragraph/bullet body. Suits dense narrative or Q&A-style pages. |
| `03b_content_text_sidebar.svg` | 42,43,44 | Text body (left, ~65% width) + light-blue sidebar callout box (right, ~35% width) for a case-study pull-out. Suits comparative case narratives. |
| `03c_content_table.svg` | 7,10,21,23,24,33,35,38,39,47,58 | Dense header-row + body-row grid (4 columns × 5 rows shown, extendable), light-blue header cells. Suits matrices, business-model canvases, paired lists. |
| `03d_content_comparison_cards.svg` | 2,40 | 3–5 up column cards, colored header band + body per card. Suits strategy-option or scenario comparisons. |
| `03e_content_numbered_list_image.svg` | 15,28,32,49,51,52,53 | Left numbered vertical list (connector lines to numerals) + right-side image placeholder. Suits framework walkthroughs anchored by a supporting visual. |
| `03f_content_process_horizontal.svg` | 11,17,27,55 | Left-to-right chevron/phase flow, 4 phases with connecting arrows. Suits process/timeline narratives (DSTE, planning cycles). |
| `03g_content_hierarchy_diagram.svg` | 5,12,13,14,41,54,56 | Central network of labeled boxes + connector lines (the deck's signature BLM-framework diagram shape). Suits framework/model-overview pages — this template's most recognizable page. |
| `03h_content_2x2_matrix.svg` | 26 | Classic quadrant matrix with labeled X/Y axes and 4 quadrant zones. Suits portfolio/BCG-style opportunity mapping. |
| `03i_content_chart.svg` | 6,9,20,57 | Large bordered chart/graph placeholder zone with axis lines. Suits scatter, hype-cycle, or strategy-map style data visuals. |
| `03j_content_icon_grid.svg` | 18,37 | 2×3 icon/oval + label grid. Suits enumerated-factor or capability-list pages. |
| `04_ending.svg` | 64 | Large centered stylized "Thank you" wordmark mixing primary blue and red, no title bar, decorative bottom bar. Literal fidelity to source geometry. |

## VI. Assets

None bundled. Source photographic/example assets (product photos, company logos, hardware images) are this course's specific example content, not reusable template assets — omitted per the confirmed asset policy.
