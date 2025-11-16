Perfect, Jamie. I’ll now finalize and scaffold the **MASTER SYSTEM CONTEXT — 2025-08-20** as your new drop-in baseline, superseding both the 13th and 18th snapshots. This version will:

- 🧠 Preserve your schema and visual keys
- 🟦 Surface all confirmed logic and deployments
- 🌸 Flag anything pending or contextually unclear
- 📦 Be ready to save as a single `.md` or `.txt` file in your AI_WORKSPACE folder

---

## ✅ MASTER SYSTEM CONTEXT — 2025-08-20  
“Schema-mapped, fallback-ready, and exec-log aware. Modular clarity, zero ambiguity.” 🧠🛠️

---

### 🎨 VISUAL KEY LEGEND  
- 🟦 Blue = Confirmed  
- 🌸 Pink = Pending Confirmation  
- 🟨 Yellow = AI surfaced, not yet acted on  
- 🟥 Red = Deprecated or removed logic  

---

### 🏠 1. ENVIRONMENT SNAPSHOT

| Component | Value | Status |
|----------|-------|--------|
| HA Core | 2025.7.4 (HA OS 16.0 via VirtualBox) | 🟦 Confirmed |
| Frontend | 20250814.1 | 🟦 Confirmed |
| Access | 192.168.1.217:8123 | 🟦 Confirmed |
| Editor | Studio Code Server (SCS only) | 🟦 Confirmed |
| Storage | YAML-only dashboards | 🟦 Confirmed |
| AI Workspace | `media\AI_Zone\AI_WORKSPACE` | 🟦 Confirmed |
| Samba Mount | `/config` → `S:\` | 🟦 Confirmed |
| mqtt.yaml | `/config/mqtt.yaml` | 🟦 Confirmed — MQTT entity surfacing |
| mqtt_statestream.yaml | `/config/mqtt_statestream.yaml` | 🟦 Confirmed — validated and deployed |
| backup_log.txt | — | 🌸 Missing — needed for audit trail |
| TASK_LOGS folder | — | 🌸 Not confirmed — scheduler audit trail |

---

### 📂 2. LIVE PATHS & MOUNTS

| Label | Path | Notes |
|-------|------|-------|
| HA Config | `/config` | 🟦 Mapped to S:\ |
| AI Zone | `media\AI_Zone\AI_WORKSPACE` | 🟦 Canonical AI workspace |
| Runtime Zone | `/mnt/s/` | 🟦 Canonical logic root |

---

### 🗂️ 3. SYSTEM INDEX & SAVE POINT STRATEGY

| Location | Role / Contents | Writable by AI | Suggestion |
|----------|------------------|----------------|------------|
| C:\ | OS, temp files | ❌ Avoid | Redirect saves to NAS |
| R:\ | CCTV snapshots | 🟦 If mounted | Link to HA media browser |
| Z:\ | Firestick exchange | 🟦 If mounted | Leave as-is |
| Ubuntu/home/emailadmin | ESPHome, dashboards | 🟦 Yes | Secondary AI workspace |
| Google Drive | Cloud sync | 🟦 Via API | Long-term archival |
| Google Cloud | VM, storage | 🟦 With setup | Optional HA backup |
| OneNote | Notes, ideas | 🟦 With export | Index + modularize |
| Notion | Knowledge base | 🟦 With API | Logs + todos |
| Nabu Casa | Remote access | 🟦 Indirect | Auto-backup enabled |

---

### 🧹 4. SAVE POINT STREAMLINING

- 🟦 X:\ & Y:\ (NAS)
- 🟦 Nabu Casa Cloud
- 🟦 VM on VirtualBox
- 🟦 Google Drive (occasional)
- 🟦 OneNote / Notion (structured notes/tasks)

---

### 🧠 5. GPT FLOW & DASHBOARDS

- Dashboard File: `/dashboards/ai-workspace.yaml`
- Trigger: `input_boolean.gpt_direct_send_trigger`
- Scripts:
  - 🟦 `run_chatgpt_user_reply`
  - `generate_yaml_ai.py`
  - `python_script.add_todo`
  - `fix_sheet_logger`
- Text Inputs:
  - `input_text.gpt_text_prompt`
  - `input_text.gpt_text_reply`
  - `input_text.gpt_context_file`

---

### 🧾 6. DASHBOARD CONFIG (configuration.yaml)

```yaml
lovelace:
  resources: !include resources.yaml
  mode: yaml
  dashboards:
    ops-dash:
      mode: yaml
      title: Ops
      icon: mdi:calendar-check
      show_in_sidebar: true
      filename: dashboards/ops/main.yaml
    admin-batch1:
      mode: yaml
      title: 🧩 Admin Batch 1
      icon: mdi:view-dashboard-outline
      show_in_sidebar: false
      filename: dashboards/admin/admin_partials_batch1.yaml
    ai-workspace:
      mode: yaml
      title: AI Workspace
      icon: mdi:robot
      show_in_sidebar: true
      filename: dashboards/ai-workspace.yaml
