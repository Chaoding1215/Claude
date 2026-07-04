---
name: distill-slide-style
version: "1.0.0"
description: Distill a style specification from a corpus of PPT/PDF samples — layout patterns, color roles, typography, chart preferences, density limits, narrative flow. Use when the user wants to mine, extract, or update design norms from a batch of decks or documents.
disable-model-invocation: true
---

Mine a sample corpus into a versioned, evidence-cited style specification. Incremental and repeatable — re-running after new samples arrive should only touch what changed.

Output docs are versioned per-corpus and live alongside the sample directory (e.g. `reference/style-spec-v{N}.md`, `reference/profiles/`), not inside this skill package — this package stays generic and reusable across different corpora; a specific corpus's findings and decisions don't belong here (see General methodology and "This corpus's specific findings" below).

## Steps

1. **Extract** — run `scripts/extract_pptx.py` and/or `scripts/extract_pdf.py` over the sample directory. Each script caches by content hash under `.distill-cache/raw/`, so unchanged files are skipped on re-runs. If one or more template/master files are available (mostly-empty files whose purpose is the template itself, not real content), also run `scripts/extract_theme.py` over all of them together plus every pptx sample — it already accepts multiple paths in one call, so this scales to however many template variants exist, not just one. This reads ground truth (theme color/font scheme, named-layout placeholder grid) instead of inferring conventions bottom-up from usage, and lets later steps flag where a sample's actual usage drifts from any known template's declared theme. **Do not assume a single uploaded template is the only variant** — org templates commonly come in families (light/dark, 16:9/4:3, per-business-unit); treat template-derived findings as scoped to the specific variant(s) seen so far, and re-run this step as more variants arrive. *Done when* every sample file has a raw JSON in the cache, the run log shows skipped-vs-extracted counts, and (if templates were provided) a theme profile covers all of them plus every pptx sample.

2. **Profile** — for each raw JSON not yet profiled, send it through `templates/profile_prompt.md` (one Claude call per sample — never batch here). *Done when* every sample has a profile JSON that parses and contains all eleven required fields (see Reference below).

3. **Aggregate** — batch profiles per the batch-size limit in Reference, run `templates/aggregate_prompt.md`, and run a second aggregation pass over the batch summaries if more than one batch was needed. *Done when* the spec document exists with all five required sections (including the Information density profile — see Reference) and every rule in it cites a real sample filename + slide number.

4. **Reconcile** — if a prior spec version exists for this corpus, this run must include the Changelog section (built into the aggregate prompt): which rules flipped or gained an exception, and which new sample caused it. *Done when* every flip is flagged for human confirmation rather than applied silently — do not let step 3 overwrite a prior mandatory rule without surfacing the contradiction.

5. **Package** — once the spec is stable across a few iterations, invoke the `writing-great-skills` skill to turn the spec into a separate, deployable skill (e.g. `<brand>-slide-style`): mandatory/preferential rules become its Reference section, cited fragments become its external reference files, and its invocation model is decided fresh — it's a different trigger ("draft a deck") from this one ("update the style guide"). The density remediation policy (Reference below) must carry over as a first-class behavior of the new skill, not just as background data. Ask the user for a descriptive-vs-prescriptive fidelity decision (which parts of the spec to follow literally vs. which to correct toward brand ground truth) if one hasn't already been made for this corpus — it changes which version of the color/font/grid rules the new skill treats as ground truth, and it's a per-corpus decision, not a reusable default. *Done when* that skill exists, can produce a draft an agent can self-check against the mandatory rules, and applies the remediation policy to any under-dense slide it drafts.

## Reference

**Raw profile → style profile required fields** (step 2 output, one object per sample):
- `layout_pattern` — recurring slide-order structure
- `color_role_mapping` — hex → role (`primary`/`accent`/`background`/`text`/...)
- `typography_hierarchy` — level → size_pt → usage
- `data_viz_preference` — chart/table type per scenario
- `text_density_rule` — characters/bullets cap per slide
- `logic_flow` — narrative arc across the deck (pptx-only — no PDF title-placeholder equivalent to extract)
- `image_treatment` — placement zone, size/coverage pattern, captioning convention
- `citation_style` — how internal vs external reference data is attributed (or not)
- `argument_structure` — per-slide content-point count convention by genre (pptx-only — paragraph counting relies on pptx text-frame structure)
- `diagram_convention` — geometric arrangement of non-text diagram shapes, interpreted semantically alongside the slide's title/text (pptx-only — diagram-shape typing has no reliable PDF equivalent)
- `branding_footer` — page-number/confidentiality/logo convention, or its explicit absence

**Aggregation batch limit**: 20–30 profiles per call. Above that, aggregate in sub-batches first, then aggregate the sub-batch summaries — never skip the second pass.

