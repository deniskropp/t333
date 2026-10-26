⫻kicklang:molecule
# kernel/molecule/consent-gated-learning-loop
# target: canon/learning.kl
# version: 2.3.0
# status: registered (ADR-0007)

⫻context/klmx:Kick/Lang
layer: kernel
role: contract-registration

⫻data/obj: "Register a learning loop in which nothing re-enters the system without explicit consent"

⫻data/spec:
  molecule_id: "consent-gated-learning-loop"
  stages: [learning, meta-learning, meta-iteration, consent-gate, re-ingestion]
  kernel_concepts:
    - Principal
    - ConsentRequest
    - ConsentDecision
    - RequestConsent
    - ReIngest
    - AddArtifact
    - GetArtifact
    - CheckNewPrompt
    - StartWorkflow
  invariant: "every re-ingested change carries an approved ConsentDecision whose candidate_hash matches the applied content"
  error_codes:
    - consent_missing
    - consent_rejected
    - contract_violation

⫻logic/learn:task
  input: results and ⫻data/trace of round_num
  output: ⫻data/insight

⫻logic/learn:meta
  input: ⫻data/insight of rounds [1..round_num]
  output: ⫻data/insight

⫻data/consent:request
  candidate_id: "<id>"
  candidate_hash: "<content hash>"
  kind: "ptas | spec | prompt_update | heuristic"
  diff: "<change against current state>"
  evidence: [ "<insight artifact names>" ]
  round_num: 3

⫻logic/validate:ethics
⫻logic/validate:integrity

⫻logic/consent
  approve_by: principal                     # never an agent, never a role
  veto_by: [ethics-gate, integrity-monitor]
  default: reject                           # silence or timeout → expired
  on_approved: ReIngest → inputs of round_num + 1
  on_other: AddArtifact archive/consent/<round_num>/<candidate_id>   # audit only

⫻logic/loop
  LOOP round UNTIL round_num == rounds
  each round: learn:task → learn:meta → consent:request → logic/consent → ReIngest (approved only)

⫻data/trace
  event: "ConsentDecision"
  record: ConsentDecision   # on every outcome, approved or not

⫻cmd/exec: consent-gate   # canon role (canon/roles.yaml); no default persona yet
  validate: molecule registration

⫻end/molecule
