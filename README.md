# T333: OCS Substrate — KickLang Meta-Framework

**T333** is the foundational **substrate** for the **Orion Collective System (OCS)** and **KickLang** meta-framework. It provides the protocols, templates, data schemas, and initialization logic for creating, managing, and evolving dynamic **Spaces** — modular, swarm-coordinated, multi-persona AI operational environments.

This repository serves as the cognitive base layer (substrate) upon which specialized tXXX agent systems, workflows, and creative/analytical projects are built. It emphasizes:

- **Meta-communicative organization** via `⫻` sectioned KickLang documents.
- **Swarm intelligence** with adaptive roles, ethical oversight, and self-healing flows.
- **High-fidelity execution** from high-level intent through structured TAS (Task-Agnostic Steps), purification, and orchestration.
- **Traceability, coherence, and resilience** as first-class concerns.

> **Status**: Foundational Substrate (OCS v2.1 / evolving toward v3.0 protocol interfaces)  
> **Normative Runtime**: canon 2.2.0-draft (`canon/runtime.kl` + JSON Schema 2020-12)  
> **Related**: Builds upon patterns from t20, t138, t141, t324, t450, t484 and the broader OCS/KickLang skill ecosystem.  
> **Usage**: Initialize new Spaces, define custom flows, or extend the agent collective.

---

## Philosophy

The OCS Substrate treats AI collaboration as a **cognitive computational linguistic transport and transform**. Natural language intent is translated into formal KickLang, executed by a unified multi-persona entity (the collective), and produces high-value, auditable artifacts.

Key principles:
- **Modularity & Clarity**: Every section starts with `⫻type/scope` for parseable, composable knowledge units.
- **Hybrid Intelligence**: Blends creative exploration (`Creative`/`Hybrid` modes) with strict ethical/protocol compliance (`Strict`/`Audit`).
- **Swarm Coordination**: Autonomous agents operate in parallel threads, synchronized via events, reconverge points, and learning loops.
- **Substrate Mindset**: Like a blockchain or OS kernel, this provides the persistent base primitives (commands, data payloads, logic gates, team matrix) that higher-level Spaces and agents inherit and extend.
- **Ethical & Resilient Core**: Dima + SystemMonitor + Halin ensure integrity; self-healing on minor failures.

This substrate enables **Space Generation** — the rapid bootstrapping of new operational contexts (e.g., innovation labs, ethics simulators, design workspaces) with consistent protocols.

---

## Normative Runtime Layer (canon 2.2.0-draft)

The `canon/` directory contains the **implementierungsneutral** runtime kernel. It defines typed, schema-backed primitives that higher Spaces and flows inherit.

- **`canon/runtime.kl`** — Normative concepts (Error, Result<T,E>, ArtifactStore, Plan, ExecutionContext, Session, LLM, Orchestrator, …)
- **`canon/schemas/*.schema.json`** — JSON Schema Draft 2020-12 for serializable data concepts
- **`CHANGES.md`** — Delta from prior informal types to the locked 2.2.0-draft surface

Key contracts introduced:
- All fallible operations return `Result<T, Error>` (no free-form error strings or null)
- Persistence is exclusively via abstract `ArtifactStore` (no filesystem assumption in canon)
- `ExecutionContext.plan` is a typed `Plan` (DAG of Tasks)
- Unified `model_id` for Agent and LLM

Non-canonical bindings and loaders live under `examples/runtime-python/`.

Validation reference: `tools/validate.py` + `examples/sample-plan.json`.

---

## KickLang & ⫻ Sections

KickLang is the formal language making the knowledge graph a living cognitive system. Documents and runtime state use structured sections:

```
⫻kicklang:header
# Kick Language Description

⫻context/klmx:Kick/Lang
...context and persona encapsulation...

⫻protocol/ocs:
...directives, data payloads, logic...

⫻team:
...agent roles...

⫻flow:
...execution sequences...

⫻data/obj: "..."
⫻data/state: { ... }
```

See `docs/ocs-space-gen.kl.md` for the complete template and Space generation instructions.

---

## OCS Protocol (v2.1)

### 1. Directives (Enhanced Control Layer)
- `⫻cmd/exec:<agent|team|flow>` — Delegate with flags (`async`, `sync`, `strict`, `collab`)
- `⫻cmd/halt:<mode>` — Interrupt (`error`, `ethics`, `manual`, `safety`)
- `⫻cmd/mode:<Strict|Creative|Fluid|Swarm|Silent|Audit|Predictive|Hybrid>`
- `⫻cmd/lang:<KickLang|Python|Markdown|JSON>`
- `⫻cmd/broadcast:{event:..., state:...}` — Swarm signaling

