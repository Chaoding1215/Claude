---
brand_id: Huawei
kind: brand
summary: Huawei corporate identity — enterprise/telecom/ICT briefings, internal reports, product and strategy decks
keywords: [huawei, enterprise, telecom, ICT, corporate, formal]
primary_color: "#C7000A"
---

# Huawei Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Huawei (华为) |
| Use Cases | Enterprise/telecom/ICT briefings, internal reports, product and strategy decks, carrier/customer presentations |
| Tone | Formal, precise, corporate, technology-forward |

## II. Color Scheme

| Role | HEX | Provenance | Notes |
|---|---|---|---|
| primary | `#C7000A` | fact | Huawei Red — theme `accent1` / `primary`, extracted from PPTX theme XML |
| secondary | `#E9002F` | fact | Brighter red variant — theme `accent2`, for emphasis/highlight elements |
| accent | `#F4A100` | fact | Amber/gold — theme `accent3`, sparing use for callouts or data-viz |
| neutral (dark) | `#232323` | fact | theme `accent5` |
| neutral (gray) | `#666666` | fact | theme `accent6` |
| text | `#1D1D1A` | fact | theme `text` (near-black) |
| bg | `#FFFFFF` | fact | theme `background_alt` — this is the light-version deck; the theme's dark variant uses `#1D1D1A` as background with `#FFFFFF` text |

Red carries the primary brand weight; use it deliberately (titles, key accents, dividers) rather than as a large fill — this matches the source deck's light, white-dominant canvas with red used as a precise accent.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | `"Arial Black", "Microsoft YaHei", "黑体", sans-serif` | 700–900 |
| body | `Arial, "Microsoft YaHei", "宋体", sans-serif` | 400 |

> Western fonts (`Arial Black` / `Arial`) are `[fact]` from the theme XML. CJK companions (`Microsoft YaHei` / `黑体` / `宋体`) are `[fact]` from observed run-level usage in the source deck's actual slide content.

## IV. Logo

- File: `./logo.png` (529×116, red flower emblem + "HUAWEI" wordmark, transparent background)
- Usage: cover-only (prefer top-left or top-right corner placement); avoid stamping on every content page
- Clearspace: leave at least 0.5× logo height of empty space on all sides; never overlap text or photographic backgrounds

## V. Voice & Tone

- Formality: formal
- Person: we (我们)
- Emoji: forbidden
- Abbreviations: spell-out-first
- Note: the source deck's cover carries a "部门 / 作者 / 日期" (Department / Author / Date) block plus a "Security Level" classification marker — a standard convention in Huawei internal documents. Include this block on the cover page when the deck is for internal circulation.

## VI. Icon Style

- Preference: linear

> Thin-stroke, precise line icons — consistent with Huawei's clean, technology-forward visual register. Prefer stroke-only icon libraries (e.g. `tabler`, `lucide`) over filled/duotone sets.
