# PPT Style Specification — v7

This version closes the open follow-up from v6: cross-validating the template's declared composition grid against where the 3 real pptx content samples (A: Telefonica, B: SD-WAN, C: BLM) actually place their title/body shapes. `extract_pptx.py` now records each slide's placeholder positions (type + slide-relative left/top/width/height), directly comparable to `extract_theme.py`'s layout-geometry output.

## New finding: composition-grid compliance is the exception, not the rule

| Sample | Total slides | Slides with **zero** placeholders (pure freeform text boxes/shapes) | Slides with a TITLE-type placeholder | ...of those, matching the template's **content-page** title zone (0.06, 0.07, 0.88, 0.14) | ...matching the template's **cover** title zone (0.07, 0.13, 0.54, 0.10) |
|---|---|---|---|---|---|
| B (SD-WAN) | 20 | 9 (45%) | 8 (40%) | 6 (30% of all slides) | 0 |
| A (Telefonica) | 13 | 12 (92%) | 1 (8%) | 1 (8% of all slides) | 0 |
| C (BLM) | 24 | 23 (96%) | 0 | 0 | 0 |

The only placeholder type C uses anywhere in the deck is `SLIDE_NUMBER`, on a single slide — not a content placeholder at all.

**Reading this together with v6's theme-compliance table**: B was the sample whose embedded *theme* (colors) matched the canonical template exactly. Even so, its *composition* only matches the template's generic content-page grid on 6 of 20 slides (30%), and its cover slide's title/subtitle placeholders — while present and typed correctly (`CENTER_TITLE`/`SUBTITLE`) — sit at a completely different position (left=0.125, top=0.164, width=0.75, height=0.348) than any of the template's 4 official cover skins (left=0.07, top=0.13, width=0.54, height=0.10). So B is faithful to the brand *palette*, but not to the brand *cover layout* — these are independent axes of compliance, and a sample can pass one while failing the other.

A and C have essentially abandoned placeholder-based layout altogether (92% and 96% freeform respectively) — consistent with v6's finding that both were authored outside the shared template (A as a multi-source patchwork, C entirely freehand).

## What this means for the composition-grid rule (v6, section 1)

The grid documented in v6 — 4 cover skins sharing one placeholder geometry, a wide single-zone contents page, a thin-header/large-body content page — is **the org's declared template, not a description of how real decks are actually laid out**. Treat it as prescriptive (what the brand guideline specifies), not descriptive (what authors do). This is a genuine fork, not a data-quality caveat to explain away:

- **If the future apply-skill's goal is brand fidelity** (produce a deck that matches official guidelines): use v6's grid as-is, plus v6's ground-truth colors/fonts (`C7000A`, theme-linked Hans fonts) rather than the empirically-common approximations (`C00000`, manually-applied Yahei).
- **If the goal is descriptive fidelity** (produce a deck indistinguishable from what this org's authors actually turn out): the grid is close to irrelevant — real slides are freeform text boxes positioned ad hoc, and the empirically-common approximations (`C00000` red, manual Yahei) are the actual house style, template notwithstanding.

**This choice needs to be made explicitly before step 5 (Package) runs**, not defaulted silently — it changes which version of nearly every rule (color, font, grid) the packaged apply-skill should treat as ground truth.

## Changelog vs v6

- **Resolved open follow-up**: composition-grid cross-validation against real content samples, previously flagged as not-yet-done. Result: compliance is rare (30% best case, 0% worst case), and even the most-compliant sample fails on the cover layout specifically.
- **New, higher-level finding**: brand-palette compliance and brand-grid compliance are independent — a sample can match one and not the other (B does). Prior versions implicitly treated "this sample matches the template" as a single yes/no property; it isn't.
- **New decision surfaced, not yet made**: descriptive vs. prescriptive fidelity as the target for the eventual apply-skill. Flagged for the user, not resolved unilaterally, since it changes which findings across the whole spec (not just this one) should be treated as ground truth.

## Remaining open follow-up

- Freeform (non-placeholder) shapes' positions aren't captured yet — only typed placeholders are. Since 45-96% of slides in this corpus use no placeholders at all, a true "empirical grid" (where do real authors actually put things, regardless of whether it's a formal placeholder) would need shape-position capture extended to text boxes generally, keyed by role (title-like vs body-like, using the same font-size/position heuristics already used for `title_text`). Not done this round — flagging as the natural next step if the empirical-fidelity path is chosen above.
