# 🧠 VSCode + Edge Integration Guide

**Tag:** #vscode_edge_setup | #ai_workspace_essentials

👋 Hi Jamie — this is your one-stop file for connecting your smart-home AI workspace, VSCode, Edge, and Home Assistant.
Keep this open during sessions — it tells you exactly what to check, open, and run.

---

### ✅ **Daily Routine (Quick Start)**

☑️ Open **AI Navigation Dashboard**
☑️ Check **AI Workspace sensors** load
☑️ Validate YAML → Developer Tools → Check Config
☑️ Run **Weekly Digest (dry-run)**
☑️ Review **copilot_session_notes.md**
☑️ Sync **Edge + GPT context** if needed
☑️ Log `#session_start` in **current_session.md**

📎 Quick links:

* [Open AI Workspace Folder](vscode://file/S:/AI_WORKSPACE/)
* [Current Session Log](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/current_session.md)
* [Home Assistant Dashboard](http://192.168.1.217:8123/ai-navigation/ai-navigation)

---

### ⚙️ How VSCode connects to HA
- Uses Home Assistant Config Helper for entity completion
- YAML validation via RedHat YAML extension
- Copilot for AI coding help
- PowerShell for Windows commands

---

### 🌐 Using Edge safely
- Use Edge Copilot for docs, forum lookups, and cross-AI context
- Drag-and-drop markdown files for context sharing
- "Refusing to connect" errors: usually safe, just retry or use direct links

---

### 💻 PowerShell commands that actually work
```powershell
setx OPENAI_API_KEY "sk-your-api-key-here"
Invoke-RestMethod -Uri "http://192.168.1.217:8123/api/states" -Headers @{Authorization="Bearer YOUR_LONG_LIVED_TOKEN"}
```

---

### 🧩 Your current tools list
| Tool                           | Purpose                          | Status       |
| ------------------------------ | -------------------------------- | ------------ |
| GitHub Copilot                 | YAML/Python scaffolding          | ✅ Active     |
| GPT (Smart Home Ops Assistant) | Validation + coordination        | ✅ Active     |
| Edge Copilot                   | Doc lookups + HA Forum cross-ref | ✅ Active     |
| REST Client                    | API testing                      | ✅ Installed  |
| Draw.io Integration            | Visual automation flow           | ✅ Installed  |
| Dev Containers                 | Optional                         | ⏳ Not set up |

---

### 🔄 Fix-and-recover checklist
- Backup path verification
- Token renewal steps
- Reset VSCode settings
- Home Assistant dashboard re-registration

---

### 🧭 Visual map (Draw.io link)
📊 [Open AI Ops Flow Diagram](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/DIAGRAMS/ai_ops_flow.drawio)

🧠 GPT → Validates YAML and coordination  
⚙️ Copilot → Implements and logs  
💬 Edge → Research & support lookups  
👤 Jamie → Approval and supervision  
🏠 HAOS → Executes automations/dashboards

---

### 📁 All key file shortcuts
- [AI_README.md](vscode://file/S:/AI_WORKSPACE/AI_README.md)
- [AI_Monitoring_Report.md](vscode://file/S:/AI_WORKSPACE/AI_Monitoring_Report.md)
- [copilot_session_notes.md](vscode://file/S:/AI_WORKSPACE/copilot_session_notes.md)
- [current_session.md](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/current_session.md)

---

### 🌐 REST Client Example
Create a file named `ha_states.http` in VSCode:

```http
GET http://192.168.1.217:8123/api/states
Authorization: Bearer YOUR_LONG_LIVED_TOKEN
```

---

### 🚀 Session Quick Start Appendix
- Launch order
- Hand-off pattern between GPT ↔ Copilot ↔ Jamie
- Emergency commands reference

---

Enjoy your session! This guide is always here for you and your AIs.
