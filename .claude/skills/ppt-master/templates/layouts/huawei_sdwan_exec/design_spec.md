---
template_id: huawei_sdwan_exec
kind: layout
category: scenario
summary: Huawei executive-briefing tech-sales deck structure — dense architecture diagrams, benchmark charts, and customer case studies behind a recurring 3-part agenda; distilled from a 21-page SD-WAN executive pitch deck
keywords: [huawei, sd-wan, enterprise-network, 5g, executive-briefing]
primary_color: "#C7000A"
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280.47 720"
replication_mode: fidelity
placeholders:
  01_cover: ["{{KICKER}}", "{{TITLE}}", "{{AUTHOR}}"]
  02_chapter_agenda: ["{{TOC_ITEM_1_TITLE}}", "{{TOC_ITEM_2_TITLE}}", "{{TOC_ITEM_3_TITLE}}"]
  03_content_highlight3: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
  04_content_product_grid: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
  05_content_dense_architecture: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}"]
  06_content_benchmark_chart: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}", "{{SOURCE}}"]
  07_content_case_study: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{KEY_MESSAGE}}", "{{CONTENT_AREA}}", "{{SOURCE}}"]
  08_content_timeline: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{DATE}}", "{{CONTENT_AREA}}"]
  09_content_bullets_generic: ["{{PAGE_TITLE}}", "{{SECTION_NAME}}", "{{CONTENT_AREA}}"]
  10_ending: ["{{CLOSING_MESSAGE}}", "{{THANK_YOU}}"]
---

# Huawei SD-WAN Executive Briefing — Design Specification

## I. Template Overview

