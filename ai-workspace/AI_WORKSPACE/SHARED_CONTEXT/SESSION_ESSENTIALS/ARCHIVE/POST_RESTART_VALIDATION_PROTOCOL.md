# 🔄 POST-RESTART VALIDATION PROTOCOL
## Jamie's Entity Creation Testing - November 2, 2025

---

## 🎯 **IMMEDIATE AFTER RESTART**

### **Step 1: Entity Verification (2 minutes)**
```
1. Go to Developer Tools → States
2. Search: "ai_" → Should show 13 new AI entities
3. Search: "integration_health" → Should show 4 integration sensors
4. Search: "mqtt_broker" → Should show MQTT monitoring
```

### **Step 2: Dashboard Testing Priority (5 minutes)**
**Test in this order:**

1. **🤖 AI Navigation Dashboard**
   - Check: AI Workspace Sync Monitor section
   - Expected: Real status instead of "Entity not found"
   - Look for: sensor.ha_sync_status, sensor.workspace_sync_status

2. **🤖 AI Workspace Dashboard**  
   - Check: Validation summary section
   - Expected: input_boolean.validation_passed toggle working
   - Look for: YAML Validation status showing "Passed" or "Unknown"

3. **🤖 AI System Insight Dashboard**
   - Check: Session tracking and agent health
   - Expected: sensor.ai_agent_health showing "Excellent/Good/Fair"
   - Look for: Live session status instead of errors

4. **🔌 Integration Health Matrix Dashboard**
   - Check: Integration status indicators
   - Expected: Health sensors showing "Healthy" or "Offline"
   - Look for: Color-coded status indicators working

---

## 📊 **SUCCESS CRITERIA**

### **✅ MAJOR SUCCESS INDICATORS:**
- **No "Entity not found" in AI dashboards** (was 20+ errors)
- **Live status data showing** instead of error messages  
- **New entities visible** in Developer Tools → States
- **Template sensors calculating** proper status values

### **🔄 PARTIAL SUCCESS (Expected):**
- **Some integration sensors may show "Unknown"** (normal - they reference entities that may not exist yet)
- **Room template still has errors** (next priority fix)
- **Some MQTT/AdGuard sensors unavailable** (need integration setup)

---

## 🚨 **IF ISSUES OCCUR**

### **Entities Not Loading:**
```powershell
# Check for YAML errors
python s:\AI_WORKSPACE\pyyaml_validator.py s:\includes\input_booleans\ai_monitoring.yaml
python s:\AI_WORKSPACE\pyyaml_validator.py s:\includes\sensors\ai_monitoring.yaml
```

### **Template Sensor Errors:**
```
Check: Home Assistant → Configuration → Logs
Look for: Template sensor errors or missing dependencies
```

### **Dashboard Still Showing Errors:**
```
1. Clear browser cache (Ctrl+Shift+R)
2. Wait 30 seconds for entity registration
3. Check entity names match exactly in dashboard YAML
```

---

## 📋 **REPORT BACK FORMAT**

### **Quick Status Report:**
```
✅ Entities Loaded: X/25 new entities visible
✅ AI Dashboards: Working/Partial/Still Broken  
✅ Integration Health: Working/Partial/Still Broken
⚠️ Issues Found: [List any remaining problems]
```

### **Next Priority Based on Results:**
- **If 90%+ success**: Move to Room Template fixes
- **If 70-90% success**: Fix remaining entity references  
- **If <70% success**: Debug entity loading issues

---

## 🏆 **TARGET OUTCOME**

**Before Restart:**
- ❌ 80+ "Entity not found" warnings
- ❌ AI dashboards showing errors throughout
- ❌ No integration health monitoring

**After Restart (Expected):**
- ✅ 60-80% reduction in entity errors
- ✅ AI dashboards showing live status
- ✅ Integration health framework active
- 🔄 Ready for Phase 2 fixes (Room Template, remaining entities)

---

**✅ STATUS: RESTART READY**  
**🔄 Next: Report validation results**  
**🎯 Goal: Confirm entity infrastructure working before proceeding to enhancement phase**

---
*Generated: November 2, 2025*  
*Entities Created: 25 across 5 files*  
*Expected: Major dashboard error reduction*