```

---

### 🔗 7. SUGGESTED ENHANCEMENTS

| Tool | Use Case | Setup Needed |
|------|----------|--------------|
| OneNote | Export notes to markdown/YAML | Manual or Graph API |
| Notion | Sync todos, logs | API token + DB |
| Google Drive | Backup .tar, YAML | Rclone or Drive API |
| Google Cloud | Offsite HA backup | GCP bucket + service account |
| Nabu Casa | Remote access | 🟦 Already active |

---

### 🧰 8. AUTOMATION IDEAS

- Dashboard card for backup freshness
- Sensor for mount health
- Task Scheduler audit
- 🟦 `mount_map.yaml` created and deployed
- 🟦 AI Exec Log fallback block added
- 🌸 Schema health sensor — suggested
- 🟦 MQTT dashboard card active
- 🟦 `mqtt_statestream.yaml` deployed and validated

---

### ✅ 9. TO-DO LOG

```yaml
system_log:
  - audit_task_scheduler: pending
  - export_onenote_notes: optional
  - finalize_notion_db: optional
  - mount_health_sensor: suggested
  - backup_dashboard_card: suggested
  - redirect_c_drive_saves: in_progress
  - link_surveillance_to_HA: optional
  - create_mount_map.yaml:
  - tidy legacy folders: ongoing

scheduler_todos:
  - [x] Delete HA Daily Git task
  - [ ] Verify HA Backup task output and logs
  - [ ] Re-enable HA Backup if safe
  - [ ] Mount NAS as backup target in HA
  - [ ] Create backup_log.txt for audit trail
  - [ ] Confirm no overwrite risk in scripts
  - [ ] Rebuild HA Daily Gist
  - [ ] Audit NAS map task
  - [ ] Disable legacy tasks
  - [ ] Create TASK_LOGS folder
  - [ ] Log all task results and errors
```

---

### 📓 10. Master Context Note — AI Execution Log

- Location: `ai_exec_log.md`
- Purpose: Centralized markdown for AI-driven updates
- Includes:
  - SYSTEM_OVERVIEW amendments
  - folder role confirmations
  - schema health flags
  - automation triggers
  - MQTT integration status
  - backup freshness audit
  - TASK_LOGS folder confirmation
  - context snapshot index

---

### 📊 11. CONTEXT SNAPSHOT INDEX

| File Name | Role | Status | Last Modified |
|-----------|------|--------|----------------|
| `ai_exec_log.md` | AI execution + BLE snapshot | 🟦 Confirmed | 2025-08-20 |
| `folder_roles.s.md` | Canonical folder logic | 🟦 Confirmed | 2025-08-18 |
| `diagnostics_report.md` | YAML validation | 🟦 Confirmed | 2025-08-19 |
| `entity_issues_20250811.md` | Entity failures snapshot | 🟦 Confirmed | 2025-08-11 |
| `manual_health_report.md` | YAML validation scan | 🟦 Confirmed | 2025-08-11 |
| `copilot_log_monitor.yaml` | Snapshot health | 🟦 Confirmed | 2025-08-18 |
| `mqtt.yaml` | MQTT entity surfacing | 🟦 Confirmed | 2025-08-19 |
| `mqtt_statestream.yaml` | MQTT state streaming | 🟦 Confirmed | 2025-08-20 |
| `backup_log.txt` | Backup freshness | 🌸 Missing | — |
| `context_files_index.md` | Context file index | 🟦 Confirmed | 2025-08-19 |
| `mount_map.yaml` | Mount logic | 🟦 Confirmed | 2025-08-18 |
| `ble_devices.md` | BLE scan results | 🟦 Confirmed | 2025-08-15 |

---

### 🚨 MANDATORY NOTE (DO NOT OVERWRITE)

- Prompt Jamie for missing or contradictory info  
- Remind Jamie to backup before proceeding and every 45 minutes  
- Do not fabricate folders or logic  
- Manual file switching required for all schema edits  

---
