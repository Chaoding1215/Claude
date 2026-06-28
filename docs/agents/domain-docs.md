# Domain Documentation Layout

**Layout**: Multi-context

- `CONTEXT-MAP.md` at root points to per-component contexts
- Each component has its own `CONTEXT.md` and `docs/adr/` directory

## Example structure

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                    ← system-wide decisions
├── src/
│   ├── <component>/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/
```
