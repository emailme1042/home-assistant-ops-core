# 🧠 LIVE ISSUE TRACKER — Home Assistant Recovery Protocol
**Date:** November 11, 2025
**Status:** Active Recovery
**Priority:** Critical (YAML errors blocking HA startup)

## 🎯 MISSION OVERVIEW
Resolve 5 critical issues preventing full HA functionality and system stability. Track progress, validate fixes, and ensure restart safety.

---

## 🚨 CRITICAL ISSUES (Block HA Startup)

### ✅ 1. YAML Syntax Error in `boiler_backup.yaml`
- **Status:** ✅ FIXED
- **Issue:** Missing colon on line 83 (`export_boiler_history:`)
- **Impact:** HA fails to load configuration.yaml
- **Fix Applied:** Added missing colon, validated YAML structure
- **Validation:** Ready for HA restart test

### 🔄 2. Template Sensor `states.automation` Errors
- **Status:** 🔄 IN PROGRESS (Partially Fixed)
- **Issue:** Incorrect `states.automation` usage in 13+ sensor files
- **Impact:** Sensors become unavailable, HA instability, intermittent disconnections
- **Files Fixed:**
  - ✅ `system_health_template.yaml` - Fixed automation count
  - ✅ `system_health_stats.yaml` - Fixed enabled automations
  - ✅ `system_health.yaml` - Fixed summary template
  - ✅ `jd_dev_board_dashboard_sensors.yaml` - Fixed dashboard sensors
  - ✅ `historical_stats_sensors.yaml` - Fixed working automations
  - ✅ `automation_status_sensors.yaml` - Template file fixed
  - ✅ `system_triage_sensors.yaml` - Fixed unavailable count
  - ✅ `system_triage_compat_sensors.yaml` - Fixed off/on counts
  - ✅ `crash_monitoring.yaml` - Fixed active/total automations
  - ✅ `disabled_automations_count.yaml` - Fixed disabled count
- **Remaining:** 3 backup files and automation files (lower priority)
- **Next:** Validate all fixes, test sensor loading

---

## ⚠️ HIGH PRIORITY ISSUES (Affect User Experience)

### 🔄 3. False "HA Starting" Warnings
- **Status:** 🔄 ANALYSIS NEEDED
- **Issue:** Multiple dashboard panels show "⚠️ Home Assistant is starting"
- **Symptoms:** System, Network, Security, Climate panels stuck in starting state
- **Root Cause:** Template sensors/markdown cards not refreshing after startup
- **Impact:** User confusion, false alarms
- **Fix Plan:**
  - Add uptime-based timeout logic (10-15 min after startup)
  - Refresh bindings in template sensors
  - Update dashboard cards with proper state detection

### 🐢 4. UI Slowness & Responsiveness
- **Status:** 🔄 DIAGNOSIS NEEDED
- **Issue:** Delayed dashboard loads, sluggish click response
- **Symptoms:** Slow page loads, unresponsive controls
- **Root Causes:**
  - Stale browser cache (JS fixes not applied)
  - `custom-attributes.js` MutationObserver timing errors
  - Previously corrupted `auto-entities.js` (now fixed)
- **Fix Plan:**
  - Hard refresh browser cache (`Ctrl+Shift+R`)
  - DevTools → Network → Disable cache → Test
  - Consider removing/replacing `custom-attributes.js`
  - Monitor for MutationObserver errors

### 📉 5. 844 Unavailable Entities
- **Status:** 🔄 MONITORING NEEDED
- **Issue:** High unavailable entity count post-restart
- **Symptoms:** 844/3027 entities unavailable (27.9%)
- **Root Cause:** Zigbee mesh not routing, MQTT devices not recovered
- **Fix Plan:**
  - Restart Zigbee2MQTT container
  - Rebalance Zigbee mesh
  - Monitor entity recovery over 30-60 minutes
  - Check MQTT broker connectivity

### 🧩 6. Flight Radar Subscription Error
- **Status:** 🔄 AUDIT NEEDED
- **Issue:** `Uncaught (in promise) {code: 'not_found', message: 'Subscription not found.'}`
- **Symptoms:** Flight radar dashboard errors
- **Root Cause:** Dashboard references missing/deleted entity
- **Fix Plan:**
  - Audit `/flight-radar/4` view for broken references
  - Remove or replace missing entity references
  - Validate all flight radar sensors exist

---

## 🛠️ RECOVERY PROTOCOL CHECKLIST

