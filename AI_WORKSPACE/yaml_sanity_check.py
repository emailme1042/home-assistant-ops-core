import glob
import os
import sys

def main(root):
    print('PWD:', os.getcwd())
    print('Inspecting root:', root)
    issues = []
    for f in glob.glob(os.path.join(root, '**', '*.yaml'), recursive=True):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                for i, line in enumerate(fh, 1):
                    if '\t' in line:
                        issues.append((f, i, 'TAB_CHAR'))
        except Exception as e:
            issues.append((f, 0, f'ERROR_OPEN:{e}'))
    if issues:
        for f, ln, msg in issues:
            print('ISSUE', f, ln, msg)
        raise SystemExit(1)
    print('SANE_OK')


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(root)
