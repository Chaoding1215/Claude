---
template_id: omea_b2b_summit
kind: layout
category: scenario
summary: Dense B2B account-strategy summit deck structure — dark-ground, gold-accent consulting register with a recurring industry-segment nav chrome; distilled from a 26-page cross-regional partner review deck
keywords: [orange, omea, b2b, consulting-dense, country-case]
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: fidelity
placeholders:
  01_chapter_speaker: ["{{CHAPTER_TITLE}}", "{{SPEAKER_NAME}}", "{{SPEAKER_ROLE}}"]
  02_content_case_shell: ["{{PAGE_TITLE}}", "{{CONTENT_AREA}}", "{{KEY_MESSAGE}}"]
  03_content_agenda_pills: ["{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_3_TITLE}}"]
  04_content_divider: ["{{DIVIDER_TITLE}}"]
  05_content_process_framework: ["{{PAGE_TITLE}}", "{{PHASE_N_LABEL}}", "{{PHASE_N_DESC}}"]
  06_ending: ["{{CLOSING_MESSAGE}}", "{{QUADRANT_N_LABEL}}"]
---

# OMEA B2B Summit — Design Specification

> Structure-only layout template distilled from a 26-page cross-regional B2B account-strategy summit deck. No identity segment — the source itself carries no single coherent brand identity (see §I); colors below are the template's own default rendering, not a locked brand, and a consuming project may substitute its own palette entirely.

## I. Template Overview

Dark-ground consulting-dense register: every content page opens with a bold title bar and, on the majority of variants, a fixed top-right industry-segment navigation strip (six category chips, one highlighted) that orients the reader to which vertical the page's case belongs to. Theme mode: dark (near-black backgrounds throughout; white body text; gold accent for emphasis). Pages favor drawn structural devices — country-map annotation clusters, KPI stat blocks, bordered data panels — over freeform blank content boxes.

**Source note (unusual, worth preserving as a fact):** the source deck's own slide-master hierarchy carries no single consistent identity — three different accent colors (a house red, a distinct global-brand orange, and an unmodified Office default blue) are inherited across the four masters the 26 slides actually use, and the same "agenda" layout exists twice in the package under two different color lineages. The *slide bodies*, however, converge on one real recurring accent — `#FFC000` gold — far more consistently than the master layer does. This template's default color rendering follows that slide-level convergence, not the inconsistent master layer, since the slide layer is what the source's authors actually designed against page after page.

## II. Color Scheme

Default rendering colors carried over from the source deck's slide-body convergence (not a locked identity — override freely):

| Role | HEX | Usage |
|---|---|---|
| background (dark ground) | `#1D1D1A` | Page background, the dominant slide-level ground throughout |
| accent (gold, primary emphasis) | `#FFC000` | Emphasized numbers, headline keywords, section labels — the one color that recurs consistently at the slide-body level |
| body text | `#FFFFFF` | Standard paragraph / label text on dark ground |
| segment-nav active | `#C00000` | Highlighted chip in the industry-segment nav strip (the segment the current page belongs to) |
| segment-nav inactive | `#333F50` | Unhighlighted chips in the same strip |
| secondary accent (client reference orange) | `#FF7900` | Used sparingly for flagship/starred callouts — a reference color from the source material, not this template's own primary |
| divider ground | `#000000` | Full-bleed background on the pure divider variant |
| structural line | `#A6A6A6` | Panel borders, data-block frames |

## III. Typography

Default stack: `Arial, "Microsoft YaHei", sans-serif` (source mixes in Calibri and 方正兰亭 family names inconsistently across masters — normalized to the one safe stack here; do not carry the source's mixed font-family lists into new content).

## IV. Signature Design Elements

- **Industry-segment navigation strip**: a fixed row of six small rounded-rect chips top-right (`F&B/Retail`, `Office`, `Hospitality`, `Education`, `Industry MPN`, `Industry SD-WAN`), one recolored `#C00000` (active) to mark the current page's vertical, the rest `#333F50`. This is the template's most recognizable recurring chrome — present on the majority of content variants (`02_content_case_shell`). Ship with the first chip active as the placed example; Strategist/Executor recolors the chip matching the actual page content.
- **Bold title bar**: top-left, `#FFC000` leading word(s) + `#FFFFFF` remainder, 28-32px bold — the deck's consistent page-opener regardless of body structure.
- **Numbered pill list vs. numbered arrow-timeline are two distinct devices, not one**: the source contains both a compact vertical 3-pill section-nav (numbered circle + rounded label bar, used for a table-of-contents-style walk-through) and a separate horizontal numbered arrow/roadmap banner (a long chevron-arrow shape with evenly spaced numbered stops and phase labels above). Do not collapse these into a single variant — `03_content_agenda_pills` covers the first, `05_content_process_framework` the second.
- **Structural geometry is load-bearing, not decorative**: like the source's country-case pages, `02_content_case_shell` bundles real bordered data-panel geometry (KPI stat blocks, map-annotation callout boxes) as part of its fixed structure, not just a blank content rectangle — Strategist fills the drawn slots.
- **No literal cover page in source**: the source's opening slide is itself a speaker/chapter page (`01_chapter_speaker` below), not a distinct title-only cover — this template therefore ships no separate `01_cover.svg`; `01_chapter_speaker` opens the roster.

## V. Page Roster

| File | Cluster source (slide #) | Description |
|---|---|---|
| `01_chapter_speaker.svg` | 1, 3 | Full dark-ground (`#1D1D1A`) speaker-intro page: large centered bold white chapter/session title, with speaker name + role credit block below. Literal fidelity to source geometry. Suits opening/keynote-speaker section breaks. |
| `02_content_case_shell.svg` | 2,4-9,11,13-20,23,25 (shared shell; body free) | Dark-ground content page: bold gold+white title bar top-left, six-chip industry-segment nav top-right (one active), bordered KPI stat blocks and map-annotation callout boxes in the free content area below. Suits any single-market or single-topic business case — this is the deck's single most common page type, though each source instance's body composition is bespoke. |
| `03_content_agenda_pills.svg` | 8, 12 | Three stacked rounded-pill rows, each preceded by a numbered red circle (1/2/3), title bar above reading "Open Discussion" register. Suits a short table-of-contents or three-part session walk-through. |
| `04_content_divider.svg` | 22 | Pure black background, no title bar, single huge centered gold section-title wordmark. Suits a hard section break with no supporting content. |
| `05_content_process_framework.svg` | 21, 24 | Horizontal numbered arrow/roadmap banner (long chevron shape, gold dot markers at each stop) with phase-label pairs above each stop. Suits a multi-step rollout plan or maturity roadmap. |
| `06_ending.svg` | 26 | Four-quadrant screen/demo grid, each quadrant a bordered image/screenshot slot with a short caption beneath. Suits a closing "live demo" or product-showcase wrap-up page. |

## VI. Assets

None bundled. Source photographic assets (country flags/maps, partner logos, product screenshots, business-specific data) are this deck's own case-specific content, not reusable template assets — omitted per the confirmed asset policy.
