# 🤖 Home Assistant AI Collaboration Repository

This repository contains **AI workspace collaboration files** for Jamie's Home Assistant system.

## 📁 Repository Contents

**Only includes**: `AI_WORKSPACE/SHARED_CONTEXT/` - Files designed for multi-AI collaboration

### 🎯 Purpose
- **Multi-AI Sync**: GitHub Copilot, Smart Home Ops (GPT), Edge Copilot coordination
- **Context Sharing**: Drag-and-drop files to other AI chats for synchronized context
- **Session Continuity**: Help Jamie remember and resume work across sessions
- **Version Control**: Track AI-assisted changes and system evolution

### 🗂️ Folder Structure

- **`SESSION_ESSENTIALS/`** → Always needed for AI collaboration
  - Current session status, active issues, next steps
  - Critical system status and recent changes
  - Quick start guides for each AI agent

- **`DEVELOPMENT_CONTEXT/`** → Technical reference as needed  
  - System architecture, entity catalogs, troubleshooting
  - Integration patterns, validation workflows

- **`AI_PROTOCOLS/`** → Multi-AI coordination templates
  - Session templates, logging standards
  - Agent role definitions and handoff protocols

- **`JD_KEY_DOCS/`** → Jamie's operational files
  - Fix reports, validation logs, key system docs
  - Health checks and recovery procedures

### 🔗 Integration with Home Assistant

**Live System**: `192.168.1.217:8123` (Local Access Only)
- **Hardware**: Home Assistant Green  
- **Core Version**: 2025.10.4
- **AI Workspace Path**: `/config/AI_WORKSPACE/SHARED_CONTEXT/`
- **Nabu Casa URL**: `https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa/` (Remote Access)

**Note**: GPT agents cannot directly access the live HA system, even through Nabu Casa URLs, due to authentication requirements. All AI collaboration happens through exported files and context sharing.

### 🚨 Security & Local-Only Policy

This workspace contains **NO sensitive data** and operates as a **local-only system**:

- No `secrets.yaml` or credentials included
- No device-specific information  
- No personal/location data
- Focus on AI collaboration workflows only
- **No remote sync** - all files remain local for security

### 🔧 VSCode Development Environment

This workspace is optimized for VSCode with comprehensive task automation:

**Available Tasks** (`Ctrl+Shift+P` → "Tasks: Run Task"):

- 🔄 **Restart Home Assistant Core** - Quick HA restart via CLI
- ✅ **Validate YAML Configuration** - Pre-restart validation
- 🧪 **GPT Monitoring Full Test** - Complete AI system test
- 🌐 **Browser Rendering Diagnostics** - Frontend troubleshooting
- 📊 **Complete System Health Check** - Comprehensive validation
- 🏠 **Open Home Assistant** - Launch web interface
- 📖 **Open Project README** - Quick documentation access

### 💾 Backup & Recovery Strategy

**Local Backup Approach** (no remote sync required):
1. **Weekly Config Backup**: Archive `/config` folder manually or via automation
2. **Session Documentation**: All changes logged in `AI_WORKSPACE/copilot_session_notes.md`
3. **Validation Reports**: Health checks stored in `validation_logs/`
4. **Recovery Dashboards**: Emergency access via `/fallback-minimal/fallback-minimal`

### 🤝 Multi-AI Workflow

**File-Based Collaboration** (No Direct HA Access):

1. **GitHub Copilot (VSCode)** → Creates/updates files in workspace
2. **Smart Home Ops (GPT)** → Analyzes exported files via drag-and-drop from Jamie  
3. **Edge Copilot** → Provides live documentation and troubleshooting references
4. **All agents** → Stay synchronized via shared context files and exported data

**GPT Collaboration Method**:
- Export YAML configurations, logs, or entity states from HA
- Drag files from `AI_WORKSPACE/SHARED_CONTEXT/` to GPT chat
- GPT analyzes exported data and provides recommendations
- Implement GPT suggestions via GitHub Copilot in VSCode

