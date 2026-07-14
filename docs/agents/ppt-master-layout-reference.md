# PPT Master — Layout Reference & Pattern Promotion Gate

Scope: **ppt-master Strategist + create-template workflow only.** This is an opt-in
mechanism, not yet implemented, for two related gaps: (1) letting a single user-supplied
reference image or PDF page ground one page's composition without becoming a permanent
asset, and (2) recovering valuable structural ideas that fidelity-mode template
distillation currently discards when a source page collapses into an existing roster
cluster. It does **not** change default pipeline behavior and does **not** override any
rule in [`strategist.md`](../../.claude/skills/ppt-master/references/strategist.md),
[`template-designer.md`](../../.claude/skills/ppt-master/references/template-designer.md),
or [`create-template.md`](../../.claude/skills/ppt-master/workflows/create-template.md);
on any conflict, those files win.

Status: **implemented.** Originally designed and shipped 2026-07-14; §4–6 below were revised
the same day after a scaling problem surfaced (see the note at the top of §4) — this file
reflects the current, corrected design, not the original one.

---

## 1. Two entry points, one shared gate

| Mechanism | Trigger | What it produces if nothing is promoted |
|---|---|---|
| **A — Layout Reference** | User supplies a reference image or PDF page for one specific page during Strategist authoring | A project-scoped `spec_lock.md` entry, structurally verified once, discarded with the project |
| **B — Pattern rescue** | `create-template.md` fidelity-mode clustering collapses a source page into an existing roster variant, but that page has a distinctive sub-pattern | Nothing — the page is absorbed into the cluster exactly as today |

Both mechanisms can surface a pattern worth keeping beyond its immediate use. Rather than
each deciding independently, both route through the same **Pattern Promotion Gate**
(§3) so the question and the bookkeeping are asked the same way regardless of which
mechanism found the pattern.

---

## 2. Mechanism A — Layout Reference (per-page, use-once by default)

**Input.** A new optional key in the project's `spec_lock.md`:

```yaml
layout_references:
  P07: { source: "refs/annual_report_2023.pdf", pdf_page: 12 }
  P09: { source: "refs/board_report.pdf", pdf_page: 4, region: [58, 12, 40, 50] }
  P11: { source: "refs/competitor_deck_screenshot.png" }
```

- `source`: path to an image (PNG/JPG) or a PDF. A PDF **must** carry `pdf_page` (1-based),
  or an inline `#page=N` suffix on the path — pick one form, not both.
- `region` (optional): normalized `[x, y, w, h]` in percent of the full page canvas. Omit for
  a reference that is already a cropped/local screenshot; supply it to point at one region
  of a larger reference page without pre-cropping.

**Authoring rule.** Strategist consults the reference for composition and structure only —
region proportions, visual hierarchy, decorative treatment. Any text, numbers, or labels
visible in the reference are **not** trustworthy content; real content still comes only from
the source material / `spec_lock.md`, exactly as today's evidence discipline already
requires. This is not a new rule, just a restatement of the existing one for a new input.

**Verification.** After Executor produces the page's SVG, run the new pairwise mode of
`verify_template_fidelity.py` (§4) comparing the generated SVG against the reference. This
reuses the existing skin-invariant occupancy-grid comparison — no new algorithm.

**Default disposition.** Use-once. The `layout_references` entry lives only in this
project's `spec_lock.md` and is never read by another project. Promotion (§3) is the
explicit exception, not the default.

---

## 3. The Pattern Promotion Gate

Triggered when: (a) a Mechanism-A page passes its fidelity check, or (b) `create-template.md`'s
fidelity clustering notices a collapsed page with a distinctive sub-pattern.

**Step 1 — classify (multi-select).** Ask which kind(s) of value the pattern carries; a
single source page can carry more than one:

- [ ] 构图/版式 (composition/layout — where things sit, column/hero/density shape)
- [ ] 层次逻辑 (information hierarchy — what gets visual weight, what order the eye follows)
- [ ] 证据/注释呈现方式 (evidence/annotation convention — footnote chips, caveat boxes, "so what" bars)
- [ ] 用色规则 (color-as-signal rule — how color is deployed to mean something, not the static palette)
- [ ] 章节节奏 (cross-page density/pacing rhythm — a sequence property, not a single-page one)

**Step 2 — per selected category, discard or promote.** Ask separately for each checked
category — a page can promote its hierarchy logic while discarding its literal composition,
or vice versa; the two decisions are independent.

> "[category] — (a) 仅本次使用，用完即弃；还是 (b) 沉淀成可复用的通用模式？"

**Step 3 — record the decision.** Whichever categories were promoted or discarded, write a
`promotion` field next to the pattern's entry (`spec_lock.md layout_references` for
Mechanism A, the candidate note for Mechanism B) so a later read of the project shows what
was decided and why — never a silent, unrecorded choice.

---

## 4. Where each category's promotion actually lands

**Revision note (2026-07-14): this section replaces the original design.** The first version
routed 层次逻辑 / 用色规则 / 章节节奏 straight into `design_spec.md` / `strategist.md` /
`template-designer.md` / a brand's `design_spec.md` — tolerable for one rescue, but the user
identified the real use case up front: distilling **many** historical PPT/PDF decks. At that
volume, "edit a shared, always-loaded file per promotion" means high-churn writes to the exact
files every Strategist invocation reads, rising merge-conflict risk across concurrent
distillation runs, and no independent unit to audit or remove a specific rule later. One
rescue (`gtm_phased_drilldown_hierarchy`, §category 层次逻辑) had already been written directly
into `strategist.md`'s Layout Pattern Library table under the old design — it was rolled back
and re-landed under the corrected design below as the first real entry.

