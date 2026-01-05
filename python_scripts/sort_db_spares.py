import os
from pathlib import Path
import shutil

SPARES = Path("S:/dashboards/db_spares")
DESTS = {
    "views": Path("S:/dashboards/views"),
    "fragments": Path("S:/dashboards/fragments"),
    "users": Path("S:/dashboards/users"),
}
LOG = Path("S:/dashboards/db_spares_move_log.txt")

def classify(file):
    with open(file, encoding="utf-8") as f:
        for line in f:
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue
            if clean.startswith("views:"):
                return "views"
            if clean.startswith("mode:"):
                return "users"
            if clean.startswith("cards:") or clean.startswith("- type:"):
                return "fragments"
            break
    return "fragments"

def move_file(file):
    kind = classify(file)
    dest_dir = DESTS.get(kind)
    if not dest_dir:
        return

    new_path = dest_dir / file.name
    shutil.move(file, new_path)
    with open(LOG, "a", encoding="utf-8") as log:
        log.write(f"{file.name} ➜ {kind}\n")
    print(f"✅ Moved {file.name} to /{kind}/")

def main():
    LOG.unlink(missing_ok=True)
    print("🔍 Scanning db_spares...\n")
    for file in SPARES.glob("*.yaml"):
        move_file(file)
    print(f"\n🎯 Spares redistributed and logged in: {LOG.name}")
    input("Press Enter to close...")

if __name__ == "__main__":
    main()
