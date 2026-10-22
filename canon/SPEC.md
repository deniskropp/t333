# t333 Canon — SPEC (canon 2.2.0)

Dieses Verzeichnis (`canon/`) ist die **neutrale Source of Truth** für alle abgeleiteten tXXX-Systeme, Spaces und Agenten. Alles außerhalb von `canon/` ist informativ (`docs/`, `README.md`) oder ein Beispiel (`examples/`, `templates/`).

## 1. Inhalt (normativ)
| Datei | Inhalt |
|---|---|
| `runtime.kl` | Runtime-Kern: Result/Error, ArtifactStore, Plan/Task, Session, ExecutionContext, LLM (abstrakt), Agent, Orchestrator |
| `tas.kl` | Task-Agnostic Steps (TAS): Datenmodell und Lebenszyklus obj → tas → ptas → Plan |
| `roles.yaml` | Abstrakte Rollen-IDs (Funktionen), ohne Personas |
| `schemas/*.schema.json` | JSON Schema 2020-12 für alle serialisierbaren Datenkonzepte |
| `VERSION` | Kanon-Version |

## 2. Notation
- Abschnittsmarker ist ausschließlich `⫻` (U+2AFB), **ohne Leerzeichen** vor dem Typ: `⫻type/scope:value`.
- `×` (U+00D7) und `⨻` (U+2A3B) sind als Marker unzulässig. Escape-Sequenzen wie `\u2afb` dürfen nicht im Text stehen bleiben.

## 3. Neutralitätsregeln
In `canon/` gilt:
- Keine Persona-Namen. Rollen werden über IDs aus `roles.yaml` angesprochen. Persona-Belegungen stehen in Profilen wie `examples/profiles/ocs-classic.yaml`.
- Keine Projekt-, Kunden-, Personen-, Modell- oder Anbieternamen und keine Dateisystem- oder SDK-Annahmen.
- **Test:** Jeder Satz muss auch dann stimmen, wenn alle Personas umbenannt werden und eine andere Implementierung (z. B. Python t20, C++/QML t484) verwendet wird.
- Durchgesetzt durch `tools/lint.py` (CI).

## 4. Referenzierung durch abgeleitete Systeme
- Abgeleitete Systeme referenzieren **t333 `main`** direkt. Es gibt **kein** Versions-Pinning-Manifest (siehe ADR-0005).
- `main` ist immer gültig: Jede Änderung läuft per Pull Request über CI (`tools/validate.py`, `tools/lint.py`).
- **Erweiterungen** verwenden einen eigenen Namensraum `⫻x-tNNN/…` (z. B. `⫻x-t484/display`) und gelangen nur per PR in den Kern.
- Bindings (konkrete LLM-Anbieter, Speicher, Loader) bleiben in den abgeleiteten Systemen oder in `examples/`.

## 5. Versionierung und Änderungsprozess
- `VERSION` folgt SemVer und dient der **Kommunikation**, nicht dem Pinning.
  - MAJOR: inkompatible Änderung an Syntax oder Schema.
  - MINOR: neues Konzept, neue Rolle oder neues optionales Feld.
  - PATCH: Klarstellung.
- Jede normative Änderung braucht einen Eintrag in `CHANGELOG.md`. Bei MINOR/MAJOR zusätzlich eine ADR unter `docs/adr/`.
- Ein Element wird mindestens eine MINOR-Version lang als `deprecated` markiert, bevor es entfernt wird.

## 6. Konformität
Ein abgeleitetes System ist **canon-konform**, wenn:
1. seine serialisierten Plan-, Task-, TAS-, Session-, … Instanzen die Schemas erfüllen;
2. Pläne die Semantikregeln erfüllen: eindeutige `task_id`s, `requires` nur auf vorhandene Tasks und zyklenfrei, `task.role` ∈ `plan.roles`;
3. die Laufzeitzuweisung `AssignAgent` gilt: Ein gesetztes `task.name` muss in `Session.agents` existieren;
4. alle fehlbaren Operationen `Result<T, Error>` liefern.
