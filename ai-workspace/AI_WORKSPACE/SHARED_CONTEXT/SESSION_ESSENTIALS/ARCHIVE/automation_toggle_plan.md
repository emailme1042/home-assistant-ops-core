# 🧠 Smart Automation Control Plan - November 3, 2025

## 🎯 Strategy: Granular Control Instead of Bulk Disable

Instead of disabling all automations indiscriminately, we've implemented a **smart toggle system** that preserves working automations (like office lighting) while allowing selective control of noisy/problematic groups.

## 🔧 Components Implemented

### 1. Helper Toggles (Input Booleans)
- `input_boolean.quiet_gpt_automations` - Controls GPT/AI-related automations
- `input_boolean.quiet_noise_automations` - Controls logging/alert/backup automations

### 2. Admin Automations
- `automation.admin_toggle_gpt_automations` - Responds to GPT toggle
- `automation.admin_toggle_noise_automations` - Responds to noise toggle

### 3. Template Sensors
- `sensor.automations_off_count` - Tracks disabled automations
- `sensor.automations_unavailable_count` - Tracks broken automations
- `sensor.automations_total_count` - Total automation count

### 4. Dashboard Integration
- Added control panel to System Triage dashboard
- Live status monitoring
- Quick toggle access

## 🎯 Automation Groups

### 🤖 GPT/AI Group (Controlled by quiet_gpt_automations)
- `automation.track_gpt_requests`
- `automation.run_gpt_when_prompt_changes`
- `automation.send_gpt_prompt_from_direct_input`
- `automation.mark_gpt_as_sent`
- `automation.admin_gpt_reply_complete`
- `automation.react_to_gpt_context_change`
- `automation.log_gpt_context_change`

### 🔇 Noisy/Logging Group (Controlled by quiet_noise_automations)
- `automation.disable_noisy_entity_logging`
- `automation.log_esp_restart_reason`
- `automation.alert_if_wsl_restart_marker_missing`
- `automation.notify_backup_created`
- `automation.notify_of_stale_updates`
- `automation.notify_system_update_available`
- `automation.sync_orphaned_files_to_recovery`
- `automation.git_sync_failure_alert`

### ✅ Core Automations (Always Left ON)
- `automation.office_light_on_when_occupied*` - Working office lighting
- `automation.office_light_off_after_no_motion*` - Office motion logic
- `automation.zigbee_motion_light_control` - Motion lighting system
- `automation.ha_control_when_home` - Presence detection
- `automation.door_open_alexa_lounge_weather_advisory` - Safety alerts
- `automation.kitchen_blinds_*` - Blind automation (if working)

## 🚀 Implementation Steps

### Step 1: Reload Helpers
```
Settings → Devices & Services → Helpers → ⟳ (Reload button)
```

### Step 2: Reload Automations  
```
Developer Tools → YAML → "Reload Automations"
```

### Step 3: Reload Template Entities
```
Developer Tools → YAML → "Reload Template Entities"
```

### Step 4: Test Toggle System
1. Go to System Triage dashboard
2. Toggle "Quiet GPT automations" ON
3. Verify GPT automations turn off (check notification)
4. Toggle back OFF to re-enable

### Step 5: Monitor Counts
Watch the automation status sensors:
- Off Count should change when toggles are used
- Unavailable Count tracks broken automations
- Total Count shows overall system size

## 📊 Quick Verification Templates

Use in Developer Tools → Templates:

```jinja2
Total: {{ states.automation | list | count }}
Off: {{ states.automation | selectattr('state','equalto','off') | list | count }}
Unavailable: {{ states.automation | selectattr('state','equalto','unavailable') | list | count }}
On: {{ states.automation | selectattr('state','equalto','on') | list | count }}
```

## 🎯 Benefits

1. **Preserve Working Systems**: Office light and other functional automations stay active
2. **Selective Noise Reduction**: Can quiet GPT/logging without affecting core functions
3. **Reversible**: One-click to re-enable any group
4. **Auditable**: Clear dashboard showing what's on/off/broken
5. **Safe**: No risk of disabling critical safety or lighting automations

## 🔄 Usage Workflow

### For System Stabilization:
1. Turn ON both quiet toggles to reduce noise
2. Monitor system health scores
3. Fix unavailable automations individually  
4. Turn OFF toggles to restore full functionality

### For Debugging:
1. Turn ON specific toggle to isolate problem group
2. Check if system stability improves
3. Work on individual automations in that group
4. Re-enable when fixed

This approach gives you **granular control** while maintaining **system safety** and **functional automation groups**.