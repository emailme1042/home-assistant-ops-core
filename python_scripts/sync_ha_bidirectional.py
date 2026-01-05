#!/usr/bin/env python3

import os
import shutil
from pathlib import Path
from datetime import datetime

# CONFIGURATION
HA_PATH = Path.home() / "ha_config"
LIVE_PATH = Path.home() / "home-assistant-dashboards" / "HA_LIVE"
SYNC_DIRS = ["dashboards", "includes", "www", "python_scripts"]

# HELPERS
def sync_folder(src: Path, dst: Path, direction: str):
    log = []
    for root, dirs, files in os.walk(src):
        rel_root = Path(root).relative_to(src)
        dst_root = dst / rel_root

        for file in files:
            src_file = Path(root) / file
            dst_file = dst_root / file
            try:
                if not dst_file.exists() or os.path.getmtime(src_file) > os.path.getmtime(dst_file):
                    dst_root.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    log.append(f"Copied {direction}: {src_file} -> {dst_file}")
            except Exception as e:
                log.append(f"Error copying {src_file}: {e}")
    return log

# MAIN
if __name__ == "__main__":
    log_file = Path.cwd() / f"sync_ha_to_live_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    all_logs = []

    for subdir in SYNC_DIRS:
        src_path = HA_PATH / subdir
        dst_path = LIVE_PATH / subdir
        logs = sync_folder(src_path, dst_path, "HA→LIVE")
        all_logs.extend(logs)

    log_file.write_text("\n".join(all_logs))
    print(f"✅ HA→LIVE sync complete. {len(all_logs)} actions logged to {log_file}")
