#!/bin/bash
# logcopilot.sh — Modular snapshot logger with keyword trigger

SNAPSHOT_FILE="/SYSTEM_OVERVIEW/copilot_snapshot.txt"
LOGFILE="/SYSTEM_OVERVIEW/ai_exec_log.md"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M %Z")
SOURCE="http://192.168.1.217:8123/admin-dash/admin-maintenance"

# Extract snapshot after keyword
SNAPSHOT=$(awk '/#copilot_snapshot:/ {flag=1; next} flag' "$SNAPSHOT_FILE")

# Log to markdown
{
  echo "## Snapshot: Admin-Maintenance Dashboard Audit"
  echo "📅 Timestamp: $TIMESTAMP"
  echo "📍 Source: $SOURCE"
  echo ""
  echo "$SNAPSHOT"
  echo ""
} >> "$LOGFILE"
