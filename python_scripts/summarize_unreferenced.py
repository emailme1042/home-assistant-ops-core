import os

# Input and output files
input_file = r"S:\unreferenced_files.txt"
output_file = r"S:\unreferenced_files_summary.txt"

# Read lines from unreferenced list
with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() and not line.startswith("###")]

# Categories
system_files = []
helpers = []
blueprints = []
archived_backups = []
potential_orphans = []

for line in lines:
    lower = line.lower()

    # System core files
    if any(core in lower for core in ["configuration.yaml", "automations.yaml", "scripts.yaml", "scenes.yaml", "ui-lovelace.yaml", "secrets.yaml"]):
        system_files.append(line)

    # Helpers
    elif "input_booleans" in lower or "input_texts" in lower or "input_numbers" in lower or "input_datetimes" in lower or "input_selects" in lower:
        helpers.append(line)

    # Blueprints
    elif "blueprints" in lower:
        blueprints.append(line)

    # Archived backups
    elif "_archived_backups" in lower or "final_auto_fixes" in lower:
        archived_backups.append(line)

    # Remaining = potential orphans
    else:
        potential_orphans.append(line)

# Write summary
with open(output_file, "w", encoding="utf-8") as f:
    f.write("### 📄 Unreferenced YAML Files Summary Report ###\n\n")

    f.write("## ✅ System Core Files (Always Used)\n")
    for item in system_files:
        f.write(item + "\n")
    f.write("\n")

    f.write("## 🟢 Helpers (Likely Used)\n")
    for item in helpers:
        f.write(item + "\n")
    f.write("\n")

    f.write("## 🔵 Blueprints (Likely Active)\n")
    for item in blueprints:
        f.write(item + "\n")
    f.write("\n")

    f.write("## ⚫ Archived Backups (Safe to Archive or Delete)\n")
    for item in archived_backups:
        f.write(item + "\n")
    f.write("\n")

    f.write("## ❓ Potential Orphans (Manual Review Suggested)\n")
    for item in potential_orphans:
        f.write(item + "\n")
    f.write("\n")

print(f"✅ Summary report generated: {output_file}")
