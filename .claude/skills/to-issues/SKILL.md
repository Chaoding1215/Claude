---
name: to-issues
description: Decompose a plan, spec, or PRD into independently-actionable issues using vertical slice methodology.
disable-model-invocation: true
---

Decompose the current plan or PRD into independently-grabbable issues.

## Steps

1. **Gather context** — read the current conversation or fetch referenced issues.
2. **Explore the codebase** (optional) — understand current state; identify prefactoring opportunities.
3. **Draft vertical slices** — each issue is a thin but COMPLETE path through every integration layer (schema, API, UI, tests). Not a horizontal slice of one layer.
4. **Quiz the user** — confirm granularity, dependencies, and whether any issues should be merged or split.
5. **Publish** approved issues to the tracker in dependency order.

## Issue Template

```
## Parent
[Link to parent issue or PRD, if applicable]

## What to build
[End-to-end behavior description — no specific file paths]

## Acceptance criteria
- [ ] ...
- [ ] ...

## Blocking dependencies
- [Other issues that must land first]
```

## Rules

- Each completed slice must be independently demoable or verifiable.
- Never close or modify parent issues.
- Avoid hardcoding file paths in issue descriptions — they go stale.
