# Architecture: Normative Kernel

## Role
The normative kernel (`canon/runtime.kl`) is the implementierungsneutral core of the OCS Node.

## Responsibilities
- Define typed primitives (Result, Error, Plan, Task, Artifact, Session, ExecutionContext, LLM, Agent, Orchestrator)
- Enforce Result discipline on all fallible operations
- Provide abstract ArtifactStore (no filesystem assumption)
- Guarantee Plan/Task DAG structure

## Key Invariants
- Exactly one of Result.value or Result.error is set
- ArtifactStore is storage-agnostic
- Task.requires forms a DAG
- model_id is the single model identifier

## Dependencies
None. The kernel depends on nothing outside itself.

## Consumed by
Kernel molecules, OCS protocol surface, Spaces, and bindings.
