# Architecture: Kernel Molecules

## Role
Kernel molecules are registrable contract units that make kernel invariants explicit and enforceable.

## Published Molecules
- `molecules/result-contracts.kl.md`
- `molecules/artifact-store.kl.md`
- `molecules/plan-task-dag.kl.md`
- `molecules/normative-contracts.kl.md` (combined)

## Responsibilities
- Register fallible operations and their Result return types
- Bind abstract interfaces (ArtifactStore)
- Enforce structural constraints (DAG)
- Provide validation hooks for SystemMonitor

## Loading
Molecules can be stored as Artifacts and loaded by the runtime to activate contract checks.
