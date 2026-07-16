---
description: Opt-in structural-fidelity gate for fidelity/mirror template decks, run between Step 6 and Step 7. Triggered only when the user explicitly asks. Compares each generated page against the templates/ SVG it declares in spec_lock.md page_layouts, using a skin-invariant occupancy metric that catches a template page collapsing into a sparse "skeleton" — a failure the LLM visual self-review does not reliably catch.
---

# Verify Template Fidelity Workflow

> Standalone, **opt-in** structural-fidelity gate. For a **fidelity** or **mirror**
> template deck, it measures — with evidence, not opinion — whether each generated page
> actually reproduces the density and structure of the template it inherited, catching the
> "骨架图" failure where a dense framework diagram is flattened into a few plain boxes.

This workflow is **conditional**, same shape as `verify-charts` / `visual-review`: it never
fires on its own and the default path is unchanged. It exists because ppt-master's other checks
have a blind spot here — `svg_quality_checker.py` validates structural rules and spec-lock drift
(colors/fonts/canvas) but not visual resemblance to the template, and `visual-review` is the
**LLM judging its own output** against a rubric, which does not reliably catch its own laziness.
This gate produces a **measured** signal instead.

## Why it is fidelity/mirror-only

The gate needs a real visual reference. `fidelity` and `mirror` templates have one — the whole
point of those modes is to reproduce a source deck's look. `standard` templates define only
header/footer (content is free), and free-design decks invent the layout, so there is no
"correct" image to compare against and the gate does not apply.

## Skin-invariant by design

`fidelity` templates supply **structure, not skin** ([`executor-base.md`](../references/executor-base.md) §1):
the Executor legitimately swaps the template's placeholder colors and text for the deck's own.
A raw pixel diff would flag that intended re-skin as a failure. This gate compares **grid
occupancy of inked (non-background) pixels**, which is skin-free: a red box and a blue box are
both "inked". It asks "is each region as visually filled as the template said it should be?" —
so recoloring passes, and only a genuine structural collapse (regions inked in the template but
near-empty in the output) fails.

## When to Run

The user **explicitly asks** to verify template fidelity / check that pages match the template /
confirm the fidelity deck did not degrade. Recognize any of:

| Pattern | Example |
|---|---|
| "check the pages match the template" | "did it actually reproduce the BLM template or flatten it?" |
| "verify template fidelity" | "run the fidelity check on the signature page" |
| "make sure it didn't skeletonize the diagram" | "confirm the framework page kept its density" |

**Default is OFF.** Never inferred from deck size, template kind, or model identity — only an
explicit request starts it.

**Prerequisites**:
1. Generated SVG pages exist in `svg_output/` (i.e. Step 6 has run).
2. The deck uses a `fidelity` or `mirror` template — `spec_lock.md page_layouts` is populated.
3. `svg_quality_checker.py` passes first — in particular its **`page_layouts` binding check**
   (the basenames resolve to real `templates/*.svg`). There is no point pixel-comparing a page
   that silently fell back to free design because its basename was a typo; fix that binding error
   before running this gate.

---

## Step 1: Run the gate

```bash
python3 scripts/verify_template_fidelity.py <project_path> --json-out <project_path>/.fidelity_render/report.json
```

- `--mode` defaults to `auto` (reads `replication_mode` from the template's `design_spec.md`);
  pass `--mode fidelity` or `--mode mirror` to force it. Mirror mode adds a raw RGB-diff pass,
  since a mirror page should match the source verbatim apart from edited text.
- `--pages P01,P07` limits the run to specific pages — e.g. just the template's signature page.
- Rendered PNGs and the JSON land in `<project_path>/.fidelity_render/` (a working artifact, like
  `.review/`; safe to delete). Requires an SVG→PNG renderer (`cairosvg`, or `svglib`+`reportlab`)
  plus Pillow and numpy — all already listed in `requirements.txt`. If no renderer is installed
  the gate **refuses to run (exit 2)** rather than reporting a hollow pass.
- Exit codes: `0` all compared pages pass · `1` at least one page failed · `2` could not run
  (no renderer, or nothing to compare).

---

## Step 2: Read the result as evidence

For each page the report gives `structural_similarity`, the list of **underfilled cells**
(regions inked in the template but near-empty in the render — the collapse signal), and, in
mirror mode, `raw_rgb_diff`. A page **fails** when underfilled cells exceed `--max-underfill`
(default 3), or, in mirror mode, when the raw skin diff exceeds `--mirror-tolerance`.

The underfilled cells are grid coordinates `(col, row)` on a 12×8 grid over the 1280×720 canvas —
they point directly at *where* the page thinned out relative to the template.

---

## Step 3: Fix by restoring structure, not by re-skinning

For each failed page, the fix is to **rebuild the collapsed region to the template's density** —
redraw the diagram / grid / dense component the template defines, at the occupancy the template
shows, then re-express it in the deck's locked skin. Do **not** respond by recoloring or by
nudging fonts; the gate is skin-invariant, so only restored structure clears it. Regenerate the
failed pages per [`executor-base.md`](../references/executor-base.md) (one page at a time), re-run
`svg_quality_checker.py`, then re-run this gate on the fixed pages (`--pages`) until they pass.

If a flagged region is a **deliberate** simplification the user approved (the template's density
was genuinely too much for this page's content), that is a legitimate exception — record it and
move on rather than padding the page back up to hit the metric. The gate surfaces collapse for a
human decision; it does not mandate maximal density.

---

## Step 4: Hand back

Once the compared pages pass (or their exceptions are recorded), continue to `SKILL.md` Step 7
(post-processing and export) as usual.

> Note: this workflow does NOT duplicate the Executor or `svg_quality_checker.py`. It adds one
> measured, skin-invariant structural check that neither of them performs, scoped to the
> fidelity/mirror decks where a template reference actually exists.
