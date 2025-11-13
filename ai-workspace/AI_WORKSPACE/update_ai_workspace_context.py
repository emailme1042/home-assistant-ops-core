import os
import subprocess
import datetime
from pathlib import Path

# --- CONFIG ---
SESSION_ESSENTIALS = Path("S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS")
MERGE_MAP = SESSION_ESSENTIALS / "merge_map.yaml"
MERGE_MAP_EXT = SESSION_ESSENTIALS / "merge_map_extensions.yaml"
MERGE_SCRIPT = SESSION_ESSENTIALS / "merge_markdown_files_resilient.py"
VALIDATE_SCRIPT = SESSION_ESSENTIALS / "validate_merge_sources.py"
LOG_FILE = SESSION_ESSENTIALS / "copilot_session_notes_merge.md"

# --- Step 1: Detect Changes ---
def get_modified_files():
    files = [f for f in SESSION_ESSENTIALS.glob("*") if f.is_file()]
    return sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)

# --- Step 2: Auto-Merge & Tag ---
def run_merge():
    if MERGE_MAP_EXT.exists():
        subprocess.run(["python", str(MERGE_SCRIPT), str(MERGE_MAP_EXT)], check=True)
    elif MERGE_MAP.exists():
        subprocess.run(["python", str(MERGE_SCRIPT), str(MERGE_MAP)], check=True)

# --- Step 3: Validate ---
def run_validate():
    if VALIDATE_SCRIPT.exists():
        subprocess.run(["python", str(VALIDATE_SCRIPT)], check=True)

# --- Step 4: Log & Notify ---
def log_update(modified_files):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = f"\n---\n\n✅ Workspace Sync Complete — {now}\n"
    log_entry += f"{len(modified_files)} files checked\n"
    log_entry += f"copilot_session_notes_merge.md updated\n"
    log_entry += "Please notify GPT and Edge Copilot to reload context\n---\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
    print("✅ AI workspace updated. Please sync external agents.")

# --- Main Routine ---
def main():
    print("Scanning for modified files...")
    modified_files = get_modified_files()
    print(f"Found {len(modified_files)} files.")
    print("Running merge...")
    run_merge()
    print("Validating...")
    run_validate()
    print("Logging update...")
    log_update(modified_files)
    print("Done.")

if __name__ == "__main__":
    main()
