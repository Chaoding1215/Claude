# PPT Master — Evidence & Density Discipline

Scope: **ppt-master Strategist only.** This is an opt-in reference that operationalizes
two gaps left open by `strategist.md` — what to do when source material is too thin to
fill a page, and how to handle conflicting figures in the source. It does **not** change
default pipeline behavior and it does **not** override any rule in
[`.claude/skills/ppt-master/references/strategist.md`](../../.claude/skills/ppt-master/references/strategist.md);
on any conflict, `strategist.md` wins.

The distilled discipline below is adapted from the MBB evidence method in the `cyber-ppt`
skill, reduced to the parts ppt-master actually lacks. It is a *methodology reference the
Strategist may read on request*, not a new workflow and not a hard gate.

---

## 1. When this applies

Read this only when one of these is true — otherwise ignore it and follow `strategist.md`:

- A page in the §IX outline has **less substance than its `page_rhythm` / `delivery_purpose`
  implies** (e.g. a `dense` page with two thin bullets).
- The source contains the **same metric with two different values** (different period, scope,
  denominator, rounding, or forecast-vs-actual).
- The user explicitly asks to **trace every figure to its source**, or to **audit** where a
  number came from.

None of the above → this file has nothing to add.

---

## 2. Source-density remediation ladder

`strategist.md` sets page count from content weight up front (prevention) and forbids
introducing facts from outside the source (the `content_divergence` hard rule). What it does
**not** name is a remedy once a specific page turns out under-supplied. Use this ladder,
lowest cost first — never silently pad:

| # | Move | Cost | Notes |
|---|---|---|---|
| 1 | **Merge adjacent thin pages** | none | Preferred. Fold the under-supplied page into a neighbor; drop the now-redundant `page_rhythm` slot. Keeps the deck honest instead of stretched. |
| 2 | **Re-scope the page** | none | Narrow the claim to what the evidence actually supports. A `dense` page with two facts becomes a `breathing` or `anchor` page landing one idea. Update `page_rhythm` in **both** `design_spec.md` §IX and `spec_lock.md`. |
| 3 | **Ask the user for more material** | low | The user supplies the missing document / figures. This is the only way to add facts and stay inside the source. |
| 4 | **Targeted `topic-research` for one gap** | medium | Only with the user's go-ahead. Runs the existing [`topic-research`](../../.claude/skills/ppt-master/workflows/topic-research.md) workflow scoped to the single missing fact, and **marks the result as network-sourced, needs verification** in `design_spec.md`. This is the one path that reaches outside the source, so it is explicit and attributed, never silent. |

**Hard rule (inherited, not weakened):** never invent a figure, projection, or claim to fill
space. Padding a page with fabricated substance is a worse outcome than a shorter, honest deck.
If none of 1–4 is available, the page shrinks or merges — it does not get filler.

---

## 3. Data-conflict protocol

When the source gives the same metric two values, **keep both** — do not silently normalize to
one. Silent normalization destroys a fact the audience may need. Procedure:

1. **Record both values** with their source location (page / sheet / table / paragraph) and
   period. In the §IX outline this becomes a small comparison, not a single averaged number.
2. **Only recompute** if the underlying inputs are present in the source and the recomputation
   is arithmetic, not judgment.
3. **State the likely cause** in one clause: rounding, different period, different scope,
   different denominator, forecast-vs-actual, or a probable source error.
4. **Let the user choose** which value the conclusion rests on **when the choice changes the
   conclusion.** If both values support the same SO-WHAT, note the range and move on.

This never overrides §strategist "facts stay sourced" — it is how you stay sourced when the
source disagrees with itself.

---

## 4. Optional evidence traceability

Only when the user asks to audit sourcing. ppt-master has no formal citation-ID mechanism, and
one is not being added to the engine. As a **session-local** discipline, the Strategist may keep
a lightweight table in the project's `analysis/` folder (not a new pipeline artifact, not read by
any script):

| Column | Meaning |
|---|---|
| claim | the fact / figure / judgment as it appears on the slide |
| source location | file + page/sheet/paragraph/table it traces to |
| confidence | `fact` / `directional` / `needs-verification` |
| note | conflict, caveat, or `topic-research` provenance if it came from §2 step 4 |

Every `needs-verification` row must correspond to something surfaced to the user (a §2-step-4
network fetch, or a gap the user was told about). This table is a working aid for the current
deck, discarded with the project — it does not become a durable ppt-master feature.

---

> This file does not duplicate `strategist.md`. It names remediation and conflict-handling
> procedures that `strategist.md` leaves implicit, for the Strategist to apply on request.
> `strategist.md` and `SKILL.md` remain authoritative for how the spec is written and how the
> pipeline runs.
