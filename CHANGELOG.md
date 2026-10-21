# Changelog

Alle relevanten Änderungen am Kanon (`canon/`). Format nach [Keep a Changelog](https://keepachangelog.com/de/1.1.0/); Versionen nach SemVer (`canon/VERSION`). Abgeleitete Systeme referenzieren `main` (siehe ADR-0005). Details pro Änderung: `CHANGES.md`.

## [2.2.0-draft] — unreleased

### Hinzugefügt
- `canon/SPEC.md`: Geltungsbereich, Notation, Neutralitätsregeln, Referenzierung über `main`, Namensraum `⫻x-tNNN/`.
- `canon/VERSION`.
- `canon/roles.yaml` (abstrakte Rollen-IDs) und das nicht kanonische Profil `examples/profiles/ocs-classic.yaml` (inklusive Kodax und Aurora).
- `canon/tas.kl` und `canon/schemas/tas.schema.json` (TAS, Herkunft t20; ADR-0006).
- `Orchestrator.AssignAgent` als Laufzeitprüfung, dass ein gesetztes `task.name` in `Session.agents` existiert (ADR-0004).
- `tools/validate.py` prüft zusätzlich die Semantik von Plänen (eindeutige IDs, Referenzen, Rollen, Zyklen, Agenten) und TAS-Instanzen.
- `tools/lint.py`: Prüfung der ⫻-Notation und der Neutralität.
- CI-Workflow `.github/workflows/canon.yml`.
- Negativ-Fixtures in `examples/invalid/`.
- ADRs 0001–0006 unter `docs/adr/`.

### Geändert
- `Task.name` ist optional.
- Artefakt-Operationen sind vereinheitlicht: nur noch `AddArtifact`/`GetArtifact` (ADR-0003).
- Einheitliche Versionslinie *canon 2.2.0*. Die Labels „OCS v2.1“, „v3.0“ und „v4.1“ stehen nur noch in `docs/ecosystem-status.md`.
- Einheitliche Notation `⫻type/scope` ohne Leerzeichen.
- `spaces/` ist in `examples/` aufgegangen.
- Persona-, Projekt- und Modellbezüge sind aus normativen Texten entfernt. README-Tabelle: Rollen-ID plus Default-Persona.

### Entfernt
- `PutArtifact`/`FetchArtifact`.

## [2.2.0-draft] — 2026-10-20 (erste Veröffentlichung)
- Normativer Runtime-Kern `canon/runtime.kl`, Schemas, Python-Bindings als Beispiel (siehe `RELEASE_NOTES_canon-2.2.0-draft.md`).
