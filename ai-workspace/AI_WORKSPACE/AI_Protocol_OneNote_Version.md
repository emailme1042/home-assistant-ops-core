# 🤖 Home Assistant AI Integration Protocol (Jamie + GPT + Copilot + Microsoft Copilot)

This file governs how multiple AI agents collaborate on maintaining and improving the Home Assistant system, under the control of Jamie.

---

## 👤 Important Notes About Jamie (All AIs Must Read)

- **Memory Support Needed**: Jamie has mental health challenges and may forget context between sessions
- **Communication Style**: Jamie may type with typos or express thoughts in non-standard ways — **always ask for clarification if unclear**
- **Navigation Aid Required**: Jamie needs **dashboard-based workflows** to visually navigate back to work-in-progress
- **File Sharing Method**: Jamie drags-and-drops markdown files from `AI_WORKSPACE/SHARED_CONTEXT/` to Edge Copilot and GPT chats for context sharing

---

## 🗝️ Agent Roles & Permissions

| Symbol | Agent | Role Description | Permissions |
|--------|-------|------------------|-------------|
| 🧠 | Smart Home Ops Assistant (GPT) | Logic validation, YAML audits, HA version checks, changelog/log tracking | Can read/write `AI_WORKSPACE/`, validate config, comment `.md`. Cannot run scripts or access `secrets.yaml`. |
| ⚙️ | GitHub Copilot (VSCode) | File edits, YAML/Python scaffolding, full path access | Full folder access (excl. `secrets.yaml`), can run scripts via `python3`, scaffold logic |
| 💬 | Microsoft Copilot (Edge) | Live HA doc lookups, GitHub bug tracking, forum monitoring | No file access. Used for real-time guidance, context crawling, issue cross-reference |
| 📝 | Microsoft Copilot (M365) | Optional. Docs, release notes, Outlook/OneNote/Teams integration | Only used by Jamie. Writes docs, agendas, summaries |
| 👤 | Jamie (System Owner) | Final approver, operator, validator-in-chief | Oversees changes, runs shell commands, triggers backups, accepts or rejects AI suggestions |

---

## 🎯 Goals

- Maintain a fully working, secure, modular, and documented Home Assistant installation
- Validate against HA Core `2025.10.4`
- Log all AI-driven actions in `copilot_session_notes.md` + `ai_exec_log.md`
- Use `AI_WORKSPACE/` as canonical zone for suggestions, logs, previews
- **Help Jamie remember context** via dashboard links and markdown files

---

## 🔁 AI Workflow Cycle

### 🔧 Default Flow
1. 👤 Jamie defines a system need or bug
2. ⚙️ Copilot (VSCode) scaffolds YAML/Python changes
3. 🧠 GPT audits logic, checks HA compatibility, logs status
4. 👤 Jamie validates via `python3 validate_yaml.py`
5. 💬 Copilot (Edge) confirms external logic (bugs/docs/forum)
6. 👤 Jamie commits changes with tag: `🟦 confirmed`, `🌸 pending`, or `🟥 deprecated`

---

## 📬 Multi-AI Communication Protocol

### 📋 Standard Message Format
```
FROM: [AI Agent Name]
TO: [Target Agent/Jamie]
RE: [Brief task description]
DATE: [YYYY-MM-DD HH:MM]

## 🎯 TASK
[Clear, specific task description]

## 📊 STATUS
[Current progress/findings]

## 🔄 NEXT ACTIONS
[What needs to happen next]

## 📁 FILES INVOLVED
[Relevant file paths]

## 🤝 HANDOFF TO
[Next responsible agent]

---
FEEDBACK REQUIRED: [What Jamie needs to confirm]
EXPECTED RESPONSE: [Timeline/format]
PRIORITY: [High/Medium/Low]

Tags: #multi_ai #ai_handoff #[session_type]
```

### 🎯 Agent-Specific Templates
- **🧠 GPT (Smart Home Ops Assistant)**: System validation, YAML audits, coordination lead
- **💬 Edge Copilot**: HA documentation research, compatibility guidance  
- **⚙️ GitHub Copilot (VSCode)**: Implementation, real-time patching, log updates

---

## 🛠️ Recovery Protocol

If a dashboard or script fails:

1. 🧠 GPT logs issue in `copilot_session_notes.md` under `#recovery`
2. ⚙️ Copilot (VSCode) runs:
   ```
   python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml 2>> /config/fix_errors.log
   ```
3. 👤 Jamie reviews `fix_sheet.yaml`, applies or reverts patch
4. 💬 Copilot (Edge) checks community/forum for related bug threads
5. `SYSTEM_OVERVIEW/` is updated with fix outcome
6. ⚙️ Copilot updates `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` with resolution

---

## 🏷️ Session Tagging Guide

Use tags in logs (`copilot_session_notes.md`, `ai_exec_log.md`) for audit traceability:

- `#session_start`, `#session_end`
- `#ai_handoff` (when passing work between AIs)
- `#validation` (for system checks)
- `#multi_ai` (for collaborative work)
- `#backup`, `#automation`, `#dashboard`, `#recovery`, `#refactor`
- `#jamie_question` (when Jamie needs clarification)
- `#context_refresh` (when helping Jamie remember previous work)

---

## 🧠 Jamie Context Notes (For All AI Agents)

- Jamie may forget session context — always surface logs or notes from `AI_WORKSPACE/`
- Jamie may type with typos or nonlinear thoughts — always clarify gently before acting
- Jamie prefers dashboard-based navigation for revisiting WIP tasks
- Jamie needs drag-and-drop file flow to Edge Copilot and GPT for clarity
- AI agents should respond clearly, without overwhelming detail, unless asked

