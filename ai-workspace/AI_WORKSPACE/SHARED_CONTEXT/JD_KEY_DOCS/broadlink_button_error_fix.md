# 🔧 Broadlink Button Error Fix Plan - November 2, 2025

## 🚨 **CRITICAL ERROR IDENTIFIED**

**Error**: `Failed to perform the action button/press. tuple index out of range`  
**Device**: Broadlink at IP `192.168.1.220` (reachable)  
**Root Cause**: Malformed `via_device` tuple referencing missing MAC address

---

## 🔍 **Root Cause Analysis**

### **The Problem**:
```python
via_device=('mac', 'e81656a150c5')  # ← Missing from device registry
```

When Broadlink Manager tries to register or reference a device using a `via_device` tuple pointing to a non-existent device, any button press action fails with `tuple index out of range`.

### **Evidence**:
- ✅ Device is **online** and reachable at `192.168.1.220`
- ✅ Broadlink integration is **loaded**
- ❌ Button actions **fail** with tuple error
- ❌ MAC `e81656a150c5` likely **missing** from device registry

---

## ✅ **Fix Options**

### **🔧 Option A: Remove via_device Reference (Recommended)**

#### **Step 1: Locate Broadlink Manager Code**
```bash
# Find the device manager file
find custom_components/ -name "*device*" -type f | grep broadlink
```

#### **Step 2: Edit device_manager.py**
- Open `custom_components/broadlink_manager/device_manager.py`
- Find line containing:
  ```python
  device_registry.async_get_or_create(..., via_device=('mac', 'e81656a150c5'))
  ```
- **Remove the `via_device` argument** or comment it out:
  ```python
  # via_device=('mac', 'e81656a150c5'),  # ← Commented out
  ```

#### **Step 3: Restart Home Assistant**
- Full restart required to reload custom integration
- Test button functionality after restart

---

### **🔁 Option B: Re-pair Broadlink Device**

#### **Step 1: Remove Existing Integration**
- Go to **Settings → Devices & Services → Broadlink Manager**
- Remove the current integration entry

#### **Step 2: Re-add Device**
- Put Broadlink device into pairing mode (long press until LED blinks)
- Add via **Settings → Add Integration → Broadlink Manager**
- Follow pairing prompts

#### **Step 3: Verify Registry Entry**
- Check `.storage/core.device_registry` for proper MAC registration
- Ensure `via_device` references are valid

---

### **🔍 Option C: Manual Registry Fix**

#### **Step 1: Check Current Registry**
- Open `.storage/core.device_registry`
- Search for `"e81656a150c5"`

#### **Step 2: Add Missing Entry (if needed)**
```json
{
  "area_id": null,
  "config_entries": ["broadlink_config_entry_id"],
  "connections": [],
  "disabled_by": null,
  "entry_type": null,
  "hw_version": null,
  "id": "generated_device_id",
  "identifiers": [["mac", "e81656a150c5"]],
  "manufacturer": "Broadlink",
  "model": "RM4 Pro",
  "name": "RM4 Pro - Office",
  "name_by_user": null,
  "sw_version": null,
  "via_device_id": null
}
```

---

## 🧪 **Testing Protocol**

### **Pre-Fix Testing**
```yaml
# This should fail with tuple error
service: button.press
target:
  entity_id: button.office_blind_up
```

### **Post-Fix Testing**
```yaml
# Test each button entity
service: button.press
target:
  entity_id: button.office_blind_up

service: button.press  
target:
  entity_id: button.office_blind_down

service: button.press
target:
  entity_id: button.office_blind_stop
```

### **Success Criteria**
- ✅ No `tuple index out of range` errors
- ✅ Button press actions execute successfully
- ✅ Physical blind responds to commands
- ✅ Entity shows proper state changes

---

## 📋 **Recovery Checklist**

- [ ] **Verify device registry** - Check for MAC `e81656a150c5`
- [ ] **Apply fix** - Remove via_device or re-pair device
- [ ] **Restart HA** - Full restart required
- [ ] **Test buttons** - Verify no tuple errors
- [ ] **Test physical control** - Confirm blind responds
- [ ] **Update documentation** - Log successful resolution

---

## 📝 **Recovery Log Template**

```markdown
## Broadlink Button Error — November 2, 2025
**Operator**: 👤 Jamie
**Assisted by**: ⚙️ GitHub Copilot

### Status Before Fix:
❌ Error: tuple index out of range on button.press (IP: 192.168.1.220)
❌ via_device MAC 'e81656a150c5' missing from registry
❌ Button actions fail despite device being reachable

### Fix Applied:
- [ ] Option A: Removed via_device reference from device_manager.py
- [ ] Option B: Re-paired Broadlink device via integration UI
- [ ] Option C: Manually added device registry entry

### Status After Fix:
✅ Button press actions execute without errors
✅ Physical blind responds to HA commands
✅ Device registry has proper MAC entry
✅ All button entities functional

**Result**: Broadlink button control fully operational
```

---

## 🎯 **Next Steps After Fix**

1. **Test All Functions**: UP/DOWN/STOP commands
2. **Update Automations**: Ensure any office blind automations work
3. **Clean Documentation**: Remove ghost entity references  
4. **Create Backup**: Document working configuration

---

**Created by**: ⚙️ GitHub Copilot (VSCode)  
**Based on**: 👤 Jamie's expert tuple error diagnosis  
**Purpose**: Complete button functionality restoration