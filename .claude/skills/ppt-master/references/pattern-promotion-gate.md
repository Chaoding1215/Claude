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
| 层次逻辑 | Prose rule appended to this project's `design_spec.md`; only if confirmed to generalize, also to `template-designer.md` or `strategist.md` | **Text edit only — no script, no index** |
| 用色规则 | One line appended to `design_spec.md` §II Color Scheme (project) or the relevant brand's `design_spec.md` (if it should generalize) | **Text edit only — no script, no index** |
| 章节节奏 | One sentence appended to `design_spec.md` §V Page Roster's overall description | **Text edit only — no script, no index** |

The three text-only categories get no script or index on purpose: they are prose principles,
not geometric assets — nothing to render, diff, or index. The promotion *is* the edit; there
is no further step. See `docs/agents/ppt-master-layout-reference.md` §4–5 for the full
rationale.
