# 🚀 NEXT SESSION STARTUP INSTRUCTIONS

## 📋 **Jamie's Session Startup Checklist**

### 🎯 **Immediate Priority: Post-Restart Validation**
1. **Check Home Assistant logs** for any startup errors
2. **Test dashboard loading** (all custom cards should render)
3. **Validate template sensors** (System Health Status, MQTT Watch, etc.)
4. **Test voice OpenAI automation** (dashboard button should work now)

---

## 📁 **FILES TO DRAG TO AI CHATS**

### 🔴 **ALWAYS DRAG FIRST** (SESSION_ESSENTIALS)
1. **`current_session.md`** - What we're working on right now
2. **`copilot_session_notes_merge.md`** - Complete session log with all fixes
3. **`hacs_repository_validation.md`** - HACS cards installation status
4. **`dashboard_resource_validation.md`** - Resource fix results

### 🟡 **CONTEXT FILES** (if needed)
5. **`AI_README.md`** - Multi-AI collaboration protocol
6. **`copilot_session_template.md`** - Session structure guide

---

## 🤖 **AI COORDINATION PROTOCOL**

### **For 🧠 GPT (Smart Home Ops Assistant)**
**Message**: "HA restart complete. Need post-restart validation. Dragging session files for context."

**Files to drag**:
- `current_session.md`
- `copilot_session_notes_merge.md`
- `AI_README.md`

### **For 💬 Edge Copilot**  
**Message**: "Home Assistant restarted after template/resource fixes. Need to validate dashboard performance."

**Files to drag**:
- `dashboard_resource_validation.md`
- `hacs_repository_validation.md`

### **For ⚙️ GitHub Copilot (VSCode)**
**Just say**: "HA restart complete. Check system health and template sensors."

---

## 🧾 **WHAT TO TELL AIs**

### **Summary for All AIs**:
> "Home Assistant just restarted after fixing:
> 1. Template format (system_status.yaml) 
> 2. Dashboard resources (removed 404s, added HACS cards)
> 3. Automation error (voice OpenAI test)
> 
> Need to validate everything is working properly."

---

## ✅ **SUCCESS CRITERIA**

### **Dashboard Loading**
- ✅ No 404 errors in browser DevTools
- ✅ All custom cards render properly
- ✅ AI Navigation dashboard accessible

### **Template Sensors**
- ✅ `sensor.system_health_status` shows values
- ✅ `sensor.mqtt_watch_status` shows CONNECTED/DISCONNECTED
- ✅ `sensor.network_latency` shows ping values

### **Voice Integration**
- ✅ Dashboard button "Test Voice → OpenAI" works
- ✅ No automation errors in logs
- ✅ TTS feedback plays correctly

---

## 🚨 **IF ISSUES FOUND**

### **Dashboard Problems**
- Check browser DevTools → Network tab for 404s
- Verify HACS cards installed properly
- Check configuration.yaml resource declarations

### **Template Sensor Issues**  
- Check Developer Tools → States for sensor values
- Review logs for template errors
- Validate entity references exist

### **Automation Problems**
- Check Developer Tools → Logs for automation errors
- Test individual services manually
- Verify input_boolean entities exist

---

## 📊 **FILE LOCATIONS REFERENCE**

**Fixed Files**:
- `s:\includes\templates\system_status.yaml` (modern format)
- `s:\includes\automations\voice_openai_test.yaml` (correct service)
- `s:\configuration.yaml` (clean resources)

**Session Files**:
- `s:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\`
- `s:\AI_WORKSPACE\copilot_session_notes_merge.md`

---

**🎯 GOAL**: Confirm all fixes worked and system is fully operational!