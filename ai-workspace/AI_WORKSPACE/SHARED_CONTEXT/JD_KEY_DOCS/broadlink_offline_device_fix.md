# 🔌 Broadlink Device Offline - Quick Fix Guide

## 🎯 **ROOT CAUSE IDENTIFIED**: Device is offline

**Status**: Broadlink RM4 pro device is offline, causing `cover.office_blind` entity to show as unavailable.

---

## ✅ **Quick Recovery Steps**

### **1. Check Device Power**
- Verify Broadlink RM4 pro has power LED on
- Check power adapter connection
- Try different power outlet if needed

### **2. Check Network Connection**
- Verify device is connected to WiFi
- Check router for device presence (look for MAC: e81656a150c5)
- Try power cycling the device (unplug 10 seconds, plug back in)

### **3. WiFi Reconnection**
If device lost WiFi connection:
- Use Broadlink app on phone to re-configure WiFi
- Or use WPS button method if router supports it
- Device should show solid WiFi indicator when connected

### **4. Test in Home Assistant**
Once device is back online:
- Go to **Developer Tools → States**
- Search `cover.office_blind`
- Should change from `unavailable` to `open` or `closed`

---

## 🎯 **Expected Timeline**
- **Device online**: 2-5 minutes after fixing connection
- **HA entity recovery**: Automatic once device reconnects
- **No HA restart needed**: Entity should auto-recover

---

## ✅ **Success Indicators**
- ✅ Broadlink device shows solid network indicator
- ✅ Device appears in router's connected devices
- ✅ `cover.office_blind` shows as available in HA
- ✅ Entity state shows `open`/`closed` (not `unavailable`)

---

## 📝 **Follow-up Actions**
Once device is online:
1. Test blind control from Developer Tools → Services
2. Verify automations work properly
3. Update documentation with "check device status" protocol

**Note**: This was actually a simple offline device issue, not a missing entity or integration problem! Good reminder to check basic connectivity first.

---
**Created by**: ⚙️ GitHub Copilot (VSCode)  
**Based on**: 👤 Jamie's device status insight  
**Purpose**: Quick offline device recovery