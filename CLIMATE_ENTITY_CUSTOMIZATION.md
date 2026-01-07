# Climate Device Entity Customization Guide

This guide helps you update entity IDs in the configuration files to match your actual device entities.

## 🔍 Finding Your Entity IDs

### Method 1: Developer Tools (Recommended)
1. Go to **Developer Tools** → **States**
2. Search for your device name (e.g., "tado", "govee", "meaco")
3. Note the exact entity IDs shown (e.g., `climate.hallway`, `fan.govee_h7106_bbbc`)

### Method 2: Settings → Integrations
1. Go to **Settings** → **Devices & Services**
2. Click on the integration (e.g., Tado, BLE Monitor)
3. Click on the device
4. View all entities for that device

## 📝 Entity ID Patterns

### Tado Devices
Default patterns used in configurations:
```yaml
climate.tado_hallway         # Hallway heating zone (Floor 1)
climate.tado_bedroom         # Bedroom heating zone (Floor 2)
climate.tado_hallway_trv_1   # First TRV in hallway
climate.tado_hallway_trv_2   # Second TRV in hallway
climate.tado_bedroom_trv_1   # First TRV in bedroom
climate.tado_bedroom_trv_2   # Second TRV in bedroom
```

**Your actual entities might be:**
```yaml
climate.hallway              # If zone names are simpler
climate.bedroom
climate.living_room          # If different zone names
sensor.hallway_temperature   # Temperature sensor
sensor.bedroom_humidity      # Humidity sensor
```

### Govee Devices
Default patterns used in configurations:
```yaml
fan.govee_fan_1                      # First Govee fan
fan.govee_fan_2                      # Second Govee fan (if applicable)
humidifier.govee_humidifier          # Govee humidifier
sensor.govee_fan_1_temperature       # Temperature sensor
sensor.govee_humidifier_humidity     # Humidity sensor
```

**Your actual entities might be:**
```yaml
fan.govee_h7106_bbbc                 # BLE device with MAC address
sensor.ble_temperature_govee_d927    # BLE sensor format
sensor.ble_humidity_govee_6172       # BLE humidity format
```

### Meaco Dehumidifier
Default patterns used in configurations:
```yaml
switch.meaco_dehumidifier            # Power switch
sensor.meaco_dehumidifier_humidity   # Humidity reading
sensor.meaco_dehumidifier_power      # Power consumption
```

**Your actual entities might be:**
```yaml
switch.smart_plug_1                  # If using generic smart plug
switch.tapo_p100_dehumidifier        # If using Tapo plug
sensor.bedroom_humidity              # If using separate humidity sensor
sensor.smart_plug_power              # Generic power sensor
```

## 🔧 Files to Update

When your entity IDs differ from defaults, update these files:

### 1. Automations
**File:** `includes/automations/climate/tado_heating_zones.yaml`
- Search for: `climate.tado_hallway` and `climate.tado_bedroom`
- Replace with your actual zone entity IDs

**File:** `includes/automations/climate/govee_fan_control.yaml`
- Search for: `fan.govee_fan_1`, `humidifier.govee_humidifier`
- Replace with your actual Govee entity IDs
- Update sensor references: `sensor.govee_fan_1_temperature`, `sensor.govee_humidifier_humidity`

**File:** `includes/automations/climate/meaco_dehumidifier.yaml`
- Search for: `switch.meaco_dehumidifier`
- Replace with your actual dehumidifier switch entity
- Update sensor references: `sensor.meaco_dehumidifier_humidity`, `sensor.meaco_dehumidifier_power`

### 2. Scripts
**File:** `includes/scripts/climate/tado_control.yaml`
- Update all references to `climate.tado_hallway` and `climate.tado_bedroom`

**File:** `includes/scripts/climate/govee_control.yaml`
- Update references to `fan.govee_fan_1` and `humidifier.govee_humidifier`

**File:** `includes/scripts/climate/meaco_control.yaml`
- Update references to `switch.meaco_dehumidifier` and related sensors

