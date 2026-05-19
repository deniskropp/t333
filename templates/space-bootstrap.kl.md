⨻ kicklang:header
# OCS Space Bootstrap Template (from T333 Substrate)

⨻ context/klmx:Space/Bootstrap
This template provides a minimal, reusable bootstrap for any new OCS Space. It encapsulates the core protocol, data schema, and launch sequence. Customize the objective, team extensions, and output focus. Inherit all v2.1 primitives from the T333 substrate.

⨻ protocol/ocs:
# Inherit full directives, data payloads, logic from substrate
# Extend only as needed for this Space's domain

⨻ data/obj: "[INSERT HIGH-LEVEL OBJECTIVE HERE]"
⨻ data/state: {
  phase: "init",
  threads: 0,
  ethics: "clear",
  mode: "Hybrid",
  coherence: "target-high",
  space_name: "[SPACE_NAME]"
}

⨻ team:
  # Core inherited from T333
  # Add domain-specific extensions here
  - extensions:
      - DomainExpert: "Specialized knowledge for this Space's focus"
      - [YourCustomRole]: "Description and responsibilities"

⨻ flow/launch:
  1. ⨻ cmd/exec:GPTASe -> ⨻ data/tas (from obj)
  2. ⨻ cmd/exec:puTASe -> ⨻ data/ptas
  3. ⨻ cmd/exec:Lyra -> ⨻ data/spec
  4. ⨻ cmd/broadcast:{event:"phase:init:swarm", space:"[SPACE_NAME]"}
  5. Swarm execution per smart-execution or custom parallel streams
  6. ⨻ logic/reconverge + ⨻ logic/learn
  7. Maintain Hybrid mode with active monitoring

⨻ logic/validate:
  - ethics: Dima
  - bias: SystemMonitor
  - semantic: Synapse
  - temporal: Chronos

⨻ cmd/mode:Hybrid
⨻ cmd/lang:KickLang

# End of bootstrap — expand with domain logic, custom flows, or full Space spec