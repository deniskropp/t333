#!/usr/bin/env python3
"""t333 canon validator.

Usage:
  validate.py                      # all schemas + examples (valid must pass, examples/invalid/* must fail)
  validate.py PLAN.json [...]      # validate given plan files
  validate.py --session S.json PLAN.json [...]   # additionally check task.name against Session.agents

Checks for plans: JSON Schema (canon/schemas/plan.schema.json), task_id uniqueness,
requires -> existing task_id, task.role in plan.roles, requires acyclic,
and (with a session) task.name (if set) in Session.agents (runtime rule of AssignAgent).
"""
import json, sys, pathlib
from jsonschema import Draft202012Validator as V
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SESSION = ROOT / "examples/sample-session.json"


def load_schemas():
    fs = sorted(ROOT.glob("canon/schemas/*.json")) + sorted(ROOT.glob("examples/runtime-python/*.json"))
    S = {f.name: json.loads(f.read_text(encoding="utf-8")) for f in fs}
    for n, x in S.items():
        V.check_schema(x)
        print(f"OK schema {n}")
    reg = Registry().with_resources((x["$id"], Resource.from_contents(x)) for x in S.values())
    return S, reg


def semantic(plan, session=None):
    errs, tasks = [], plan.get("tasks", [])
    ids, seen = set(), set()
    for t in tasks:
        i = t.get("task_id")
        if i in seen:
            errs.append(f"duplicate task_id '{i}'")
        seen.add(i); ids.add(i)
    titles = {r.get("title") for r in plan.get("roles", [])}
    agents = {a.get("name") for a in (session or {}).get("agents", [])}
    for t in tasks:
        tid = t.get("task_id")
        if t.get("role") not in titles:
            errs.append(f"task '{tid}': unknown role '{t.get('role')}' (known: {sorted(titles)})")
        for r in t.get("requires", []):
            if r not in ids:
                errs.append(f"task '{tid}': requires unknown task_id '{r}'")
        if session is not None and t.get("name") is not None and t["name"] not in agents:
            errs.append(f"task '{tid}': assigned agent '{t['name']}' not in Session.agents {sorted(agents)} (unknown_agent)")
    graph = {t.get("task_id"): [r for r in t.get("requires", []) if r in ids] for t in tasks}
    state, stack = {}, []

    def dfs(n):
        state[n] = 1; stack.append(n)
        for m in graph.get(n, []):
            if state.get(m) == 1:
                return stack[stack.index(m):] + [m]
            if not state.get(m):
                c = dfs(m)
                if c:
                    return c
        state[n] = 2; stack.pop()
        return None

    for n in graph:
        if not state.get(n):
            c = dfs(n)
            if c:
                errs.append("cycle in requires: " + " -> ".join(c))
                break
    return errs


def rel(p):
    p = p.resolve()
    return p.relative_to(ROOT) if ROOT in p.parents else p


def check(paths, validator, session=None, kind="plan"):
    bad = 0
    for p in paths:
        doc = json.loads(p.read_text(encoding="utf-8"))
        errs = [f"schema: {e.message}" for e in validator.iter_errors(doc)]
        if kind == "plan":
            errs += semantic(doc, session)
        elif kind == "tas":
            ids = [t.get("id") for t in doc] if isinstance(doc, list) else []
            errs += [f"duplicate TAS id '{i}'" for i in {i for i in ids if ids.count(i) > 1}]
        if errs:
            bad += 1
            print(f"FAIL {rel(p)}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS {rel(p)}")
    return bad


def main(argv):
    S, reg = load_schemas()
    plan_v = V(S["plan.schema.json"], registry=reg)
    session = None
    if argv[:1] == ["--session"]:
        sp = pathlib.Path(argv[1]); argv = argv[2:]
        session = json.loads(sp.read_text(encoding="utf-8"))
        errs = list(V(S["session.schema.json"], registry=reg).iter_errors(session))
        if errs:
            print(f"FAIL session {sp}: {errs[0].message}"); return 1
    if argv:
        return 1 if check([pathlib.Path(a) for a in argv], plan_v, session) else 0

    # default suite
    session = json.loads(DEFAULT_SESSION.read_text(encoding="utf-8"))
    sess_v = V(S["session.schema.json"], registry=reg)
    tas_v = V({"type": "array", "items": {"$ref": S["tas.schema.json"]["$id"]}}, registry=reg) if "tas.schema.json" in S else None
    print("\n# valid examples (must PASS)")
    bad_valid = check([DEFAULT_SESSION], sess_v, kind="session")
    bad_valid += check(sorted(ROOT.glob("examples/sample-plan*.json")), plan_v, session)
    if tas_v:
        bad_valid += check(sorted(ROOT.glob("examples/sample-tas*.json")), tas_v, kind="tas")
    print("\n# invalid fixtures (must FAIL)")
    inv = sorted(ROOT.glob("examples/invalid/*.json"))
    inv_tas = [p for p in inv if p.name.startswith("tas-")]
    inv_plan = [p for p in inv if p not in inv_tas]
    failed = check(inv_plan, plan_v, session) + (check(inv_tas, tas_v, kind="tas") if tas_v else 0)
    ok = bad_valid == 0 and failed == len(inv)
    print(f"\n{'OK' if ok else 'UNEXPECTED'}: valid failing={bad_valid} (expected 0); "
          f"invalid failing={failed} (expected {len(inv)})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
