# 🔧 Zigbee2MQTT Quick Fixes - Not Dual Coordinator Issue!

## ✅ **Good News: No Dual Coordinator Problem**

The gray "Coordinator" is likely just a Sonoff socket being displayed with confusing labeling in Z2M. This is a **display/routing issue**, not a hardware conflict.

## 🎯 **Real Issues to Fix**

### **1. Socket Z1 Overload** ⚠️ **MAIN ISSUE**
- Currently handling 5+ devices
- Creating bottleneck and poor performance
- Needs device redistribution

### **2. Poor Signal Quality** ⚠️ **CONNECTIVITY**
- Red/orange lines = weak connections (LQI < 100)
- Likely due to distance or interference
- Can be improved with better routing

### **3. Socket Z3 Isolation** ⚠️ **UNDERUTILIZED**
- Currently not routing any devices
- May be positioned poorly
- Could help balance network load

## 🛠️ **Easy Fixes You Can Do Now**

### **Fix 1: Force Device Re-routing** (Immediate)
In Zigbee2MQTT interface:

1. **Go to Map tab** (where you took screenshot)
2. **Click on overloaded devices** (Office Motion, Outside Temp)
3. **Look for "Force remove" or "Re-interview"** button
4. **Re-pair closer to Socket Z2 or Z3**

### **Fix 2: Improve Socket Placement** (Physical)
**Socket Z3 (isolated one):**
- Move closer to devices that need routing
- Ensure it's within range of other devices
- Avoid placing near WiFi router or PC (interference)

### **Fix 3: Z2M Settings Adjustment** (Configuration)
In Zigbee2MQTT settings:

```yaml
# Advanced settings to try:
permit_join: false  # Only open when adding devices
homeassistant: true
legacy: false
advanced:
  network_key: GENERATE  # If network is unstable
  pan_id: GENERATE       # If interference
  channel: 25           # Try different channel (11, 15, 20, 25)
```

## 🔧 **Step-by-Step Quick Fix**

### **Step 1: Re-balance Network Load**
1. **Remove Office Motion Sensor from Z1:**
   - Z2M → Devices → Office Motion → Remove
   - Physical move closer to Socket Z2
   - Re-pair by holding button

2. **Move Outside Temp Humidity:**
   - Same process, move closer to Socket Z3
   - This will activate Z3 as a router

### **Step 2: Test Signal Quality**
After re-pairing:
- Check map for green connections
- LQI should be >100 for good connections
- Red lines should disappear

### **Step 3: Optimize Channel** (If still issues)
```bash
# In Z2M, try different channels to avoid interference:
# Channel 11: Less WiFi overlap
# Channel 25: Usually clearest
# Channel 20: Good middle ground
```

## 📊 **Expected Results**

**After fixes:**
- ✅ Socket Z1: 2-3 devices (balanced)
- ✅ Socket Z2: 2-3 devices (active)
- ✅ Socket Z3: 2-3 devices (utilized)
- ✅ Green connections (LQI >100)
- ✅ Faster response times
- ✅ More stable network

## ⚡ **Quick Test Commands**

**Check current channel:**
```bash
# In Z2M logs, look for:
# "Starting zigbee-herdsman on channel X"
```

**Force network map refresh:**
- Click refresh button in Z2M map
- Wait 2-3 minutes for updated topology

## 🎯 **Priority Actions**

1. **Immediate:** Re-pair Office Motion to Socket Z2
2. **Today:** Move Outside Temp to Socket Z3  
3. **If issues persist:** Try different Z2M channel

The network should stabilize quickly once the load is balanced across all three sockets!

Want me to walk you through the device re-pairing process step by step?