# Architecture: Bindings

## Role
Bindings provide concrete implementations of abstract kernel interfaces.

## Location
`examples/runtime-python/bindings.kl` (explicitly non-canonical)

## Examples
- FileArtifactStore implements ArtifactStore
- Gemini / Olli / Kimi implement LLM
- LoadConfig, LoadPrompts, etc.

## Boundary Rule
Bindings may use filesystems, provider SDKs, and configuration formats.
These details must never appear in the normative kernel or molecules.
