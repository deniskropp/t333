import json,glob
from jsonschema import Draft202012Validator as V
from referencing import Registry,Resource
fs=glob.glob("canon/schemas/*.json")+glob.glob("examples/runtime-python/*.json")
S={f:json.load(open(f)) for f in fs}
for f,x in S.items(): V.check_schema(x); print("OK schema",f)
reg=Registry().with_resources((x["$id"],Resource.from_contents(x)) for x in S.values())
plan=json.load(open("examples/sample-plan.json"))
v=V(S["canon/schemas/plan.schema.json"],registry=reg)
errs=list(v.iter_errors(plan)); print("sample plan errors:",errs or 0)
bad={"roles":[],"tasks":[{"task_id":"x"}]}
print("negative test errors:",len(list(v.iter_errors(bad))))
