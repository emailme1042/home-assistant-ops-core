# 🧠 Jamie's Broadlink Recovery Plan - November 2, 2025

## 🎯 **OBJECTIVE: Get cover.office_blind Entity Back Online**

**Root Cause**: Missing `via_device` MAC address in device registry causing entity unavailability

**Target Entity**: `cover.office_blind` (RF controlled via Broadlink RM4 pro)

---

## ✅ **Step-by-Step Recovery Protocol**

### **1. Check Integration Status**
- Go to **Settings → Devices & Services**
- Find **Broadlink Manager**
- Confirm:
  - ✅ Integration is loaded
  - ✅ No red error banner
  - ✅ Devices are listed (e.g. `Office Blind`, `Teddy Fan`, etc.)

**Expected Result**: Integration shows as healthy with devices visible

---

### **2. Verify Device Registry**
- Open `.storage/core.device_registry` in VSCode
- Search for:
  ```json
  "identifiers": [["mac", "e81656a150c5"]]
  ```
- **If missing**:
  - Add manually via UI or YAML
  - Or remove `via_device` reference from Broadlink Manager code (line 44 in `device_manager.py`)

**Expected Result**: MAC address `e81656a150c5` found in device registry

---

### **3. Re-Pair the Device (If Needed)**
If `cover.office_blind` is missing or unavailable:
- Go to **Settings → Devices & Services → Broadlink Manager**
- Click **Add Device**
- Put the Broadlink device into pairing mode (usually long press until LED blinks)
- Follow prompts to re-add it

**Expected Result**: Device re-appears with working entities

---

### **4. Reload the Integration**
- Go to **Developer Tools → Services**
- Call:
  ```yaml
  service: homeassistant.reload_config_entry
  data:
    entry_id: <Broadlink entry ID>
  ```
- **Alternative**: Restart Home Assistant if entry ID is unknown

**Expected Result**: Integration reloads with fresh entity registration

---

### **5. Test Entity Availability**
- Go to **Developer Tools → States**
- Search `cover.office_blind`
- Confirm:
  - ✅ `state: open` or `closed` (not `unavailable`)
  - ✅ Attributes like `friendly_name`, `supported_features` are present

**Expected Result**: Entity shows as available with proper state

---

### **6. Test Blind Control**
From **Developer Tools → Services**:

```yaml
# Test UP command
service: cover.open_cover
target:
  entity_id: cover.office_blind

# Test DOWN command  
service: cover.close_cover
target:
  entity_id: cover.office_blind

# Test STOP command
service: cover.stop_cover
target:
  entity_id: cover.office_blind
```

**Expected Result**: Blind responds to all three commands

---

## 📋 **Recovery Success Checklist**

- [ ] Broadlink Manager integration loaded and healthy
- [ ] MAC address `e81656a150c5` present in device registry
- [ ] `cover.office_blind` entity shows as available (not unavailable)
- [ ] Entity has proper state (`open`/`closed`) and attributes
- [ ] UP/DOWN/STOP commands work from Services panel
- [ ] Office blind physically responds to HA commands

---

## 🚨 **Troubleshooting Fallbacks**

### **If Entity Still Missing**:
1. **Check entity registry**: `.storage/core.entity_registry` for `cover.office_blind`
2. **Manual entity creation**: Use YAML config if UI integration fails
3. **Alternative discovery**: Look for `switch.office_blind_*` or `button.office_blind_*` entities
4. **Fresh integration setup**: Remove and re-add Broadlink Manager integration

### **If Physical Control Fails**:
1. **IR code verification**: Test from Broadlink Manager app on phone
2. **Device positioning**: Ensure RM4 pro has clear line-of-sight to blind
3. **Code re-learning**: Re-teach IR commands if they've drifted
4. **Backup entity types**: Check for switch/button equivalents

---

## 📝 **Recovery Log Template**

```markdown
## Broadlink Recovery — November 2, 2025
**Operator**: 👤 Jamie  
**Assisted by**: ⚙️ GitHub Copilot

### Status Before Recovery:
❌ cover.office_blind: unavailable
❌ Missing via_device MAC 'e81656a150c5'
❌ Integration shows device but no working entities

### Recovery Actions Taken:
- [ ] Checked Settings → Devices & Services → Broadlink Manager
- [ ] Verified .storage/core.device_registry for MAC address
- [ ] Re-paired device via integration UI
- [ ] Reloaded integration / restarted HA
- [ ] Tested entity availability in Developer Tools

### Status After Recovery:
✅ cover.office_blind: [open/closed]
✅ Device MAC registered properly
✅ UP/DOWN/STOP commands functional
✅ Physical blind responds to HA control

**Result**: Broadlink integration fully operational
```

---

## 🎯 **Next Steps After Recovery**

1. **Update Documentation**: Remove ghost references to non-existent entities
2. **Test Automations**: Verify any office blind automations work with recovered entity
3. **Dashboard Integration**: Add blind control to user dashboards
4. **Backup Configuration**: Document working setup for future reference

---

**Created by**: ⚙️ GitHub Copilot (VSCode)  
**Based on**: 👤 Jamie's expert Broadlink recovery methodology  
**Purpose**: Complete entity recovery and integration health restoration