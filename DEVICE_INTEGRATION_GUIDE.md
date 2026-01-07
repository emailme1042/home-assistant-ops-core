# Device Integration Guide

This guide explains how to integrate Tado heating zones, Govee devices, and Meaco dehumidifier into Home Assistant.

## 🌡️ Tado Integration

### Prerequisites
1. Tado account with configured zones
2. Tado devices connected to your Wi-Fi network

### Setup Steps

#### Step 1: Add Tado Integration (UI)
1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for "Tado"
4. Enter your Tado credentials
5. The integration will auto-discover your zones and TRVs

#### Step 2: Expected Entities
After integration, you should see:
- `climate.tado_hallway` - Hallway zone (Floor 1)
- `climate.tado_bedroom` - Bedroom zone (Floor 2)
- `climate.tado_hallway_trv_1` - First TRV in hallway
- `climate.tado_hallway_trv_2` - Second TRV in hallway
- `climate.tado_bedroom_trv_1` - First TRV in bedroom
- `climate.tado_bedroom_trv_2` - Second TRV in bedroom

**Note:** Entity names may vary based on your Tado setup. Check **Developer Tools** → **States** after integration.

## 🌀 Govee Devices Integration

### Prerequisites
1. Govee devices (fans and humidifier)
2. BLE Monitor custom component (already installed in this setup)

### Setup Steps

#### Option 1: Bluetooth Integration (Recommended)
1. Ensure Bluetooth is enabled on your Home Assistant host
2. Govee devices will be auto-discovered via BLE Monitor
3. Check **Settings** → **Devices & Services** → **BLE Monitor**

#### Option 2: Govee Home Integration
1. Install Govee Home integration via HACS
2. Go to **Settings** → **Devices & Services**
3. Click **+ Add Integration**
4. Search for "Govee"
5. Enter your Govee API key (from Govee Home app)

#### Expected Entities
- `fan.govee_fan_1` - First Govee fan
- `fan.govee_fan_2` - Second Govee fan (if applicable)
- `humidifier.govee_humidifier` - Govee humidifier
- `sensor.govee_fan_1_temperature` - Temperature sensor (if supported)
- `sensor.govee_humidifier_humidity` - Humidity level

## 💧 Meaco Dehumidifier Integration

### Prerequisites
1. Meaco dehumidifier with Wi-Fi or smart plug
2. Compatible integration method (see options below)

### Setup Steps

#### Option 1: Smart Plug Control (Simplest)
1. Connect dehumidifier to a smart plug (e.g., TP-Link Tapo, already in custom_components)
2. Configure smart plug through its integration
3. Create template switch for dehumidifier control

#### Option 2: Meross LAN Integration (if Meross-compatible)
1. Already installed in custom_components
2. Go to **Settings** → **Devices & Services**
3. Check if Meaco is Meross-compatible
4. Add via Meross LAN integration

#### Expected Entities
- `switch.meaco_dehumidifier` - On/off control
- `sensor.meaco_dehumidifier_power` - Power consumption (if available)
- `sensor.meaco_dehumidifier_humidity` - Current humidity reading

## 🍎 Apple TV Control Setup

All devices configured through this guide will be automatically available in the Home Assistant Companion app on Apple TV.

### Verification Steps
1. Open Home Assistant app on Apple TV
2. Navigate to climate controls
3. Verify all Tado zones appear
4. Check fan and humidifier controls are accessible
5. Test dehumidifier switch functionality

### Dashboard Optimization for Apple TV
- Climate cards use large touch targets
- Simple on/off controls for fans
- Temperature controls with clear labeling
- Voice control compatible entity naming

## 📋 Configuration Files Added

The following files have been created to support these devices:

### Climate & Heating
- `includes/automations/climate/tado_heating_zones.yaml` - Tado automation rules
- `includes/scripts/climate/tado_control.yaml` - Tado control scripts
- `includes/templates/climate_sensors.yaml` - Climate sensor templates

### Govee Devices
- `includes/automations/climate/govee_fan_control.yaml` - Fan automation
- `includes/scripts/climate/govee_control.yaml` - Govee control scripts

### Meaco Dehumidifier
- `includes/automations/climate/meaco_dehumidifier.yaml` - Dehumidifier automation
- `includes/scripts/climate/meaco_control.yaml` - Dehumidifier control scripts

### Dashboard
- `dashboards/climate_control.yaml` - Climate control dashboard for Apple TV

## 🧪 Testing

After adding devices, validate your configuration:

```bash
# Check YAML syntax
ha core check

# Or use the validation script
python3 /config/scripts/validate_yaml.py /config
```

## 🔧 Troubleshooting

### Tado devices not appearing
- Verify Tado account credentials
- Check Wi-Fi connectivity of Tado devices
- Restart Home Assistant after integration

### Govee devices not discovered
- Ensure Bluetooth is enabled and in range
- Check BLE Monitor integration is active
- Verify device batteries if battery-powered

### Meaco dehumidifier not responding
- Check smart plug power supply
- Verify dehumidifier physical power switch is ON
- Test smart plug independently first

## 📚 Additional Resources

- [Tado Integration Documentation](https://www.home-assistant.io/integrations/tado/)
- [BLE Monitor GitHub](https://github.com/custom-components/ble_monitor)
- [Home Assistant Climate Documentation](https://www.home-assistant.io/integrations/climate/)
