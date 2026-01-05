#!/bin/bash

INDEX_FILE="/SYSTEM_OVERVIEW/meta/system_index.yaml"
DELTA_FILE="/SYSTEM_OVERVIEW/meta/context_delta.yaml"
LOG_FILE="/SYSTEM_OVERVIEW/ai_exec_log.md"

echo "🔄 Starting AI Session..." >> "$LOG_FILE"
echo "Timestamp: $(date)" >> "$LOG_FILE"

# Extract key paths
MOUNT_MAP=$(grep 'mount_map_file:' "$INDEX_FILE" | awk '{print $2}')
CONTEXT_FILES=$(grep 'ai_context_files:' -A 10 "$INDEX_FILE" | grep '-' | awk '{print $2}')

# Check for context delta
if [ -f "$DELTA_FILE" ]; then
  echo "🧠 Context delta detected:" >> "$LOG_FILE"
  cat "$DELTA_FILE" >> "$LOG_FILE"
else
  echo "✅ No context delta found." >> "$LOG_FILE"
fi

# Confirm all context files exist
for file in $CONTEXT_FILES; do
  if [ ! -f "/SYSTEM_OVERVIEW/$file" ]; then
    echo "❌ Missing: $file" >> "$LOG_FILE"
  else
    echo "✅ Found: $file" >> "$LOG_FILE"
  fi
done

echo "🟢 AI Session Ready." >> "$LOG_FILE"
