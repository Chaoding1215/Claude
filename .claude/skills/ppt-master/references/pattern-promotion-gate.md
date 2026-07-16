# Pattern Promotion Gate

Shared confirmation gate for two entry points: Layout Reference (Strategist, per-page) and
Pattern Rescue (create-template.md, fidelity-mode clustering). Both route through this one
definition instead of each asking the question their own way. Full rationale and file-level
plan: [`docs/agents/ppt-master-layout-reference.md`](../../../../docs/agents/ppt-master-layout-reference.md).

Default behavior without this gate: Layout Reference is use-once (discarded with the
project); a collapsed fidelity-cluster page is silently absorbed. This gate is the only path
that turns either into a durable, reusable asset — it is never invoked automatically.

## Step 1 — classify (multi-select)

A single source page can carry more than one kind of value. Ask which apply:

- [ ] **构图/版式** — composition/layout: where things sit, column/hero/density shape
- [ ] **层次逻辑** — information hierarchy: what gets visual weight, what order the eye follows
- [ ] **证据/注释呈现方式** — evidence/annotation convention: footnote chips, caveat boxes, "so what" bars
- [ ] **用色规则** — color-as-signal rule: how color is deployed to mean something (not the static palette)
- [ ] **章节节奏** — cross-page density/pacing rhythm: a sequence property, not a single-page one

## Step 2 — per selected category, discard or promote

Ask separately for each checked category — decisions are independent. A page may promote its
hierarchy logic while discarding its literal composition, or vice versa.

> "[category] — (a) 仅本次使用，用完即弃；还是 (b) 沉淀成可复用的通用模式？"

## Step 3 — record the decision

Every classified category gets a `promotion: discard | promoted` entry recorded next to the
pattern (`spec_lock.md layout_references` for Layout Reference; the candidate note for
Pattern Rescue). Never leave the choice unrecorded.

## Where promotion lands, by category

| Category | Destination | Mechanism |
|---|---|---|
| 构图/版式 | `templates/charts/_candidates/<source>_candidates.md` (staging) → human-curated into `templates/charts/charts_index.json` + a new `<key>.svg` | New staging file + existing index |
| 证据/注释呈现方式 | Same staging/index path — `charts_index.json` already has a structural-type branch; add keys like `evidence_tag_chip`, `so_what_ribbon` | Reuses existing mechanism |
| 层次逻辑 | New file in [`distilled-principles/`](distilled-principles/_index.md) + one new row in its `_index.md` | New file + index row — never an edit to `strategist.md` / `template-designer.md` prose |
| 用色规则 | Same — new `distilled-principles/` file, tagged `scope: brand:<name>` if it's brand-specific or `scope: global` if not | New file + index row — never an edit to a brand's `design_spec.md` |
| 章节节奏 | Same — new `distilled-principles/` file, tagged `scope: scenario:<tag>` if scenario-specific or `scope: global` if not | New file + index row |

All three text-only categories land in the same library, distinguished only by their
`category` and `scope` frontmatter fields — never by a different destination file. This is
deliberate: at the volume of distilling many historical decks, every promotion must be a
**pure addition** (one new small file, one new index row) — never an edit to a shared,
always-loaded file like `strategist.md`, `template-designer.md`, or a brand's `design_spec.md`.
Those three canonical files each get exactly one stable pointer to `distilled-principles/_index.md`,
written once, never touched again per promotion. See
`docs/agents/ppt-master-layout-reference.md` §4–5 for the full rationale and the incident that
prompted this design (an earlier rescue was written directly into `strategist.md`'s body, then
rolled back into this library once the volume problem was recognized).
