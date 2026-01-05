# 🚨 EMERGENCY STABILITY FIX - Hard Refresh Causing HA Restart

## 🔍 ROOT CAUSE IDENTIFIED

**Hard refresh triggering HA restart indicates CRITICAL frontend resource exhaustion:**

### **Browser Console Issues (From Screenshot)**
- ❌ **CustomElementRegistry conflicts** - Multiple component registrations
- ❌ **Custom sidebar YAML errors** - Failed to read properties
- ❌ **Resource preload timeouts** - Frontend loading failures  
- ⚠️ **Material theme deprecation** - Will be removed in HA 2025

### **Backend Template Overload (From Logs)**
- ❌ **1,118 unavailable entities** overwhelming system
- ❌ **Template errors**: Unsafe dict operations in entity calculations
- ❌ **Cloud timeouts**: Nabu Casa API overwhelmed
- ❌ **MQTT/Network stress**: Multiple device connection failures

## 🚨 EMERGENCY ACTIONS REQUIRED

### **IMMEDIATE (Before Next Hard Refresh)**
1. **Disable Custom Sidebar** (causing YAML errors):
   ```yaml
   # Comment out in configuration.yaml:
   # - /local/community/custom-sidebar/custom-sidebar-yaml.js
   ```

2. **Reduce Frontend Resources** (too many components loading):
   ```yaml
   # Keep only essential cards in lovelace resources
   ```

3. **Fix Template Sensors** (causing backend overload):
   - Sensor with unsafe dict operations needs defensive coding

### **HARDWARE vs SOFTWARE**
- ❌ **NOT Hardware Issue** - HA Green can handle this load
- ✅ **Frontend Resource Exhaustion** - Too many JS components + template errors
- ✅ **Browser Memory Overload** - Hard refresh forces full reload triggering restart

## 🔧 STABILITY FIXES TO APPLY

### **1. Custom Sidebar Emergency Disable**
The browser errors show custom-sidebar-yaml.js failing to read properties. This is causing cascading frontend failures.

### **2. Template Error Fix**
Backend template trying to modify immutable dict objects - needs defensive patterns.

### **3. Resource Cleanup**
28+ custom components may be overwhelming HA Green's frontend compilation.

## 📊 RISK ASSESSMENT

**Current State**: **CRITICAL** - Hard refresh causing HA restarts
**Impact**: Frontend instability → Backend overload → System restart
**Priority**: **IMMEDIATE** - One more hard refresh could cause longer downtime

## 🎯 SUCCESS CRITERIA

After fixes:
- ✅ Hard refresh should NOT cause HA restart
- ✅ Browser console should show minimal errors
- ✅ Custom sidebar should load without failures
- ✅ Template sensors should not error

## 📋 NEXT ACTIONS

1. **Apply custom sidebar fix** (comment out problematic resource)
2. **Fix template sensor** with unsafe dict operations  
3. **Test hard refresh** (should be stable)
4. **Validate Zigbee Mesh Surgery** dashboard accessibility

**Status**: **EMERGENCY PROTOCOL INITIATED** - Stability fixes in progress!