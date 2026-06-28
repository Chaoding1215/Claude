---
name: improve-codebase-architecture
description: Surface architectural weaknesses in the codebase and propose deepening refactors. Use when the user wants to improve the codebase for agents or maintainability.
disable-model-invocation: true
---

Surface "deepening opportunities" — refactors that transform shallow modules into deeper, more testable ones.

## Phase 1: Explore

Read `CONTEXT.md` and any ADRs. Then walk the codebase organically, looking for friction:

- Where does understanding one concept require bouncing between many small modules?
- Which modules have interfaces that rival their implementations in complexity?
- What code is untested or hard to test?

Apply the **deletion test**: if deleting a module merely relocates complexity rather than reducing it, that's a deepening opportunity.

Use the `/codebase-design` vocabulary throughout: module, interface, depth, seam, adapter, leverage, locality. Avoid generic terms like "component," "service," or "boundary."

## Phase 2: Visual report

Generate a self-contained HTML report (timestamped, placed in temp) showing refactoring candidates. Each candidate card includes:

- Affected files
- Problem statement
- Proposed solution
- Benefits framed as locality and leverage gains
- Before/after diagrams (Mermaid, styled with Tailwind)

Rank candidates by strength. Recommend which one to tackle first.

## Phase 3: Grilling loop

Once the user selects a candidate:

1. Run `/grilling` to explore design constraints interactively.
2. Run `/domain-modeling` to keep terminology current — add undefined concepts to `CONTEXT.md`, sharpen fuzzy terms, propose ADRs for decisions worth recording.
3. The selected candidate becomes an idea you can take into the main flow at `/grill-with-docs`.

## Rules

- Never propose interfaces before grilling; focus on diagnosis first.
- Respect existing ADRs unless the current friction warrants revisiting them.
