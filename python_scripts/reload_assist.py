# reload_assist.py
storage_path = "/config/.storage/core.assist_pipeline"
import os

if os.path.exists(storage_path):
    os.rename(storage_path, storage_path + ".bak")

# HA will regenerate this on restart
