---
name: codebase-design
description: Apply deep module principles when designing or reviewing code structure. Use when the user asks about architecture, module design, or how to structure code.
---

Design **deep modules** — implementations that hide substantial complexity behind minimal interfaces.

## Vocabulary

- **Module** — any bounded unit (function, class, package, service) with an interface and implementation
- **Interface** — everything a caller must understand to use the module: types, invariants, constraints, error modes, performance facts — not just signatures
- **Depth** — the amount of behaviour a caller can exercise per unit of interface they learn; deep modules concentrate complexity internally
- **Seam** — where behaviour changes without local editing (Feathers' term); the location decision is separate from what lives behind it
- **Adapter** — a concrete implementation satisfying an interface
- **Leverage** — the efficiency callers gain from depth

## Core principle

Depth is a property of the interface, not the implementation. Internal seams enable testable, composable internals while preserving a slim external surface.

## Deletion test

If you removed this module, would complexity vanish or scatter across callers? If it scatters, the module provides genuine leverage. If it vanishes, the module was shallow — consider removing it.

## Testability

Good interfaces naturally support testing:
- Accept dependencies rather than constructing them
- Return values instead of producing side effects
- Minimise surface area (fewer methods, simpler parameters)

The interface is the test surface — callers and tests cross the same boundary.

## Avoid

- Shallow modules where the interface rivals the implementation in complexity
- Modules that require callers to bounce between many small files to understand one concept
- Abstractions that exist before there are two concrete things to abstract
