## 🔒 Canonical Logic Model: `s:` as Config Root Across All Zones

**Status:** Locked  
**Last Confirmed:** 2025-08-18  
**Author:** Jamie + AI

---

### 🔑 Core Principle

- `s:` is the **canonical config root** across all zones.
- It is mounted as `` and treated as the source of truth.
- No script, folder, or runtime may reference `s:` or `config` directly.
- Only markdowns and AI agents (Copilot, GPT, etc.) may interpret and surface this mapping.

## 🔒 Folder Access Logic — Finalized 2025-08-20

- HAOS: Accesses `key_info-md/` directly. Never prefix with `/config/`
- WSL/VSC: Accesses via `/mnt/s/SYSTEM_OVERVIEW/key_info-md/`, but logic must drop `/mnt/s/` and `SYSTEM_OVERVIEW`
- AI: Reads markdowns directly. No mount logic injected.
  ✅ All scripts, sensors, and dashboards now reference `key_info-md/` only

### 🧭 Execution vs Mount Zones

| Folder Path            | Role                | Writable | Notes                                                       |
| ---------------------- | ------------------- | -------- | ----------------------------------------------------------- |
| `/config/ai_workspace` | AI Execution Zone   | ✅ Yes   | Used for scripts, shell commands, GPT workflows, audit logs |
| `/media/AI_Zone`       | External Mount Zone | ⚠️ Maybe | Used for backups, dashboards, and manual inspection only    |

### 📁 Log Folder Roles

| Folder Path                       | Role                | Notes                                          |
| --------------------------------- | ------------------- | ---------------------------------------------- |
| `/config/ai_workspace/logs/`      | Modular log storage | Split by function; surfaced only if actionable |
| `/config/ai_workspace/changelog/` | Audit changelogs    | Human-readable, AI-attributed                  |

---

### 🧭 Zone Behavior Summary

| Zone                                 | Access to `s:`                 | Role              | Notes                                    |
| ------------------------------------ | ------------------------------ | ----------------- | ---------------------------------------- |
| **HAOS (via Studio Code Server)**    | ✅ Mounted as `/config`        | 🔒 Core Principle | Full access to config root               |
| **Studio Code Server (inside HAOS)** | ✅ Mounted as `/config`        | 🔒 Real HAOS      | Must treat as config only                |
| **WSL (on PC)**                      | ✅ Mounted as ``               | AI Runtime Zone   | Safe for Git, logging, and modular ops   |
| **Visual Studio Code (on PC)**       | ✅ Mounted as ``               | Mirrors WSL logic | Full access                              |
| **AI Agents (Copilot, GPT, etc.)**   | ✅ Interpret `s:` via markdown | Knowledge layer   | May access any folders if asked by Jamie |
| **OpenAI (via Alexa + Nabu Casa)**   | ✅ Included                    | Persistent access | Paid subscriber integration              |

---

### 🚫 Path Discipline

- No operational logic may reference `s:` or `config` directly.
- All scripts, folders, and runtime logic must operate without hardcoded paths.
- Only markdowns and AI agents may surface `s:` for clarity, audit, and knowledge.

---

### 🧠 Mental Anchor

- `s:` is not a real folder — it is a **mapped config root**.
- Folder roles are physical — surfaced in markdowns and AI sessions Only.

---

**Reminder:**  
This logic model is non-negotiable.  
Any breach risks irreversible data loss or cognitive drift.  
AI agents must respect this model in all sessions with Jamie.
