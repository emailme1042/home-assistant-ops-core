# FLIGHT RADAR SUBSCRIPTION FIX
# Resolving "Subscription not found" errors in flight radar dashboard

## 🎯 ISSUE IDENTIFIED
**Error:** `Uncaught (in promise) {code: 'not_found', message: 'Subscription not found.'}`

**Root Cause:** Dashboard references entities that don't exist or haven't been loaded yet after configuration changes.

## 🔍 MISSING ENTITIES ANALYSIS

### ✅ ENTITIES WE CREATED (Should Exist After Restart)
- `sensor.aircraft_proximity_alert` ✅
- `sensor.closest_aircraft_distance` ✅
- `sensor.adsb_receiver_status` ✅
- `sensor.adsb_signal_strength` ✅
- `sensor.aircraft_vertical_rate` ✅
- `sensor.aircraft_average_speed` ✅
- `sensor.flight_activity_trend` ✅
- `input_boolean.flight_proximity_alerts` ✅
- `input_number.flight_alert_distance_km` ✅
- `input_select.flight_history_timeframe` ✅
- `input_datetime.flight_playback_timestamp` ✅
- `input_button.play_flight_history` ✅

### ❌ ENTITIES REFERENCED BUT MISSING
**Flightradar24 Integration Entities (May Not Exist):**
- `sensor.aircraft_count` - Expected from Flightradar24 MQTT
- `sensor.lowest_aircraft_altitude` - Expected from Flightradar24 MQTT
- `sensor.flightradar24_most_tracked` - May not exist
- `sensor.flightradar24_additional_tracked` - May not exist
- `sensor.opensky` - May not exist

**Controls & Automation Entities (Don't Exist):**
- `automation.flight_alert_takeoff_or_landing` ❌
- `switch.api_data_fetching` ❌
- `text.flightradar24_add_to_track` ❌
- `text.flightradar24_remove_from_track` ❌
- `light.brown_lamp` ❌
- `update.flightradar24_card_update` ❌
- `update.flightradar24_update` ❌

## 🛠️ IMMEDIATE FIXES

### 1. Remove References to Non-Existent Entities
**File:** `s:\dashboards\planes.yaml`

**Remove these entity references:**
```yaml
# In Controls & Alerts view - remove these:
- automation.flight_alert_takeoff_or_landing  # Doesn't exist
- switch.api_data_fetching                    # Doesn't exist
- text.flightradar24_add_to_track            # Doesn't exist
- text.flightradar24_remove_from_track       # Doesn't exist
- light.brown_lamp                           # Doesn't exist
- update.flightradar24_card_update           # Doesn't exist
- update.flightradar24_update                # Doesn't exist

# In Technical Data view - check these exist:
- sensor.flightradar24_most_tracked          # May not exist
- sensor.flightradar24_additional_tracked    # May not exist
- sensor.opensky                             # May not exist
```

### 2. Replace with Available Entities
**Replace missing entities with:**
```yaml
# Instead of missing automation:
- automation.flight_proximity_alert           # We created this

# Instead of missing switch:
- input_boolean.flight_proximity_alerts       # We created this

# Instead of missing text inputs:
- input_select.flight_history_timeframe       # We created this
- input_number.flight_alert_distance_km       # We created this

# Instead of missing light:
# Remove or replace with actual light entity if available
```

### 4. Template Sensor Circular References Fixed
**Issue**: 4 template sensors had circular references in icon_template causing unavailability
**Sensors Fixed**:
- `sensor.aircraft_proximity_alert` - Referenced itself in icon_template
- `sensor.aircraft_vertical_rate` - Referenced itself in icon_template  
- `sensor.adsb_receiver_status` - Referenced itself in icon_template
- `sensor.flight_activity_trend` - Referenced itself in icon_template

**Fix Applied**: Replaced self-references with direct logic using underlying data sources

## 🚀 VALIDATION STEPS

### Step 1: Check Entity Existence
```bash
# After HA restart, verify entities exist:
# Go to Developer Tools → States
# Search for: sensor.aircraft_proximity_alert
# Should show: state, attributes, etc.
```

### Step 2: Test Dashboard Loading
```bash
# Navigate to Flight Radar HQ dashboard
# Check browser console for subscription errors
# Verify all cards load without "Entity not found"
```

### Step 3: Validate Subscriptions
```bash
# Use browser dev tools:
# Network tab → WS (WebSocket connections)
# Should see successful subscriptions, not 404 errors
```

## 📋 REQUIRED ACTIONS

1. **Remove non-existent entity references** from dashboard
2. **Replace with available entities** we created
3. **Add conditional cards** for optional entities
4. **Restart HA** to load new sensors and inputs
5. **Test dashboard** for subscription errors
6. **Monitor logs** for any remaining issues

## 🎯 EXPECTED RESULTS

**After fixes:**
- ✅ No "Subscription not found" errors
- ✅ All dashboard cards load properly
- ✅ Entities show real data (not "unavailable")
- ✅ WebSocket subscriptions succeed
- ✅ Frontend components can bind to data streams

## 📁 FILES TO MODIFY

- `s:\dashboards\planes.yaml` - Remove/replace missing entity references
- `s:\includes\sensors\adsb_enhanced_sensors.yaml` - Already created ✅
- `s:\includes\input_booleans\flight_proximity_alerts.yaml` - Split from flight_controls.yaml ✅
- `s:\includes\input_numbers\flight_alert_distance_km.yaml` - Split from flight_controls.yaml ✅
- `s:\includes\input_selects\flight_history_timeframe.yaml` - Split from flight_controls.yaml ✅
- `s:\includes\input_datetimes\flight_playback_timestamp.yaml` - Split from flight_controls.yaml ✅
- `s:\includes\input_buttons\play_flight_history.yaml` - Split from flight_controls.yaml ✅

## 🏷️ TAGS
#subscription_not_found #flight_radar_fix #entity_validation #dashboard_cleanup #restart_required