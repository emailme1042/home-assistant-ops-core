import os
import json

print("DEBUG: Starting context collector...")

output_dir = "/config/ai_suggestions"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = os.path.join(output_dir, "context_snapshot.txt")

# -------- CONFIG --------
storage_dir = "/config/.storage/"
files_to_read = {
    "core.entity_registry": "Entities",
    "core.device_registry": "Devices",
    "core.area_registry": "Areas",
    "core.zone_registry": "Zones",
}
yaml_files = {
    "automations.yaml": "Automations",
    "scripts.yaml": "Scripts",
    "scenes.yaml": "Scenes",
}
# ------------------------

lines = []

# Read JSON storage files
for filename, section_name in files_to_read.items():
    path = os.path.join(storage_dir, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        lines.append(f"### {section_name}\n")
        lines.append(json.dumps(data, indent=2))
        lines.append("\n\n")
    else:
        lines.append(f"### {section_name}\nNot found.\n\n")

# Read YAML files
for filename, section_name in yaml_files.items():
    path = os.path.join("/config", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        lines.append(f"### {section_name}\n")
        lines.append(content)
        lines.append("\n\n")
    else:
        lines.append(f"### {section_name}\nNot found.\n\n")

# Write snapshot
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"DEBUG: Context snapshot written to {output_file}")
