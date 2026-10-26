# Changelog

Alle relevanten Änderungen am Kanon (`canon/`). Format nach [Keep a Changelog](https://keepachangelog.com/de/1.1.0/); Versionen nach SemVer (`canon/VERSION`). Abgeleitete Systeme referenzieren `main` (siehe ADR-0005). Details pro Änderung: `CHANGES.md`.

## [Unreleased] — 2.4.0-draft

`canon/VERSION` = `2.4.0-draft` (Entwicklungslinie nach dem Release 2.3.0). Letzter Release: `canon-v2.3.0`.

### Geändert
- Housekeeping: Die Einträge zu 2.2.0 und 2.3.0 nennen die gesetzten Tags jetzt in der Vergangenheitsform mit Commit (`canon-v2.2.0` → 055f4da, `canon-v2.3.0` → bde5cc0).
- `canon/VERSION` von `2.3.0` auf `2.4.0-draft` angehoben, damit kein weiterer Tag auf einer veralteten Version landet.

## [2.3.0] — 2026-10-26

Release von canon 2.3.0 (MINOR: neues Konzept, neue Rolle, neues Schema). Enthält PR #4. `canon/VERSION` = `2.3.0`, Tag `canon-v2.3.0` wurde auf den Merge-Commit bde5cc0 gesetzt. ADR-0007 ist angenommen.

### Hinzugefügt
- `canon/learning.kl`: Consent-gesteuerte Lernschleife mit `Principal`, `ConsentRequest`, `ConsentDecision`, `RequestConsent`, `ReIngest` und `LearningLoop` (ADR-0007).
- `canon/schemas/consent.schema.json` (`request`, `decision`; `approved` nur durch den Principal und ohne Veto, `vetoed` nur mit Veto).
- Rolle `consent-gate` in `canon/roles.yaml` (noch ohne Persona im Profil `ocs-classic`).
- Fehlercodes `consent_missing` und `consent_rejected`.
- `tools/validate.py` prüft Consent-Instanzen und `ReIngest`-Vorbedingungen statisch.
- Beispiele `examples/sample-plan-consent-loop.json`, `sample-consent-*.json`, `sample-reingest.json`; Negativ-Fixtures `examples/invalid/consent-*.json` und `reingest-*.json`.
- Molekül `molecules/consent-gated-learning-loop.kl.md` (informativ).
- ADR-0007.
- Informativ: `⫻logic/consent`, `⫻data/consent:request|decision`, Scopes `⫻logic/learn:task|meta`.

### Geändert
- `CheckNewPrompts`/`CheckNewPrompt`: Prompt-Updates aus Lernzyklen nur noch über `ReIngest` (nur Beschreibung, keine Signaturänderung).
- `canon/SPEC.md`: `learning.kl` in §1, Konformitätsregel 5 in §6.

## [2.2.0] — 2026-10-22

Release von canon 2.2.0. Enthält alle Änderungen gegenüber 2.2.0-draft (PR #2). `canon/VERSION` = `2.2.0`, Tag `canon-v2.2.0` wurde auf den Merge-Commit 055f4da gesetzt.

### Hinzugefügt
- `canon/SPEC.md`: Geltungsbereich, Notation, Neutralitätsregeln, Referenzierung über `main`, Namensraum `⫻x-tNNN/`.
- `canon/VERSION`.
- `canon/roles.yaml` (abstrakte Rollen-IDs) und das nicht kanonische Profil `examples/profiles/ocs-classic.yaml` (inklusive Kodax und Aurora).
- `canon/tas.kl` und `canon/schemas/tas.schema.json` (TAS, Herkunft t20; ADR-0006).
- `Orchestrator.AssignAgent` als Laufzeitprüfung, dass ein gesetztes `task.name` in `Session.agents` existiert (ADR-0004).
- `tools/validate.py` prüft zusätzlich die Semantik von Plänen (eindeutige IDs, Referenzen, Rollen, Zyklen, Agenten) und TAS-Instanzen.
- `tools/lint.py`: Prüfung der ⫻-Notation und der Neutralität.
- CI-Workflow `.github/workflows/canon.yml` (aktiv seit 93040d7).
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
