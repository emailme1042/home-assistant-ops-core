# Climate Device Integration - Testing Checklist

This checklist helps verify that all climate device configurations are working correctly.

## 📋 Pre-Integration Checklist

### Before Adding Devices
- [ ] Review `DEVICE_INTEGRATION_GUIDE.md` for setup instructions
- [ ] Backup current Home Assistant configuration
- [ ] Ensure Home Assistant is running version 2024.1 or later
- [ ] Verify network connectivity for all devices

### Required Integrations
- [ ] Tado integration available (check Settings → Integrations)
- [ ] BLE Monitor custom component installed (for Govee BLE devices)
- [ ] Smart plug integration for Meaco (if using smart plug method)

## 🔧 Device Setup Steps

### 1. Tado Heating System
- [ ] Add Tado integration through UI (Settings → Add Integration → Tado)
- [ ] Enter Tado account credentials
- [ ] Verify all zones appear in Developer Tools → States
- [ ] Expected entities:
  - [ ] `climate.tado_hallway` or similar
  - [ ] `climate.tado_bedroom` or similar
  - [ ] TRV entities (2 per floor)
- [ ] Update entity IDs in configuration files if different from defaults
- [ ] Test manual temperature adjustment via UI

### 2. Govee Devices
- [ ] Enable Bluetooth on Home Assistant host
- [ ] Verify BLE Monitor integration is active
- [ ] Check for Govee device discovery in integrations
- [ ] Expected entities:
  - [ ] `fan.govee_fan_1` or similar
  - [ ] `humidifier.govee_humidifier` or similar
  - [ ] Temperature/humidity sensors
- [ ] Update entity IDs in configuration files if different
- [ ] Test fan on/off via UI
- [ ] Test humidifier control via UI

### 3. Meaco Dehumidifier
- [ ] Connect dehumidifier to smart plug (if applicable)
- [ ] Add smart plug integration
- [ ] Create switch entity for dehumidifier
- [ ] Expected entities:
  - [ ] `switch.meaco_dehumidifier`
  - [ ] `sensor.meaco_dehumidifier_humidity` (if available)
  - [ ] `sensor.meaco_dehumidifier_power` (if available)
- [ ] Update entity IDs in configuration files
- [ ] Test switch on/off via UI

## ✅ Configuration Validation

### YAML Syntax Check
```bash
# Check all climate configuration files
cd /config
python3 -c "import yaml; yaml.safe_load(open('includes/automations/climate/tado_heating_zones.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/automations/climate/govee_fan_control.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/automations/climate/meaco_dehumidifier.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/scripts/climate/tado_control.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/scripts/climate/govee_control.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/scripts/climate/meaco_control.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('includes/templates/climate_sensors.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('dashboards/climate_control.yaml'))"
```

### Home Assistant Configuration Check
- [ ] Run configuration check: Developer Tools → YAML → Check Configuration
- [ ] Verify no errors related to climate files
- [ ] Fix any entity ID mismatches
- [ ] Restart Home Assistant

## 🧪 Functional Testing

### Template Sensors
- [ ] Check Developer Tools → States for new sensors:
  - [ ] `sensor.tado_hallway_status`
  - [ ] `sensor.tado_bedroom_status`
  - [ ] `sensor.home_average_temperature`
  - [ ] `sensor.heating_demand_active`
  - [ ] `sensor.govee_fan_status_summary`
  - [ ] `sensor.govee_humidifier_status_summary`
  - [ ] `sensor.meaco_dehumidifier_status_summary`
  - [ ] `sensor.climate_control_summary`
  - [ ] `binary_sensor.heating_required`
  - [ ] `binary_sensor.humidity_too_high`
  - [ ] `binary_sensor.humidity_too_low`
- [ ] Verify all sensors show valid states (not "unavailable" or "unknown")

### Automations
- [ ] Navigate to Settings → Automations & Scenes
- [ ] Verify all climate automations are loaded:
  - [ ] Tado Morning Warmup - Hallway
  - [ ] Tado Morning Warmup - Bedroom
  - [ ] Tado Evening Comfort Mode
  - [ ] Tado Night Mode Economy
  - [ ] Tado Away Mode Detection
  - [ ] Tado Home Mode Detection
  - [ ] Tado Low Temperature Alert
  - [ ] Govee Fan Auto on High Temperature
  - [ ] Govee Fan Auto off Normal Temperature
  - [ ] Govee Humidifier Auto Control
  - [ ] Govee Fan Night Mode
  - [ ] Govee Humidifier Night Schedule
  - [ ] Govee Devices Morning Stop
  - [ ] Meaco Dehumidifier High Humidity Auto On
  - [ ] Meaco Dehumidifier Normal Humidity Auto Off
  - [ ] Meaco Dehumidifier Schedule Morning
  - [ ] Meaco Dehumidifier Schedule Evening Stop
  - [ ] Meaco Dehumidifier High Power Alert
  - [ ] Meaco Dehumidifier Moisture Extraction Monitor
- [ ] Test enabling/disabling automations
- [ ] Manually trigger an automation to verify it works

