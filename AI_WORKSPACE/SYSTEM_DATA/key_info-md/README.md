# 🧠 key_info-md — AI Memory & Dashboard Sync Layer

This folder contains markdowns that are:
- 📊 Surfaced live to dashboards
- 🧠 Read by Copilot, GPT, and OpenAI for memory and context
- 🔔 Monitored for freshness, errors, and missing logic
- 🔗 Linked to `AI_Zone/` and `SYSTEM_OVERVIEW/` for full system understanding

## 🔧 AI Agent Protocol
- AI must **read all files in this folder before acting**
- If any file is **missing, stale, or contradictory**, AI must **notify Jamie immediately**
- No silent edits. All changes must be surfaced in `ai_exec_log.md` and `copilot_session_notes.md`
- OpenAI agents may act freely based on task context; Copilot and GPT must prompt Jamie before any logic change

## 📂 Key Files & Roles

| File Name                          | Role / Purpose                                      | Status       |
|-----------------------------------|-----------------------------------------------------|--------------|
| `ai_exec_log.md`                  | AI actions, BLE snapshots, sync triggers            | ✅ Confirmed |
| `audit_log.s.md`                 | Canonical logic lock-in, folder role enforcement    | ✅ Confirmed |
| `BLE Devices Snapshot.md`         | BLE scan results                                    | ✅ Confirmed |
| `context_files_index.md`          | Index of all context files                          | ✅ Confirmed |
| `copilot_snapshot.md`             | Copilot session summary                             | ✅ Confirmed |
| `copilot_snapshot.template.md`    | Snapshot template for reuse                         | ✅ Confirmed |
| `dashboard-map.md`                | Dashboard layout and card logic                     | ✅ Confirmed |
| `diagnostics_report.md`          | YAML validation and dashboard error surfacing       | ✅ Confirmed |
| `entity_issues_20250811.md`       | Entity failures and unavailable states              | ✅ Confirmed |
| `error_summary.md`                | Summary of YAML and system errors                   | ✅ Confirmed |
| `fix_sheet_summary.md`            | Fixes applied and pending                           | ✅ Confirmed |
| `folder_roles.s.md`              | Canonical folder logic (symlinked)                  | ✅ Confirmed |
| `gpt_response.md`                 | GPT replies and suggestions                         | ✅ Confirmed |
| `ha_integrations.md`             | HA integrations and entity mapping                  | ✅ Confirmed |
| `ha_summary.md`                   | HA system overview                                  | ✅ Confirmed |
| `home-assistant.md`              | Full HA config and logic summary                    | ✅ Confirmed |
| `manual_health_report.md`         | Manual YAML scan and health check                   | ✅ Confirmed |
| `master_context.md`               | Session context anchor                              | ✅ Confirmed |
| `Master_System_Context_2025-08-18.md` | Full system snapshot (Aug 18)                  | ✅ Confirmed |
| `Master_System_Context_2025-08-20.md` | Full system snapshot (Aug 20)                  | ✅ Confirmed |
| `session_prompt.s.md`            | AI session prompt logic                             | ✅ Confirmed |

## 🔗 Folder References
- `AI_Zone/` — Session entry, context sync, and script staging  
- `SYSTEM_OVERVIEW/` — Finalized structure, mounts, and dashboard logic  
- `CP_GPT_Tab_Data/` — Mirrors markdowns for Edge tab surfacing

## 🧭 Usage Notes
- Place all files in Edge tabs for Copilot/GPT session grounding  
- OpenAI agents may act freely unless logic is locked  
- AI must prompt Jamie if any file is missing, stale, or unclear  
- All updates must be logged in `ai_exec_log.md`  
- Dashboard cards will surface only actionable issues from these files

## 🧠 Prompt-To Actions
- [ ] Confirm `backup_log.txt` creation for audit trail  
- [ ] Confirm `TASK_LOGS/` folder for scheduler sync  
- [ ] Scaffold `copilot_log_monitor.md` from YAML  
- [ ] Mirror `gpt_context.yaml` into `gpt_context.md`  
- [ ] Add `context_snapshot_index.md` for visual timestamp tracking  
- [ ] Slim down duplicates once dashboard surfacing is confirmed

