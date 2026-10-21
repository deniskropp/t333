# Architecture: OCS Protocol Surface

## Role
The OCS protocol (⫻ sections) is the meta-communicative interface between user intent and the kernel.

## Primary Sections
- `⫻cmd/` — directives (exec, halt, mode, lang)
- `⫻data/` — payloads (obj, tas, ptas, state, trace, insight)
- `⫻logic/` — control and validation
- `⫻flow/` — execution sequences
- `⫻team/` — agent roles

## Relationship to Kernel
Protocol sections are translated into kernel operations (GeneratePlan, ExecuteTask, AddArtifact, etc.).
All fallible translations respect Result discipline.
