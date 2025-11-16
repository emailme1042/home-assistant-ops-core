#!/bin/bash

# Anchors
AI_WORKSPACE="/config/AI_WORKSPACE"
HA_ZONE="/HA_Zone"
PY_SCRIPTS="/python_scripts"
LOG_FILE="$HA_ZONE/session_logs/folder_validation.md"

# Timestamp
echo "## Folder Validation Report — $(date)" > "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Folder check function
check_folder() {
    if [ -d "$1" ]; then
        echo "- ✅ Folder exists: \`$1\`" >> "$LOG_FILE"
    else
        echo "- ❌ Missing folder: \`$1\`" >> "$LOG_FILE"
    fi
}

# File check function
check_file() {
    if [ -f "$1" ]; then
        echo "  - ✅ Found file: \`$(basename "$1")\`" >> "$LOG_FILE"
    else
        echo "  - ⚠️ Missing file: \`$(basename "$1")\`" >> "$LOG_FILE"
    fi
}

# Validate AI Zone
echo "### AI Workspace ($AI_WORKSPACE)" >> "$LOG_FILE"
for folder in meta LOGS templates test_rw python_scripts scripts; do
    check_folder "$AI_WORKSPACE/$folder"
done

# Validate HA Zone
echo "" >> "$LOG_FILE"
echo "### HA Zone ($HA_ZONE)" >> "$LOG_FILE"
for folder in session_logs dashboard_payloads sync_events yaml_validation; do
    check_folder "$HA_ZONE/$folder"
done
check_file "$HA_ZONE/yaml_validation/fix_sheet.yaml"
check_file "$HA_ZONE/yaml_validation/validation_history.md"

# Validate HA Runtime
echo "" >> "$LOG_FILE"
echo "### HA Runtime Scripts" >> "$LOG_FILE"
check_folder "$PY_SCRIPTS"
check_folder "/scripts"

# Final note
echo "" >> "$LOG_FILE"
echo "_Validation complete. Review above for missing folders or files._" >> "$LOG_FILE"
