# ADR-0007: Consent-gesteuerte Lernschleife

- Status: vorgeschlagen · Datum: 2026-10-25

## Kontext
`⫻logic/learn` („rewrites TAS heuristics“) und `⫻rule/self-adaptation` stehen nur informativ in `docs/ocs-space-gen.kl.md`. Der Kanon hat keinen Begriff dafür, wann Lernergebnisse ins System zurückfließen dürfen. Gleichzeitig wenden `CheckNewPrompts`/`CheckNewPrompt` Prompt-Updates direkt an. Ein Lernzyklus könnte das System also ohne Freigabe umschreiben. Eine Schleife innerhalb eines Plans ist nicht möglich, weil `requires` zyklenfrei sein muss (SPEC §6).

## Entscheidung
- Neu: `canon/learning.kl` mit `Principal`, `ConsentRequest`, `ConsentDecision`, `RequestConsent`, `ReIngest` und `LearningLoop` sowie `canon/schemas/consent.schema.json`. Alle fehlbaren Operationen liefern ein `Result` (ADR-0002). Jedes Gate-Ergebnis (`approved`, `rejected`, `vetoed`, `expired`) ist ein Wert, kein Fehler.
- Stufen: Learning → Meta-Learning → Meta-Iteration → Consent Gate → Re-Ingestion. Die Rückkante läuft über Runden: `ReIngest` liefert die Inputs für `round_num + 1` innerhalb desselben `StartWorkflow`-Laufs (begrenzt durch `rounds`), nicht über `requires`.
- Neue Rolle `consent-gate` in `canon/roles.yaml`. Zustimmen darf nur der **Principal**, der kein Agent ist (`decided_by` ∉ `Session.agents`). `ethics-gate` und `integrity-monitor` können ein Veto einlegen; ein Veto schlägt jede Zustimmung. Schweigen und Timeout ergeben `expired` und gelten als Ablehnung. `conflict-resolution` entscheidet nie über eine Freigabe.
- Die Zustimmung ist an den `candidate_hash` gebunden und gilt für genau ein `ReIngest`.
- Jede Entscheidung wird per `AddArtifact` abgelegt: `approved` unter `consent/<round_num>/<candidate_id>`, alle anderen unter `archive/consent/<round_num>/<candidate_id>`, jeweils zusätzlich als `⫻data/trace`. Artefaktnamen sind Schlüssel, keine Pfade (ADR-0003). Das Archiv ist kein Lern-Input.
- `ReIngest` ist der einzige kanonische Weg zurück. Lernbedingte Prompt-Updates laufen nicht direkt über `CheckNewPrompts`, sondern über `ReIngest` → `CheckNewPrompt` mit dem freigegebenen Diff.
- Neue Fehlercodes (ergänzen die Liste aus ADR-0002, die nicht umgeschrieben wird): `consent_missing` (keine passende Entscheidung), `consent_rejected` (Entscheidung nicht `approved`). Hash-Abweichung oder ein Agent als Zustimmender: `contract_violation`.
- Ein Ethik-Veto löst das bestehende `⫻cmd/halt:ethics` aus. Es wird kein neuer Halt-Modus eingeführt.
- Die neuen Protokoll-Elemente `⫻logic/consent`, `⫻data/consent:request|decision` und die Scopes `⫻logic/learn:task|meta` sind informativ (`docs/`), wie das übrige Direktiven-Vokabular.
- Persona-Belegung von `consent-gate` nur in Profilen (`examples/profiles/`).

## Konsequenzen
- MINOR-Version (canon 2.3.0): neues Konzept, neue Rolle, neues Schema. `canon/VERSION` wird erst im Release-Commit angehoben (Muster 2.2.0).
- `tools/validate.py` prüft `examples/sample-consent*.json`, `examples/sample-reingest*.json` und die Negativ-Fixtures `examples/invalid/consent-*.json` / `reingest-*.json` (`consent_missing`, `consent_rejected`, Hash-Abweichung, Agent als Principal, `approved` mit Veto).
- Abgeleitete Systeme müssen ihren Lern- bzw. Self-Adaptation-Pfad hinter `RequestConsent`/`ReIngest` legen, um canon-konform zu bleiben (SPEC §6 Regel 5).
- `CheckNewPrompts` liefert weiter `void` statt `Result` (Abweichung von SPEC §6 Regel 4). Das gefährdet das Gate nicht, weil lernbedingte Updates nur über `ReIngest` laufen. Die Umstellung auf `Result` ist eine eigene, brechende Änderung mit Migrationshinweis und Tests.

## Geklärte Fragen (2026-10-26)
- **Persona für `consent-gate`:** Im Kanon gibt es keine. `examples/profiles/ocs-classic.yaml` bekommt vorerst auch keinen Eintrag, sondern erst, wenn ein Profil eine sichtbare Identität braucht.
- **Verweigerte Zustimmung:** `rejected`, `vetoed` und `expired` sind Gate-Ereignisse, keine gescheiterte Runde. Sie werden nicht re-ingested, und eine folgende Runde läuft auf dem unveränderten Stand. Eine Runde gilt nur dann als gescheitert, wenn die Runtime das ausdrücklich festlegt. Für Auswertungen zählt der Entscheidungsstatus. Der Fehlercode `consent_rejected` entsteht nur, wenn `ReIngest` trotzdem mit einer nicht freigegebenen Entscheidung aufgerufen wird.
- **`kind`:** Es bleibt bei den vier Werten `ptas`, `spec`, `prompt_update` und `heuristic`.
- **Vertretung des Principal:** Der Kanon kennt keine Vertretung. Eine delegierte Freigabe gehört in die Profil- bzw. Policy-Schicht, und auch eine Vertretung darf kein Agent sein.
- **Meta-Learning:** Das ist keine eigene Rolle, sondern eine Aufgabe von `coordination`, dem Fallback-Owner laut `canon/roles.yaml`.
