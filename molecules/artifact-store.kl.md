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
    - PutArtifact
    - FetchArtifact
  registration:
    interface: ArtifactStore
    operations:
      - PutArtifact → Result<void, Error>
      - FetchArtifact → Result<Artifact, Error>
    invariant: "no filesystem or directory assumption"
    error_codes:
      - not_found

⫻logic/register:
  kernel.bind(ArtifactStore, abstract: true)
  kernel.bind(PutArtifact, return_type: Result<void, Error>)
  kernel.bind(FetchArtifact, return_type: Result<Artifact, Error>)
  kernel.enforce(invariant: "storage-agnostic")

⫻logic/validate:
  if operation implies filesystem path:
    raise kernel.Error(code: "contract_violation", message: "filesystem assumption forbidden in canon")
  if FetchArtifact misses and error.code != "not_found":
    raise kernel.Error(code: "contract_violation")

⫻data/state:
  registered: true
  kernel_version: "2.2.0-draft"
  molecule: "artifact-store"
  abstract: true

⫻cmd/exec: SystemMonitor
  validate: molecule registration

⫻end/molecule
