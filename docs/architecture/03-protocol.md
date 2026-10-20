# Architecture: OCS Protocol Surface

## Role
The OCS protocol (\\u2afb sections) is the meta-communicative interface between user intent and the kernel.

## Primary Sections
- `\\u2afbcmd/` — directives (exec, halt, mode, lang)
- `\\u2afbdata/` — payloads (obj, tas, ptas, state, trace, insight)
- `\\u2afblogic/` — control and validation
- `\\u2afbflow/` — execution sequences
- `\\u2afbteam/` — agent roles

## Relationship to Kernel
Protocol sections are translated into kernel operations (GeneratePlan, ExecuteTask, PutArtifact, etc.).
All fallible translations respect Result discipline.
