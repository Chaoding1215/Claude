---
name: writing-great-skills
description: Reference for writing and editing skills well.
disable-model-invocation: true
---

A skill exists to wrangle determinism out of a stochastic system. **Predictability** — the agent taking the same *process* every run, not producing the same output — is the root virtue.

## Invocation models

**Model-invoked**: the agent can trigger the skill autonomously based on its description. Adds context load. Use when the agent must reach the skill on its own, or another skill must invoke it.

**User-invoked** (`disable-model-invocation: true`): only triggered manually. Reduces context load, increases cognitive load. Use for skills the user initiates themselves.

## Writing descriptions (model-invoked skills)

- Front-load the **leading word** — the most distinctive term that triggers invocation.
- List distinct triggers; don't duplicate synonyms.
- Exclude information already in the body.

## Information hierarchy

Rank content from highest to lowest priority:

1. **Steps** — in-skill, ordered actions with checkable completion criteria
2. **Reference** — in-skill definitions, rules, facts consulted on demand
3. **External reference** — pointers to files or URLs outside the skill

Move content down the ladder when possible. Keep the main body scannable.

## Splitting skills

Divide only when justified by:
- **Invocation** — two distinct leading words that shouldn't share a trigger
- **Sequence** — an early step that gets skipped when bundled with later steps (premature completion)

## Failure modes

- **Premature completion** — steps that end before genuine completion criteria are met
- **Duplication** — the same meaning appearing in multiple places
- **Sediment** — stale content that accumulates and is never pruned
- **Sprawl** — skills too long to scan, even when all content is relevant (use external reference files)
- **No-ops** — sentences that don't change agent behavior

## Leading words

Compact, pretrained concepts anchor agent execution more efficiently than long explanations. "tight feedback loop," "tracer bullet," "red-green-refactor," "vertical slice" carry more weight per token than prose equivalents.
