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

If a prior spec is provided below (`docs/style-spec-v{N-1}.md`), also output:

5. **Changelog** — which rules flipped or gained a new exception versus the
   prior version, and which new sample caused the change. Flag every flip
   explicitly for human confirmation — do not silently overwrite a prior
   mandatory rule.

Style profiles:
{{PROFILE_JSONS}}

Prior spec (omit this section entirely if none exists yet):
{{PRIOR_SPEC}}
