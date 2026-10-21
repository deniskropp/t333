#!/usr/bin/env python3
"""Validate t333 canon schemas and plan instances. Usage: validate.py [plan.json ...]"""
import json, glob, sys, pathlib
from jsonschema import Draft202012Validator as V
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_schemas():
    fs = sorted(ROOT.glob("canon/schemas/*.json")) + sorted(ROOT.glob("examples/runtime-python/*.json"))
    S = {f.name: json.loads(f.read_text()) for f in fs}
    for n, x in S.items():
        V.check_schema(x); print(f"OK schema {n}")
    reg = Registry().with_resources((x["$id"], Resource.from_contents(x)) for x in S.values())
    return S, reg

def semantic(plan):
    errs, tasks = [], plan.get("tasks", [])
    ids, seen = set(), set()
    for t in tasks:
        i = t.get("task_id")
        if i in seen: errs.append(f"duplicate task_id '{i}'")
        seen.add(i); ids.add(i)
    titles = {r.get("title") for r in plan.get("roles", [])}
    for t in tasks:
        if t.get("role") not in titles:
            errs.append(f"task '{t.get('task_id')}': unknown role '{t.get('role')}' (known: {sorted(titles)})")
        for r in t.get("requires", []):
            if r not in ids: errs.append(f"task '{t.get('task_id')}': requires unknown task_id '{r}'")
    graph = {t.get("task_id"): [r for r in t.get("requires", []) if r in ids] for t in tasks}
    state, stack = {}, []
    def dfs(n):
        state[n] = 1; stack.append(n)
        for m in graph.get(n, []):
            if state.get(m) == 1:
                return stack[stack.index(m):] + [m]
            if not state.get(m):
                c = dfs(m)
                if c: return c
        state[n] = 2; stack.pop(); return None
    for n in graph:
        if not state.get(n):
            c = dfs(n)
            if c: errs.append("cycle in requires: " + " -> ".join(c)); break
    return errs

def main(paths):
    S, reg = load_schemas()
    v = V(S["plan.schema.json"], registry=reg)
    if not paths:
        paths = [ROOT / "examples/sample-plan.json"] + sorted(ROOT.glob("examples/invalid/*.json"))
    bad = 0
    for p in map(pathlib.Path, paths):
        plan = json.loads(p.read_text())
        errs = [f"schema: {e.message}" for e in v.iter_errors(plan)] + semantic(plan)
        rel = p.resolve().relative_to(ROOT) if ROOT in p.resolve().parents else p
        if errs:
            bad += 1; print(f"FAIL {rel}"); [print(f"  - {e}") for e in errs]
        else:
            print(f"PASS {rel}")
    return bad

if __name__ == "__main__":
    n = main(sys.argv[1:])
    expected = sum(1 for _ in ROOT.glob("examples/invalid/*.json")) if len(sys.argv) == 1 else 0
    if len(sys.argv) == 1:
        ok = n == expected
        print(f"\n{'OK' if ok else 'UNEXPECTED'}: {n} failing (expected {expected}: all of examples/invalid/)")
        sys.exit(0 if ok else 1)
    sys.exit(1 if n else 0)
