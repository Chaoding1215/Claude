---
name: setup-matt-pocock-skills
description: Configure the repo infrastructure that the other Matt Pocock engineering skills depend on. Run once before using any engineering flow.
disable-model-invocation: true
---

Configure three things the other engineering skills depend on. Do them in order, one section at a time — present findings, ask, confirm, then write.

## Step 1: Explore

Before asking anything, inspect the repo:
- `git remote -v` to detect GitHub or GitLab
- Look for existing `CLAUDE.md`, `AGENTS.md`, `docs/agents/`, markdown issue files
- Check for prior configurations from this skill

## Step 2: Issue tracker

Determine where issues live. Present your finding and ask the user to confirm or correct.

Options:
- **GitHub Issues** (default if a GitHub remote exists)
- **GitLab Issues** (default if a GitLab remote exists)
- **Local markdown** — good for solo projects with no hosted tracker
- **Other** — user specifies

## Step 3: Triage label vocabulary

Map the five canonical states to the actual label strings used in the tracker. Present defaults and ask the user to confirm or override:

| Canonical state | Default label string |
|---|---|
| needs-triage | `needs-triage` |
| needs-info | `needs-info` |
| ready-for-agent | `ready-for-agent` |
| ready-for-human | `ready-for-human` |
| wontfix | `wontfix` |

## Step 4: Domain documentation layout

Ask whether the repo uses:
- **Single context** — one `CONTEXT.md` at root, one `docs/adr/` directory
- **Multi-context** — `CONTEXT-MAP.md` at root pointing to per-component `CONTEXT.md` files (for monorepos)

## Step 5: Write configuration

Show the user a draft of the output before writing. After confirmation, write:

1. An `## Agent skills` section in `CLAUDE.md` (or `AGENTS.md` if that's the convention) describing the configured infrastructure.
2. Three files in `docs/agents/`:
   - `issue-tracker.md` — tracker type and label vocabulary
   - `domain-docs.md` — context layout and file paths
   - `triage-states.md` — canonical state definitions

Notify the user when complete and suggest running `/ask-matt` to explore the available flows.
