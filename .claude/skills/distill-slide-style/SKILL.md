---
name: distill-slide-style
description: Distill a style specification from a corpus of PPT/PDF samples — layout patterns, color roles, typography, chart preferences, density limits, narrative flow. Use when the user wants to mine, extract, or update design norms from a batch of decks or documents.
disable-model-invocation: true
---

Mine a sample corpus into a versioned, evidence-cited style specification. Incremental and repeatable — re-running after new samples arrive should only touch what changed.

## Steps

1. **Extract** — run `scripts/extract_pptx.py` and/or `scripts/extract_pdf.py` over the sample directory. Each script caches by content hash under `.distill-cache/raw/`, so unchanged files are skipped on re-runs. If a canonical template/master file is available (a mostly-empty file whose purpose is the template itself, not real content), also run `scripts/extract_theme.py` over it and over every pptx sample — this reads ground truth (theme color/font scheme, named-layout placeholder grid) instead of inferring conventions bottom-up from usage, and lets later steps flag where a sample's actual usage drifts from its own declared theme. *Done when* every sample file has a raw JSON in the cache, the run log shows skipped-vs-extracted counts, and (if a template was provided) `theme_profile.json` covers the template plus every pptx sample.

2. **Profile** — for each raw JSON not yet profiled, send it through `templates/profile_prompt.md` (one Claude call per sample — never batch here). *Done when* every sample has a `profiles/<hash>.json` that parses as JSON and contains all eight required fields (see Reference below).

3. **Aggregate** — batch profiles per the batch-size limit in Reference, run `templates/aggregate_prompt.md`, and run a second aggregation pass over the batch summaries if more than one batch was needed. *Done when* `docs/style-spec-v{N}.md` exists with all five required sections (including the Information density profile — see Reference) and every rule in it cites a real sample filename + slide number.

4. **Reconcile** — if `docs/style-spec-v{N-1}.md` exists, this run must include the Changelog section (built into the aggregate prompt): which rules flipped or gained an exception, and which new sample caused it. *Done when* every flip is flagged for human confirmation rather than applied silently — do not let step 3 overwrite a prior mandatory rule without surfacing the contradiction.

5. **Package** — once the spec is stable across a few iterations, invoke the `writing-great-skills` skill to turn `docs/style-spec-v{N}.md` into a separate, deployable skill (e.g. `<brand>-slide-style`): mandatory/preferential rules become its Reference section, cited fragments become its external reference files, and its invocation model is decided fresh — it's a different trigger ("draft a deck") from this one ("update the style guide"). The density remediation policy (Reference below) must carry over as a first-class behavior of the new skill, not just as background data — it's what the new skill runs whenever a slide it's drafting can't reach its genre's density floor. If a canonical template was used (step 1), ask the user the descriptive-vs-prescriptive question (Reference below) before packaging — it decides which version of the color/font/grid rules the new skill treats as ground truth. *Done when* that skill exists, can produce a draft an agent can self-check against the mandatory rules, and applies the remediation policy to any under-dense slide it drafts.

## Reference

**Raw profile → style profile required fields** (step 2 output, one object per sample):
- `layout_pattern` — recurring slide-order structure
- `color_role_mapping` — hex → role (`primary`/`accent`/`background`/`text`/...)
- `typography_hierarchy` — level → size_pt → usage
- `data_viz_preference` — chart/table type per scenario
- `text_density_rule` — characters/bullets cap per slide
- `logic_flow` — narrative arc across the deck
- `image_treatment` — placement zone, size/coverage pattern, captioning convention
- `citation_style` — how internal vs external reference data is attributed (or not)

**Aggregation batch limit**: 20–30 profiles per call. Above that, aggregate in sub-batches first, then aggregate the sub-batch summaries — never skip the second pass.

**Spec document sections** (step 3 output): Mandatory rules (>80% consistency), Preferential rules (majority + noted exceptions), Prohibitions (never observed), Reference examples (one citation per rule — no exceptions), Information density profile (role- and genre-segmented density bands + remediation policy — see below).

