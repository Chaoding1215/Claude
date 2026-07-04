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
- `text_density_rule`: string. The apparent cap on words/bullets per slide.
- `logic_flow`: string. The narrative arc across slides (e.g. "problem → data
  → conclusion → action items").

Respond in the same language as the source deck's text. Ground every field in
the extraction data — do not invent patterns the data doesn't support.

Extraction data:
{{RAW_JSON}}
