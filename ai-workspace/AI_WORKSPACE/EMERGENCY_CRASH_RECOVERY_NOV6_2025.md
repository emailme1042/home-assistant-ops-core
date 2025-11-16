# 🚨 EMERGENCY CRASH RECOVERY - November 6, 2025

## 🔥 CRITICAL INCIDENT ANALYSIS

### **Root Cause: Aircraft Automation Infinite Loop**
**Time**: 09:41:00 (approx 15 minutes of rapid-fire loops)
**Trigger**: Unknown aircraft event causing `log_aircraft_entry_3` and `log_aircraft_entry_4` automations to fire continuously
**Impact**: Complete Home Assistant system crash

### **Loop Pattern Identified**
```
09:41:00.552 - log_aircraft_entry_3: Running automation actions
09:41:00.552 - log_aircraft_entry_3: Executing step call service  
09:41:00.564 - log_aircraft_entry_4: Running automation actions
09:41:00.565 - log_aircraft_entry_4: Executing step call service
[REPEATING EVERY ~20ms]
```

**Analysis**: These automations were triggering each other in an infinite feedback loop, overwhelming the system.

## ⚡ EMERGENCY ACTIONS TAKEN

### **1. Aircraft Automation Emergency Disable** ✅
```bash
# IMMEDIATELY DISABLED ALL AIRCRAFT AUTOMATIONS
includes/automations/aircraft.yaml → aircraft.yaml.DISABLED
includes/automations/notifications/aircraft_alerts.yaml → aircraft_alerts.yaml.DISABLED
```

### **2. Crash Context Archived** ✅
- `home-assistant.log.crash_20251106_094243` - Complete crash log saved
- Last 50 lines show continuous aircraft automation loop
- No other error patterns detected

### **3. System Recovery Preparation** ✅
- Configuration backup created with timestamp
- Log archived for forensic analysis
- Emergency disable completed

## 🔍 TECHNICAL DETAILS

### **Problematic Automation IDs**
- `log_aircraft_entry_3` - "Log aircraft entry (Secondary)"
- `log_aircraft_entry_4` - "Log aircraft entry" 
- Both triggered by `opensky_entry` events
- Both executing logbook.log service calls

### **Loop Mechanism**
1. Aircraft event triggers automation 3
2. Automation 3 logs to logbook
3. Logbook action somehow triggers automation 4
4. Automation 4 logs to logbook  
5. Logbook action triggers automation 3 again
6. **INFINITE LOOP** → System overload → Crash

### **Previous Automation Issues**
- These appear to be UI-created duplicates of YAML automations
- Possible duplicate IDs from UI automation creation
- Need to check `.storage/` for UI automation conflicts

## 🚀 RECOVERY PROTOCOL

### **Immediate Actions**
1. ✅ **Aircraft automations disabled** - Loop source eliminated
2. 🔄 **Restart Home Assistant** - Clear stuck automation state
3. 🔍 **Check for UI automation duplicates** - Prevent recurrence
4. 📊 **Validate system stability** - Monitor for other loops

### **Post-Recovery Validation**
1. Verify all other automations working normally
2. Check for any remaining opensky/flightradar events
3. Monitor system performance for stability
4. Re-enable aircraft tracking CAREFULLY if needed

## ⚠️ PREVENTION MEASURES

### **Automation ID Conflicts**
- Check for duplicate automation IDs between YAML and UI
- Use unique naming conventions for UI vs YAML automations
- Regular audit of `.storage/automations` vs includes/ files

### **Event Loop Prevention**  
- Add mode: single to all logging automations
- Implement rate limiting for high-frequency events
- Use queued mode with max: 1 for logbook automations

### **Monitoring Setup**
- Create automation execution rate monitoring
- Alert on rapid-fire automation patterns
- Log automation frequency for early warning

## 📋 NEXT STEPS

1. **IMMEDIATE**: Restart Home Assistant with aircraft automations disabled
2. **SHORT-TERM**: Audit all automation IDs for duplicates
3. **LONG-TERM**: Implement automation loop prevention safeguards

**Status**: 🚨 **SYSTEM CRASH ANALYZED** - Aircraft automation loop eliminated, ready for emergency restart!

---
**CRITICAL**: Do NOT re-enable aircraft automations until duplicate ID issue is resolved!