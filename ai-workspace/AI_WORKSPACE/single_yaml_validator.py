"""Validate a single YAML file using PyYAML.
Usage: python single_yaml_validator.py <file.yaml>
"""

import sys
import yaml
import os

def validate(file_path):
    if not os.path.isfile(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(2)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✅ YAML is valid: {file_path}")
    except yaml.YAMLError as e:
        print(f"❌ YAML error in {file_path}:\n{e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error:\n{e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python single_yaml_validator.py <file.yaml>")
        sys.exit(1)
    validate(sys.argv[1])