### 3. Template Sensors
**File:** `includes/templates/climate_sensors.yaml`
- Update all entity references in template sensors
- This file has the most entity references to update

### 4. Dashboard
**File:** `dashboards/climate_control.yaml`
- Update entity references in all cards
- Particularly important for thermostat and control cards

## 🔄 Search and Replace Guide

### Using Find and Replace (Recommended)
If you have many occurrences, use your editor's find-and-replace:

**Example: Tado Zone Names**
1. Find: `climate.tado_hallway`
2. Replace: `climate.your_actual_hallway_entity`
3. Apply across all climate files

**Example: Govee Fan**
1. Find: `fan.govee_fan_1`
2. Replace: `fan.govee_h7106_bbbc` (or your actual entity)
3. Apply across govee-related files

### Command Line Method
```bash
cd /config

# Replace Tado entities
grep -r "climate.tado_hallway" includes/automations/climate/ includes/scripts/climate/ includes/templates/climate_sensors.yaml dashboards/climate_control.yaml

# Do the same for other entity patterns
grep -r "fan.govee_fan_1" includes/
grep -r "switch.meaco_dehumidifier" includes/
```

## ✅ Verification Checklist

After updating entity IDs:
- [ ] Check YAML syntax: Developer Tools → YAML → Check Configuration
- [ ] Reload automations: Developer Tools → YAML → Automations
- [ ] Reload scripts: Developer Tools → YAML → Scripts
- [ ] Reload template entities: Developer Tools → YAML → Template Entities
- [ ] Verify template sensors appear in Developer Tools → States
- [ ] Test one automation manually
- [ ] Test one script manually
- [ ] Check dashboard displays correctly

## 📋 Entity ID Reference Table

Create your own reference table:

| Configuration Name | Your Actual Entity ID | Notes |
|-------------------|----------------------|-------|
| climate.tado_hallway | `_________________` | Hallway zone |
| climate.tado_bedroom | `_________________` | Bedroom zone |
| climate.tado_hallway_trv_1 | `_________________` | Hallway TRV 1 |
| climate.tado_hallway_trv_2 | `_________________` | Hallway TRV 2 |
| climate.tado_bedroom_trv_1 | `_________________` | Bedroom TRV 1 |
| climate.tado_bedroom_trv_2 | `_________________` | Bedroom TRV 2 |
| fan.govee_fan_1 | `_________________` | Govee fan |
| humidifier.govee_humidifier | `_________________` | Govee humidifier |
| sensor.govee_fan_1_temperature | `_________________` | Fan temp sensor |
| sensor.govee_humidifier_humidity | `_________________` | Humidity sensor |
| switch.meaco_dehumidifier | `_________________` | Dehumidifier switch |
| sensor.meaco_dehumidifier_humidity | `_________________` | Dehumidifier humidity |
| sensor.meaco_dehumidifier_power | `_________________` | Dehumidifier power |

## 🎯 Quick Start

If you want to test with placeholder entities first:

1. **Create Template Test Entities** (Developer Tools → Template):
   ```yaml
   # Create fake climate entity for testing
   template:
     - climate:
         - name: "Test Hallway"
           unique_id: test_hallway_climate
           current_temperature: 20
           target_temperature: 21
   ```

2. **Update Configurations** to use test entities

3. **Verify Everything Works** before adding real devices

4. **Replace Test Entities** with real ones once devices are set up

## 💡 Tips

- **Use Consistent Naming**: If your zone is named "lounge" instead of "hallway", update ALL references
- **Keep a Backup**: Save original files before mass find-and-replace
- **Test Incrementally**: Update one file at a time, test, then continue
- **Document Changes**: Keep notes of what you changed and why
- **Use Comments**: Add comments in YAML to indicate customizations

## 🔗 Related Documentation

- `DEVICE_INTEGRATION_GUIDE.md` - Device setup instructions
- `CLIMATE_TESTING_CHECKLIST.md` - Testing procedures
- `configuration.yaml` - Main configuration file

---

**Note:** Entity IDs are case-sensitive. Use exact matches from Developer Tools.
