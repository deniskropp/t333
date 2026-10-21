# ADR-0006: TAS als Kanon-Konzept, Herkunft t20

- Status: angenommen · Datum: 2026-10-21

## Kontext
Task-Agnostic Steps (TAS) sind zentral für den Ablauf `⫻data/obj → tas → ptas → spec`, waren in t333 aber nur als Payload-Namen erwähnt. Definiert sind sie in **deniskropp/t20**:
- `docs/kl-task-agnostic-steps.md` (Playbook: Identify/Extract → Structure → Layer → Transfer → Context → Purify)
- `src/t20/assets/prompts/gptase_instructions.txt` (Datenschema: `id`, `name`, `description` (≥30 Zeichen), `category` ∈ {Init, Analysis, Planning, Execution, Refactoring, Review}, `purpose`, optional `keywords`, `applicability_notes`, `examples_of_usage`, `typical_inputs`, `typical_outputs`)
- `src/t20/assets/prompts/putase_instructions.txt` (Purify-Methodik)
- `src/t20/kicklang/OCS.klang` (Phase3 EXTRACT_TAS durch mehrere Extraktoren → CONSOLIDATE → Phase4 PURIFY)

## Entscheidung
- Neu: `canon/tas.kl` (`TAS`, `TASCategory`, `ExtractTAS`, `PurifyTAS`, `PlanFromTAS`) und `canon/schemas/tas.schema.json`. Alle Operationen liefern ein `Result`.
- Personas (GPTASe, TASe, uTASe, puTASe) bleiben im Profil `examples/profiles/ocs-classic.yaml`.
- Referenzimplementierung ist Python (t20). t484 (C++/QML, OCS/Node Engine) ist ein optionales Binding.

## Konsequenzen
- Die t20-Prompts bleiben Implementierungsdetail. Das Kanon-Schema ist die Vertragsgrundlage.
- `examples/sample-tas.json` und ein Negativ-Fixture werden in CI geprüft.
