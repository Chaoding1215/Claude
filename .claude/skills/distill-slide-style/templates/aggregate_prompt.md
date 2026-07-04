# Step 3 prompt — cross-sample aggregation

Batch size: 20-30 style profiles per call. Above that, aggregate in batches
first, then run this same prompt again over the batch summaries — never
treat an intermediate batch summary as the final spec.

---

Below are N style-profile JSON objects, one per deck. Derive cross-sample
norms and output an executable style specification with these sections:

1. **Mandatory rules** — patterns consistent across >80% of samples (e.g.
   "titles never exceed 12 characters").
2. **Preferential rules** — patterns most samples follow, with noted
   exceptions and the scenarios where the exception applies.
3. **Prohibitions** — practices that never appear in any sample.
4. **Reference examples** — for every rule above, cite one concrete sample
   (filename + slide number) that demonstrates it. No rule may exist without
   a citation.

5. **Information density profile** — this is a high-priority, standing
   requirement, not optional detail. Segment every slide/page by role before
   computing density, don't pool everything into one number:
   - Classify each slide/page as `cover`, `toc`, `divider` (a short
     transitional slide — flag any non-cover/toc/closing slide well below
     the sample's own content median as a divider candidate), `closing`, or
     `content`.
   - Report a density band (min/median/max characters) per role, pooled
     across samples.
   - Then break `content` down further **by genre/scenario**, not just by
     file format — e.g. a pitch deck and a framework-teaching deck can both
     be pptx and still have very different legitimate density floors. Name
     the genre, give its band, cite the samples in it.
   - Explicitly separate "low density by design" (cover/divider/closing —
     never flag these as a problem) from "low density that may indicate
     thin source material" (a `content`-role slide sitting notably below
     its genre's own floor).
   - **Density remediation policy**: for a `content`-role slide whose
     available source material can't reach its genre's density floor,
     recommend in this priority order — (1) consolidate: merge adjacent
     thin source units onto one slide if they form one coherent idea, (2)
     web search: fill a missing factual/public-data gap, flagged for user
     verification before finalizing, (3) ask the user: request
     supplementary material when the gap is proprietary or a judgment call
     only they can make. Never pad with filler just to hit a number.

If a prior spec version is provided below (e.g. `reference/style-spec-v{N-1}.md`), also output:

6. **Changelog** — which rules flipped or gained a new exception versus the
   prior version, and which new sample caused the change. Flag every flip
   explicitly for human confirmation — do not silently overwrite a prior
   mandatory rule.

Style profiles:
{{PROFILE_JSONS}}

Prior spec (omit this section entirely if none exists yet):
{{PRIOR_SPEC}}
