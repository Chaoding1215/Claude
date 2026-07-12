---
description: Opt-in pilot-page preview gate at the start of the Executor phase. Triggered only when the user explicitly asks. Before the normal continuous SVG pass, the Executor renders one or two representative pages first and HARD STOPS so the user can confirm composition, density, and visual language before the whole deck is committed.
---

# Blueprint Preview Workflow

> Standalone, **opt-in** pilot-page gate. The default Executor phase generates every SVG page
> in one continuous pass and the only visual check is *after* pages are drawn. When the user
> explicitly asks to see the look before committing the deck, the Executor draws a small set of
> **pilot pages** first, renders them through the existing pipeline, then **stops** for the user
> to confirm — or adjust the spec — before the remaining pages are generated.

This workflow is **conditional**, same shape as `refine-spec`: it never fires on its own and the
default path is unchanged. It fills the gap that `refine-spec` does not — `refine-spec` reviews the
**text spec** before generation; this reviews the **realized composition** of a real page. It is
implemented entirely in ppt-master's native SVG terms: pilot pages are ordinary `svg_output/`
pages rendered by the existing tooling, **not** throwaway bitmap mockups. Nothing about the
one-continuous-pass, hand-authored-SVG discipline changes for the rest of the deck.

## When to Run

The user **explicitly asks** to preview the look / a sample page / the composition before the
full deck is generated. Recognize any of:

| Pattern | Example |
|---|---|
| "show me one page first" | "do a sample slide before you build all of them" |
| "let me see the style on a real page before the rest" | "render the cover and one content page, then pause" |
| "preview the composition before committing the deck" | "I want to approve the look before you grind out 20 slides" |

**Default is OFF.** No request → the Executor runs its normal continuous pass and this workflow
never starts. Do **not** infer it from deck size, template kind, or model identity.

**Prerequisite**: `design_spec.md` + `spec_lock.md` exist and the Strategist confirmation stage is
settled (i.e. the pipeline is at the entry of Step 6). This gate sits at the *start* of the
Executor phase, not before it.

---

## Step 1: Pick the pilot pages

Choose the **smallest set that de-risks the look** — normally 1–2 pages, never the whole deck:

- **The cover (`P01`)** — its `Cover impact` composition is the highest-variance page and sets tone.
- **One representative content page** — pick the page whose `page_rhythm` is `dense` and whose
  `page_layouts` / `page_charts` entry is the most-reused structure in the deck, so confirming it
  validates the pattern the rest inherit.

For a **fidelity / mirror template** deck (e.g. a `create-template` `fidelity` package), prefer the
template's **signature page** as the second pilot — the structurally richest reused variant
(dense diagram, network/framework figure, curve-heavy chart). Confirming it early is where a
fidelity deck most often diverges from intent.

State which pages you picked and why in one line, then proceed — do not ask the user to choose the
pilot set unless they offered a preference.

---

## Step 2: Generate and render the pilot pages only

Generate **only** the pilot pages, following `executor-base.md` exactly as in the normal Step 6:
per-page re-read of `spec_lock.md`, hand-authored SVG, one page at a time, into `svg_output/`.
Then make them viewable through existing tooling — no new mechanism:

1. Run the **Quality Check Gate** on what exists: `scripts/svg_quality_checker.py <project_path>`.
   Any `error` blocks — fix and re-check before showing the user (a broken pilot is not a preview).
2. Start / reuse live preview (`scripts/svg_editor/server.py --live --daemon`) so the user sees the
   real rendered page, per [`live-preview.md`](./live-preview.md).

Do **not** run `finalize_svg.py` or `svg_to_pptx.py` here — pilot review happens on the working
`svg_output/` SVGs, which stay in the pipeline. Export is still Step 7, once the full deck exists.

---

## Step 3: ⛔ HARD STOP — present, confirm, or revise

Present the rendered pilot pages and **wait for explicit approval or revision before generating any
further page**. This is a conditional BLOCKING point that exists only on this opt-in path; the
default pipeline keeps its auto-proceed discipline untouched.

Discuss in **prose** — do not emit a scored rubric or per-axis grades (against project convention).
The user is judging the realized page, so keep the lenses concrete and composition-level:

- **Composition** — does the layout follow the page's information weight, or fall back to a uniform
  symmetric grid (the "AI-generated" look)?
- **Density** — does the filled page match the `page_rhythm` / `delivery_purpose` intent, or is it
  thinner / more crammed than planned? (If thinner, see
  [`docs/agents/ppt-master-evidence.md`](../../../../docs/agents/ppt-master-evidence.md) §2.)
- **Visual language** — do the locked colors, typography ramp, icon character, and any chart
  structure read as intended on a real page?

Route the outcome:

- **Approve** → go to Step 4.
- **Small composition fix** (spacing, an element's position, one color role) → adjust the pilot SVG
  directly (or via live-preview edit), re-run the Quality Check Gate, re-present.
- **Spec-level change** (color scheme, typography, layout pattern, page rhythm, outline) → this is a
  spec revision, not an Executor tweak. Hand back to [`refine-spec.md`](./refine-spec.md) to change
  `design_spec.md` + `spec_lock.md` (keep both in sync; `spec_lock.md` wins on divergence), then
  **regenerate the pilot** under the revised spec before continuing. Do not carry a
  spec-contradicting pilot forward.

Iterate as many rounds as the user wants. The loop ends only when the user explicitly approves the
pilot.

---

## Step 4: Hand back to the continuous pass

Once the pilot is approved, the locked spec and the approved pilot pages both reflect the final look.
Return to `SKILL.md` Step 6 and generate the **remaining** pages in the normal one-continuous-pass
discipline — the approved pilot pages are already done and are **not** redrawn. Then run the
Quality Check Gate across the full `svg_output/` and continue to Step 7 as usual.

> Note: this workflow does NOT duplicate the Executor. It inserts one see-before-you-commit
> checkpoint at the start of generation, implemented with the existing SVG pipeline and preview
> tooling. `executor-base.md` / `SKILL.md` remain authoritative for how pages are generated.
