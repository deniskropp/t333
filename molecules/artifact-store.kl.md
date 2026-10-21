⫻kicklang:molecule
# kernel/molecule/artifact-store
# target: canon/runtime.kl
# version: 2.2.0-draft
# status: normative-registration

⫻context/klmx:Kick/Lang
layer: kernel
role: contract-registration

⫻data/obj: "Register ArtifactStore as a first-class kernel molecule"

⫻data/spec:
  molecule_id: "artifact-store"
  kernel_concepts:
    - ArtifactStore
    - Artifact
    - AddArtifact
    - GetArtifact
  registration:
    interface: ArtifactStore
    operations:
      - AddArtifact → Result<void, Error>
      - GetArtifact → Result<Artifact, Error>
    invariant: "no filesystem or directory assumption"
    error_codes:
      - not_found

⫻logic/register:
  kernel.bind(ArtifactStore, abstract: true)
  kernel.bind(AddArtifact, return_type: Result<void, Error>)
  kernel.bind(GetArtifact, return_type: Result<Artifact, Error>)
  kernel.enforce(invariant: "storage-agnostic")

⫻logic/validate:
  if operation implies filesystem path:
    raise kernel.Error(code: "contract_violation", message: "filesystem assumption forbidden in canon")
  if GetArtifact misses and error.code != "not_found":
    raise kernel.Error(code: "contract_violation")

⫻data/state:
  registered: true
  kernel_version: "2.2.0-draft"
  molecule: "artifact-store"
  abstract: true

⫻cmd/exec: integrity-monitor   # canon role (canon/roles.yaml); default persona: examples/profiles/ocs-classic.yaml
  validate: molecule registration

⫻end/molecule
