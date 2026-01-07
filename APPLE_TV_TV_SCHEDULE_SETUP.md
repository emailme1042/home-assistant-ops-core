# 📱 Apple TV Compatibility & TV Schedule Integration - Setup Guide

## ✅ Completed Changes

### 1. Updated groups.yaml for Apple TV Compatibility

**Changes Made:**
- ✅ Removed climate zones from `hacontrol_01` (now focused on lights only)
- ✅ Created new `hacontrol_04` (Heating Zones) group
  - Includes: `climate.lounge`, `climate.bedroom` (Tado TRVs)
- ✅ Created new `hacontrol_05` (Fans & Ventilation) group
  - Includes: `switch.teddy_fan_2`
  - Note: `fan.bedroom_fan` is commented out - uncomment if this entity exists
- ✅ Removed duplicate entities between groups
- ✅ Kept `cover.blind_tilt_94a1` in Security group only (security-relevant blind)

**Apple TV Benefits:**
- Dedicated heating zones group for easy climate control
- Climate entities no longer mixed with lights (cleaner organization)
- Fan controls in dedicated group
- No duplicate entities across groups
- All groups follow Apple TV/HomeKit best practices with proper icons

### 2. TV Schedule iCal Integration

**Changes Made:**
- ✅ Created `includes/calendars/tv_schedule.yaml` with setup instructions
- ✅ Updated `packages/tv_schedule_integrations.yaml` with calendar reference
- ✅ Updated `dashboards/tv_schedule.yaml` with calendar card and setup instructions

**Calendar URL:** `https://tvcal.app/ical/326blc`

## 🔧 Setup Steps Required (Manual Steps for Jamie)

### Step 1: Install ICS Calendar Integration

1. Open Home Assistant
2. Go to **HACS** → **Integrations**
3. Click **Explore & Download Repositories**
4. Search for **"ICS Calendar"** or **"iCalendar"**
5. Click **Download** and restart Home Assistant if prompted

### Step 2: Add TV Schedule Calendar

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration** (bottom right)
3. Search for **"ICS Calendar"** or **"iCalendar"**
4. Enter the following details:
   - **Name:** TV Schedule
   - **URL:** `https://tvcal.app/ical/326blc`
   - **Days to look ahead:** 30 (or your preference)
5. Click **Submit**

### Step 3: Verify Calendar Entity

After setup, you should see:
- Entity: `calendar.tv_schedule`
- Check in **Developer Tools** → **States** to verify

### Step 4: Enable Calendar in Dashboard

1. Open `dashboards/tv_schedule.yaml` in a text editor
2. Find the commented calendar card (around line 63-68)
3. Uncomment the calendar card:
   ```yaml
   - type: calendar
     entities:
       - calendar.tv_schedule
     title: "TV Schedule Calendar"
   ```
4. Save and refresh your TV Schedule dashboard

### Step 5: Test Auto-Reload

The calendar should automatically refresh based on the configured scan interval. To manually test:

1. Go to **Developer Tools** → **Services**
2. Search for `calendar.get_events`
3. Select the service and choose `calendar.tv_schedule`
4. Click **Call Service** to test

## 🔄 Auto-Reload Configuration

### Groups Auto-Reload

Groups automatically reload when you:
1. Edit `groups.yaml`
2. Go to **Developer Tools** → **YAML** → **Groups**
3. Click **Reload Groups**

**Or use the service:**
```yaml
service: group.reload
```

### Calendar Auto-Reload

The ICS Calendar integration automatically refreshes based on its configuration (typically every hour). No manual intervention needed after initial setup.

### Packages Auto-Reload

To reload packages (including TV schedule integrations):
1. Go to **Developer Tools** → **YAML** → **All YAML configuration**
2. Click **Check Configuration** first
3. Then **Restart Home Assistant** if changes were made

## 📝 Entity Reference

### Climate Entities (Tado TRVs)
- `climate.lounge` - Lounge heating zone
- `climate.bedroom` - Bedroom heating zone

