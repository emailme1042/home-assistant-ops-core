# Climate Device Integration - Quick Start

## 🎯 What's Been Added

This PR adds comprehensive support for:
- **Tado Heating System** - 2 zones (Hallway/Floor 1, Bedroom/Floor 2) with TRV support
- **Govee Devices** - Smart fans and humidifier with BLE integration
- **Meaco Dehumidifier** - Smart plug controlled with humidity monitoring

## 📁 Files Overview

### Configuration Files (8 files)
```
includes/automations/climate/
├── tado_heating_zones.yaml      # 8 automations for Tado zones
├── govee_fan_control.yaml       # 6 automations for Govee devices
└── meaco_dehumidifier.yaml      # 6 automations for Meaco

includes/scripts/climate/
├── tado_control.yaml            # 7 scripts (boost, eco, comfort, etc.)
├── govee_control.yaml           # 7 scripts (speed, modes, etc.)
└── meaco_control.yaml           # 6 scripts (quick dry, laundry, etc.)

includes/templates/
└── climate_sensors.yaml         # 13 template sensors

dashboards/
└── climate_control.yaml         # 3-view Apple TV dashboard
```

### Input Helpers (3 files, 21 helpers total)
```
includes/input_numbers/
└── climate_preferences.yaml     # 9 numeric settings

includes/input_booleans/
└── climate_controls.yaml        # 8 toggle switches

includes/input_selects/
└── climate_modes.yaml           # 4 mode selectors
```

### Documentation (3 files)
```
DEVICE_INTEGRATION_GUIDE.md      # How to add devices via UI
CLIMATE_TESTING_CHECKLIST.md    # Complete testing procedures
CLIMATE_ENTITY_CUSTOMIZATION.md # How to update entity IDs
```

## ⚡ Quick Setup (5 Steps)

### Step 1: Add Integrations (UI)
Go to **Settings → Add Integration** and add:
- Tado (enter credentials)
- Govee/BLE Monitor (auto-discover)
- Smart Plug (for Meaco)

### Step 2: Find Entity IDs
Go to **Developer Tools → States** and note:
- Your Tado zone entities (e.g., `climate.hallway`)
- Your Govee entities (e.g., `fan.govee_h7106`)
- Your dehumidifier switch (e.g., `switch.smart_plug_1`)

### Step 3: Update Entity IDs
Use find-and-replace in your editor:
- Replace `climate.tado_hallway` with your actual entity
- Replace `fan.govee_fan_1` with your actual entity
- Replace `switch.meaco_dehumidifier` with your actual entity

See `CLIMATE_ENTITY_CUSTOMIZATION.md` for detailed instructions.

### Step 4: Restart Home Assistant
```bash
# Developer Tools → YAML → Check Configuration
# Then restart Home Assistant
```

### Step 5: Test on Apple TV
Open Home Assistant app on Apple TV and navigate to "Climate Control" dashboard.

## 🎮 What You Can Control

### Via Dashboard
- **Thermostat Controls** - Set temperature for each zone
- **Fan Speed** - Low/Medium/High presets
- **Humidifier** - On/off and target humidity
- **Dehumidifier** - On/off and quick modes
- **Quick Actions** - Boost heating, eco mode, sleep mode
- **Scenes** - Summer mode, winter mode, etc.

### Via Automations (Automatic)
- Morning warmup (6:00-6:30 AM)
- Evening comfort (18:00)
- Night economy (23:00)
- Away mode (when no one home)
- High/low temperature alerts
- Auto fan control (>25°C)
- Auto humidity control (40-60%)
- Auto dehumidifier (>65%)

### Via Scripts (Manual)
- Boost all zones (2 hours)
- Comfort mode (21°C)
- Eco mode (17°C)
- Summer cooling
- Winter humidifying
- Quick dry (4 hours)
- Laundry mode (6 hours)

## 📱 Apple TV Features

The dashboard is optimized for Apple TV with:
- ✅ Large, touch-friendly controls
- ✅ Clear temperature displays
- ✅ Simple on/off buttons
- ✅ Quick action shortcuts
- ✅ Three organized views
- ✅ Voice control ready

## 🔍 Troubleshooting

**Problem:** Entity not found errors
**Solution:** Update entity IDs in configuration files (see Step 3 above)

**Problem:** Automations not working
**Solution:** Check automation is enabled in Settings → Automations

**Problem:** Dashboard not showing
**Solution:** Check `configuration.yaml` has climate_control dashboard entry

**Problem:** Sensors show "unavailable"
**Solution:** Verify devices are added via integrations first

For more help, see `CLIMATE_TESTING_CHECKLIST.md`

## 📊 Expected Behavior

Once configured, you should see:
- Heating follows daily schedule automatically
- Away mode activates when everyone leaves
- Fan turns on when temperature is high
- Humidifier maintains 40-60% humidity
- Dehumidifier activates above 65% humidity
- Low temperature alerts below 15°C

## 🎯 Customization

All settings can be adjusted via input helpers without editing YAML:
- Temperature preferences
- Humidity targets
- Auto-control toggles
- Notification preferences
- Timer durations

## 📚 Need More Help?

1. **Setup Guide** - `DEVICE_INTEGRATION_GUIDE.md`
2. **Testing** - `CLIMATE_TESTING_CHECKLIST.md`
3. **Customization** - `CLIMATE_ENTITY_CUSTOMIZATION.md`

## ✨ What's Great About This Setup

- **Zero Breaking Changes** - All new files, nothing modified
- **Modular** - Easy to enable/disable specific features
- **Flexible** - Works with actual entity names after customization
- **Well Documented** - Three detailed guides included
- **Energy Efficient** - Smart schedules and away detection
- **Apple TV Ready** - Large controls optimized for TV viewing
- **Tested** - All YAML validated before commit

---

**Ready to Use?** Start with Step 1 above! 🚀
