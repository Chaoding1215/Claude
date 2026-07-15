# Candidates rescued from the Huawei SD-WAN executive briefing source deck

Source: the 21-slide Huawei SD-WAN executive pitch PPTX distilled into
`templates/layouts/huawei_sdwan_exec/` (2026-07-15). Rescued via the
[Pattern Promotion Gate](../../../references/pattern-promotion-gate.md), user
confirmed **promote** for both.

Staging only — not yet curated into `charts_index.json`. See this directory's
`README.md` for the curation procedure.

---

### competitive_multiplier_bars

- **Source**: Huawei SD-WAN source deck, slides 8 and 14 (market-share timeline
  and Tolly third-party benchmark pages)
- **Category**: 构图/版式
- **Proposed summary**: "Pick for a pairwise performance comparison where the
  headline message is a multiplier ratio (e.g. '3x', '5x faster') rather than
  the raw values themselves. Skip if more than two parties are compared (use
  `grouped_bar_chart`) or the ratio itself isn't the point (use `column_chart` /
  `grouped_bar_chart` with plain value labels)."
- **Structural description**: A short paired-bar cluster where the emphasized
  bar (own product, brand color) carries a large floating "Nx" badge directly
  above it; the muted competitor bar (neutral gray) sits alongside with no
  badge. Distinct from the existing `grouped_bar_chart` entry, whose summary
  has no badge-annotation convention — that entry shows values, this one shows
  a ratio as the primary visual message.
- **Promotion decision**: promoted (pending curation)

### case_study_before_after_stats

- **Source**: Huawei SD-WAN source deck, slides 19 and 20 (China Construction
  Bank and Ping An Technology customer case studies)
- **Category**: 证据/注释呈现方式
- **Proposed summary**: "Pick for a named customer case study needing a clear
  before/after contrast plus 2-3 quantified outcome callouts. Skip if there's
  no before/after framing (use a plain quote/testimonial layout) or more than
  3 stats are needed (use a dashboard-style page)."
- **Structural description**: Two side-by-side panels (before state, muted;
  after state, brand-accented) separated by a centered "VS" marker, with a row
  of 2-3 large stat numbers + short labels beneath, and a source line at the
  foot. Distinct from the existing `comparison_table` / `comparison_columns`
  entries, which compare products/plans/pricing tiers — this pattern is
  specifically an evidentiary customer-proof-point format, not a feature or
  pricing comparison.
- **Promotion decision**: promoted (pending curation)

---

## Corroborating note for an existing staged candidate

`05_content_dense_architecture.svg` in `huawei_sdwan_exec` (representative
hub-and-4-node technical diagram, built from source slides 5/13/15/17) is the
**same pattern class** as `hub_spoke_topology`, already staged in
[`omea_b2b_summit_source_candidates.md`](omea_b2b_summit_source_candidates.md)
— a literal technical/network architecture diagram with labeled connectors,
distinct from the existing generic `hub_spoke` entry (abstract capability
radiating, no connector-level labels). This is a second, independent source
wanting the same not-yet-curated pattern — strengthens the case for curating
`hub_spoke_topology` into `charts_index.json`, not a new candidate in its own
right.
