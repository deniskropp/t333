⫻kicklang:molecule
# kernel/molecule/plan-task-dag
# target: canon/runtime.kl
# version: 2.2.0-draft
# status: normative-registration

⫻context/klmx:Kick/Lang
layer: kernel
role: contract-registration

⫻data/obj: "Register Plan/Task DAG as a first-class kernel molecule"

⫻data/spec:
  molecule_id: "plan-task-dag"
  kernel_concepts:
    - Plan
    - Task
    - Role
  registration:
    structure:
      Plan:
        roles: list<Role>
        tasks: list<Task>
      Task:
        task_id: string
        role: string
        requires: list<string>
    invariant: "requires forms a directed acyclic graph"
    validation: plan.schema.json

⫻logic/register:
  kernel.bind(Plan, schema: plan.schema.json)
  kernel.bind(Task.requires, constraint: DAG)
  kernel.enforce(invariant: "no cycles in requires")

⫻logic/validate:
  if cycle detected in Task.requires:
    raise kernel.Error(code: "invalid_plan", message: "cycle in task DAG")
  if Task.role not in Plan.roles:
    raise kernel.Error(code: "invalid_plan", message: "unknown role")

⫻data/state:
  registered: true
  kernel_version: "2.2.0-draft"
  molecule: "plan-task-dag"
  dag_enforced: true

⫻cmd/exec: SystemMonitor
  validate: molecule registration

⫻end/molecule
