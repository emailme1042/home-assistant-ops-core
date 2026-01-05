import os

def write_log(entries):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, 'w') as log:
        for entry in entries:
            log.write(entry + '\n')

from datetime import datetime

# Adjust these paths to match your actual folder structure
ROOTS = {
    "python_scripts": "python_scripts",
    "scripts": "scripts",
    "ascripts": "ascripts"
}
LOG_PATH = "SYSTEM_OVERVIEW/key_info-md/script_role_audit.md"

MOVE_ENABLED = False  # Set to True to auto-move flagged files to ascripts

def classify_script(name, content):
    if name.endswith(".sh"):
        return "Shell", "Move to ascripts"
    if "subprocess" in content or "os.system" in content:
        return "Python (Shell)", "Move to ascripts"
    if "hass" in content or "input_text" in content:
        return "HA Python", "Keep in python_scripts"
    return "Python (Generic)", "Review manually"

def scan_folder(folder_name, path):
    entries = []
    if not os.path.exists(path):
        return entries
    for fname in os.listdir(path):
        fpath = os.path.join(path, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            content = ""
        role, suggestion = classify_script(fname, content)
        entries.append((folder_name, fname, role, suggestion))
        if MOVE_ENABLED and suggestion == "Move to ascripts":
            try:
                os.rename(fpath, os.path.join(ROOTS["ascripts"], fname))
            except Exception as e:
                pass  # Skip move if error
    return entries

def write_log(entries):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_PATH, 'w') as log:
        log.write(f"# 🧠 Script Role Audit\n")
        log.write(f"_Generated: {timestamp}_\n\n")
        log.write("| Folder | Script | Type | Recommendation |\n")
        log.write("|--------|--------|------|----------------|\n")
        for folder, fname, role, suggestion in entries:
            log.write(f"| {folder} | {fname} | {role} | {suggestion} |\n")

def main():
    all_entries = []
    for folder, path in ROOTS.items():
        all_entries.extend(scan_folder(folder, path))
    write_log(all_entries)

if __name__ == "__main__":
    main()
