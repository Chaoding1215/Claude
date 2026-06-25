---
name: diagnosing-bugs
description: Diagnose a bug or performance problem using a structured six-phase process. Use when the user reports a bug or asks you to investigate unexpected behavior.
---

Diagnose the bug using this six-phase process.

## Phase 1: Build a feedback loop

This is the skill. Establish a tight, deterministic pass/fail signal before doing anything else. Options in priority order:

- Failing unit or integration test
- HTTP script (`curl`, `.http` file)
- CLI invocation with a fixture
- Headless browser automation
- Captured trace replay
- Differential comparison (known-good vs. broken)
- Custom harness

A 30-second flaky loop is barely better than no loop; a 2-second deterministic one is tight.

**If you catch yourself reading code to build a theory before this loop exists, stop.**

## Phase 2: Reproduce and minimise

Run the loop to confirm the bug appears. Then strip away non-essential elements while maintaining the failure. The minimal reproduction is the real artifact.

## Phase 3: Hypothesise

Generate 3–5 ranked, falsifiable hypotheses before testing anything. Each must predict a specific outcome if correct.

## Phase 4: Instrument

Test hypotheses one at a time. Prefer a debugger over scattered logging. Tag all debug statements uniquely (e.g. `[BUG-HUNT]`) for easy cleanup.

## Phase 5: Fix and regression test

Write the regression test *before* applying the fix — at the correct seam, where it genuinely exercises the failure pattern. Then apply the fix and verify it turns the test green.

## Phase 6: Cleanup and post-mortem

Remove all debug instrumentation. Verify the original scenario passes. Note what architectural change could have prevented this bug.
