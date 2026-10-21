# ADR-0004: `Task.name` optional, Zuweisung zur Laufzeit

- Status: angenommen · Datum: 2026-10-21

## Kontext
Ein Plan legt fest, *was* zu tun ist und welche *Rolle* es tut. Welcher konkrete Agent den Task ausführt, steht oft erst zur Laufzeit fest, weil die Agenten pro Session unterschiedlich sind. Ein Pflichtfeld `name` würde Pläne an eine bestimmte Session binden.

## Entscheidung
- `Task.name` ist optional (Schema und `runtime.kl`).
- Neues Konzept `Orchestrator.AssignAgent(session, task) → Result<Agent, Error>`:
  - Ist `name` gesetzt, **muss** es in `Session.agents` existieren (`unknown_agent`).
  - Sonst wird per `FindAgentByRole` gewählt (`no_agent_for_role`).

## Konsequenzen
- `tools/validate.py --session S.json PLAN.json` prüft die Regel statisch. Der Standardlauf nutzt `examples/sample-session.json`.
- Fixture `examples/invalid/unknown-agent.json`.
