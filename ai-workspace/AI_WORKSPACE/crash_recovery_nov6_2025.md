# 🚨 HA Crash Analysis & Recovery Protocol

## 📊 **Current Status After Crash**

**Date**: November 6, 2025  
**VSCode File Access**: ✅ **WORKING** - Can read/write files  
**Changes Applied**: 
- ✅ Removed vibration→lamp automation (aircraft noise detection)
- ✅ Created boiler monitoring system using vibration sensor
- ✅ Added comprehensive logging and tracking

## 🔍 **Crash Pattern Analysis**

**Recent Crash Frequency**: High - "keeps on happening for a while now"  
**Potential Causes**:
1. **Frontend Resource Loading** - Fixed HACS paths yesterday
2. **Zigbee Network Instability** - Z1 overload + new Z3 socket
3. **Custom Components** - 32+ custom integrations loading
4. **Memory/Performance** - HA Green hardware limitations

## 🛠️ **Immediate Recovery Actions**

### **1. Safe Restart Protocol**
```bash
# Via SSH Terminal:
ha core restart

# Or via HA UI:
# Settings → System → Restart
```

### **2. Zigbee Network Fix** (Priority)
**Problem**: Socket Z1 overloaded, causing network instability  
**Quick Fix**: 
- Z2M → Settings → Advanced → Change Channel to 25
- Or physically move devices closer to Socket Z2/Z3

### **3. Log Analysis Commands**
```bash
# Check recent crashes:
tail -100 /config/home-assistant.log | grep -i error

# Archive old log:
mv /config/home-assistant.log /config/home-assistant.log.crash_$(date +%Y%m%d_%H%M%S)
```

## 📋 **New Boiler Monitoring System**

**Vibration Sensor Repurposed**:
- ✅ **Was**: Aircraft noise → Orange lamp alert
- ✅ **Now**: Boiler activity → Runtime logging

**New Entities Created**:
- `input_boolean.boiler_running_status` - Current status
- `input_datetime.boiler_last_start/stop` - Timestamps  
- `counter.boiler_cycles_today` - Daily cycle count
- `sensor.boiler_current_runtime` - Live runtime display
- `sensor.boiler_status_summary` - Overview status

**Logging Features**:
- All start/stop events logged to HA Logbook
- Daily runtime tracking with history
- Automatic midnight reset of counters
- 2-minute delay to avoid false stops

## 🎯 **Next Steps After Restart**

1. **Validate new boiler monitoring** - Check sensors appear
2. **Test vibration sensor** - Should now track boiler, not lamp
3. **Fix Zigbee network** - Rebalance or change channel
4. **Monitor crash frequency** - Track if stability improves

## ⚠️ **Crash Prevention Strategy**

**Zigbee Network**: Fix overloaded Socket Z1  
**Frontend**: Monitor for resource loading errors  
**Memory**: Consider disabling unused custom components  
**Logging**: Archive large log files regularly

**Status**: All file changes complete, ready for HA restart to activate boiler monitoring!