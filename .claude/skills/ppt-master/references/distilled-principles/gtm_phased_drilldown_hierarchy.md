---
key: gtm_phased_drilldown_hierarchy
category: 层次逻辑
scope: global
source: OMEA B2B Summit source deck, slide 22 ("GTM Practice Reference: 3 Phases 6 Steps for Rapid SME Growth")
---

# Grouped-tier drill-down

A phased/staged process where 2-4 steps nest under each phase, and only selected steps
warrant expanded detail.

**Composition**: Phase labels bracket their steps above a step ribbon (dashed connector
groups 2-3 markers per phase); a lower row holds 2-4 expanded panels, one per selected step,
each free to hold its own sub-diagram — do not expand every step, only the ones with enough
substance to fill a panel.

## Why this is its own pattern, not a plain step ribbon

A flat ribbon (numbered steps only) loses the phase→step ownership relationship the moment it
has more than one grouping tier — the viewer can no longer tell which steps belong to which
phase, and there's nowhere for the deck to go deeper on the steps that matter most. The two
tiers (phase-grouping above, selective drill-down below) are what make this different from
`chevron_chain_with_tail` / `process_flow` in the chart catalog, which are single-tier.

## Provenance

Rescued via the [Pattern Promotion Gate](../pattern-promotion-gate.md) from a real source
deck's process page that a fidelity-mode roster extraction had flattened down to the bare
ribbon, losing both the phase-grouping tier and the entire drill-down zone — confirmed
reusable beyond that one project (`scope: global`).
