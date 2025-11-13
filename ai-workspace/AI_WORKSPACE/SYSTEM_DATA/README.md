# 🧠 SYSTEM_OVERVIEW — AI-Aware Control Center

This folder anchors the finalized structure, dashboard logic, and AI context triggers for Jamie's Home Assistant system. It is the canonical source for all mounts, roles, and automation logic. AI agents must treat this folder as the **final authority** for system state, while referencing `AI_Zone/` for session context and staging.

## 🔧 Purpose
- Surface finalized structure and dashboard logic
- Provide safe access rules for AI agents
- Link all modular components (YAMLs, markdowns, OneNote, Git)
- Mirror AI session logs and context from `AI_Zone/`

## 🤖 AI Agent Protocol
- AI must **reference both `SYSTEM_OVERVIEW/` and `AI_Zone/`** before acting
- If any file is **missing, stale, or contradictory**, AI must **notify Jamie immediately**
- No silent edits or assumptions—**explicit confirmation required**
- All actions must be logged in `ai_exec_log.md` and surfaced in `copilot_session_notes.md`
- **Never reference `S:/`, `mnt/s`, or `/config`** — use mapped logic from `mount_map.yaml`

## 🔗 Linked Folder
- `AI_Zone/` — Session entry, context sync, and script staging
- Both folders support mirrored execution logic and script compatibility

## 📂 Key Files
- `structure_index.yaml` → Final layout of mounts and roles
- `gpt_context.yaml` → AI logic and safe access rules
- `todo_master.yaml` → Modular task list
- `mindmap_links.yaml` → Links OneNote pages to system components
- `changelog.md` → Tracks updates and AI actions
- `folder_roles.s.md` → Symlinked from `AI_Zone/`
- `ai_exec_log.md` → Symlinked from `AI_Zone/`

## 📋 Suggested Markdown Conversions (from YAMLs)
These YAMLs contain live logic that could benefit from `.md` mirrors for AI readability and dashboard surfacing:
- `copilot_log_monitor.yaml` → `copilot_log_monitor.md`
- `gpt_context.yaml` → `gpt_context.md` (summary + AI rules)
- `todo_master.yaml` → `todo_master.md` (task list + status)
- `structure_index.yaml` → `structure_index.md` (visual layout)
- `mindmap_links.yaml` → `mindmap_links.md` (OneNote map)

## 🧭 Usage Notes
- `SYSTEM_OVERVIEW/` is the **final source of truth** for AI and dashboard logic
- `AI_Zone/` stages context and logs, but defers to this folder for structure
- All markdowns are versioned—never deleted
- Git sync is one-way unless manually triggered

