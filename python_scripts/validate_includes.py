#!/usr/bin/env python3
import os, sys, yaml

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True, ""
    except Exception as e:
        return False, str(e)

def main():
    verbose = "--verbose" in sys.argv
    base_path = "/includes"
    print(f"🔍 Scanning includes in {base_path}...")

    for root, _, files in os.walk(base_path):
        for name in files:
            if name.endswith(".yaml") or name.endswith(".yml"):
                path = os.path.join(root, name)
                valid, error = validate_yaml(path)
                if not valid:
                    print(f"⚠️ Error in {name}: {error}")
                elif verbose:
                    print(f"✅ {name} OK")
    print("✅ Scan complete.")

if __name__ == "__main__":
    main()
