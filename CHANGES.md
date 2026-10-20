# CHANGES — Input `runtime/types.py`-KickLang → t333 canon 2.2.0-draft

Aufteilung: `canon/runtime.kl` ist normativ und neutral. `examples/runtime-python/bindings.kl` ist nicht kanonisch.

## Neue Typen
- **Error, Result<T,E>, SchemaRef** neu eingeführt. Begründung: einheitliche Fehlerbehandlung statt Fehler-Strings und `null`.
- **ArtifactStore** (mit PutArtifact/FetchArtifact) neu. Begründung: `Session` soll keine Ablage im Dateisystem voraussetzen.
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
- Geprüft mit `tools/validate.py`. Gültige Beispiele: `examples/sample-plan.json`.
