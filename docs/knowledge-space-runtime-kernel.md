# Knowledge Space: Normative Runtime Kernel

## Scope
Canon 2.2.0-draft (`canon/runtime.kl` + schemas).

## Core Contracts
- **Result&lt;T, Error&gt;** — Exactly one of `value` or `error` is set. Replaces free-form strings and null.
- **ArtifactStore** — Abstract key/value persistence. No filesystem assumption in canon. Bindings (e.g. FileArtifactStore) live in `examples/`.
- **Plan / Task DAG** — `Task.requires` forms a directed acyclic graph. Validated by schema.
- **model_id** — Single identifier for both Agent and LLM.

## Key Concepts
| Concept | Purpose | Schema |
|---------|---------|--------|
| Error | Structured failure | error.schema.json |
| Plan | Roles + Tasks | plan.schema.json |
| Session | Workflow runtime | session.schema.json |
| ExecutionContext | Step state | execution-context.schema.json |
| Artifact | Named data unit | artifact.schema.json |

## Inheritance Rule
Higher Spaces and flows must consume these primitives. Non-canonical details remain in `examples/runtime-python/`.

## Validation
`python tools/validate.py`
