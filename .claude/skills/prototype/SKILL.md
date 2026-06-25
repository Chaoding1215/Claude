---
name: prototype
description: Build throwaway code to answer a specific design question.
disable-model-invocation: true
---

A prototype is **throwaway code that answers a question**. The question decides the shape.

## Two branches

**Logic branch** — the question is about state or business logic:
- Build an interactive terminal app
- Display full state after each action
- In-memory state only (no persistence unless persistence is the thing being tested)

**UI branch** — the question is about what something should look like:
- Build multiple UI variations on a single route
- Toggle between them via URL parameter

If unclear which branch applies, identify it from the user's prompt and surrounding code, or ask.

## Rules (both branches)

1. **Mark as throwaway** — name it obviously (`prototype-`, `spike-`, etc.). Place it near the relevant production code but never mixed in.
2. **Single command** — runnable via one project task (`pnpm`, `python`, etc.) with no extra setup.
3. **No persistence** — keep state in memory unless persistence is the thing being tested.
4. **Minimal polish** — skip tests, error handling beyond core functionality, and unnecessary abstractions.
5. **Show the state** — display full state changes after each interaction so learnings are visible.

## After the prototype answers its question

- Delete it, or integrate validated decisions into production code.
- Document the question and answer (commit message, ADR, or note) before removal.
- Never let prototype code become permanent.
