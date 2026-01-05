#!/usr/bin/env python3
import os
import sys
import yaml

# Use command line argument or default to current directory
BASE_DIR = sys.argv[1] if len(sys.argv) > 1 else "/config/includes"
error_found = False

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding='utf-8') as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"ERROR {file}: {str(e).splitlines()[0]}")
                error_found = True
                break
            except UnicodeDecodeError as e:
                print(f"ENCODING ERROR {file}: {str(e)}")
                error_found = True
                break

if not error_found:
    print("OK")
else:
    print("VALIDATION FAILED")
    sys.exit(1)