**Settled conventions** (decided once, do not re-litigate in future reconcile passes):
- Title-pattern rules (`logic_flow`, headline-as-title) are pptx-only evidence, permanently. PDF sources have no title-placeholder equivalent to extract, so PDF samples simply don't vote on these rules — this is a scope limit, not an open gap to close.
- Font-family findings are scenario-conditioned, not directly comparable across source formats: pptx sources (internal-use/working files) report actual CJK font names (e.g. Microsoft Yahei); PDF sources (external-use/distributed exports) report Latin-substitute font names even on CJK-text pages, because PDF export commonly re-encodes/subsets fonts for portability. Write font rules as a pair — one for the internal/pptx scenario, one for the external/PDF scenario — rather than merging them into a single cross-format rule or discarding the PDF signal as noise.
- Density is never a single global number. Segment by role first (cover/toc/divider/closing/content — the first four are deliberately terse and must never be flagged as under-dense), then segment `content` further by genre/scenario, since two samples in the same file format can have very different legitimate density floors (a pitch deck and a framework-teaching deck can both be pptx).
- Raw image counts are not comparable across source formats. pdfplumber's `image_count` enumerates every embedded raster XObject (icons, logo fragments, textures), typically 10-20x the pptx script's picture-shape count for a visually similar deck. Compare placement-zone and captioning patterns within a format, not raw counts across formats.
- **Empirical usage and declared theme can and do diverge — check both, and report the gap as a finding, not noise.** Confirmed cases: (1) samples' own embedded themes almost always declare a generic CJK fallback font (SimSun/宋体) as the Hans-script default, while authors manually override to Microsoft Yahei on nearly every run — the theme's font scheme is effectively vestigial in practice; (2) the empirically dominant red (`C00000`) is PowerPoint's standard-palette "Dark Red" swatch, not the org theme's actual accent1 (`C7000A`) — visually near-identical, numerically distinct, meaning authors reach for a habit swatch instead of the theme-linked color chip. When a canonical template is available, always cross-check a sample's dominant empirical hex values against its own theme's accents (exact match / near-miss-within-a-few-RGB-units / unrelated) before writing a color or font rule — "near-miss" is itself the finding, not extraction noise.
- A sample's theme identity is itself a compliance signal. Compare a pptx sample's embedded theme(s) (`extract_theme.py`) against the canonical template's theme: an exact accent-color match means the sample was built from the shared master; a completely unrelated theme (different accent hues entirely) plus colors that don't even match *that sample's own* theme means the deck was very likely authored freehand, outside the shared template, and its conventions should be weighted accordingly (still real data, but "how an unguided author drifts" rather than "the house style").
- **Palette compliance and grid compliance are independent axes — check both, never infer one from the other.** Confirmed case: a sample can match the canonical template's theme colors exactly while still not using any of its placeholder-based composition grid (verified by comparing `extract_pptx.py`'s per-slide `placeholders` positions against `extract_theme.py`'s layout geometry). Across this corpus, composition-grid compliance is rare even where color compliance is high — most slides in most samples use freeform text boxes, not layout placeholders, so the template's declared grid is closer to aspirational brand guidance than to a description of actual practice.
- **Descriptive vs. prescriptive fidelity is an unresolved fork that step 5 must not default silently.** Nearly every rule in this spec has two possible readings once a canonical template exists: what the template/brand guideline specifies (prescriptive — e.g. accent `C7000A`, theme-linked Hans fonts, the official grid) vs. what authors actually, repeatedly do (descriptive — e.g. `C00000`, manually-applied Yahei, freeform positioning). Ask the user which one the packaged apply-skill should target before step 5 runs; don't silently pick the empirical majority just because it's what most rules in this document are built from.

**Density remediation policy** (high-priority, carried into the packaged apply-skill per step 5 — this is what fires whenever drafting hits a `content` slide whose source material can't reach its genre's density floor): try in order — (1) **consolidate** adjacent thin source units onto one slide if they form one coherent idea, (2) **web search** to fill a missing factual/public-data gap, flagged for user verification before finalizing, (3) **ask the user** for supplementary material when the gap is proprietary or a judgment call only they can make. Never pad with filler just to hit a number.

## External reference

- `scripts/extract_pptx.py` — python-pptx batch extraction, incremental by content hash
- `scripts/extract_pdf.py` — pdfplumber equivalent for PDF sources
- `scripts/extract_theme.py` — ground-truth theme/master/layout extraction (color+font scheme, named-layout placeholder grid), run against a canonical template plus every pptx sample when one is available
- `templates/profile_prompt.md` — step 2 prompt (single sample → JSON)
- `templates/aggregate_prompt.md` — step 3 prompt (N profiles → spec + changelog)
- `docs/style-spec-v{N}.md` — versioned output; keep old versions for the reconcile step
