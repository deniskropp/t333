# ADR-0002: Result/Error statt Fehler-Strings und `null`

- Status: angenommen · Datum: 2026-10-20

## Kontext
Die Python-Runtime gab bei Fehlern `optional<string>`, leere Dicts oder `null` zurück. Aufrufer konnten „kein Ergebnis“ nicht von „Fehler“ unterscheiden.

## Entscheidung
Alle fehlbaren Operationen liefern `Result<T, Error>`. Dabei ist genau eines der Felder `value` und `error` gesetzt.
- `Error` hat `code`, `message`, optional `details` und `retryable` (Schema: `canon/schemas/error.schema.json`).
- Bekannte Codes: `llm_unavailable`, `invalid_plan`, `task_failed`, `not_found`, `unknown_agent`, `no_agent_for_role`, `invalid_tas`, `contract_violation`.

## Konsequenzen
- Bindings müssen Ausnahmen bzw. SDK-Fehler in `Error` übersetzen.
- Das Molekül `molecules/result-contracts.kl.md` registriert die Invariante.
