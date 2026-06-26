---
name: handoff
description: Compact the current conversation into a handoff document so a fresh agent can continue in a new session.
disable-model-invocation: true
argument-hint: What will the next session focus on?
---

Compact this conversation into a handoff document for a fresh agent to continue.

## Rules

- Save to the user's OS temp directory (`/tmp` or equivalent) — **not** the workspace.
- Do not duplicate existing artifacts (PRDs, ADRs, issues, plans) — reference them by path or URL instead.
- Redact sensitive data: API keys, passwords, PII.
- Include a **Suggested skills** section listing the skills the next agent should know about.
- Tailor the content based on the user's argument (what the next session will focus on).

## Document structure

```
# Handoff: [brief description]

## Context
[What we were doing and why]

## Current state
[Where things stand right now]

## Key decisions made
[Non-obvious choices and their rationale — reference ADRs/PRDs rather than repeating them]

## Next session focus
[What the user said they want to tackle next]

## Suggested skills
- /[skill] — [why it's relevant]
```

After writing the file, tell the user the path and suggest they open a new session referencing it.
