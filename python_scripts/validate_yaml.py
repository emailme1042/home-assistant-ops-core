#!/usr/bin/env python3
import os
import yaml

BASE_DIR = "/config/includes"
error_found = False

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            path = os.path.join(root, file)
            try:
                with open(path, "r") as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"❌ {file}: {str(e).splitlines()[0]}")
                error_found = True
                break

if not error_found:
    print("✅ OK")
