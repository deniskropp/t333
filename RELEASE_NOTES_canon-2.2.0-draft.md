# Release Notes — canon-2.2.0-draft

Normative runtime substrate layer for the Orion Collective System (OCS) / KickLang meta-framework.

---

## Deutsch

## canon-2.2.0-draft

Normative Runtime-Substratschicht für das Orion Collective System (OCS) / KickLang Meta-Framework.

Dieser Entwurf fixiert den implementierungsneutralen Runtime-Kern, den höhere Spaces, Flows und Agenten erben.

### Hinzugefügt
- **`canon/runtime.kl`** — Normative Konzepte: `Error`, `Result<T,E>`, `SchemaRef`, `ArtifactStore`, `Plan`, `Task`, `Role`, `Artifact`, `AgentOutput`, `Session`, `ExecutionContext`, `LLM`, `Agent`, `Orchestrator`
- **`canon/schemas/`** — JSON Schema Draft 2020-12 für alle serialisierbaren Datenkonzepte
- **`CHANGES.md`** — Delta von den vorherigen informellen Typen zur fixierten 2.2.0-draft-Oberfläche
- **`tools/validate.py`** — Referenz-Validator für Schemas und sample-plan
- **`examples/sample-plan.json`** — Gültiges Plan-Beispiel
- Nicht-kanonische Python-Runtime-Bindings und Config-Schema unter `examples/runtime-python/`

### Geändert
- Alle fehlbaren Operationen liefern jetzt `Result<T, Error>` (keine freien Fehler-Strings oder null mehr)
- Persistenz läuft ausschließlich über die abstrakte `ArtifactStore` (keine Dateisystem-Annahme im Canon)
- `ExecutionContext.plan` ist ein typisierter `Plan` (DAG aus Tasks)
- Einheitliches `model_id` für Agent und LLM
- README um explizite normative-Schicht-Sektion und aktualisierte Projektstruktur erweitert

### Hinweise
- Bindings, Loader und provider-spezifische Details bleiben nicht-kanonisch (siehe `examples/`)
- Voll kompatibel mit bestehender OCS v2.1 Space-Generierung, three-agent-core und KickLang v4.1+-Mustern
- Öffentliche Oberfläche entspricht jetzt dem Runtime-Modell des privaten/Skill-Ökosystems

**Vollständiger Vergleich:** siehe `CHANGES.md`  
**Validierung:** `python tools/validate.py`

---

## English

## canon-2.2.0-draft

Normative runtime substrate layer for the Orion Collective System (OCS) / KickLang meta-framework.

This draft locks the implementierungsneutral runtime kernel that higher Spaces, flows, and agents inherit.

### Added
- **`canon/runtime.kl`** — Normative concepts: `Error`, `Result<T,E>`, `SchemaRef`, `ArtifactStore`, `Plan`, `Task`, `Role`, `Artifact`, `AgentOutput`, `Session`, `ExecutionContext`, `LLM`, `Agent`, `Orchestrator`
- **`canon/schemas/`** — JSON Schema Draft 2020-12 for all serializable data concepts
- **`CHANGES.md`** — Delta from prior informal types to the locked 2.2.0-draft surface
- **`tools/validate.py`** — Reference schema + sample-plan validator
- **`examples/sample-plan.json`** — Valid Plan example
- Non-canonical Python runtime bindings and config schema under `examples/runtime-python/`

### Changed
- All fallible operations now return `Result<T, Error>` (no free-form error strings or null)
- Persistence is exclusively via abstract `ArtifactStore` (no filesystem assumption in canon)
- `ExecutionContext.plan` is a typed `Plan` (DAG of Tasks)
- Unified `model_id` for both Agent and LLM
- README updated with explicit normative-layer section and revised project structure

### Notes
- Bindings, loaders, and provider-specific details remain non-canonical (see `examples/`)
- Fully compatible with existing OCS v2.1 Space generation, three-agent-core, and KickLang v4.1+ patterns
- Public surface now matches the private/skill ecosystem runtime model

**Full comparison:** see `CHANGES.md`  
**Validation:** `python tools/validate.py`