### Phase 1: Critical Fixes (Pre-Restart)
- [x] Fix `boiler_backup.yaml` YAML syntax
- [x] Fix template sensor `states.automation` errors
- [ ] Validate all YAML files pass syntax check
- [ ] Update session logs with fixes applied

### Phase 2: HA Restart & Validation
- [ ] Perform HA core restart
- [ ] Monitor startup logs for errors
- [ ] Validate configuration loads successfully
- [ ] Check entity availability (target: <100 unavailable)

### Phase 3: UI & Performance Fixes
- [ ] Clear browser cache (Ctrl+Shift+R)
- [ ] Test dashboard responsiveness
- [ ] Resolve "HA Starting" false warnings
- [ ] Monitor for MutationObserver errors

### Phase 4: Integration Recovery
- [ ] Restart Zigbee2MQTT container
- [ ] Rebalance Zigbee mesh
- [ ] Monitor entity recovery progress
- [ ] Fix flight radar subscription errors

### Phase 5: Performance Audit
- [ ] Enable Profiler integration
- [ ] Run CPU profile (60 seconds)
- [ ] Run memory profile (60 seconds)
- [ ] Analyze bottlenecks and slow components
- [ ] Create optimization plan

---

## 📊 VALIDATION METRICS

### Pre-Fix Baseline (Nov 10, 2025)
- **Entity Health:** 844 unavailable / 3027 total (27.9%)
- **YAML Errors:** 1 critical (boiler_backup.yaml)
- **Template Errors:** 13+ sensor files with `states.automation` issues
- **UI Performance:** Sluggish, cache-related delays
- **System Warnings:** Multiple "HA Starting" false positives

### Target Post-Fix (Nov 11, 2025)
- **Entity Health:** <100 unavailable / 3000+ total (<3.3%)
- **YAML Errors:** 0 critical errors
- **Template Errors:** 0 sensor loading failures
- **UI Performance:** Responsive, <2s load times
- **System Warnings:** Accurate status reporting

---

## 🔍 DIAGNOSTIC TOOLS READY

### Performance Profiling Setup
```yaml
# Add to configuration.yaml if not present
profiler:
```

### Browser Cache Clearing Protocol
1. Press `Ctrl+Shift+R` (hard refresh)
2. Open DevTools → Network tab
3. Check "Disable cache"
4. Refresh page and monitor for errors

### Entity Recovery Monitoring
```yaml
# Template sensor for tracking recovery
sensor:
  - platform: template
    sensors:
      entity_recovery_progress:
        friendly_name: "Entity Recovery Progress"
        value_template: >
          {% set total = states | count %}
          {% set unavailable = states | selectattr('state', 'in', ['unavailable', 'unknown']) | list | count %}
          {% set percent = ((total - unavailable) / total * 100) | round(1) %}
          {{ percent }}%
```

---

## 📝 SESSION LOG INTEGRATION

### Fixed Files Log
- `includes/shell_commands/boiler_backup.yaml` - Added missing colon
- `includes/sensors/system_health_template.yaml` - Fixed automation count
- `includes/sensors/system_health_stats.yaml` - Fixed enabled automations
- `includes/sensors/system_health.yaml` - Fixed summary template
- `includes/sensors/jd_dev_board_dashboard_sensors.yaml` - Fixed dashboard sensors
- `includes/sensors/historical_stats_sensors.yaml` - Fixed working automations
- `includes/templates/automation_status_sensors.yaml` - Template fixes
- `includes/templates/system_triage_sensors.yaml` - Fixed unavailable count
- `includes/templates/system_triage_compat_sensors.yaml` - Fixed off/on counts
- `includes/sensors/crash_monitoring.yaml` - Fixed active/total automations
- `includes/sensors/disabled_automations_count.yaml` - Fixed disabled count

### Next Session Priorities
1. Complete template sensor validation
2. Perform HA restart test
3. Address UI performance issues
4. Monitor entity recovery
5. Fix flight radar subscription errors

---

**🎯 MISSION STATUS:** Critical YAML errors resolved, template sensor fixes in progress. Ready for restart validation and UI optimization phase.

**📈 SUCCESS METRICS:**
- ✅ 1/1 critical YAML errors fixed
- 🔄 10/13 template sensor files fixed
- 🎯 Target: Full system stability by restart completion</content>
<parameter name="filePath">s:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\LIVE_ISSUE_TRACKER.md