### Scripts
- [ ] Navigate to Settings → Automations & Scenes → Scripts
- [ ] Verify all climate scripts are loaded:
  - [ ] Tado Set Zone Temperature
  - [ ] Boost Tado Heating
  - [ ] Enable Tado Eco Mode
  - [ ] Enable Tado Comfort Mode
  - [ ] Turn Off All Tado Heating
  - [ ] Sync Tado Zone Temperatures
  - [ ] Tado Weekend Heating Schedule
  - [ ] Set Govee Fan Speed
  - [ ] Toggle Govee Fan Oscillation
  - [ ] Govee Humidifier Quick Boost
  - [ ] Govee Devices Sleep Mode
  - [ ] Turn Off All Govee Devices
  - [ ] Govee Summer Cooling Mode
  - [ ] Govee Winter Comfort Mode
  - [ ] Meaco Quick Dry Mode
  - [ ] Toggle Meaco Dehumidifier
  - [ ] Meaco Laundry Drying Mode
  - [ ] Meaco Bathroom Boost
  - [ ] Meaco Daily Maintenance Run
  - [ ] Check Meaco Status
- [ ] Run at least one script from each category
- [ ] Verify script executes without errors

### Input Helpers
- [ ] Navigate to Settings → Devices & Services → Helpers
- [ ] Verify climate input helpers exist:
  - [ ] Climate preference numbers (9 helpers)
  - [ ] Climate control booleans (8 helpers)
  - [ ] Climate mode selects (4 helpers)
- [ ] Test adjusting values
- [ ] Verify values persist after Home Assistant restart

### Dashboard
- [ ] Navigate to Climate Control dashboard in sidebar
- [ ] Verify all three views load:
  - [ ] Home (overview and heating zones)
  - [ ] Fans & Humidity
  - [ ] Scenes
- [ ] Test thermostat controls for Tado zones
- [ ] Test fan speed buttons
- [ ] Test humidifier controls
- [ ] Test dehumidifier controls
- [ ] Verify all quick action buttons work
- [ ] Test scene buttons

## 🍎 Apple TV Testing

### Setup Apple TV
- [ ] Install Home Assistant Companion app on Apple TV
- [ ] Login to your Home Assistant instance
- [ ] Navigate to dashboards

### Dashboard Verification
- [ ] Open Climate Control dashboard on Apple TV
- [ ] Verify readable text sizes (optimized for TV viewing)
- [ ] Test touch controls are responsive
- [ ] Verify all cards display correctly
- [ ] Test thermostat controls with Apple TV remote
- [ ] Test button presses for scripts
- [ ] Navigate between dashboard views

### Voice Control (if Apple TV has Siri)
- [ ] Test "Hey Siri, set hallway temperature to 21 degrees"
- [ ] Test "Hey Siri, turn on the fan"
- [ ] Test "Hey Siri, turn off the dehumidifier"

## 🔍 Monitoring & Maintenance

### Daily Checks (First Week)
- [ ] Monitor automation triggers in Settings → Automations
- [ ] Check for any error notifications
- [ ] Verify temperature readings are accurate
- [ ] Confirm heating cycles match schedule
- [ ] Review humidity levels

### Weekly Checks
- [ ] Review automation history
- [ ] Check for any failed automations
- [ ] Verify energy usage is as expected
- [ ] Adjust schedules if needed
- [ ] Update temperature preferences based on comfort

### Monthly Maintenance
- [ ] Review and optimize automation rules
- [ ] Check for Home Assistant updates
- [ ] Verify all devices are still responsive
- [ ] Update documentation with any changes
- [ ] Clean device sensors (if applicable)

## 📊 Expected Behavior

### Normal Operation
- Heating zones should follow schedule (6:00/6:30 AM warmup, 18:00 evening comfort, 23:00 night economy)
- Away mode should activate after 30 minutes with no one home
- Fan should auto-start if temperature exceeds 25°C
- Humidifier should maintain 40-60% humidity range
- Dehumidifier should activate above 65% humidity
- Low temperature alerts should trigger below 15°C

### Energy Saving Features
- Eco mode reduces temperature to 17°C
- Night mode reduces temperature to 18°C
- Away mode enables energy-saving preset
- Fan runs at reduced speed at night (22:00)

## ❌ Troubleshooting

### Common Issues

**Entity Not Found Errors**
- Check actual entity IDs in Developer Tools → States
- Update configuration files with correct entity IDs
- Reload automations/scripts: Developer Tools → YAML

**Automations Not Triggering**
- Verify automation is enabled in Settings → Automations
- Check automation conditions are met
- Review automation traces in automation details

**Dashboard Not Loading**
- Check browser console for errors
- Verify dashboard YAML is valid
- Try clearing browser cache
- Check lovelace configuration in configuration.yaml

**Devices Not Responding**
- Check device power and connectivity
- Verify integration is active in Settings → Integrations
- Restart integration if needed
- Check Home Assistant logs for errors

## 📝 Documentation Updates

After successful testing:
- [ ] Document actual entity IDs used
- [ ] Update automation schedules if changed
- [ ] Note any custom configurations
- [ ] Add photos of dashboard on Apple TV
- [ ] Update README with lessons learned

## ✨ Customization Ideas

Once basic functionality is confirmed:
- [ ] Add window sensors for better heating control
- [ ] Integrate weather forecast for predictive heating
- [ ] Add energy monitoring for cost tracking
- [ ] Create custom notifications for mobile devices
- [ ] Add presence detection for per-person preferences
- [ ] Integrate with voice assistants (Alexa, Google)
- [ ] Create seasonal automation rule variants

---

**Last Updated:** January 2026
**Tested On:** Home Assistant 2025.x
**Status:** Ready for Testing
