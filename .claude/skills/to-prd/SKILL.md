---
name: to-prd
description: Turn the current conversation into a Product Requirements Document and publish it to the issue tracker.
disable-model-invocation: true
---

Synthesise the current conversation into a PRD without conducting additional interviews.

## Steps

1. **Explore the repo** — understand the current state of the codebase. Apply domain vocabulary from `CONTEXT.md` and respect existing ADRs.
2. **Identify testing seams** — map where this feature will be tested. Prefer existing integration points; minimise new seams across the codebase. Confirm the approach with the user before proceeding.
3. **Generate the PRD** using the template below.
4. **Publish** to the issue tracker with a `ready-for-agent` triage label.

## PRD Template

```
## Problem Statement
[User-perspective description of the issue — what's broken or missing]

## Solution
[User-perspective resolution — what changes in the user's experience]

## User Stories
1. As a [role], I want [action], so that [benefit].
2. ...

## Implementation Decisions
- [Modules and interfaces involved]
- [Technical choices and architectural patterns]
- [Schema changes and API contracts]
- (No file paths — they go stale)

## Testing Decisions
- [External behavior tests and module coverage]
- [Where tests live and what seams they cross]

## Out of Scope
- [Explicitly excluded adjacent concerns]

## Further Notes
[Any additional context]
```
