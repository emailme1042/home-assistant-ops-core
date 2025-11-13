#!/bin/bash
mkdir -p ~/AI_WORKSPACE/db
timestamp=$(date +"%Y-%m-%d %H:%M")
echo "## Mount Audit Sync — $timestamp" >> ~/AI_WORKSPACE/db/mount_audit.md
cat ~/AI_WORKSPACE/logs/latest_log.yaml >> ~/AI_WORKSPACE/db/mount_audit.md
echo -e "\n---\n" >> ~/AI_WORKSPACE/db/mount_audit.md
