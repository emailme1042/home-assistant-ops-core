# Aqara Device Migration: Matter → Zigbee2MQTT
# Guide to get richer sensor data from your Aqara devices

## 🎯 WHY MIGRATE TO Z2M?
**Current Matter Limitation:** Only basic on/off occupancy detection
**Z2M Benefits:**
- ✅ Battery level monitoring
- ✅ Link quality (LQI) tracking
- ✅ Vibration intensity data
- ✅ Temperature readings (if available)
- ✅ More reliable Zigbee mesh
- ✅ Detailed device diagnostics

## 📋 DEVICES TO MIGRATE
Based on your setup:
1. **Aqara Vibration Sensor** (currently binary_sensor.aqara_vibration_sensor_occupancy)
2. **Aqara E1 TRVs** (currently climate entities with limited data)

## 🛠️ MIGRATION STEPS

### Step 1: Prepare Zigbee2MQTT
**Already configured!** Your Z2M is running on port 8099 with these devices:
- Bathroom Motion Sensor ✅
- Office Motion Sensor ✅
- Bathroom Water Sensor ✅
- Outside Temp Humidity ✅
- Button Zigbee ✅

### Step 2: Factory Reset Aqara Devices
**For each device:**
1. Press and hold reset button for 5+ seconds until LED flashes
2. Device enters pairing mode (LED rapidly flashing)

### Step 3: Pair with Zigbee2MQTT
**Via Z2M Frontend (http://homeassistant.local:8099):**
1. Go to Z2M web interface
2. Click "Permit Join" button
3. Press pairing button on Aqara device
4. Device appears in Z2M with rich MQTT topics

### Step 4: Update HA Configuration
**Remove Matter integration:**
- Settings → Devices & Services
- Remove Matter integration
- Delete old Aqara entities

**New MQTT sensors will auto-discover!**

## 📊 EXPECTED NEW ENTITIES (Z2M)

### Vibration Sensor (Example: 0x1234567890abcdef)
```
sensor.aqara_vibration_sensor_battery          # Battery %
sensor.aqara_vibration_sensor_linkquality      # LQI 0-255
sensor.aqara_vibration_sensor_voltage          # Voltage
binary_sensor.aqara_vibration_sensor_occupancy # Motion detect
sensor.aqara_vibration_sensor_angle_x          # X-axis angle
sensor.aqara_vibration_sensor_angle_y          # Y-axis angle
sensor.aqara_vibration_sensor_angle_z          # Z-axis angle
sensor.aqara_vibration_sensor_temperature      # Temperature (if available)
```

### TRV Example (Example: 0x1234567890fedcba)
```
climate.aqara_trv_heating                      # Full climate control
sensor.aqara_trv_battery                       # Battery %
sensor.aqara_trv_linkquality                   # LQI 0-255
sensor.aqara_trv_position                      # Valve position 0-100%
sensor.aqara_trv_temperature                   # Local temperature
binary_sensor.aqara_trv_window_open            # Window detection
```

## 🔧 UPDATED BOILER SENSORS (After Migration)

### Enhanced Vibration Detection
```yaml
# In includes/sensors/boiler_usage_detection.yaml
heating_demand_active:
  value_template: >
    {# Z2M provides richer vibration data #}
    {% set vibration = states('sensor.aqara_vibration_sensor_angle_x') | float(0) %}
    {% set thermostat_vib_up = states('sensor.thermostat_upstairs_vibration_angle') | float(0) %}
    {% set thermostat_vib_down = states('sensor.thermostat_downstairs_vibration_angle') | float(0) %}

    {# Detect significant vibration (boiler running) #}
    {{ vibration > 10 or thermostat_vib_up > 5 or thermostat_vib_down > 5 or
       is_state('climate.lounge', 'heat') or is_state('climate.bedroom', 'heat') }}
```

### TRV Position Monitoring
```yaml
# Real TRV position data instead of placeholders
trv_lounge_position:
  state_topic: "zigbee2mqtt/Lounge_TRV"
  value_template: "{{ value_json.position }}"
  unit_of_measurement: "%"

trv_bedroom_position:
  state_topic: "zigbee2mqtt/Bedroom_TRV"
  value_template: "{{ value_json.position }}"
  unit_of_measurement: "%"
```

## 📈 DATA IMPROVEMENTS EXPECTED

| Metric | Matter (Current) | Z2M (After Migration) |
|--------|------------------|------------------------|
| Vibration Sensor | Binary occupancy only | Battery, LQI, angles, temp |
| TRV Data | Basic climate control | Position %, battery, window detect |
| Reliability | Matter protocol | Mature Zigbee mesh |
| Diagnostics | Limited | Full device health |

## 🎯 IMMEDIATE BENEFITS FOR BOILER MONITORING

1. **Better Heating Detection:** TRV position shows actual valve opening
2. **Vibration Intensity:** Distinguish boiler modulation levels
3. **Battery Monitoring:** Know when devices need replacement
4. **Link Quality:** Identify mesh optimization opportunities
5. **Temperature Data:** Additional environmental monitoring

## 🚀 QUICK START GUIDE

**Ready to migrate? Here's the fast track:**

1. **Backup current config** (just in case)
2. **Factory reset one Aqara device** (start with vibration sensor)
3. **Permit join in Z2M** → Pair device
4. **Verify rich MQTT data** in Z2M frontend
5. **Update HA entity references** in boiler sensors
6. **Test enhanced boiler monitoring**

**The vibration sensor alone will give us 5x more data points!**

Would you like me to create the specific MQTT sensor configurations for your expected Z2M device topics?