### Fan Entities
- `switch.teddy_fan_2` - Teddy's room fan (switch-based)
- `fan.bedroom_fan` - Bedroom fan (commented out - verify if exists)

**Note on Govee Devices:** 
The system has Govee temperature/humidity sensors (H5075, H5105) and possible light devices (H618A), but no Govee fans were found in the current configuration. If you have Govee fans or air purifiers that need to be added:
1. Verify they are integrated in Home Assistant (check Settings → Devices & Services)
2. Find their entity IDs in Developer Tools → States
3. Add them to the `hacontrol_05` (Fans & Ventilation) group in groups.yaml

### Dehumidifier Entities
**Note:** No dehumidifier entities were found in the current configuration. If you have dehumidifiers, they may be:
- Integrated as `humidifier.` entities (Home Assistant uses the humidifier domain for both humidifiers and dehumidifiers)
- Switch-based devices (e.g., `switch.dehumidifier_name`)
- Smart plugs controlling dehumidifiers

To add dehumidifiers, find them in **Developer Tools** → **States** and add to groups.yaml:

```yaml
# Add to hacontrol_05 (Fans & Ventilation) or create a new group
- humidifier.bedroom_dehumidifier
- switch.dehumidifier_name
```

### Calendar Entity (After Setup)
- `calendar.tv_schedule` - TV schedule from tvcal.app

## 🎯 Testing Checklist

- [ ] Groups reload successfully: `Developer Tools → YAML → Groups → Reload Groups`
- [ ] Climate entities appear in Apple TV Home app
- [ ] Fan controls accessible via Apple TV
- [ ] ICS Calendar integration installed via HACS
- [ ] TV Schedule calendar added via UI
- [ ] `calendar.tv_schedule` entity exists in Developer Tools → States
- [ ] TV Schedule dashboard shows calendar events
- [ ] Calendar auto-refreshes (check after 1 hour)

## 🚨 Troubleshooting

### Groups Not Showing in Apple TV

1. Check if entities exist: **Developer Tools** → **States**
2. Verify entity IDs match exactly (case-sensitive)
3. Reload groups: **Developer Tools** → **YAML** → **Groups** → **Reload Groups**
4. Check Home Assistant logs for errors

### Calendar Not Loading

1. Verify ICS Calendar integration is installed (HACS)
2. Check the URL is accessible: `https://tvcal.app/ical/326blc`
3. Review logs: **Settings** → **System** → **Logs**
4. Try re-adding the integration with a different name

### Entity Not Found Errors

If you see errors about missing entities:
- `fan.bedroom_fan` - Uncomment in groups.yaml only if this entity exists
- Check entity names in **Developer Tools** → **States**
- Update groups.yaml with actual entity names

## 📚 Related Files

- `groups.yaml` - Main groups configuration
- `packages/tv_schedule_integrations.yaml` - TV schedule package
- `dashboards/tv_schedule.yaml` - TV schedule dashboard
- `includes/calendars/tv_schedule.yaml` - Calendar setup instructions
- `configuration.yaml` - Main configuration (already includes packages)

## ✅ Validation Status

All YAML files have been validated and are error-free:
- ✅ groups.yaml
- ✅ packages/tv_schedule_integrations.yaml
- ✅ dashboards/tv_schedule.yaml
- ✅ includes/calendars/tv_schedule.yaml

## 🎉 Expected Results

After completing setup:
1. **Apple TV Home App** will show organized groups:
   - Lights & Climate (with heating zones)
   - Media Zone
   - Security Essentials
   - Heating Zones (Tado TRVs)
   - Fans & Ventilation

2. **TV Schedule Dashboard** will display:
   - Calendar view of upcoming TV shows
   - Integration with tvcal.app schedule
   - Auto-updating schedule data

3. **Auto-Reload** will ensure:
   - Groups reload without restart
   - Calendar updates automatically
   - Minimal manual intervention needed
