"""Parse every YAML file under a root directory using PyYAML and report exact errors.
Usage: python pyyaml_validator.py [root]
"""

import sys
import glob
import os

try:
    import yaml
except Exception as e:
    print('❌ MISSING_PYYAML:', e)
    sys.exit(2)


def validate(root):
    errors = []
    scanned = 0
    for f in glob.glob(os.path.join(root, '**', '*.yaml'), recursive=True):
        scanned += 1
        print(f"Validating: {f}")
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                yaml.safe_load(fh)
        except yaml.YAMLError as e:
            print(f"❌ YAML ERROR in {f}: {e}")
            errors.append((f, str(e)))
        except Exception as e:
            print(f"❌ ERROR_OPEN in {f}: {e}")
            errors.append((f, f'ERROR_OPEN: {e}'))
    return errors, scanned


def main():
    root = '.'
    if len(sys.argv) > 1:
        root = sys.argv[1]
    root = os.path.abspath(root)
    print(f"\nVALIDATOR ROOT: {root}")
    if not os.path.isdir(root):
        print(f"❌ ROOT NOT FOUND: {root}")
        sys.exit(3)

    errors, scanned = validate(root)
    print(f"\nScanned {scanned} YAML files.")

    if errors:
        print(f"\n{len(errors)} file(s) failed validation:\n")
        for f, msg in errors:
            print(f"FILE: {f}\n   ERROR: {msg}\n")
        sys.exit(1)
    else:
        print("All YAML files validated successfully.\n")


if __name__ == '__main__':
    main()
