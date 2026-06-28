# Learning Record Format

Learning records are stored in `./learning-records/` with sequential naming (`0001-slug.md`, `0002-slug.md`, etc.) and serve as teaching equivalents of Architecture Decision Records.

## Core Purpose

They capture "non-obvious lessons, key insights, and stated prior knowledge" to inform future instruction and calculate the zone of proximal development.

## Minimal Template

A learning record requires only a title and 1–3 sentences explaining what was learned and its relevance to future sessions. That suffices; extensive sections aren't mandatory.

## Optional Additions

Include these only when they meaningfully enhance the record:
- **Status** frontmatter (active or superseded reference)
- **Evidence** (how understanding was demonstrated)
- **Implications** (what this enables or prevents next)

## When to Create One

Write a record when:
1. The user demonstrated genuine understanding of something non-trivial
2. The user disclosed prior knowledge and its depth
3. A misconception was identified and corrected
4. The mission shifted based on new learning

## When Not to Write

Skip records for material merely covered without evidence, definitions already in the glossary, or session activity logs.

## Supersession Practice

Rather than delete contradicted records, mark them `Status: superseded by LR-NNNN` to preserve the evolution of understanding.
