⫻kicklang:molecule
# kernel/molecule/normative-contracts
# target: canon/runtime.kl
# version: 2.2.0
# status: normative-registration
# contains: result-contracts + artifact-store + plan-task-dag

⫻context/klmx:Kick/Lang
layer: kernel
role: contract-registration

⫻data/obj: "Register the core normative contracts as a single kernel molecule set"

⫻data/spec:
  molecule_id: "normative-contracts"
  version: "2.2.0"
  contracts:
    - result-contracts
    - artifact-store
    - plan-task-dag

# ----- Result -----
⫻logic/register result:
  fallible_ops: [GeneratePlan, ExecuteTask, CurrentStep, AddArtifact, GetArtifact, GenerateContent]
  return_type: Result<T, Error>
  invariant: "exactly one of value or error"

# ----- ArtifactStore -----
⫻logic/register artifact-store:
  interface: ArtifactStore
  operations:
    AddArtifact → Result<void, Error>
    GetArtifact → Result<Artifact, Error>
  invariant: "storage-agnostic; no filesystem assumption"
  error_codes: [not_found]

# ----- Plan/Task DAG -----
⫻logic/register plan-task-dag:
  structure:
    Plan.roles: list<Role>
    Plan.tasks: list<Task>
    Task.requires: list<string>
  invariant: "requires forms a DAG"
  schema: plan.schema.json

⫻logic/validate:
  if not result.ok and result.error == null: raise Error(code: "contract_violation")
  if result.ok and result.value == null: raise Error(code: "contract_violation")
  if operation implies filesystem: raise Error(code: "contract_violation")
  if cycle in Task.requires: raise Error(code: "invalid_plan")
  if Task.role not in Plan.roles: raise Error(code: "invalid_plan")

⫻data/state:
  registered: true
  kernel_version: "2.2.0"
  molecules:
    - result-contracts
    - artifact-store
    - plan-task-dag
  status: "sealed"

⫻cmd/exec: integrity-monitor   # canon role (canon/roles.yaml); default persona: examples/profiles/ocs-classic.yaml
  validate: combined molecule registration

⫻end/molecule
