# Quick Reference: Adding Devices to Apple TV Groups

## 🔍 Finding Entity IDs

1. Open Home Assistant
2. Go to **Developer Tools** → **States**
3. Search for your device name or type (e.g., "fan", "climate", "humidifier")
4. Copy the entity ID (e.g., `fan.bedroom_fan`)

## 📝 Adding Entities to groups.yaml

### Climate/Heating Devices (Tado TRVs, Thermostats)
Add to `hacontrol_04` (Heating Zones):
```yaml
hacontrol_04:
  name: Heating Zones
  icon: mdi:radiator
  entities:
    - climate.lounge
    - climate.bedroom
    - climate.your_new_room  # Add here
```

### Fans and Ventilation
Add to `hacontrol_05` (Fans & Ventilation):
```yaml
hacontrol_05:
  name: Fans & Ventilation
  icon: mdi:fan
  entities:
    - switch.teddy_fan_2
    - fan.bedroom_fan  # Uncomment if exists
    - fan.your_new_fan  # Add here
```

### Dehumidifiers/Humidifiers
Add to `hacontrol_05` or create new group:
```yaml
hacontrol_05:
  name: Fans & Ventilation
  icon: mdi:fan
  entities:
    - switch.teddy_fan_2
    - humidifier.bedroom_dehumidifier  # Add here
```

### Govee Devices

**Current Govee devices in system:**
- Govee H5075, H5105 - Temperature/Humidity sensors
- Govee H618A - Possible light devices

**If you have Govee fans/air purifiers:**
1. Check if integrated: **Settings** → **Devices & Services** → Search "Govee"
2. If not integrated, add via:
   - HACS → Search "Govee"
   - Or Settings → Add Integration → Search "Govee"
3. Find entity IDs in Developer Tools → States
4. Add to `hacontrol_05` (Fans & Ventilation)

Example:
```yaml
hacontrol_05:
  name: Fans & Ventilation
  icon: mdi:fan
  entities:
    - switch.teddy_fan_2
    - fan.govee_h7101_fan  # Govee tower fan
    - fan.govee_h6199_purifier  # Govee air purifier
```

## 🔄 Reloading Groups After Changes

**Method 1: Via UI (No Restart Required)**
1. Edit `groups.yaml`
2. Go to **Developer Tools** → **YAML**
3. Click **Groups** → **Reload Groups**

**Method 2: Via Service**
```yaml
service: group.reload
```

**Method 3: Check First (Recommended)**
1. Go to **Developer Tools** → **YAML**
2. Click **Check Configuration**
3. If valid, click **Reload Groups**

## 🎯 Common Entity Domains

| Domain | Description | Example |
|--------|-------------|---------|
| `climate.` | Thermostats, TRVs, HVAC | `climate.lounge` |
| `fan.` | Fans (with speed control) | `fan.bedroom_fan` |
| `switch.` | On/Off devices | `switch.teddy_fan_2` |
| `humidifier.` | Humidifiers & Dehumidifiers | `humidifier.dehumidifier` |
| `light.` | Lights | `light.hallway_5` |
| `cover.` | Blinds, Curtains | `cover.kitchen_blind` |
| `media_player.` | Media devices | `media_player.lounge` |

## ⚠️ Troubleshooting

### Entity Not Showing in Apple TV Home App
- Verify entity exists in **Developer Tools** → **States**
- Check entity is supported by HomeKit/Matter integration
- Reload groups after adding
- Restart Home Assistant if necessary

### Entity ID Doesn't Exist
- Device may not be integrated yet
- Check **Settings** → **Devices & Services**
- Look for pending integrations or discovery notifications
- Some devices need HACS custom integrations

### Group Not Loading
- Check YAML syntax: `python3 scripts/validate_yaml.py groups.yaml`
- Ensure proper indentation (2 spaces)
- Entity IDs must match exactly (case-sensitive)
- No duplicate entity IDs in same group

## 📚 Supported Group Types for Apple TV

Apple TV Home app works best with:
- ✅ Lights (`light.`)
- ✅ Switches (`switch.`)
- ✅ Climate devices (`climate.`)
- ✅ Fans (`fan.`)
- ✅ Covers (`cover.`)
- ✅ Locks (`lock.`)
- ⚠️ Sensors (read-only, limited support)
- ❌ Automations (not exposed to HomeKit)
- ❌ Scripts (not exposed to HomeKit)

## 🔗 Related Files

- `groups.yaml` - Main groups configuration
- `configuration.yaml` - References groups.yaml
- `APPLE_TV_TV_SCHEDULE_SETUP.md` - Full setup guide

## ✅ Validation Command

Always validate before reloading:
```bash
python3 scripts/validate_yaml.py groups.yaml
```
