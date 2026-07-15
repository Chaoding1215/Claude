# Candidates rescued from the OMEA B2B Summit source deck

Source: the 26-slide original client PPTX that `templates/layouts/omea_b2b_summit/` was
distilled from (re-imported via `pptx_template_import.py` for a fidelity re-check on
2026-07-14). These three patterns did not survive the original 6-role roster distillation —
rescued via the [Pattern Promotion Gate](../../../references/pattern-promotion-gate.md),
user confirmed **promote** for all three.

Staging only — not yet curated into `charts_index.json`. See this directory's `README.md`
for the curation procedure.

---

### gtm_phased_drilldown

- **Source**: OMEA B2B Summit source deck, slide 22 ("GTM Practice Reference: 3 Phases 6 Steps
  for Rapid SME Growth")
- **Category**: 构图/版式 (composition also carries a 层次逻辑 aspect — see the separate
  prose-rule promotion at [`distilled-principles/gtm_phased_drilldown_hierarchy.md`](../../../references/distilled-principles/gtm_phased_drilldown_hierarchy.md)
  (`scope: global`), since the hierarchy principle was confirmed to generalize beyond this
  one source)
- **Proposed summary**: "Pick for a phased process (2-4 phases, each grouping 2-4 steps) that
  also needs per-step or per-phase drill-down detail below the main flow. Skip if the process
  has no phase grouping (use `chevron_chain_with_tail` / `process_flow`) or no drill-down
  content (use a plain step ribbon)."
- **Structural description**: A horizontal ribbon/arrow spans the page with numbered step
  markers; phase-group labels sit above the ribbon, each bracketing 2-3 steps with a dashed
  connector; below the ribbon, a row of 2-4 expanded panels drill into selected steps, each
  panel free to hold its own sub-diagram (the source used a small org/relationship diagram in
  one panel and icon-labeled item rows in others). The existing `05_content_process_framework`
  roster variant only captured the top-level ribbon + step markers — the phase-grouping tier
  and the entire drill-down zone were dropped during the original distillation.
- **Promotion decision**: promoted (pending curation)

### hub_spoke_topology

- **Source**: OMEA B2B Summit source deck, slide 14 ("China Unicom: Building a Green,
  Simplified, Secure, and All-Optical Hotel")
- **Category**: 构图/版式
- **Proposed summary**: "Pick for a technical/network architecture diagram: one central hub
  node connecting to multiple labeled endpoint nodes via distinct connection lines, with
  inline component labels (e.g. splitter, gateway, controller) on the connectors themselves.
  Skip for a generic org chart with no connector-level labels (use `hub_inward_arrows`) or a
  data-flow diagram without a literal hub (use `sankey_chart` / `process_flow`)."
- **Structural description**: A single hub node (source used "MainFTTO") branches to several
  endpoint boxes (source used four rooms/functions: guest room, lobby/corridor, dining room,
  CCTV), each connection line carrying its own small label for the physical/logical component
  it represents. Typically embedded inside a 3-column page (context / diagram / results) rather
  than filling the whole page. No existing roster variant or `charts_index.json` entry covers
  this pattern — it is a net-new addition, not a captured-but-thinned one.
- **Promotion decision**: promoted (pending curation)
- **Corroborating occurrence**: the Huawei SD-WAN executive briefing source
  (distilled 2026-07-15) independently wanted the same pattern class — see
  [`huawei_sdwan_exec_candidates.md`](huawei_sdwan_exec_candidates.md)'s
  corroborating note. Two independent sources now want this pattern; treat as
  a stronger curation priority, not a second candidate.

### screenshot_showcase_grid

- **Source**: OMEA B2B Summit source deck, slide 25 ("Demo & More Details Are Available in
  The Booth")
- **Category**: 构图/版式
- **Proposed summary**: "Pick for presenting 3-4 product screenshots or demo captures side by
  side, each under its own labeled header bar. Skip for a single hero screenshot (use a plain
  image layout) or more than 4 items (use a scrolling/paginated reference instead)."
- **Structural description**: An even grid (source used 2x2) of image slots, each preceded by
  a full-width label bar naming what the screenshot shows. No existing roster variant or
  `charts_index.json` entry covers a multi-screenshot showcase grid; closest neighbors
  (`comparison` family) assume text/data content, not image slots.
- **Promotion decision**: promoted (pending curation)
