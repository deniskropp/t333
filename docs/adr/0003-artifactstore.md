# ADR-0003: Abstrakter ArtifactStore (AddArtifact/GetArtifact)

- Status: angenommen · Datum: 2026-10-20 (Namensvereinheitlichung 2026-10-21)

## Kontext
`Session.session_dir` setzte ein Dateisystem voraus. Außerdem existierten zwei Namenspaare für dieselbe Operation: `PutArtifact`/`FetchArtifact` und `AddArtifact`/`GetArtifact`.

## Entscheidung
- `Session.store: ArtifactStore`, ohne Annahme über Dateisystem oder Datenbank.
- Kanonische Operationen sind nur `AddArtifact(name, content) → Result<void, Error>` und `GetArtifact(name) → Result<Artifact, Error>` (`not_found`). Sie sind primär auf `ArtifactStore` definiert; `Session` delegiert an `Session.store`.
- `PutArtifact`/`FetchArtifact` entfallen.

## Konsequenzen
Der verzeichnisbasierte Speicher ist ein Binding (`FileArtifactStore` in `examples/runtime-python/bindings.kl`).
