import os
import yaml
import re

ROOT_PATH = "S:\\"  # Your mounted config root
OUTPUT_FILE = os.path.join(ROOT_PATH, "unreferenced_files.txt")

# --- Recursive include resolver ---
def extract_includes_from_file(file_path, processed_files=None):
    if processed_files is None:
        processed_files = set()
    includes = set()

    # Avoid loops
    file_path = os.path.normpath(file_path)
    if file_path in processed_files:
        return includes
    processed_files.add(file_path)

    if not os.path.exists(file_path) or not file_path.endswith((".yaml", ".yml")):
        return includes

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find !include or !include_dir_* references
    matches = re.findall(r'!include\S*\s+([^\n]+)', content)

    for match in matches:
        inc_path = match.strip().split('#')[0].strip()
        full_path = os.path.join(os.path.dirname(file_path), inc_path)
        full_path = os.path.normpath(full_path)

        if os.path.isfile(full_path):
            includes.add(full_path)
            # Recursively scan inside this file
            includes.update(extract_includes_from_file(full_path, processed_files))
        elif os.path.isdir(full_path):
            for dirpath, _, filenames in os.walk(full_path):
                for f in filenames:
                    if f.endswith((".yaml", ".yml")):
                        sub_file = os.path.normpath(os.path.join(dirpath, f))
                        includes.add(sub_file)
                        includes.update(extract_includes_from_file(sub_file, processed_files))

    return includes

# --- Collect all YAML files in the whole config tree ---
all_yaml_files = set()
for dirpath, _, filenames in os.walk(ROOT_PATH):
    for f in filenames:
        if f.endswith((".yaml", ".yml")):
            full_file = os.path.normpath(os.path.join(dirpath, f))
            all_yaml_files.add(full_file)

# --- Start recursive collection from main entry files ---
config_file = os.path.join(ROOT_PATH, "configuration.yaml")
ui_lovelace_file = os.path.join(ROOT_PATH, "ui-lovelace.yaml")

referenced_files = set()
referenced_files.update(extract_includes_from_file(config_file))
referenced_files.update(extract_includes_from_file(ui_lovelace_file))

# You can add more roots if needed, e.g.:
# automations_file = os.path.join(ROOT_PATH, "automations.yaml")
# referenced_files.update(extract_includes_from_file(automations_file))

# --- Compare ---
unused_files = all_yaml_files - referenced_files

# --- Write report ---
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("### Unreferenced YAML Files (FULL RECURSIVE SCAN) ###\n\n")
    for file in sorted(unused_files):
        f.write(file + "\n")

print(f"✅ Recursive analysis complete. Found {len(unused_files)} unreferenced YAML files.")
print(f"Report saved to: {OUTPUT_FILE}")

# This script scans the entire Home Assistant configuration directory for YAML files,
# extracts all `!include` and `!include_dir_*` references recursively, and then