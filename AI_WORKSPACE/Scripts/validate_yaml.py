#!/usr/bin/env python3
import os
import sys
import yaml

def main(base_dir):
    error_found = False
    if not os.path.isdir(base_dir):
        print(f'BASE_DIR_NOT_FOUND: {base_dir}')
        return 2
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        yaml.safe_load(f)
                except yaml.YAMLError as e:
                    print(f'ERROR {path}: {e}')
                    error_found = True
    if not error_found:
        print('OK')
        return 0
    return 1


if __name__ == '__main__':
    # default to repository includes directory if present, otherwise fall back to /config/includes
    default = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'includes'))
    base = sys.argv[1] if len(sys.argv) > 1 else default
    sys.exit(main(base))
