# Broadlink Entity Discovery Plan - November 2, 2025

## 🎯 **OBJECTIVE: Find the 3 Broadlink Entities**

**Based on Jamie's screenshot**: Broadlink integration shows "RM4 pro - Office" with **3 entities**

**CORRECTED UNDERSTANDING**:
- **Kitchen blind**: SwitchBot integration (`cover.kitchen_blinds`) ✅ 
- **Lounge blind**: RF controlled via Broadlink RM4 pro
- **Office blind**: RF controlled via Broadlink RM4 pro

## 🔍 **Discovery Strategy**

### **Step 1: Check Developer Tools → States**
Search for entities containing:
- `broadlink`
- `rm4` 
- `remote`
- `lounge` (blind control)
- `office` (blind control)

### **Step 2: Expected Entity Patterns**
**Based on RM4 pro RF control**, the 3 entities are likely:

#### **Option A: Switch Entities**

```yaml
switch.lounge_blind_up
switch.lounge_blind_down  
switch.office_blind_up
# OR combined control:
switch.rm4_pro_blind_control
```

#### **Option B: Button Entities**

```yaml
button.lounge_blind_up
button.lounge_blind_down
button.office_blind_up
# OR action-based:
button.rm4_pro_lounge_blind
button.rm4_pro_office_blind
```

#### **Option C: Remote/IR Entities**

```yaml
remote.rm4_pro_office
switch.rm4_pro_lounge_[action]
switch.rm4_pro_office_[action]
```

### **Step 3: Device ID Discovery**
**Device ID from URL**: `9b80d1f00d8671a7c68935157d5f57bd`

Search device registry for this ID to find associated entities.

## 🛠️ **Discovery Commands**

### **Template for Entity Search**
```jinja2
{# Search for all Broadlink-related entities #}
{% for state in states %}
  {% if 'broadlink' in state.entity_id.lower() 
     or 'rm4' in state.entity_id.lower()
     or 'remote' in state.entity_id.lower()
     or (state.attributes.device_id is defined and 
         '9b80d1f00d8671a7c68935157d5f57bd' in state.attributes.device_id) %}
    {{ state.entity_id }}: {{ state.state }} ({{ state.domain }})
  {% endif %}
{% endfor %}
```

### **Search by Device ID**
```jinja2
{# Find entities linked to Broadlink device #}
{% for state in states %}
  {% if state.attributes.device_id is defined %}
    {% if '9b80d1f00d8671a7c68935157d5f57bd' in state.attributes.device_id %}
      {{ state.entity_id }}: {{ state.state }}
    {% endif %}
  {% endif %}
{% endfor %}
```

### **Office-Related Entity Search**
```jinja2
{# Find office entities that might be Broadlink-controlled #}
{% for state in states %}
  {% if 'office' in state.entity_id.lower() and 
        (state.domain in ['switch', 'button', 'remote', 'cover']) %}
    {{ state.entity_id }}: {{ state.state }} (via {{ state.attributes.get('via_device', 'direct') }})
  {% endif %}
{% endfor %}
```

## 📋 **Next Actions for Jamie**

### **1. Developer Tools → Template**
Copy and paste each template above to find the actual entities.

### **2. Settings → Devices & Services → Broadlink**
- Click on "RM4 pro - Office" device
- Note down the 3 entity names shown
- Check entity domains (switch/button/remote)

### **3. Test Entity Functionality**
Once entities are found:
- Test each entity from Developer Tools → Services
- Verify IR commands are working
- Document actual entity names

## 🎯 **Expected Outcome**

**Find the 3 real entities** that replace the ghost `cover.office_blind` reference:

```yaml
# Example expected results:
switch.rm4_pro_office_blind_up: off
switch.rm4_pro_office_blind_down: off  
switch.rm4_pro_office_blind_stop: off
```

## 📊 **Documentation Update Plan**

Once real entities are discovered:

1. **Update Documentation**: Replace all `cover.office_blind` references
2. **Create Cover Template**: If needed, create a template cover using the switch entities
3. **Update Automations**: Fix any automation references to use real entities
4. **Test Integration**: Verify office blind control works properly

## 🏆 **Success Criteria**

- ✅ All 3 Broadlink entities identified by name and domain
- ✅ Entity functionality tested and working  
- ✅ Ghost `cover.office_blind` references cleaned up
- ✅ Documentation updated with correct entity names
- ✅ Office blind automation functional (if it exists)

---
**Created by**: ⚙️ GitHub Copilot (VSCode)  
**Corrected by**: 👤 Jamie's visual verification  
**Next**: Discovery execution in HA Developer Tools