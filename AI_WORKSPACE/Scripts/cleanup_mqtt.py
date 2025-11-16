#!/usr/bin/env python3
"""Cleanup script for MQTT monitoring artifacts.
Removes stale MQTT topic cache files older than a threshold.
"""
import os
import time
from pathlib import Path

CACHE_PATH = Path("/config/ai_workspace/mqtt_topic_cache.json")
MAX_AGE_SECONDS = 7 * 24 * 3600  # 7 days

def main():
    if not CACHE_PATH.exists():
        print(f"No cache file at {CACHE_PATH}")
        return

    mtime = CACHE_PATH.stat().st_mtime
    age = time.time() - mtime
    if age > MAX_AGE_SECONDS:
        try:
            CACHE_PATH.unlink()
            print(f"Removed stale cache file: {CACHE_PATH}")
        except Exception as e:
            print(f"Failed to remove {CACHE_PATH}: {e}")
    else:
        print(f"Cache file is recent ({int(age)}s); no action taken")

if __name__ == '__main__':
    main()
