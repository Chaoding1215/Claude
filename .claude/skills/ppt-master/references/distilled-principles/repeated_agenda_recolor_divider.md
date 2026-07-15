---
key: repeated_agenda_recolor_divider
category: 章节节奏
scope: global
source: Huawei SD-WAN executive briefing source deck, slides 2/6/18 (the same agenda slide reused 3x as section transitions)
---

# Repeated-agenda-with-recolor as a section divider

An alternative to a persistent per-page navigation strip: instead of showing
"which section am I in" chrome on every single page, re-show the deck's full
agenda/outline slide once before each section, recoloring whichever item
matches the upcoming section to the accent color + bold weight while every
other item stays neutral gray/regular weight.

## Why this is a distinct, real alternative — not a lesser version of a nav strip

`omea_b2b_summit`'s convention is a **persistent** six-chip strip present on
every content page, one chip highlighted at all times — the navigational
signal is always visible but takes up permanent chrome real estate on every
single page. This Huawei source's convention trades that constant visibility
for **zero per-page chrome cost**: the orientation signal only appears once
per section, at the moment of transition, and costs nothing on the pages in
between. Neither is strictly better — persistent chrome suits decks where
readers jump between pages non-linearly and need constant orientation;
repeated-agenda-recolor suits decks meant to be read start-to-finish, where a
full-page section transition is itself a welcome pacing beat.

## Application

- Reuse the identical agenda content (same items, same order, same wording)
  every time it recurs — do not reword or reorder between instances.
  Recoloring is the only thing that changes.
- One item highlighted per instance: accent color + bold. All others: neutral
  dark gray, regular weight. Never highlight more than one item, never leave
  none highlighted on a section-transition instance.
- Works best for 3-5 section decks — beyond that, a repeated full-page agenda
  costs more attention per transition than it's worth; prefer the persistent
  strip instead at that scale.

## Provenance

Rescued via the [Pattern Promotion Gate](../pattern-promotion-gate.md) —
confirmed reusable beyond the one source deck (`scope: global`).
