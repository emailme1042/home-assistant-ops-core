# Technical Guide & Integration Reference — November 13, 2025

## 🧠 VSCode + Edge Integration Guide

### **Daily Routine (Quick Start)**
☑️ Open **AI Navigation Dashboard**
☑️ Check **AI Workspace sensors** load
☑️ Validate YAML → Developer Tools → YAML → **Check Configuration**
☑️ Review **copilot_session_notes.md**
☑️ Sync **Edge + GPT context** if needed
☑️ Log `#session_start` in **current_session.md**

### **How VSCode connects to HA**
- Uses Home Assistant Config Helper for entity completion
- YAML validation via RedHat YAML extension
- Copilot for AI coding help
- PowerShell for Windows commands

### **Using Edge safely**
- Use Edge Copilot for docs, forum lookups, and cross-AI context
- Drag-and-drop markdown files for context sharing
- "Refusing to connect" errors: usually safe, just retry or use direct links

### **PowerShell commands that actually work**
```powershell
setx OPENAI_API_KEY "sk-your-api-key-here"
Invoke-RestMethod -Uri "http://192.168.1.217:8123/api/states" -Headers @{Authorization="Bearer YOUR_LONG_LIVED_TOKEN"}
```

### **Your current tools list**
| Tool                           | Purpose                          | Status       |
| ------------------------------ | -------------------------------- | ------------ |
| GitHub Copilot                 | YAML/Python scaffolding          | ✅ Active     |
| GPT (Smart Home Ops Assistant) | Validation + coordination        | ✅ Active     |
| Edge Copilot                   | Doc lookups + HA Forum cross-ref | ✅ Active     |
| REST Client                    | API testing                      | ✅ Installed  |
| Draw.io Integration            | Visual automation flow           | ✅ Installed  |

### **Fix-and-recover checklist**
- Backup path verification
- Token renewal steps
- Reset VSCode settings
- Home Assistant dashboard re-registration

### **Visual map (Draw.io link)**
📊 [Open AI Ops Flow Diagram](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/DIAGRAMS/ai_ops_flow.drawio)

🧠 GPT → Validates YAML and coordination
⚙️ Copilot → Implements and logs
💬 Edge → Research & support lookups
👤 Jamie → Approval and supervision
🏠 HAOS → Executes automations/dashboards