### 2. Data Payloads
Core containers maintained in every Space:
- `⫻data/obj` — Master objective
- `⫻data/tas` / `⫻data/ptas` — Task-Agnostic Steps (raw → purified via puTASe)
- `⫻data/spec` — Execution blueprint / workflow spec
- `⫻data/state` — Live operational state
- `⫻data/trace` — Immutable activity log
- `⫻data/insight` — Derived knowledge from learning cycles
- `⫻data/logic`, `⫻data/event`, `⫻data/rv`, `⫻data/cite`, `⫻data/var`

### 3. Logic Primitives
- `⫻logic/if`, `⫻logic/switch`, `⫻logic/loop`, `⫻logic/reconverge`, `⫻logic/learn` (reflective)
- Monitoring layer: `⫻logic/error` (ethics → Dima, bias → SystemMonitor, conflict → Halin) and `⫻logic/validate` (integrity checkpoints)

### 4. Team Roles (Adaptive Agents)

| Role              | Responsibility                              | Notes |
|-------------------|---------------------------------------------|-------|
| GPTASe            | TAS extractor                               | Initial task decomposition |
| puTASe            | TAS purifier                                | Cleans & validates steps |
| Lyra              | Prompt Engineer / Workflow Structurer       | Specs & refinement |
| Fizz La Metta     | Coordinator / System Monitor                | Cognitive coordination |
| AI Tutor          | Knowledge transfer                          | - |
| Codein            | Code Investigator                           | - |
| Dima              | Ethical Compliance / Joint Decisions        | Halt on ethics |
| AR-00L            | Visual Assets                               | - |
| QllickBuzz / QllickFizz | Operational Rules                      | Mode & rule enforcement |
| WePlan            | Strategic / Tailored Plans                  | - |
| Kick La Metta     | NL to Formal Translation                    | - |
| Orchestrator      | Dynamic Role Adaptation / Holistic / Swarm  | Central flow control |
| SystemMonitor     | Integrity Monitoring                        | Validation checkpoints |
| **Synapse**       | Inter-agent memory & semantic consistency   | NewOCS addition |
| **Chronos**       | Temporal dependencies & scheduling          | NewOCS addition |
| **Halin**         | Conflict resolution (creative vs ethical)   | NewOCS addition |

### 5. Execution Flows (Swarm+)
- Standard sequential TAS → ptas → spec → swarm
- `⫻flow/smart-execution`
- `⫻flow/swarm` with spawn/merge/rebalance, event-based sync, self-healing

### 6. Meta Rules (NewOCS addition)
- `⫻rule/self-adaptation` — agents adjust internal behavior via reflective logic
- `⫻rule/transparency` — every execution command produces an auditable trace
- `⫻rule/fallback` — control ownership ambiguities resolved through Fizz La Metta

### 7. KickLang Layers (NewOCS addition)
- **ISO-style specification** — role-bound, graph-native cognitive orchestration language (normative refs, conformance, syntax, semantics, governance, formal grammar)
- **Cognitive Transform Layer (CTL)** — converts NL/symbolic intents into coherent graph operations
- **Bridge Layer** — binds cognitive flow to agent execution via hierarchical feedback loops

Full details and launch sequences in `docs/`.

---

## Space Initialization Protocol

### 1. Purpose Definition
Define **Type** (concept lab, ethics simulator, AI-design workspace, data-fusion hub...), **Scope**, **Output Focus**.

Example Space: **HelioDeck** — Swarm-based reasoning for innovation prototyping under ethical oversight.

### 2. Core Initialization
```
⫻cmd/mode:Hybrid
⫻cmd/lang:KickLang
⫻cmd/exec:Fizz La Metta sync
⫻cmd/broadcast:{event:"SpaceInit", state:"active"}
```

### 3. Schema Configuration
Maintain standard `⫻data/*` containers. Example:
```
⫻data/obj: "Enable autonomous cross-agent creativity under ethical governance"
⫻data/state: {phase:"boot", threads:0, ethics:"clear", mode:"Hybrid"}
```

### 4. Agent Assignment Matrix
See table above. Allocate according to Space needs (core + extensions).

### 5. Launch Flow (abridged)
1. `⫻cmd/exec:GPTASe` → `⫻data/tas`
2. `⫻cmd/exec:puTASe` → `⫻data/ptas`
3. `⫻cmd/exec:Lyra` → `⫻data/spec`
4. Broadcast swarm init
5. Parallel swarm execution (design/code/ethics layers)
6. `⫻logic/reconverge` + `⫻logic/learn`
7. Ongoing monitoring via validate hooks

### 6. Monitoring & Termination
- Validation checkpoints (`ethics` → Dima, `bias` → SystemMonitor)
- `⫻cmd/halt:manual` on conclusion
- Export `⫻data/trace` + archive `⫻data/insight`
- Broadcast `SpaceClosed`

See full protocol and templates in `docs/`.

---

## Project Structure

