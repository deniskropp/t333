# CHANGES — Input `runtime/types.py`-KickLang → t333 canon 2.2.0-draft

Aufteilung: `canon/runtime.kl` ist normativ und neutral. `examples/runtime-python/bindings.kl` ist nicht kanonisch.

## Neue Typen
- **Error, Result<T,E>, SchemaRef** neu eingeführt. Begründung: einheitliche Fehlerbehandlung statt Fehler-Strings und `null`.
- **ArtifactStore** (mit AddArtifact/GetArtifact) neu. Begründung: `Session` soll keine Ablage im Dateisystem voraussetzen.
- **LLM, ExecutionContext, Session** sind jetzt vollständig definiert. Im Input wurden sie nur angenommen („Assuming … elsewhere“).

## Geänderte Felder und Signaturen
- `ExecutionContext.plan`: `map<string,any>` → `Plan`. Begründung: typsicher und gegen ein Schema prüfbar.
- `CurrentStep`: Ausgabe `map` → `Result<Task, Error>` (Fehler, wenn `step_index` außerhalb des Plans liegt).
- `ExecuteTask`: `optional<string>` → `Result<AgentOutput, Error>`.
- `GeneratePlan`: `map` (bei Fehler leer) → `Result<Plan, Error>`. `file_contents` → `inputs: list<Artifact>`.
- `StartWorkflow`: `files: list<string>` (Pfade) → `inputs: list<Artifact>` und Rückgabe `Result<void, Error>`.
- `GenerateContent`: `response_schema: BaseModel` (Pydantic) → `schema_ref: SchemaRef` (JSON Schema 2020-12). `model_name` → `model_id`. Rückgabe `Result<string, Error>`.
- **`Agent.model` und `LLM.species` → einheitlich `model_id`.** Begründung: Beide Felder bedeuteten dasselbe, und „species“ ist kein neutraler Begriff.
- `Session.session_dir` → `Session.store: ArtifactStore`. Der Verzeichnisbezug lebt als `FileArtifactStore` in den Bindings weiter.
- `AddArtifact`/`GetArtifact`: Beschreibung ohne „directory“. Rückgabe ist jetzt ein `Result`, `GetArtifact` liefert `Artifact` statt `any`.
- `RecordArtifact`, `CheckNewPrompt`, `InstantiateAgent`: Rückgabe ist jetzt ein `Result`, statt `void` oder `optional`.
- `Artifact`: optionales Feld `media_type` ergänzt.
- `LLM.functions`: `Factory` entfernt, denn das Erzeugen von Instanzen gehört zur Implementierung.

## Verschoben nach `examples/runtime-python/bindings.kl` (nicht kanonisch)
- `Gemini`, `Olli`, `Kimi` (jetzt `implements: LLM`, `species` → `model_id`), `GetClient`, `Factory`.
- `LoadConfig`, `LoadAgentTemplates` (`default_model` → `default_model_id`), `LoadPrompts`. Begründung: YAML-, Pfad- und Dateiformate sind Implementierungsdetails.
- `RuntimeConfig` inklusive Schema. Begründung: `logging_level` und `api_endpoints` sind spezifisch für diese Runtime.

## Schemas
- `canon/schemas/{role,task,plan,artifact,agent-output,error,session,execution-context}.schema.json` (Draft 2020-12).
- `session` und `execution-context` decken nur den serialisierbaren Teil ab: Statt der Objekte stehen dort `session_id` bzw. `store_ref`.
- Geprüft mit `tools/validate.py`. Gültiges Beispiel: `examples/sample-plan.json`.

## Revision 2 (freigegebene offene Punkte)
- **Einheitliche Namen:** `PutArtifact` und `FetchArtifact` entfallen. Kanonisch sind nur noch `AddArtifact`/`GetArtifact`. Sie sind primär auf `ArtifactStore` definiert, und `Session` delegiert an `Session.store`. `FileArtifactStore` in den Bindings nutzt dieselben Namen.
- **Beibehalten wie beschlossen:** `inputs: list<Artifact>` und die Session-Zustände `init`/`running`/`done`/`failed`.
- **`tools/validate.py` prüft jetzt auch die Semantik von Plänen:**
  - Eindeutigkeit der `task_id`s
  - ob `requires` nur auf vorhandene Tasks verweist
  - ob `task.role` einem Rollentitel in `plan.roles` entspricht
  - ob `requires` zyklenfrei ist (ein gefundener Zyklus wird ausgegeben)
- `validate.py` läuft aus jedem Verzeichnis. Ohne Argumente prüft es das gültige Beispiel und alle Negativfälle, mit Argumenten die angegebenen Plan-Dateien.
- **Negativ-Fixtures** in `examples/invalid/`: `duplicate-id`, `dangling-ref`, `cycle`, `unknown-role`.

## Revision 3 (canon/2.2.0)
- **`Task.name` ist optional:** Die Agentenzuweisung erfolgt zur Laufzeit.
  - Neues Konzept `AssignAgent(session, task) → Result<Agent, Error>` am `Orchestrator`.
  - Ist `name` gesetzt, muss es in `Session.agents` existieren (`unknown_agent`). Sonst wird über `FindAgentByRole` zugewiesen (`no_agent_for_role`).
- `task.schema.json`: `name` ist dokumentiert und optional.
- `validate.py` prüft optional `task.name` gegen eine Session (`--session`). Im Standardlauf wird `examples/sample-session.json` verwendet.
- **Neue Beispiele:** `examples/sample-session.json`, `examples/sample-plan-unassigned.json`. **Neues Negativ-Fixture:** `examples/invalid/unknown-agent.json`.
- **TAS-Konzept:** Neu sind `canon/tas.kl` (`TAS`, `TASCategory`, `ExtractTAS`, `PurifyTAS`, `PlanFromTAS`) und `canon/schemas/tas.schema.json`.
  - Abgeleitet aus deniskropp/t20: `src/t20/assets/prompts/gptase_instructions.txt` und `docs/kl-task-agnostic-steps.md`.
  - Beispiel: `examples/sample-tas.json`. Negativ-Fixture: `examples/invalid/tas-bad-category-and-duplicate.json`.
- **Aufräumen nach dem SSoT-Vorschlag:**
  - ⫻-Notation vereinheitlicht und `spaces/` nach `examples/` verschoben.
  - Neu: `canon/roles.yaml` und das Profil `examples/profiles/ocs-classic.yaml`.
  - Einheitliche Versionslinie *canon 2.2.0*.
  - Persona- und Projektbezüge aus normativen Texten entfernt.
  - Neu: `canon/SPEC.md` und `CHANGELOG.md`, dazu ADRs unter `docs/adr/`.
- **CI:** `ci/canon.yml` (Ziel: `.github/workflows/canon.yml`) führt `tools/validate.py` und `tools/lint.py` aus.
