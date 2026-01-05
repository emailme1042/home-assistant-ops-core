#!/bin/bash
LOG="/www/context_snapshots/sync_log.txt"
STATUS="/www/context_snapshots/gpt_status.txt"
HEALTH="/www/context_snapshots/manual_health_report.txt"

echo "[$(date)] 🔧 Running daily permission fix..." >> "$LOG"
sudo chmod 664 /www/context_snapshots/*.{yaml,txt}
echo "[$(date)] ✅ Permission fix complete." >> "$LOG"

echo "Test log entry - $(date)" | sudo tee -a "$STATUS" > /dev/null
echo "Test sync log - $(date)" | sudo tee -a "$HEALTH" > /dev/null