```
t333/
├── README.md                 # This file (substrate definition)
├── CHANGES.md                 # Canon 2.2.0-draft delta
├── .gitignore
├── canon/
│   ├── runtime.kl              # Normative runtime kernel (2.2.0-draft)
│   └── schemas/                # JSON Schema 2020-12 (Plan, Task, Error, Session, …)
├── docs/
│   └── ocs-space-gen.kl.md   # Master template + Space gen instructions
├── templates/
│   └── space-bootstrap.kl.md # Reusable bootstrap
├── examples/
│   ├── HelioDeck-space-init.md
│   ├── sample-plan.json       # Valid Plan example
│   └── runtime-python/        # Non-canonical bindings & config schema
├── spaces/
│   ├── AetherWeave-space-init.md
│   └── ForgeWeave-space-init.md
├── tools/
│   └── validate.py            # Schema + sample validation reference
└── visualizations/
    └── ocs-kg-explorer.html      # OCS knowledge-graph explorer
```

---

## Getting Started

1. Clone / initialize this substrate.
2. Study `docs/ocs-space-gen.kl.md` and the normative kernel in `canon/runtime.kl`.
3. Define your Space purpose.
4. Use the initialization commands and flows to bootstrap.
5. Extend team or add custom `⫻logic/*` as needed.
6. Run in `Hybrid` or `Swarm` mode for balanced creativity + governance.

Example high-level invocation (conceptual):
```
⫻cmd/exec:Orchestrator
⫻data/obj: "Create a new ethics-aware innovation Space called HelioDeck"
```

The substrate will guide decomposition, agent assignment, and execution.

---

## New Spaces Created with Templates

The following example Spaces were generated directly from the `templates/space-bootstrap.kl.md` and master protocol:

- **AetherWeave** (`spaces/AetherWeave-space-init.md`)  
  Hybrid creative narrative & world-building lab with emotional resonance tracking, lore consistency, and ethical narrative guardrails. Ideal for stories, games, and lore-heavy projects.

- **ForgeWeave** (`spaces/ForgeWeave-space-init.md`)  
  Code + creative substrate evolution lab focused on modernization, refactoring, architectural innovation, and documentation. Perfect for extending tXXX systems and technical meta-tools.

These demonstrate practical application of the substrate for both creative and technical domains.

---

## Extensibility & Future

- Add new roles via `new_roles` in team definitions.
- Evolve modes (`Predictive`, `Hybrid`).
- Integrate with higher tXXX systems or MCP/HF ecosystems.
- Persistent Meta-DNA across Spaces via Synapse + Chronos.
- Self-documenting via `⫻logic/learn` cycles.
- Extend the normative kernel under `canon/` while keeping bindings in `examples/`.

This substrate is designed to be **forked, extended, and specialized** while preserving core coherence.

---

## License & Attribution

Foundational patterns inspired by the tXXX series (deniskropp).  
KickLang / OCS protocols developed for meta-artificial intelligence Spaces.  
Use responsibly under ethical oversight (Dima layer always active).

**High-value artifacts produced here become the seeds for new specialized repositories and operational Spaces.**

---

## Status Update — October 2026

The substrate remains the canonical public reference for OCS Space generation and KickLang sectioned protocols. Since initial release:

- Three-agent-core (KickForge / KickFlow / KickGuard) has become the dominant orchestration pattern across the ecosystem and is fully compatible with this substrate's team and flow model.
- KickLang has advanced to v4.1+ with parser/emitter cores, Meta-Playbook patterns, and bidirectional bridges (see related repos).
- Living skill ecosystem (ocs-skill-builder, kicklang-meta-playbook, tas-forecast-cycle, aetheris-video-pipeline, and others) consumes and extends these protocols.
- **Normative runtime layer (canon 2.2.0-draft)** is now public: typed Result/Error, abstract ArtifactStore, schema-validated Plan/Task/Session.
- Public journal (@DeniOliK) and model handoffs (Grok, Copilot, Google AI Mode) continue to treat the substrate as living reference.
- Related public documentation and engines: t20 (KickLang specs), t324 (Unified MetaForge/OCS docs), t484 (OCS/Node Engine), t450 (Meta-Infrastructure workspace), parallel_f-kicklang-wrapper.

Public surface has lagged private/skill development; this update restores alignment. Next increments: schema freeze notes, explicit v3.0 protocol mapping, and onboarding examples for external Spaces.

*Substrate initialized: 2026-05-19*  
*Core: OCS v2.1 + KickLang Space Generation Template*  
*Normative runtime: canon 2.2.0-draft (2026-10-20)*  
*Status refresh: 2026-10-20*

**Sigil note:** Canonical section marker is `⫻` (U+2AFB). Previous drafts used multiplication sign (×); normalized here for consistent rendering across editors and parsers.