Not all five categories have the same shape of "asset," so they don't all promote to the same
place — but none of them promote by editing an existing shared file's body anymore:

| Category | Promotion target | Mechanism |
|---|---|---|
| 构图/版式 | `templates/charts/_candidates/<source>_candidates.md` (staging) → human-curated into `templates/charts/charts_index.json` + a new `<key>.svg` | New staging file + existing index, unchanged schema |
| 证据/注释呈现方式 | Same as above — `charts_index.json` already has a structural-type branch; add keys like `evidence_tag_chip`, `so_what_ribbon` | Reuses existing mechanism, no new branch needed |
| 层次逻辑 | New file in [`references/distilled-principles/`](../../.claude/skills/ppt-master/references/distilled-principles/_index.md) + one new row in its `_index.md` | **New file + index row — never an edit to `strategist.md` prose** |
| 用色规则 | Same library, tagged `scope: brand:<name>` if brand-specific or `scope: global` if not | **New file + index row — never an edit to a brand's `design_spec.md`** |
| 章节节奏 | Same library, tagged `scope: scenario:<tag>` if scenario-specific or `scope: global` if not | **New file + index row — never an edit to a project's `design_spec.md` on the "generalize" path** |

**Why all three text categories now share one library instead of three destinations:** the
only real difference between them is *what the rule is about* (hierarchy / color / pacing),
not *where it should physically live* — a `scope` tag on the entry (§ below) does the
generalization/brand/scenario targeting that used to require picking between a project file,
a brand file, or a canonical reference file. One library, one consistent append-only shape.

This mirrors a pattern the codebase already uses successfully for a different axis of
variation — [`references/visual-styles/`](../../.claude/skills/ppt-master/references/visual-styles/_index.md)
and [`references/image-renderings/`](../../.claude/skills/ppt-master/references/image-renderings/_index.md)
both use "one index table + one file per named entry, read only what's relevant, never glob
the directory." `distilled-principles/` is the same shape applied to rescued prose principles
instead of visual styles or AI-image renderings.

---

## 5. Consequence: promotion is a pure addition, not an edit to shared files

Every promotion of 层次逻辑 / 用色规则 / 章节节奏 now means exactly two writes: **one new
`distilled-principles/<key>.md` file, and one new row in `distilled-principles/_index.md`.**
Neither touches `strategist.md`, `template-designer.md`, `create-template.md`, or any brand's
`design_spec.md` — those four get exactly **one** stable pointer sentence each (already
written, see §6), and never need editing again as new principles accumulate. 构图/版式 and
证据/注释呈现方式 keep their existing `_candidates/*.md` staging → `charts_index.json`
curation path, which was already append-only and did not need correcting.

This is still intentionally light — no registrar script, no schema validation, no JSON for
the prose entries (a markdown table row is enough, same as `visual-styles/_index.md`). What
changed is *only* where the row and file land, not how much process surrounds adding them.

---

## 6. Files changed (implementation log)

| File | Change |
|---|---|
| `scripts/verify_template_fidelity.py` | Added `--pair --generated <svg> --reference <image\|pdf> [--pdf-page N] [--region x,y,w,h] [--json-out]`. Reuses `compare_page()` unchanged; adds `_load_reference_to_png()` (rasterize PDF page or load+resize a raster image) and `_crop_region()` (percent-box crop on both sides before comparing). Existing project-level path untouched — tested full-page, region-crop, and 5 error paths with zero regression. |
| `references/strategist.md` | Documented the `layout_references` schema near §4 Layout Pattern Library; documented the authoring rule (reference informs composition only, never trusted for content). One stable pointer line to `distilled-principles/_index.md` — this is the only Layout-Pattern-Library edit this file needs going forward. |
| `references/pattern-promotion-gate.md` | The shared gate itself. Routing table's three text-rule rows point at `distilled-principles/`, not at `design_spec.md` / brand files. |
| `workflows/create-template.md` | After fidelity clustering, for a collapsed page with a distinctive sub-pattern, invokes the shared gate instead of silently absorbing the page into its cluster. |
| `templates/charts/_candidates/` | Staging ground for 构图/版式 and 证据/注释呈现方式 promotions awaiting human curation into `charts_index.json`. Contains `omea_b2b_summit_source_candidates.md` (3 real rescued candidates as of this writing). |
| `templates/charts/charts_index.json` | Gains new keys only after a human curates a staged candidate — never written to directly by the gate. |
| `references/distilled-principles/_index.md` + `references/distilled-principles/<key>.md` | New library for 层次逻辑 / 用色规则 / 章节节奏. Contains `gtm_phased_drilldown_hierarchy` (`scope: global`) as of this writing — the rolled-back-and-relanded entry described in §4. |

---

> This file does not duplicate `strategist.md`, `template-designer.md`, or
> `create-template.md`. It names a new opt-in mechanism those files don't yet have. On any
> conflict, those three remain authoritative.
