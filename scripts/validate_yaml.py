#!/usr/bin/env python3
import os
import yaml

BASE_DIR = "/config/includes"
errors = []

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                errors.append(f"❌ {file}: {str(e).splitlines()[0]}")

if errors:
    for err in errors:
        print(err)
else:
    print("✅ All YAML files are valid.")