Executive-level B2B technology sales deck: dense, data-driven, credibility-first. Distilled from a real Huawei SD-WAN pitch deck whose 21 slides ranged from near-empty highlight pages to extremely dense multi-node architecture diagrams — the template preserves that density range rather than flattening it to one rhythm. Light theme only (source's own master/layout inheritance was itself fragmented across 14 nominal masters, but structural analysis of all 89 master/layout files found only ~7 genuinely distinct chrome families; the rest were exact-byte duplicates or near-empty unused stubs — this template adopts the dominant white/red family, the one the populated content masters actually converge on).

## II. Color Scheme

**Not a locked identity — this is `kind: layout`, override freely.** The values below are the source deck's own observed convergence, kept as a default rendering reference for when this template is used without a brand package:

| Role | HEX | Usage |
|---|---|---|
| background | `#FFFFFF` | Page background throughout |
| accent (Huawei red) | `#C7000A` / `#C00000` | Highlighted agenda item, key numbers, headline emphasis, primary chart series |
| title text | `#1D1D1A` | Page titles, cover title |
| body text | `#333333` | Card labels, body copy |
| muted text | `#666666` / `#9A9A9A` | Subtitles, source lines, muted labels |
| section-tag chip | `#A3A3A3` fill, `#FFFFFF` text | Running top-right section badge |
| neutral panel | `#FAFAFA` / `#F5F5F5`, border `#E0E0E0` / `#DEDEDE` | Card and diagram-node fills |

If a brand package is loaded alongside this layout, its Color Scheme wins outright per the hard rule in `SKILL.md` Step 3 — none of the above survives.

## III. Typography

Default stack: `Arial, "Microsoft YaHei", sans-serif` (matches the source's own theme fonts — `majorLatin`/`minorLatin: Arial`, with Microsoft YaHei as the observed CJK companion). No template-specific divergence from the library default.

## IV. Signature Design Elements

- **Running section-tag chip**: every content page carries a small gray (`#A3A3A3`) rectangle flush against the top-right corner (122×29px), white bold centered text naming the current sub-theme (e.g. the source used "5G上行" / "3x业界性能" / "品质体验" as its three running sub-themes). This is the template's most recognizable recurring chrome — present on every `03`–`09` content variant.
- **Repeated 3-item agenda as section divider**: the source reuses one agenda slide **three times** as its section transitions, recoloring whichever item matches the upcoming section to bold Huawei red (`#C7000A`) while the other two stay dark gray regular weight. `02_chapter_agenda.svg` ships with item 1 highlighted as the sample — recolor per instance when this variant repeats across a deck.
- **Cover/ending bookend**: both `01_cover` and `10_ending` share one full-bleed hero photo (`cover_hero.jpg`, bundled) at reduced strength (a 32%-opacity white wash over the photo) with left-aligned dark text — the same visual bookend opens and closes the deck.
- **Density range, not one rhythm**: the source's content pages span from a bare 3-highlight page to an extremely dense multi-node architecture diagram. Do not normalize every content page to the same density — `05_content_dense_architecture` is deliberately the template's heaviest page and should stay that way when real content is dense enough to warrant it.

## V. Page Roster

| File | Cluster source (slides) | Description |
|---|---|---|
| `01_cover.svg` | 1 | Literal fidelity. Full-bleed hero photo, kicker + bold title + department/author line, all left-aligned in the lower-middle band. |
| `02_chapter_agenda.svg` | 2, 6, 18 (same slide reused 3×) | Adapted. Plain white background, 3-item "Ø" bulleted agenda list, one item bold red = current section. Suits any 3-part deck's section transitions. |
| `03_content_highlight3.svg` | 9, 12 | Adapted. Centered page title, 3 numbered highlight cards (headline + short label) in a row, decorative band below for a supporting device/diagram image. Suits "N key differentiators" pages. |
| `04_content_product_grid.svg` | 10 | Adapted. Left title + running section chip, 4 equal product cards (name + image slot + 2-line spec). Suits a product-family or SKU comparison page. |
| `05_content_dense_architecture.svg` | 5, 13, 15, 17 | Adapted. The template's densest variant: left context line, a central hub-and-4-node technical diagram, and a right results callout panel. Suits technical architecture, dataflow, or multi-stage process pages that need real information density. |
| `06_content_benchmark_chart.svg` | 8, 14 | Adapted. Left title + subtitle, a 3-pair grouped bar comparison with multiplier badges (e.g. "2x"/"4x"/"5x") above the winning bars, a source/legend panel on the right. Suits competitive benchmark or before/after metric pages. |
| `07_content_case_study.svg` | 19, 20 | Adapted. Before/after two-panel comparison with a "VS" marker, 3 stat callouts below, source line at the foot. Suits customer case studies and named-account proof points. |
| `08_content_timeline.svg` | 7 | Adapted. Horizontal axis with 5 milestone markers (date above, description below), the rightmost marker emphasized as "today", plus a supporting icon/diagram band beneath. Suits company or product history pages. |
| `09_content_bullets_generic.svg` | 3, 4, 11, 16 | Standard flexible content page — only header + running section chip fixed, content area free. Suits any page that doesn't match a more specific variant above. |
| `10_ending.svg` | 21 | Literal fidelity. Same hero photo bookend as the cover, 2-line closing slogan in the same lower-left band. |

## VI. Assets

- `cover_hero.jpg` (1920×1080, RGB — re-encoded from the source's CMYK JPEG) — the deck's signature bookend photo (aerial city network interchange + aircraft, "connected world" motif), used at reduced strength behind both `01_cover` and `10_ending`. Not a brand asset; swap freely per deck.

No Huawei logo/emblem is bundled — the existing `templates/brands/Huawei/` brand package already owns that asset. When this layout is paired with that brand package, its logo placement guidance applies; when used standalone, leave the bottom-right cover/ending corner (~100×100px) empty or supply a project-specific mark.

## VII. Placeholder Overrides

- `01_cover` uses `{{KICKER}}` (not in the canonical table) for the small "引领智能IP网络"-style eyebrow line above the main title, plus canonical `{{TITLE}}` and `{{AUTHOR}}` (repurposed as the department/org line, which is exactly `{{AUTHOR}}`'s canonical role).
- Every `03`–`09` content variant declares a shared header contract: canonical `{{PAGE_TITLE}}` for the page title and `{{SECTION_NAME}}` repurposed as the running top-right section-tag chip (canonical role is a footer field; this template moves it to the header badge — declared here per the override rule).
- `10_ending` uses `{{CLOSING_MESSAGE}}` and `{{THANK_YOU}}` for its two-line slogan; both are canonical ending-page placeholders.