**Alternative: API Bridge Setup**:
If you want GPT to process live HA data, a read-only API bridge can be configured to export structured data into files that GPT can then analyze safely.

### 🚨 HA Connection Issues & Troubleshooting

**"Lost connection with Home Assistant" (VSCode notification)**:

- This is normal when HA reloads/restarts frequently
- Use **📸 Mini Snapshot** task - works without tokens even when HA is unstable
- Files created: `AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/ha_core_*.txt`

**High Unavailable Entity Count (1090+ entities)**:

- **Normal after restart**: Container sensors (Grafana, VLC, MotionEye, etc.) show unavailable until containers start
- **Common culprits**: CPU/Memory sensors from stopped add-ons or containers
- **ESP restarts**: "unknown" restart reason indicates ESP device connectivity issues
- **MQTT sensors**: May show unavailable until MQTT integration reconnects

**Token Issues** (`AI_WORKSPACE/SHARED_CONTEXT/.ha_token`):

- If HA restarts frequently, tokens may become temperamental
- Recreate token: HA → Profile → Long-Lived Access Tokens → Create new
- Save: `echo NEW_TOKEN > AI_WORKSPACE/SHARED_CONTEXT/.ha_token`
- For basic diagnostics, use token-free tasks first

**Windows PowerShell Compatibility**:

- All VSCode tasks now use PowerShell-compatible syntax
- **HA CLI (`ha`) NOT available in Windows PowerShell** - only in HA SSH add-on
- For HA CLI commands: Settings → Add-ons → SSH & Web Terminal → Open Web UI
- Windows tasks focus on file management and REST API calls
- Use `Add-Content` instead of `>>` for file appending
- Use `Out-File` with `-Encoding UTF8` for initial file creation

**Home Assistant CLI Access**:

- **From Windows**: No direct `ha` command access
- **From HA SSH Add-on**: Full `ha` CLI available
  1. Go to http://192.168.1.217:8123
  2. Settings → Add-ons → SSH & Web Terminal
  3. Install and start SSH add-on
  4. Click "Open Web UI" for terminal access
  5. Run: `ha core info`, `ha core check`, `ha core logs`, etc.

**Entity Unavailability Management**:

- **1090+ unavailable entities** are typically Docker/add-on CPU & memory sensors
- These show "unavailable" when containers are stopped or not installed
- **Quick suppression** (add to `configuration.yaml`):
  ```yaml
  homeassistant:
    customize_glob:
      "sensor.*_cpu_percent":
        hidden: true
      "sensor.*_memory_percent":
        hidden: true

  recorder:
    exclude:
      entity_globs:
        - sensor.*_cpu_percent
        - sensor.*_memory_percent

  logbook:
    exclude:
      entity_globs:
        - sensor.*_cpu_percent
        - sensor.*_memory_percent
  ```
- Then: **Developer Tools → YAML → Reload Core** (no restart needed)

**Quick Data Export for GPT Analysis**:

1. **Create token file**: Get long-lived token from HA Profile → Save to `.ha_token`
2. **Run Windows REST task**: `📥 Windows REST Snapshot (no HA CLI needed)`
3. **Drag these files to GPT chat**:
   - `entities.csv` - Complete entity list with states
   - `entity_counts_by_domain.txt` - Domain summary
   - `config.json` - HA configuration and components
   - `entity_registry.json` - Entity details (optional)

**Windows REST API Workflow**:
```powershell
# 1. Save your HA long-lived token (one-time setup)
"YOUR_TOKEN_HERE" | Out-File -Encoding ascii AI_WORKSPACE/SHARED_CONTEXT/.ha_token

# 2. Test the connection works
Test-Path AI_WORKSPACE/SHARED_CONTEXT/.ha_token

# 3. Run the REST snapshot task in VSCode
# Ctrl+Shift+P → Tasks: Run Task → "📥 Windows REST Snapshot (no HA CLI needed)"
```

---

**Last Updated**: November 3, 2025  
**Maintained By**: Jamie + AI Team (⚙️🧠💬)