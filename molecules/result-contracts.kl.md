⫻kicklang:molecule
# kernel/molecule/result-contracts
# target: canon/runtime.kl
# version: 2.2.0-draft
# status: normative-registration

⫻context/klmx:Kick/Lang
layer: kernel
role: contract-registration

⫻data/obj: "Register Result discipline as a first-class kernel molecule"

⫻data/spec:
  molecule_id: "result-contracts"
  kernel_concepts:
    - Result
    - Error
  registration:
    fallible_ops:
      - GeneratePlan
      - ExecuteTask
      - CurrentStep
      - AddArtifact
      - GetArtifact
      - GenerateContent
    return_type: "Result<T, Error>"
    invariant: "exactly one of value or error"

⫻logic/register:
  for op in fallible_ops:
    kernel.bind(op, return_type: Result)
    kernel.enforce(invariant)

⫻logic/validate:
  if not result.ok and result.error == null:
    raise kernel.Error(code: "contract_violation")
  if result.ok and result.value == null:
    raise kernel.Error(code: "contract_violation")

⫻data/state:
  registered: true
  kernel_version: "2.2.0-draft"
  molecule: "result-contracts"

⫻cmd/exec: integrity-monitor   # canon role (canon/roles.yaml); default persona: examples/profiles/ocs-classic.yaml
  validate: molecule registration

⫻end/molecule
