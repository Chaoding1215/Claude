# Step 2 prompt — single-sample style profile

Feed this one raw extraction JSON at a time (`.distill-cache/raw/<hash>.json`).
Never batch multiple samples into one call here — batching happens in step 3.

---

You are a senior presentation design consultant. Below is structured extraction
data for one deck. Analyze it and output a single JSON object — no prose outside
the JSON — with exactly these fields:

- `layout_pattern`: string. The recurring layout structure (e.g. "each section:
  1 title slide + 3 content slides + 1 summary slide").
- `color_role_mapping`: object mapping each hex color to its role (`primary`,
  `accent`, `background`, `text`, etc.), inferred from frequency and position.
- `typography_hierarchy`: array of `{level, size_pt, usage}` — e.g. title vs
  body font sizes and what each is used for.
- `data_viz_preference`: object describing which chart/table types appear and
  in what scenarios (e.g. "bar charts for comparisons, line charts for trends
  over time").
- `text_density_rule`: string. The apparent cap on characters/bullets per slide.
- `logic_flow`: string. The narrative arc across slides (e.g. "problem → data
  → conclusion → action items").
- `image_treatment`: object describing where images are placed (`zone`
  distribution — full-bleed vs corner/edge vs centered), whether they're
  usually captioned, and any size/coverage pattern (e.g. "full-bleed hero
  images on section-opener slides, small captioned screenshots elsewhere").
- `citation_style`: string. How the deck attributes data to its source, if at
  all — e.g. "external market figures carry a small-font 'Source: X' footer;
  internal/proprietary figures are uncited" or "no citation markers found in
  this sample." Absence of citations is itself a finding — report it, don't
  skip the field.
- `argument_structure` (pptx sources only — omit for PDF, don't guess): string.
  The typical number of content points (`content_paragraph_count`) on a
  substantive slide, and whether it's flat or bimodal (e.g. "median 18 points
  per slide, fairly flat" vs "bimodal — most slides carry 2-3 navigation
  points, a minority carry 20+ in a dense explanation slide").
- `diagram_convention` (pptx sources only — omit for PDF): string. What
  `diagram_geometry` reveals about non-text diagram shapes, interpreted using
  the slide's title/text as context — e.g. "recurring 2D icon grids (4-8 rows
  x 3-6 cols) used for capability/logo walls; no single-row or single-column
  sequence diagrams found, so no evidence of funnel/timeline/process-arrow
  conventions in this sample." The geometry alone can't distinguish a real
  matrix from an unstructured scatter — use the nearby text to decide, and
  say so if you can't tell.
- `branding_footer`: string. Page-number/confidentiality/logo convention found
  (`branding_markers`, `placeholders` of type `SLIDE_NUMBER`/`FOOTER`/`DATE`),
  or its explicit absence — e.g. "'{page} Huawei Confidential' on every page"
  or "no footer/branding marker found in this sample." Absence is a finding.

Respond in the same language as the source deck's text. Ground every field in
the extraction data — do not invent patterns the data doesn't support.

Extraction data:
{{RAW_JSON}}
