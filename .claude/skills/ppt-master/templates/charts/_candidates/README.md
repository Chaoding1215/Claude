# Promotion Candidates (staging — not live templates)

Files here are **not** part of the library `charts_index.json` indexes. They are candidates
for 构图/版式 (composition/layout) or 证据/注释呈现方式 (evidence/annotation convention)
patterns rescued via the [Pattern Promotion Gate](../../../references/pattern-promotion-gate.md),
awaiting human curation before being promoted into `charts_index.json` + a real `<key>.svg`.

Full mechanism and rationale: [`docs/agents/ppt-master-layout-reference.md`](../../../../../../docs/agents/ppt-master-layout-reference.md).

## Format

One markdown file per source, named `<source_template_id>_candidates.md`. Each candidate
entry inside follows the same summary grammar as `charts_index.json` so curation is a
copy-paste, not a rewrite:

```markdown
### candidate_key_in_snake_case

- **Source**: `templates/decks/<template_id>/` page `<page_file>` (or Layout Reference
  project `<project_name>` page `<page_key>`)
- **Category**: 构图/版式 | 证据/注释呈现方式
- **Proposed summary**: "Pick for <content shape + scale>. Skip if <reason → alternative>."
- **Structural description**: <what makes this distinct from existing charts_index.json entries — one or two sentences>
- **Promotion decision**: promoted (pending curation)
```

## Curation into charts_index.json

A human (or a session explicitly asked to do this) reviews entries here, and for each one
worth keeping:

1. Author the real `<key>.svg` following [`CHART_STYLE_GUIDE.md`](../CHART_STYLE_GUIDE.md).
2. Add the `charts.<key>` entry to `charts_index.json` with the finalized `summary`.
3. Remove the candidate entry from this staging file (or delete the file if it was the last entry).

Nothing here is read by Strategist's Template Match pass (§ Template Match in
`strategist.md`) — only `charts_index.json` is. Staging candidates have no effect on
generation until curated.
