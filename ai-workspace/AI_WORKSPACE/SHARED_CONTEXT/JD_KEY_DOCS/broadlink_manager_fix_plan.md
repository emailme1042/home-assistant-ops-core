# Broadlink Manager Fix Action Plan

## 🚨 **Critical Issue**
```
Error: via_device MAC 'e81656a150c5' missing
Entity: cover.office_blind  
Integration: Broadlink Manager
Impact: Office blind automation affected
```

## 🔍 **Issue Analysis**

### **Error Context**
- **MAC Address**: `e81656a150c5` - Missing device reference
- **Entity Type**: `cover.office_blind` - Window/blind control
- **Integration**: Broadlink Manager (IR/RF device control)
- **HA Version**: 2025.12.0 compatibility concern

### **Potential Root Causes**
1. **Device Registration**: Broadlink device not properly registered in HA
2. **MAC Address Change**: Hardware replacement or network configuration change
3. **Integration Update**: Broadlink Manager integration version compatibility
4. **Device Offline**: Physical device disconnected or powered off

## 🛠️ **Diagnostic Steps**

### **Step 1: Check Device Status**
```yaml
# Check in Developer Tools → States
- Look for: device_tracker.e81656a150c5
- Look for: switch.broadlink_*
- Look for: sensor.broadlink_*
```

### **Step 2: Broadlink Manager Integration**
```yaml
# Settings → Devices & Services → Broadlink Manager
- Check integration status
- Look for red warning indicators  
- Verify device list shows office blind controller
```

### **Step 3: Network Discovery**
```yaml
# Check network devices for MAC e81656a150c5
- Router DHCP client list
- Network scanner tools
- Broadlink device LED status
```

## 🔧 **Fix Options**

### **Option A: Re-add Broadlink Device**
1. Remove existing Broadlink Manager integration
2. Power cycle Broadlink device (unplug 30 seconds)
3. Re-add via Settings → Add Integration → Broadlink Manager
4. Follow device discovery process

### **Option B: Update Device Registry**
```yaml
# If device exists but MAC changed
1. Settings → Devices & Services → Devices
2. Find old Broadlink device entry
3. Update device information or remove/re-add
```

### **Option C: Manual Entity Creation**
```yaml
# Create cover entity directly if Broadlink works
cover:
  - platform: broadlink
    host: [IP_ADDRESS]
    mac: 'e81656a150c5'
    type: rm4_mini
    switches:
      office_blind_up:
        command_on: [IR_CODE_UP]
      office_blind_down:  
        command_on: [IR_CODE_DOWN]
```

## ⚡ **Quick Test Commands**

### **Check Current Status**
```python
# In Developer Tools → Template
{{ states('cover.office_blind') }}
{{ state_attr('cover.office_blind', 'via_device') }}
```

### **Find Broadlink Devices**
```python
# Find all Broadlink-related entities
{% for state in states %}
  {% if 'broadlink' in state.entity_id.lower() %}
    {{ state.entity_id }}: {{ state.state }}
  {% endif %}
{% endfor %}
```

## 📋 **Recovery Protocol**

### **If Device Found Online**
1. ✅ Update device registry with correct MAC
2. ✅ Restart Home Assistant
3. ✅ Test office_blind entity operation

### **If Device Not Found**
1. ❌ Check physical device power/connectivity
2. ❌ Verify network settings and DHCP
3. ❌ Consider device replacement if hardware failed

### **If Integration Issues**
1. 🔄 Update Broadlink Manager via HACS
2. 🔄 Check HA 2025.12.0 compatibility notes
3. 🔄 Review integration logs for detailed errors

## 🎯 **Expected Outcome**
- ✅ `cover.office_blind` entity available and responsive
- ✅ No via_device MAC errors in logs
- ✅ Office blind automation working correctly
- ✅ Compatible with HA 2025.12.0

## 📊 **Success Validation**
```yaml
# Test these after fix
1. Developer Tools → States → cover.office_blind (should show available)
2. Try manual blind control from entity card
3. Check automation logs for office blind triggers
4. Verify no error messages in home-assistant.log
```

---
**Priority**: 🚨 **URGENT** - Affects office automation reliability  
**Next Action**: Check current Broadlink Manager integration status  
**Estimated Time**: 15-30 minutes depending on root cause