# Distilled Principles — Index

A **distilled principle** is a prose rule rescued from historical PPT/PDF material via the
[Pattern Promotion Gate](../pattern-promotion-gate.md) — 层次逻辑 (information hierarchy),
用色规则 (color-as-signal rule), or 章节节奏 (cross-page pacing), the three categories the
gate deliberately gives no SVG/script/index of their own (see gate §"Where promotion lands").
This index is that lightweight home: same shape as [`visual-styles/_index.md`](../visual-styles/_index.md)
and [`image-renderings/_index.md`](../image-renderings/_index.md) — one table row + one small
file per principle, never a paragraph inserted into `strategist.md` / `template-designer.md`
prose. Full rationale: [`docs/agents/ppt-master-layout-reference.md`](../../../../../docs/agents/ppt-master-layout-reference.md).

**Why this exists as its own tier**: at small volume, folding a rescued principle straight
into `strategist.md`'s body was tolerable. At the volume of distilling many historical decks,
that turns a file every Strategist invocation reads into a high-churn, merge-conflict-prone
document that grows with content most decks will never use. Moving each principle to its own
file, referenced from one stable table row, makes every future rescue **a pure addition** —
a new file plus one new table row — never an edit to existing prose in a shared file.

---

## 1. Catalog

Each principle has its own file with the rule itself, the failure mode it prevents, and its
source provenance. **Read only the entries whose `scope` matches the current job** — never
glob the whole directory (same discipline as `visual-styles/` and `image-renderings/`).

| Key | One-line rule | Category | Scope | Source |
|---|---|---|---|---|
| [`gtm_phased_drilldown_hierarchy`](./gtm_phased_drilldown_hierarchy.md) | A phase-grouped process must keep the phase→step ownership visible, and drill down only on the steps with enough substance to fill a panel | 层次逻辑 | `global` | OMEA B2B Summit source deck, slide 22 |

---

## 2. Scope field

| Value | Applies to |
|---|---|
| `global` | Any project, any brand |
| `brand:<name>` | Only projects using that brand (e.g. `brand:Huawei`) — replaces editing that brand's `design_spec.md` directly |
| `scenario:<tag>` | Only projects matching that scenario/vertical (e.g. `scenario:financial-briefing`) |

A principle may carry more than one scope tag if it genuinely applies to more than one brand
or scenario — list them comma-separated in the Scope column.

---

## 3. How to use

1. **Strategist**, while authoring `design_spec.md` §V (Layout Pattern Library) or the outline
   generally: read this index's table (not the individual files) and note any `global` entry
   plus any entry whose scope matches the current brand/scenario.
2. Open only the matched entries' own files for the actual rule text.
3. Apply as a **reference**, same standing as the built-in Layout Pattern Library rows in
   `strategist.md` §4 — not a hard requirement, a considered default.
4. **create-template.md** (Pattern Rescue) and **Strategist** (Layout Reference promotion)
   are the only two writers to this index — see the
   [Pattern Promotion Gate](../pattern-promotion-gate.md) for when a rescue reaches here.

**Adding a new principle**: append one row to the table above (do not renumber or reorder
existing rows beyond alphabetical/logical grouping) and create `<key>.md` next to this file.
Never edit an existing principle's file to fold in a new, different rule — a genuinely
different rescued principle gets a new key, even if related to an existing one.
