# Knowledge Space: Runtime Contracts

## Result Discipline
All fallible operations return `Result&lt;T, Error&gt;`.
- `ok: true` → `value` is set
- `ok: false` → `error` is set
- Error codes include `llm_unavailable`, `invalid_plan`, `task_failed`, `not_found`

## ArtifactStore Contract
```
PutArtifact(name, content) → Result&lt;void, Error&gt;
FetchArtifact(name) → Result&lt;Artifact, Error&gt;  // not_found if missing
```
Session holds a reference (`store` / `store_ref`). No directory assumption in canon.

## Plan Contract
- `roles: list&lt;Role&gt;`
- `tasks: list&lt;Task&gt;` with `requires` forming a DAG
- Validated against `plan.schema.json`

## Non-Canonical Boundary
Provider bindings (Gemini, Olli, Kimi), YAML loaders, and filesystem stores live exclusively under `examples/runtime-python/`.

## Reference
See `CHANGES.md` for the full delta to 2.2.0-draft.
