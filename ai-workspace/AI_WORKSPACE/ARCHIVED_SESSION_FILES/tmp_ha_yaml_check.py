import sys, glob, os
try:
    import yaml
except Exception as e:
    print('MISSING_PYYAML', e)
    sys.exit(2)

root = sys.argv[1] if len(sys.argv) > 1 else '.'
root = os.path.abspath(root)
print('CHECK_ROOT:', root)
errors = []
pattern = os.path.join(root, '**', '*.yaml')
for f in glob.glob(pattern, recursive=True):
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            yaml.safe_load(fh)
    except Exception as e:
        errors.append((f, str(e)))
if errors:
    for f, msg in errors:
        print('ERROR in', f, ':', msg)
    sys.exit(1)
print('YAML_OK')