**Spec document sections** (step 3 output): Mandatory rules (>80% consistency), Preferential rules (majority + noted exceptions), Prohibitions (never observed), Reference examples (one citation per rule — no exceptions), Information density profile (role- and genre-segmented density bands + remediation policy — see below).

**General methodology** (applies to any corpus this skill mines — not specific to one run's findings):
- Density is never a single global number. Segment by role first (cover/toc/divider/closing/content — the first four are deliberately terse and must never be flagged as under-dense), then segment `content` further by genre/scenario, since two samples in the same file format can have very different legitimate density floors (a pitch deck and a framework-teaching deck can both be pptx).
- Raw image counts are not comparable across source formats. pdfplumber's `image_count` enumerates every embedded raster XObject (icons, logo fragments, textures), typically 10-20x the pptx script's picture-shape count for a visually similar deck. Compare placement-zone and captioning patterns within a format, not raw counts across formats.
- Font-family and color findings are not directly comparable across pptx vs. PDF sources — PDF export commonly re-encodes/subsets fonts and can't carry theme links, so a PDF's reported font/color may reflect the export pipeline rather than deck design. Report each format's findings separately rather than merging or discarding either as noise.
- Empirical usage and declared theme can and do diverge — when a canonical template is available, always cross-check a sample's dominant hex values and fonts against its own theme's declarations before writing a color or font rule. A near-miss (visually close, numerically distinct) is itself a finding worth reporting, not extraction noise.
- A sample's theme identity is itself a compliance signal, independent of its composition/grid compliance — check both, never infer one from the other. A sample can match a canonical template's colors exactly while never using its placeholder-based layout at all.
- Check authoring-tool origin (`docProps/app.xml` for pptx, producer/creator metadata for PDF) before trusting a grid/placeholder-based finding — an export pipeline (e.g. Google Slides → pptx) can flatten placeholder linkage regardless of how faithfully the original followed a template, confounding "authors ignore the grid" with "the export drops the grid." This confound doesn't extend to color/font habit findings, which show up independent of authoring tool.
- `classify_diagram_geometry` (in `extract_pptx.py`) only reports row/column clustering (grid / horizontal-sequence / vertical-stack / cluster) — it cannot tell a real matrix/table apart from an unstructured icon scatter, or detect pyramid tapering. Treat "grid" as "not a single row or column," not as a confirmed semantic diagram type; step 2 profiling must look at the actual shapes and the slide's title/text to assign the real semantic label.
- Footer/branding conventions (page number, confidentiality marker, logo) are genre-dependent, not corpus-wide, and can differ even between same-format, same-tool-origin samples. Don't assume a footer convention found in one sample generalizes to the rest of the corpus — report it per-genre like density.
- Don't assume a single uploaded template is the only variant. When more template files arrive for the same corpus, re-run `extract_theme.py` across all of them together and check whether they share or diverge on accent/font scheme before treating any single-template finding as settled.

**This corpus's specific findings and decisions** (Huawei/Telefonica corpus, 6 content samples + 1 template) are documented in `reference/style-spec-v9.md` (and the version history `v2`-`v8` alongside it) — do not duplicate that detail here. Notably: the accent-color and grid-compliance findings, the Google-Slides-vs-PowerPoint authoring-tool split, and the descriptive-fidelity-with-color-override decision for the eventual apply-skill are all specific to this corpus and provisional pending more samples/template variants — re-derive them for any other corpus rather than assuming they transfer.

**Density remediation policy** (high-priority, carried into the packaged apply-skill per step 5 — this is what fires whenever drafting hits a `content` slide whose source material can't reach its genre's density floor): try in order — (1) **consolidate** adjacent thin source units onto one slide if they form one coherent idea, (2) **web search** to fill a missing factual/public-data gap, flagged for user verification before finalizing, (3) **ask the user** for supplementary material when the gap is proprietary or a judgment call only they can make. Never pad with filler just to hit a number.

## External reference

- `scripts/extract_pptx.py` — python-pptx batch extraction, incremental by content hash (also captures placeholder positions, diagram-shape geometry, paragraph counts, branding keywords, and file-level authoring-tool fingerprint)
- `scripts/extract_pdf.py` — pdfplumber equivalent for PDF sources (branding keywords + authoring-tool via PDF producer/creator metadata; no paragraph/diagram equivalent — see General methodology)
- `scripts/extract_theme.py` — ground-truth theme/master/layout extraction (color+font scheme, named-layout placeholder grid), run against all known template variants plus every pptx sample
- `templates/profile_prompt.md` — step 2 prompt (single sample → JSON)
- `templates/aggregate_prompt.md` — step 3 prompt (N profiles → spec + changelog)
- `reference/style-spec-v{N}.md`, `reference/profiles/` — this corpus's versioned output and per-sample profiles; keep old spec versions for the reconcile step
