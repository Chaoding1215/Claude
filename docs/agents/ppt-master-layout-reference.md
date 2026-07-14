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

Status: **design only — not implemented.** This file is the plan; nothing below has been
built yet.

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

Not all five categories have the same shape of "asset," so they don't all promote to the
same place. Two of them are deliberately **not** given a new script or index — see the note
at the end of this section for why.

| Category | Promotion target | Mechanism |
|---|---|---|
| 构图/版式 | `templates/charts/_candidates/<source>_candidates.md` (staging) → human-curated into `templates/charts/charts_index.json` + a new `<key>.svg` | New staging file + existing index, unchanged schema |
| 证据/注释呈现方式 | Same as above — `charts_index.json` already has a structural-type branch; add keys like `evidence_tag_chip`, `so_what_ribbon` | Reuses existing mechanism, no new branch needed |
| 层次逻辑 | A prose rule appended to **this project's** `design_spec.md`, and — only if the user confirms it should generalize beyond this one project — to [`template-designer.md`](../../.claude/skills/ppt-master/references/template-designer.md) or [`strategist.md`](../../.claude/skills/ppt-master/references/strategist.md) as a named principle | **Text edit only — no script, no index** |
| 用色规则 | A one-line rule appended to `design_spec.md` §II Color Scheme (project-level) or the relevant brand's `design_spec.md` (if it should generalize to every deck using that brand) | **Text edit only — no script, no index** |
| 章节节奏 | A sentence appended to `design_spec.md` §V Page Roster's overall description (e.g. "sections alternate dense-analysis / breathing pages") | **Text edit only — no script, no index** |

**Why 层次逻辑 / 用色规则 / 章节节奏 get no new script or directory:** these three are prose
principles, not geometric assets — there is nothing to render, diff, or index. Building a
schema/script for them would force a rule like "lead with the conclusion, not the evidence"
into a rigid structured field it doesn't need, and no downstream tool would ever query it
programmatically (Strategist just reads prose, same as it reads every other `design_spec.md`
section today). A file edit is the entire mechanism, by design — not a placeholder for
future tooling.

---

## 5. Consequence: promotion for these three categories is always a manual MD edit

Because §4 gives 层次逻辑 / 用色规则 / 章节节奏 no persisted script or index, **every time
one of them is promoted, the only thing that happens is someone (Strategist, in the current
session) edits the relevant `design_spec.md` (or, for a generalize-beyond-this-project
decision, `template-designer.md` / `strategist.md` / a brand's `design_spec.md`) by hand.**
There is no batch job, no registrar script, no JSON index entry for these three — unlike
构图/版式 and 证据/注释呈现方式, which do get a durable file (`_candidates/*.md`, eventually
`charts_index.json` + an `.svg`) plus a registrar step.

This is intentional, not a stopgap: the promotion *is* the edit. If a later session finds
these three categories are being promoted often enough that hand-editing is a real burden,
that would be the signal to reconsider — not evidence the current design is incomplete.

---

## 6. Files to change (implementation plan, not yet executed)

| File | Change |
|---|---|
| `scripts/verify_template_fidelity.py` | Add `--pair --generated <svg> --reference <image\|pdf> [--pdf-page N] [--region x,y,w,h] [--json-out]`. Reuses `compare_page()` unchanged; adds `_load_reference_to_png()` (rasterize PDF page or load+resize a raster image) and `_crop_region()` (percent-box crop on both sides before comparing). Existing project-level path is untouched. |
| `references/strategist.md` | Document the `layout_references` schema (§2 of this file) near §4 Layout Pattern Library; document the authoring rule (reference informs composition only, never trusted for content). |
| New `references/pattern-promotion-gate.md` | The shared gate itself (§3 of this file) — both Mechanism A (strategist.md) and Mechanism B (create-template.md) point to this one definition instead of duplicating the question/schema. |
| `workflows/create-template.md` | After fidelity clustering, for a collapsed page with a distinctive sub-pattern, invoke the shared gate instead of silently absorbing the page into its cluster (today's behavior when no promotion is chosen). |
| `templates/charts/_candidates/` (new dir) | Staging ground for 构图/版式 and 证据/注释呈现方式 promotions awaiting human curation into `charts_index.json`. |
| `templates/charts/charts_index.json` | Gains new keys only after a human curates a staged candidate — never written to directly by the gate. |

---

> This file does not duplicate `strategist.md`, `template-designer.md`, or
> `create-template.md`. It names a new opt-in mechanism those files don't yet have. On any
> conflict, those three remain authoritative.