---

## 📁 Core Folders & File Expectations

| Folder / File | Purpose |
|---------------|---------|
| `AI_WORKSPACE/` | Logs, previews, outputs, shell results |
| `AI_WORKSPACE/SHARED_CONTEXT/` | **Drag-and-drop files for Edge Copilot and GPT** |
| `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` | **Active work tracker - Jamie can always open this to resume** |
| `SYSTEM_OVERVIEW/` | Markdown anchors, snapshot reference points |
| `dashboards/SYSTEM_OVERVIEW/` | Dashboard YAML files that surface AI work |
| `includes/` | Modular YAML files (sensors, automations) |
| `python_scripts/` | AI-referenced business logic scripts |
| `fix_sheet.yaml` | YAML validation results |
| `copilot_session_notes.md` | Per-session record, structured via template |
| `ai_exec_log.md` | Raw log of AI actions or shell calls |
| `docs/` | Central AI documentation hub (optional organization) |

---

## 📂 File Organization Strategy

- No agent touches `secrets.yaml` or `.storage/`
- No deletions from dashboards or `SYSTEM_OVERVIEW/` without 👤 Jamie approval
- All AI work begins with a `#session_start` and ends with `#session_end`
- Only 👤 Jamie approves commit or restart actions
- **Always update `SHARED_CONTEXT/current_session.md`** when work changes so Jamie can resume easily
- **Always ask Jamie for clarification** if communication is unclear

---

## 🤝 Question Routing Guide (Who to Ask What)

| Question Type | Ask Who | Why |
|---------------|---------|-----|
| SYSTEM_OVERVIEW tagging patterns | 🧠 GPT | Knows HA architecture and dashboard structure |
| Fallback validation workflows | 🧠 GPT + 💬 Edge Copilot | GPT for HA specifics, Edge for community solutions |
| Troubleshooting error patterns | 🧠 GPT + 💬 Edge Copilot | GPT for logic, Edge for recent bug reports |
| File/code editing, scaffolding | ⚙️ GitHub Copilot (VSCode) | Direct file system access and editing |
| Home Assistant version compatibility | 🧠 GPT + 💬 Edge Copilot | GPT for changelog, Edge for breaking changes docs |
| Python script logic | ⚙️ GitHub Copilot (VSCode) | Can read, edit, and test scripts directly |
| Dashboard design/layout | 🧠 GPT | Knows Lovelace/YAML dashboard patterns |
| Live community forum searches | 💬 Edge Copilot | Real-time web access |

---

## 🧭 Dashboard Navigation for Jamie

All AIs should help maintain these dashboard links in `dashboards/SYSTEM_OVERVIEW/ai_navigation.yaml`:

- **Current Session** → Link to `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` (rendered in dashboard)
- **Recent Changes** → Link to last 5 entries in `ai_exec_log.md`
- **Active Issues** → Link to `#recovery` tagged items in `copilot_session_notes.md`
- **Quick Actions** → Buttons to run validators, health checks

---

## 📤 File Sharing Workflow

When Jamie needs to share context with other AIs:

1. ⚙️ Copilot creates/updates markdown in `AI_WORKSPACE/SHARED_CONTEXT/`
2. 👤 Jamie drags file to Edge browser (for 💬 Edge Copilot)
3. 👤 Jamie drags file to GPT chat (for 🧠 GPT)
4. All AIs now have synchronized context

**Standard context files to maintain:**
- `current_session.md` — What we're working on right now
- `recent_changes.md` — Last 10 changes made
- `active_issues.md` — Open problems or todos
- `system_status.md` — Health check results, validator outputs

---

## 🔄 Session Start Checklist (All AIs)

When Jamie starts a new session:

1. ⚙️ Read `AI_WORKSPACE/SHARED_CONTEXT/current_session.md`
2. ⚙️ Update `copilot_session_notes.md` with `#session_start` + timestamp
3. ⚙️ Ask Jamie: "We were working on [X]. Continue, or start something new?"
4. 🧠 GPT: Read same file if shared via drag-and-drop
5. 💬 Edge Copilot: Check for HA Core updates or breaking changes since last session

---

## 📋 Template: current_session.md

```
# Current Session — [Date]

## 🎯 Goal
[What Jamie wants to accomplish]

## 📍 Current Status
[Where we are in the workflow]

## ✅ Completed Steps
1. [Step 1]
2. [Step 2]

## 🔲 Next Steps
1. [Next action]
2. [Following action]

## 🤔 Open Questions
- [Question 1]
- [Question 2]

## 📎 Related Files
- [Path to file 1]
- [Path to file 2]
```

---

## 🔁 Session Close Routine

At the end of each task or session:

- 🧠 GPT updates `copilot_session_notes.md` and `ai_exec_log.md`
- ⚙️ Copilot (VSCode) updates `SHARED_CONTEXT/current_session.md` and dashboard links if needed
- 💬 Copilot (Edge) may be used to cross-reference bugs, add notes
- 👤 Jamie validates or rejects with tags: `🟦 confirmed`, `🌸 pending`, or `🟥 deprecated`

**Template for handoff:**
```
**NEXT RESPONSIBLE AGENT**: [⚙️ Copilot / 🧠 GPT / 💬 Edge Copilot / 👤 Jamie]
**QUESTIONS FOR NEXT AGENT OR JAMIE**: 
- [Question 1]
- [Question 2]
```

---

**Last Updated**: 2025-11-01  
**Protocol Version**: 1.1  
**Maintained By**: Jamie + AI Team (⚙️🧠💬)