#!/usr/bin/env python3
import os
import shutil
import yaml

# Problem files
files = [
    "/dashboards/users/home.yaml",
    "/includes/input_booleans/all_input_booleans_combined.yaml",
    "/includes/templates/jit_plugin_sensor.yaml",
    "/includes/input_selects/input_select.mood.yaml"
]

backup_dir = "/HA_BACKUPS/syntax_repair_backup"
os.makedirs(backup_dir, exist_ok=True)

def backup_file(path):
    shutil.copy2(path, os.path.join(backup_dir, os.path.basename(path)))

def try_parse(yaml_text):
    try:
        yaml.safe_load(yaml_text)
        return True
    except yaml.YAMLError:
        return False

def repair_content(content):
    # Remove document start markers
    lines = [line for line in content.splitlines() if line.strip() != "---"]

    # Tabs -> spaces
    lines = [line.replace("\t", "  ") for line in lines]

    # Remove stray ?
    new_lines = []
    for line in lines:
        if line.strip() == "?":
            continue
        new_lines.append(line)
    lines = new_lines

    # Add missing colons for simple key value pairs
    fixed_lines = []
    for line in lines:
        if (
            ":" not in line
            and not line.strip().startswith("#")
            and line.strip() != ""
            and " " in line.strip()
        ):
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                line = f"{parts[0]}: {parts[1]}"
        fixed_lines.append(line)

    return "\n".join(fixed_lines) + "\n"

print(f"📦 Backing up to {backup_dir}...")

for file in files:
    if not os.path.exists(file):
        print(f"⚠️ Skipping missing file: {file}")
        continue

    backup_file(file)

    with open(file, "r", encoding="utf-8") as f:
        original = f.read()

    if try_parse(original):
        print(f"✅ Already valid: {file}")
        continue

    repaired = repair_content(original)

    if try_parse(repaired):
        with open(file, "w", encoding="utf-8") as f:
            f.write(repaired)
        print(f"🔹 Fixed: {file}")
    else:
        print(f"❌ Could not auto-fix: {file} — manual review needed")

print("✅ Syntax repair attempt complete.")
