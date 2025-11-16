# Home Assistant AI Workspace — Copilot Instructions

**⚠️ IMPORTANT: Read [`AI_WORKSPACE/AI_README.md`](../AI_WORKSPACE/AI_README.md) for multi-AI collaboration protocol**

This is a **modular Home Assistant installation** with 3 AI agents working together:
- ⚙️ **GitHub Copilot (VSCode)** — File editing, scaffolding, validation
- 🧠 **Smart Home Ops Assistant (GPT)** — Logic validation, HA compatibility, logging  
- 💬 **Microsoft Copilot (Edge)** — Live docs, forum monitoring, issue tracking

**About Jamie**: Has memory challenges, may type with typos, needs dashboard navigation for context. Always ask for clarification if unclear.

**Context Sharing**: Maintain files in `AI_WORKSPACE/SHARED_CONTEXT/` organized in clear folders:
- **SESSION_ESSENTIALS** → Always drag to AI chats at start of session
- **DEVELOPMENT_CONTEXT** → Grab specific files when working on particular areas  
- **AI_PROTOCOLS** → Reference files for multi-AI coordination
- **JD_KEY_DOCS** → Jamie's operational files, fix reports, validation logs

---

## 🧑‍💻 JAMIE'S SESSION PROMPT (What To Do Each Session)

Please ensure the following across all files and integrations:

1. **YAML Compliance**
   - All YAML must meet current Home Assistant schema requirements
   - Entity names must match actual devices and locations (e.g., `media_player.lounge_alexa`)
   - Automations, scripts, and services must be functional and validated

2. **Performance & Optimization**
   - Suggest HACS integrations where performance or UI improvements are expected
   - Advise if anything in the current setup could be improved or deprecated
   - Flag any breaking changes or deprecated features in HA Core

3. **Multi-AI Collaboration**
   - Confirm if the current AI collaboration plan (GPT, Edge Copilot, VSCode Copilot) needs adjustment
   - Ensure all agents can parse and respond to shared context files

### 🤖 Task Routing Protocol (FROM → TO → TODO Format)

Use this standardized routing table format for assigning tasks to the most capable agent or human in the loop. Always include this table when multiple tasks need coordination across agents.

| FROM (Agent) | TO (Agent/User) | TODO (Best-Placed Action) |
|--------------|------------------|----------------------------|
| [Source Agent] | [Target Agent/User] | [Specific, actionable task description] |

**Routing Guidelines:**
- **EDGE** (Microsoft Copilot): Live docs, forum monitoring, issue tracking, external research
- **GPTs** (Smart Home Ops Assistant): Logic validation, HA compatibility, YAML audits, summarization
- **VSC** (GitHub Copilot): File editing, scaffolding, validation, code execution
- **Jamie** (System Owner): Hardware inspection, UI settings, OneNote extraction, manual confirmations

**Example Usage:**
| FROM (Agent) | TO (Agent/User) | TODO (Best-Placed Action) |
|--------------|------------------|----------------------------|
| **EDGE** (HA Notifications) | **GPTs** | Parse and summarize the 1495 unavailable entities into categories |
| **EDGE** (HA Notifications) | **Jamie** | Re-enable Remote UI: Settings → Cloud → Enable Remote Control |

### 📨 Standardized Message Format

**All multi-AI communications must follow this structured format for auditability:**

```
FROM: [Agent or Person]
TO: [Recipient Agent(s) or Person]
RE: [Brief topic / purpose]
DATE: [YYYY-MM-DD HH:MM]

## 🎯 TASK / CONTEXT
[Short, factual description of what's happening or being handled]

## 🔄 NEXT ACTIONS
[Specific actions, who does what, and expected outputs]

## 📁 FILES / COMMANDS
[List of files, paths, or terminal commands involved]

## 🤝 HANDOFF / STATUS
[Current status, who holds baton next, priority level]
```

**Example:**
```
FROM: Smart Home Ops Assistant
TO: Edge Copilot
RE: Network Bridge Diagnostics
DATE: 2025-11-15 21:25

## 🎯 TASK / CONTEXT
Supervisor and CoreDNS containers restart cleanly but DNS resolution still fails.

## 🔄 NEXT ACTIONS
1. Run `ha network info`
2. Check supervisor logs for NetworkManager errors
3. Confirm HTTPS reachability to ui.nabu.casa

## 📁 FILES / COMMANDS
N/A – terminal output only.

## 🤝 HANDOFF / STATUS
Status: 🔄 Awaiting Edge Copilot results
Priority: HIGH
```

**Implementation Notes:**
- All agents (Smart Home Ops, Edge Copilot, Cloud Copilot) must use this format
- VS Code Copilot must begin all messages with this header structure
- Timestamps should use local time for readability
- Baton passing must be explicit in HANDOFF section

4. **OpenAI Integration**
   - Confirm if OpenAI paid tier is fully integrated or needs attention
   - Validate `rest_command`, `script.query_openai`, and `intent_script` flows

## 📁 Documents to Surface for Multi-AI Sessions

