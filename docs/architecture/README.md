# OCS Node Architecture

Top-level index of the OCS Node architecture as defined by the normative substrate (canon 2.3.0).

## Layers

| # | Document | Layer | Description |
|---|----------|-------|-------------|
| 01 | [01-kernel.md](01-kernel.md) | Normative Kernel | Typed primitives, Result discipline, abstract ArtifactStore, DAG Plans |
| 02 | [02-molecules.md](02-molecules.md) | Kernel Molecules | Registrable contract units (Result, ArtifactStore, Plan/Task DAG) |
| 03 | [03-protocol.md](03-protocol.md) | OCS Protocol | ⫻-section meta-communicative surface |
| 04 | [04-spaces.md](04-spaces.md) | Spaces | Instantiated operational environments |
| 05 | [05-bindings.md](05-bindings.md) | Bindings | Non-canonical concrete implementations |

## Overview

```
Spaces / Flows / Agents
        ↓
OCS Protocol (⫻ sections)
        ↓
Kernel Molecules
        ↓
Normative Kernel (canon/runtime.kl)
        ↓
Bindings (examples/)
```

## Invariants
- Result discipline on all fallible operations
- ArtifactStore is storage-agnostic
- Plan/Task structure is a DAG
- Bindings never leak into the kernel

## Related
- `canon/runtime.kl`
- `molecules/`
- `CHANGES.md`
- `RELEASE_NOTES_canon-2.2.0.md`