### **All key file shortcuts**
- [AI_README.md](vscode://file/S:/AI_WORKSPACE/AI_README.md)
- [copilot_session_notes.md](vscode://file/S:/AI_WORKSPACE/copilot_session_notes.md)
- [current_session.md](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/current_session.md)

### **REST Client Example**
Create a file named `ha_states.http` in VSCode:
```http
GET http://192.168.1.217:8123/api/states
Authorization: Bearer YOUR_LONG_LIVED_TOKEN
```

---

## 🧠 PERFORMANCE AUDIT PROTOCOL — Home Assistant Bottleneck Analysis

### **Audit Overview**
Systematic performance analysis using HA's built-in Profiler integration to identify slow components, memory leaks, and optimization opportunities.

### **Profiler Integration Setup**
1. Navigate to **Settings → Devices & Services → Add Integration**
2. Search for **"Profiler"**
3. Click **"Add Integration"**
4. Confirm setup (no additional configuration needed)

### **Performance Profiling Execution**

#### CPU Profile (60 seconds)
```yaml
service: profiler.start
data:
  seconds: 60
```

#### Memory Profile (60 seconds)
```yaml
service: profiler.memory
data:
  seconds: 60
```

### **Common Bottlenecks to Identify**

1. **Slow Integrations**: SmartThings, Synology, TuneBlade, MQTT broker
2. **Heavy Template Sensors**: Complex Jinja2 expressions, large data processing
3. **Memory Leaks**: Custom cards holding references, stale entity objects
4. **Database Performance**: Large home-assistant_v2.db, excessive retention
5. **Frontend Rendering**: Complex Lovelace configurations, heavy custom cards

### **Optimization Recommendations**

#### Immediate Actions (< 30 minutes)
```yaml
# Reduce recorder retention
recorder:
  purge_keep_days: 3  # Currently 7

# Optimize sensor polling
sensor:
  - platform: template
    scan_interval: 120  # Increase from 30-60s where possible
```

#### Medium-term Fixes (1-2 hours)
- Simplify complex template sensors
- Reduce dashboard complexity
- Optimize automation triggers
- Update custom component versions

#### Long-term Improvements (Days)
- Migrate to MariaDB
- Implement caching layers
- Redesign heavy dashboards
- Upgrade hardware if needed

### **Success Metrics**
- **CPU Usage:** < 20% average during normal operation
- **Memory Usage:** < 600MB stable (no gradual increase)
- **UI Response:** < 2 seconds for dashboard loads
- **Entity Availability:** > 95%
- **Startup Time:** < 5 minutes

---

## 📊 **Session Tagging Guide**

### **Standard Tags**
- `#session_start`, `#session_end` - Session boundaries
- `#ai_handoff` - When passing work between AIs
- `#validation` - System checks and YAML validation
- `#multi_ai` - Collaborative work across agents
- `#backup`, `#automation`, `#dashboard`, `#recovery`, `#refactor` - Task types
- `#jamie_question` - When clarification needed from Jamie
- `#context_refresh` - When helping Jamie remember previous work

### **Priority Tags**
- `#urgent` - Requires immediate attention
- `#critical` - System functionality impaired
- `#high` - Important but not blocking
- `#medium` - Nice to have
- `#low` - Future consideration

### **Status Tags**
- `#in_progress` - Currently working on
- `#completed` - Successfully finished
- `#blocked` - Waiting on dependencies
- `#cancelled` - No longer needed

---

## 📊 **Live Issue Tracking**

### **Current Critical Issues**
- **Entity Unavailability**: 1227/3533 entities unavailable (34.7%)
- **System Health**: 0.0% (expected >80%)
- **GPT Access**: Remote UI disabled
- **MQTT Status**: Broker running but entities unavailable

### **Automation Errors**
- System Health GA Notification uses an unknown action
- Debug - Office Motion Sensor Activity uses an unknown action
- ADS-B Signal Quality Monitor uses an unknown action
- GPT Access Health Monitor uses an unknown action
- Automation Bedroom Lamp Auto-Off (Zigbee Button Timer) failed to set up
- Automation Self-Healing: Notify Service Fallback failed to set up
- Automation Al Periodic Runner (Active Mode) (DISABLED - Performance) failed to set up
- Dashboard Performance Improvement uses an unknown action
- Notify if HACS integration fails uses an unknown action

### **System Metrics**
- **HA Version**: 2025.11.1
- **Supervisor**: 2025.11.2
- **Total Entities**: 3533
- **Unavailable Entities**: 1227
- **System Health**: 0.0%
- **Automations**: 0 (expected >168)
- **Scripts**: 0 (expected >119)

### **Recent Changes**
- Disabled performance-heavy template sensors
- Fixed YAML duplicate keys
- Switched to storage dashboard mode
- Created comprehensive status updates

---

## 🔧 **Quick Commands Reference**

### **YAML Validation**
```bash
python3 /config/scripts/validate_yaml.py /config
```

### **Entity Health Check**
```bash
python3 -c "import requests; r = requests.get('http://localhost:8123/api/states', headers={'Authorization': 'Bearer YOUR_LONG_LIVED_TOKEN'}); print(f'Total entities: {len(r.json())}')"
```

### **MQTT Broker Check**
```bash
python3 -c "import paho.mqtt.client as mqtt; client = mqtt.Client(); client.connect('localhost', 1883, 60); print('MQTT connected')"
```

### **Container Status Check**
```bash
docker ps | grep -E "(esphome|mqtt|mosquitto)"
```

### **System Stats**
```bash
ha core stats
```

---

## 📞 **Emergency Contacts & Resources**

### **HA Official Resources**
- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Community Forums](https://community.home-assistant.io/)
- [GitHub Issues](https://github.com/home-assistant/core/issues)

### **Multi-AI Coordination**
- **GitHub Copilot (VSCode)**: Config edits and validation
- **Smart Home Ops Assistant (GPT)**: Logic validation and HA compatibility
- **Microsoft Copilot (Edge)**: Live docs and forum monitoring

### **Quick File Access**
- [AI_README.md](vscode://file/S:/AI_WORKSPACE/AI_README.md)
- [copilot_session_notes.md](vscode://file/S:/AI_WORKSPACE/copilot_session_notes.md)
- [current_session.md](vscode://file/S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/current_session.md)

**Last Updated**: November 13, 2025</content>
<parameter name="filePath">s:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\technical_guide.md