Surface these files at the start of each session for context sharing from `S:\AI_WORKSPACE\SHARED_CONTEXT\`:

### 📋 SESSION_ESSENTIALS (Always needed)
| File | Purpose |
|------|---------|
| `current_session.md` | What we're working on right now |
| `active_issues.md` | Open questions and todos |
| `recent_changes.md` | Last changes made |
| `system_status.md` | Health checks and validator results |
| `NEXT_STEPS_FOR_JAMIE.md` | What Jamie should do next |
| `QUICK_START.md` | GPT-specific quick reference |

### 🔧 DEVELOPMENT_CONTEXT (As needed)
| File | Purpose |
|------|---------|
| `entity_catalog.md` | All entities, their purposes, locations |
| `device_registry.md` | All devices, integrations, capabilities |
| `hacs_components.md` | Installed HACS, their functions |
| `automation_patterns.md` | Common automation templates |
| `dashboard_structure.md` | All dashboards, their purposes |
| `validation_workflows.md` | How to run validators, fix issues |
| `integration_endpoints.md` | REST commands, Flask services, APIs |
| `troubleshooting_guide.md` | Common fixes, recovery procedures |

### 🤖 AI_PROTOCOLS (Reference)
| File | Purpose |
|------|---------|
| `AI_README.md` | Multi-agent collaboration protocol |
| `copilot_session_template.md` | Logging template |
| `openai_setup_guide.md` | OpenAI integration details |

## ⚠️ Common Issues & Fixes

**TTS Script Missing Error:**
```
Action script.tts_test_script not found.
```
Fix: Ensure `tts_test_script.yaml` is correctly loaded in scripts config:
```yaml
script:
  tts_test_script:
    alias: TTS Test Script
    sequence:
      - service: notify.alexa_media_lounge_alexa
        data:
          message: "This is a test message from Jamie's AI system."
          data:
            type: tts
```

**Broken Dashboard Links:**
- Use `file:///S:/...` links for Windows Explorer/Edge browser access (for drag-and-drop to other AIs)
- Ensure dashboards are registered in `configuration.yaml` lovelace section
- Validate markdown cards use `type: markdown` with clickable links

**Dashboard Navigation Note:**
- Sidebar "AI Navigation" → Dashboard "AI Workspace Navigation" → URL `/ai-navigation/ai-navigation`
- Sidebar "AI Workspace" → Dashboard "AI Workspace Overview" → URL `/ai-workspace/ai-overview`
- Both dashboards serve different purposes: Navigation for workflow, Workspace for quick links

**Path Convention Clarification:**
- `ai_workspace/` is the correct alias mapped in `mount_map.yaml` for the AI workspace
- Always use actual paths: `S:/AI_WORKSPACE/`, `/config/AI_WORKSPACE/`, or relative paths from workspace root
- Reference `../AI_WORKSPACE/mount_map.yaml` for current path mapping and workspace organization

---

## 🧑‍💻 GitHub Copilot Session Startup Protocol

**At the start of every new session, I will automatically:**

1. **📁 Verify SHARED_CONTEXT Structure** — Check all folders exist and are accessible
2. **🔄 Sync Key Files** — Update JD_KEY_DOCS with latest validation reports and operational files  
3. **✅ Run Health Checks** — YAML validation, service connectivity, entity status
4. **📝 Update Context** — Refresh current_session.md and system_status.md
5. **🚨 Report Issues** — Alert Jamie to any problems before proceeding
6. **🤝 Confirm Readiness** — Ensure all files ready for multi-AI collaboration

**Standard Session Opening**: "System check complete. [ISSUES/ALL_CLEAR] Ready to continue with [PREVIOUS_WORK] or start something new?"

## ✅ Quick Reference

