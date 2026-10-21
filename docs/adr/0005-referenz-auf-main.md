# ADR-0005: Abgeleitete Repos referenzieren t333 `main`

- Status: angenommen · Datum: 2026-10-21 · ersetzt den früheren Vorschlag (Pinning per `ocs-manifest.yaml`/Tag)

## Kontext
Der SSoT-Vorschlag sah vor, dass abgeleitete Repos (t20, t138, t141, t324, t450, t484, …) eine bestimmte Kanon-Version per Manifest pinnen. Das ist für das kleine, eng gekoppelte Ökosystem zu viel Aufwand.

## Entscheidung
- Abgeleitete Systeme referenzieren **t333 `main`**. Es gibt kein Pinning-Manifest und keine verpflichtenden Release-Tags.
- `main` wird durch CI gültig gehalten (`.github/workflows/canon.yml`). Änderungen kommen nur per PR.
- `canon/VERSION` (SemVer) und `CHANGELOG.md` dienen der Kommunikation. Breaking Changes werden dort und per ADR angekündigt.
- Erweiterungen verwenden den Namensraum `⫻x-tNNN/…`.

## Konsequenzen
- Breaking Changes wirken sofort auf alle Konsumenten. Daher gilt: Deprecation vor Entfernung, und große Änderungen nur mit ADR.
- Ein späteres Pinning bleibt möglich (neue ADR).
