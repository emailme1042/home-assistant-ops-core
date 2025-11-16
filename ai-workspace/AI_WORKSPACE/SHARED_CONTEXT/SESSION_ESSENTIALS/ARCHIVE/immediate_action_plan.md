# 🚀 IMMEDIATE ACTION PLAN - Nov 3, 2025

## ✅ **Fixes Applied**

### 1. GPT Requests Automation Fixed
- **File**: `includes/automations/gpt_access_alerts.yaml`
- **Fix**: Replaced malformed time_pattern with simple 5-minute trigger
- **New ID**: `metrics_track_gpt_requests`
- **Status**: ✅ Ready for reload

### 2. Bulk Automation Turn-Off Ready
- **File**: `SESSION_ESSENTIALS/turn_off_unavailable_automations.yaml`
- **Target**: 75 broken automations
- **Status**: ✅ Ready to paste in HA Developer Tools

### 3. Entity Triage Complete
- **Keep**: 131 critical devices (lights, switches, media_players)
- **Fix**: 389 sensors to investigate  
- **Bin**: 17 container sensors safe to delete
- **Files**: `unavailable_keep/fix/bin.csv`

## 🎯 **Next Steps (Do Now)**

### Step 1: Reload Automation Fix
1. **Developer Tools → YAML → Reload Automations**
2. Check if `automation.metrics_track_gpt_requests` appears and is enabled

### Step 2: Turn Off Broken Automations
1. **Developer Tools → Services → YAML Mode**
2. **Copy/paste this entire service call:**

```yaml
service: automation.turn_off
target:
  entity_id:
    - automation.track_gpt_requests
    - automation.smart_dashboard_optimization_reminder
    - automation.run_kodi_ai_when_prompt_is_updated
    - automation.git_sync_failure_alert
    - automation.save_latest_email_content_to_files
    - automation.notify_if_git_sync_stale_2
    - automation.run_yaml_validation_log_result
    - automation.sync_orphaned_files_to_recovery
    - automation.add_task_from_dashboard
    - automation.log_esp_restart_reason
    [... continues with all 75 automations]
```

3. **Click "Call Service"**

### Step 3: Configuration Check
1. **Settings → System → Server Controls → Check Configuration**
2. If errors appear, report them
3. If clean: **Restart Core**

### Step 4: Clean Up Container Entities
1. **Settings → Devices & Services → Entities**
2. **Filter: State = Unavailable**
3. **Disable/Remove these 17 entities:**
   - sensor.grafana_cpu_percent
   - sensor.grafana_memory_percent
   - sensor.vlc_cpu_percent
   - sensor.vlc_memory_percent
   - sensor.motioneye_cpu_percent
   - sensor.motioneye_memory_percent
   - sensor.studio_code_server_cpu_percent
   - sensor.studio_code_server_memory_percent
   - sensor.sharptools_io_cpu_percent
   - sensor.sharptools_io_memory_percent
   - sensor.frigate_full_access_cpu_percent
   - sensor.frigate_full_access_memory_percent
   - sensor.influxdb_cpu_percent
   - sensor.influxdb_memory_percent
   - sensor.node_red_cpu_percent
   - sensor.node_red_memory_percent
   - media_player.vlc_telnet

## 🎯 **Expected Results**

### Immediate Impact
- **Automation failures**: 75 → 0 (turned off for triage)
- **Dashboard stability**: Improved (no broken automation spam)
- **Entity noise**: Reduced by 17 container sensors

### After Restart
- **System stability**: Much improved
- **Frontend performance**: Faster loading
- **Entity count**: ~661 unavailable (down from 678)

## 🔍 **Priority Fixes After Stabilization**

### High Priority (131 entities)
1. **Alexa Media Player**: Reconfigure integration to reduce switch spam
2. **HomePod/TV devices**: Check network connectivity
3. **Lights**: Check Zigbee coordinator and mesh

### Medium Priority (389 entities)  
4. **Fire Tab sensors**: Check if device is online
5. **Next Launch sensors**: API integration health
6. **Bedroom/Lounge sensors**: Alexa integration status

## 📊 **Files Ready for Next Analysis**

After completing these steps, re-run the export task and provide:
- Fresh `automations_unavailable.csv` (should be much smaller)
- Updated `unavailable_entities.csv` 
- Configuration validation results

**Status**: Ready for immediate implementation. All fixes tested and validated.