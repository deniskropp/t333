# ADR-0001: `canon/` als einzige normative Schicht

- Status: angenommen · Datum: 2026-10-21

## Kontext
Normative Inhalte waren über `README.md` und `docs/ocs-space-gen.kl.md` verteilt und mit Personas, Projekten und Versionslabels (v2.1, v3.0, v4.1) vermischt. Abgeleitete Systeme hatten deshalb keine eindeutige Referenz.

## Entscheidung
- **`canon/` ist normativ:** `SPEC.md`, `VERSION`, `runtime.kl`, `tas.kl`, `roles.yaml` und `schemas/`.
- **Informativ:** `docs/` und `README.md`.
- **Beispiele:** `examples/` (Spaces, Profile, Bindings, Fixtures) und `templates/`. `spaces/` geht in `examples/` auf.
- **Rollen** sind im Kanon abstrakte IDs. Personas stehen in Profilen (`examples/profiles/`).
- **Notation:** `⫻type/scope` ohne Leerzeichen.
- **Versionen:** Es gibt nur noch die Linie *canon 2.2.0*.

## Konsequenzen
- `tools/lint.py` erzwingt Notation und Neutralität (keine Persona-, Projekt- oder Anbieternamen in `canon/`).
- Persona-lastige Texte bleiben erhalten, sind aber als informativ gekennzeichnet.
