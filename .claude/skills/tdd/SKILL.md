---
name: tdd
description: Write code test-first using vertical slices and tracer bullets. Use when the user asks to implement something with TDD, or asks you to write tests first.
---

Tests verify behavior through public interfaces, not implementation details.

Good tests work like integration tests: they exercise real code paths and document what the system does. Poor tests couple to internals — they mock collaborators, test private methods, and break during refactoring even when behavior is unchanged.

## Critical anti-pattern: horizontal slices

Do not write all tests before any implementation. That produces tests which verify imagined behavior, check structural shapes instead of outcomes, and become insensitive to real changes.

Use **vertical slices via tracer bullets**: one test → minimal code to pass → next test. Each cycle responds to what the previous revealed.

## Workflow

**1. Planning**
- Confirm the required interface with the user.
- Prioritize testable behaviors (most critical first).
- Identify opportunities for deep, simple modules.
- Get user approval before writing any code.

**2. Tracer bullet**
- Write one test verifying a single system capability end-to-end.
- Write the minimum code to make it pass.

**3. Incremental loop**
- Add one test at a time.
- Write only enough code to satisfy each new test.
- Never speculate about future tests.

**4. Refactor**
- Only after all tests are green.
- Extract duplication, deepen module design.
- Never refactor while tests are failing.

## Checklist per cycle

- [ ] Test describes behavior, not implementation
- [ ] Test uses only public interfaces
- [ ] Test would survive an internal refactor
