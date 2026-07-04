# PPT Style Specification — v8

This version resolves the fork v7 flagged (descriptive vs. prescriptive fidelity) and updates the affected rules accordingly. No new samples this round.

## Resolution: descriptive fidelity by default, color is the one prescriptive override

**Decision**: the future apply-skill targets what authors actually, repeatedly do — with one explicit exception for the accent color.

| Dimension | Target for the apply-skill | Rationale |
|---|---|---|
| **Accent color** | **`C7000A`** (template's true accent1) — *not* `C00000` | Explicit override. `C00000` is a habit-driven approximation (PowerPoint's standard-palette "Dark Red" swatch), not the real brand color; corrected deliberately. |
| Secondary/gold accent (senior-audience scenario) | `F4A100` (template's accent3) — *not* `FFC000` | Same override logic, extended by analogy; apply only if/when that scenario actually arises — not pre-emptively generalized to other slots. |
| CJK font | Microsoft Yahei (empirical) | Descriptive. Every sample's own theme declares 宋体/SimSun as default, but authors override to Yahei on nearly every run — Yahei is real, repeated practice, and gets kept as-is rather than "corrected" to the theme's nominal default. |
| Composition grid | Freeform text-box positioning (empirical), not the template's placeholder grid | Descriptive. Grid compliance was rare even in the color-compliant sample (B/SD-WAN, 30% of slides at best, 0% on covers) — see v7. The apply-skill should reproduce how these decks actually get laid out, not the aspirational template geometry. |
| Density floors, image treatment, citation style | As observed per genre (v4/v5) | Descriptive — unaffected by this decision, no prescriptive alternative was ever on the table for these. |

**Why color and not the rest**: color is the one dimension where the "authentic" value is both known precisely (the theme XML gives an exact hex) and cosmetically almost invisible to override (C7000A vs C00000 differ by single-digit RGB units — swapping one for the other doesn't make a drafted deck look unlike its source material the way using the official grid or theme fonts would). Font and grid corrections would produce a visibly different, more "templated" look than what real decks in this corpus actually look like — which would defeat descriptive fidelity. Color correction is effectively free in that sense; the others aren't.

## Updated rule text

**Mandatory rule 1.1 (was: "Accent color is dark red `C00000`")** becomes:

> **Accent color target is `C7000A`.** Empirically, authors across this corpus consistently reach for `C00000` (PowerPoint's standard-palette "Dark Red" swatch) as a close approximation — present as a top-3-frequency color in 5 of 6 content samples (A, B, C, E, F; exception D, which uses the template's actual accent3 `F4A100` gold family for its senior-audience scenario). The apply-skill should render `C7000A` (the template's true accent1) rather than reproducing the `C00000` approximation.

**Preferential rule 2.5 (font family) is unchanged** — Microsoft Yahei stays the target, explicitly *not* corrected to the theme's nominal 宋体 default, per the descriptive-fidelity decision.

**Section 1 composition grid (v6) is retained as reference documentation of the official template, but is explicitly marked out-of-scope as a target for the apply-skill** — kept in the spec for completeness (someone may want brand-compliant grid output later), but the apply-skill built from this spec should not use it by default.

## Changelog vs v7

- **Resolved**: the descriptive/prescriptive fork. Decision: descriptive by default, color is the sole prescriptive override (`C7000A`, and `F4A100` by analogy if the gold scenario arises). Encoded in `SKILL.md` so step 5 doesn't re-ask this on a future run.
- **Updated**: Mandatory rule 1.1's target value, from the empirically-observed `C00000` to the corrected `C7000A`. This is the first rule in the spec whose *target* value differs from its *evidence* value — worth flagging clearly in the apply-skill's eventual Reference section so it's not read as a citation error.
- **Unchanged**: every other rule — this version is a resolution/annotation pass, not a new-evidence pass.
