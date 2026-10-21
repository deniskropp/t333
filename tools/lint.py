#!/usr/bin/env python3
"""t333 canon lint: ⫻ notation + neutrality (name blocklist) + roles/profile consistency."""
import re, sys, pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEXT = {".md", ".kl", ".yaml", ".yml", ".json"}
SKIP = {".git", "visualizations"}

# Project / person / vendor / model names that must never appear in the normative layer.
BLOCKLIST = ["DirectFB", "DeniOliK", "Grok", "Copilot", "Gemini", "Ollama", "Olli", "Kimi",
             "HuggingFace", "OpenAI", "Google", "Move & Traffic", "MTC GmbH", "Jetson"]
NORMATIVE = ["canon"]

errors = []


def files(dirs=None):
    for p in sorted(ROOT.rglob("*")):
        r = p.relative_to(ROOT)
        if not p.is_file() or p.suffix not in TEXT or set(r.parts) & SKIP:
            continue
        if dirs and r.parts[0] not in dirs:
            continue
        yield p, r


# 1. ⫻ notation everywhere
for p, r in files():
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"⫻ [a-z][\w-]*[/:]", line):
            errors.append(f"{r}:{n}: space after ⫻ (use ⫻type/scope)")
        if re.search(r"(^|[\s`])[×⨻][a-z]", line):
            errors.append(f"{r}:{n}: legacy sigil (× or ⨻) used as section marker")
        if "\\\\u2afb" in line.lower():
            errors.append(f"{r}:{n}: escaped sigil \\\\u2afb (write ⫻)")

# 2. roles / profile consistency
roles = yaml.safe_load((ROOT / "canon/roles.yaml").read_text(encoding="utf-8"))["roles"]
ids = [x["id"] for x in roles]
for d in {i for i in ids if ids.count(i) > 1}:
    errors.append(f"canon/roles.yaml: duplicate role id '{d}'")
personas = set()
for prof in sorted((ROOT / "examples/profiles").glob("*.yaml")):
    y = yaml.safe_load(prof.read_text(encoding="utf-8"))
    exempt = set(y.get("canon_concept_names", []))
    for rid, names in y.get("bindings", {}).items():
        if rid not in ids:
            errors.append(f"{prof.relative_to(ROOT)}: binds unknown canon role '{rid}'")
        personas |= set(names) - exempt
    for rid in set(ids) - set(y.get("bindings", {})):
        print(f"note: {prof.relative_to(ROOT)} has no binding for role '{rid}'")

# 3. neutrality in canon/
names = BLOCKLIST + sorted(personas)
for p, r in files(NORMATIVE):
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        for w in names:
            if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", line):
                kind = "persona" if w in personas else "project/vendor name"
                errors.append(f"{r}:{n}: {kind} '{w}' not allowed in canon/")

for e in errors:
    print("ERROR", e)
print(f"lint: {len(errors)} error(s); checked {len(names)} names, {len(ids)} roles")
sys.exit(1 if errors else 0)
