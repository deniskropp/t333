# Knowledge Space: Runtime Contracts

## Result Discipline
All fallible operations return `Result<T, Error>`.
- `ok: true` → `value` is set
- `ok: false` → `error` is set
- Error codes include `llm_unavailable`, `invalid_plan`, `task_failed`, `not_found`

## ArtifactStore Contract
```
AddArtifact(name, content) → Result<void, Error>
GetArtifact(name) → Result<Artifact, Error>  // not_found if missing
```
Session holds a reference (`store` / `store_ref`). No directory assumption in canon.

## Plan Contract
- `roles: list<Role>`
- `tasks: list<Task>` with `requires` forming a DAG
- Validated against `plan.schema.json`

## Non-Canonical Boundary
Provider bindings (Gemini, Olli, Kimi), YAML loaders, and filesystem stores live exclusively under `examples/runtime-python/`.

## Reference
See `CHANGES.md` for the full delta to 2.2.0-draft.