- **Workspace type**: Home Assistant YAML config with AI staging area at `AI_WORKSPACE/`
- **Path convention**: Always use `S:/AI_WORKSPACE/`, `/config/AI_WORKSPACE/`, or relative paths from workspace root
- **Context Sharing**: Use organized `AI_WORKSPACE/SHARED_CONTEXT/` structure:
  - **SESSION_ESSENTIALS/**: Always drag to AI chats at session start
  - **DEVELOPMENT_CONTEXT/**: System knowledge for specific development work
  - **AI_PROTOCOLS/**: Multi-AI collaboration templates and guides
- **Logging**: Log every edit to `AI_WORKSPACE/ai_exec_log.md` and summarize in `AI_WORKSPACE/copilot_session_notes.md`
  - **Required fields**: timestamp, affected files, validator results, fallback logic
  - Use [`../AI_WORKSPACE/copilot_session_template.md`](../AI_WORKSPACE/copilot_session_template.md) for structure
- **Validation**: Run validators before pushing changes (see commands below)
- **Never edit**: `secrets.yaml` or `.storage/` files
- **SYSTEM_OVERVIEW surfacing**: All new automations, sensors, or dashboard blocks should be tagged and surfaced in `dashboards/SYSTEM_OVERVIEW/` for visibility — follow existing patterns in that directory

## 🏗️ Architecture & Key Patterns

**Modular YAML Structure**:
- `configuration.yaml` — Core config with `!include` directives for clean separation
- `includes/` — Organized by component type (automations/, sensors/, scripts/, etc.)
- `shell_command:` entries for validation, Flask integration, and AI workflows

**Multi-Dashboard System**:
- `dashboards/SYSTEM_OVERVIEW/` — Surface all AI work with structured markdown anchors
- `dashboards/admin/` — Admin batches (batch1-14) for organized UI management  
- Use `!include` pattern: `filename: dashboards/path/file.yaml`

**External Service Integration**:
- Flask services on `192.168.1.203:5001` and `localhost:5006` for GPT endpoints
- REST commands defined in `includes/rest_commands/rest.yaml` with explicit headers
- MQTT discovery monitoring via Python scripts in `AI_WORKSPACE/Scripts/`

**Validation Workflows**:
```yaml
# Always run before changes
shell_command.validate_yaml        # Full config validation 
shell_command.validate_automations # Automation-specific checks
shell_command.check_flask_status   # External service health
```

**High-value files**:
- [`../configuration.yaml`](../configuration.yaml) — shell_command entries (e.g. `validate_yaml`, `check_flask_status`) and modular includes
- [`../includes/rest_commands/rest.yaml`](../includes/rest_commands/rest.yaml) — REST endpoints (OpenAI, local JIT at `192.168.1.203:5001`, `127.0.0.1:5001/5005`) and example payloads
- [`../AI_WORKSPACE/README.md`](../AI_WORKSPACE/README.md), [`../AI_WORKSPACE/mount_map.yaml`](../AI_WORKSPACE/mount_map.yaml) — AI agent protocol and path mapping
- [`../AI_WORKSPACE/copilot_session_template.md`](../AI_WORKSPACE/copilot_session_template.md) — required session logging format

## Integration Patterns

- **REST**: All external calls (OpenAI, local Flask/JIT) use explicit endpoints and headers from `includes/rest_commands/rest.yaml`
- **Shell commands**: Defined in `configuration.yaml`, e.g. `run_gpt_via_flask` posts to `http://localhost:5006/run_command`
- **Dashboards**: Modular, use `!include`, surfaced in Home Assistant UI

## Developer Workflows & Commands

### Validation (run before changes)

```powershell
# Full YAML validation
python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml 2>> /config/fix_errors.log; echo "$(Get-Date) - YAML validation complete." >> /config/fix_sheet.yaml

# Fallback: validate includes only (if full validation fails)
python3 /config/scripts/validate_yaml.py /config/includes > /config/includes_fix_sheet.yaml 2>> /config/includes_fix_errors.log
```

### Health Checks

```powershell
# Check Flask health
curl -s -o $null -w "%{http_code}" http://localhost:5006/run_gpt

# Run AI preview (non-destructive)
python3 /config/python_scripts/ai_generate_suggestions.py
```

## Safe Autonomous Actions

- Run non-destructive validators: `shell_command.validate_yaml`, `shell_command.validate_includes_yaml`, `shell_command.validate_automations`
- Check service health: `shell_command.check_flask_status`
- Append logs and diagnostics under `AI_WORKSPACE/` (follow logging templates)

## Prohibited Actions (Require Approval)

- Never change `secrets.yaml` or `.storage/` files
- Do not delete files in `AI_WORKSPACE/`, `SYSTEM_OVERVIEW/`, or `dashboards/` without approval
- No one-way git syncs or production dashboard edits without Jamie's consent
- Avoid referencing `S:/`, `mnt/s`, or `/config` directly — use `AI_WORKSPACE/mount_map.yaml` mapping
- Never use `AI_Zone/` paths in YAML files — use `ai_workspace/` alias or actual paths instead

## When in Doubt

Append a short summary to [`../AI_WORKSPACE/copilot_session_notes.md`](../AI_WORKSPACE/copilot_session_notes.md) and request guidance from Jamie. If a file appears stale or contradictory, report it rather than editing.

---

## 🧠 HAOS/HACS AI Instruction Standards (2025.x)

### ✅ YAML Validation Rules
- Use dictionary format for integrations (e.g. `mqtt:` must not be a list)
- Validate all YAML with `validate_yaml.py` before restart
- Flag deprecated keys: `broker`, `discovery`, `discovery_prefix`
- Enforce 2-space indentation, no tabs

### ✅ MQTT Integration Schema
```yaml
mqtt:
  host: core-mosquitto
  port: 1883
  username: homeassistant
  password: Donkey123
```

### ✅ HACS Component Standards
- No YAML config allowed — setup must be UI-only
- Require `manifest.json` with `domain`, `name`, `version`, `codeowners`
- Optional `hacs.json` for metadata
- One integration per repo under `/custom_components/`

### ✅ Recorder/Logbook Optimization
```yaml
recorder:
  exclude:
    domains: [automation, script, mqtt]
    entities: [sensor.cpu_temp, sensor.mqtt_last_message_age_*]

logbook:
  exclude:
    domains: [automation, script, mqtt]

history:
  exclude:
    domains: [automation, script, mqtt]
```

### ✅ Restart Safety
- Run `ha core check` before restart
- Log all config errors to `active_issues.md`
