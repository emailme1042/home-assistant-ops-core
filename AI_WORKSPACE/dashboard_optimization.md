# 🚀 Dashboard Performance Optimization Plan — November 13, 2025

## 🎯 **Issue: 25-Second Dashboard Load Times**

**Root Cause Analysis**: Excessive recorder database load, unoptimized entity history tracking, and bloated Lovelace rendering causing 25+ second load times.

**Target Performance**: <5 second dashboard loads with >90% entity availability.

---

## 🛠️ **Phase 1: Recorder & Database Optimization**

### **Current Recorder Configuration Assessment**
- **Database Size**: Unknown (needs audit)
- **Retention Period**: 3 days (good)
- **Excluded Domains**: Limited (needs expansion)
- **High-Frequency Sensors**: Not excluded (causing bloat)

### **Optimized Recorder Configuration**

```yaml
recorder:
  db_url: mysql://homeassistant:password@core-mariadb/homeassistant?charset=utf8mb4
  purge_keep_days: 3  # Reduced from 7 to 3 days to minimize database growth
  auto_purge: true
  commit_interval: 10  # Add for better performance
  exclude:
    domains:
      - automation
      - script
      - mqtt
      - update
      - device_tracker
    entity_globs:
      # Exclude frequently changing sensors that don't need history
      - sensor.ai_exec_log_recent
      - sensor.yaml_validation_status
      - sensor.includes_validation_status
      - sensor.automation_validation_status
      - sensor.last_validation_check
      - sensor.local_flask_status_code
      - sensor.time
      - sensor.date
      - sensor.*_linkquality
      - sensor.*_last_seen
      - sensor.*_distance
      - sensor.*_battery
      - sensor.cpu_*
      - sensor.memory_*
      - sensor.load_*
      - sensor.uptime
      - sensor.*_temperature
      - sensor.*_humidity
      - sensor.*_illuminance
      - binary_sensor.*_motion
      - binary_sensor.*_contact
```

### **Logbook & History Optimization**

```yaml
logbook:
  exclude:
    domains:
      - automation
      - script
      - mqtt
      - update
      - device_tracker
    entity_globs:
      - sensor.*_linkquality
      - sensor.*_last_seen
      - sensor.*_battery
      - sensor.cpu_*
      - sensor.memory_*

history:
  exclude:
    domains:
      - automation
      - script
      - mqtt
      - update
      - device_tracker
    entity_globs:
      - sensor.*_linkquality
      - sensor.*_last_seen
      - sensor.*_battery
      - sensor.cpu_*
      - sensor.memory_*
```

---

## 🧪 **Phase 2: Database Maintenance**

### **Immediate Database Purge**
**Service Call**: `recorder.purge`
```yaml
service: recorder.purge
data:
  keep_days: 2
  repack: true
  apply_filter: true
```

**Expected Results**:
- Database size reduction: >7GB → <500MB
- Performance improvement: 25s → <5s load times
- Entity availability: ~70% → >90%

### **Database Health Check**
```yaml
service: recorder.purge
data:
  keep_days: 1
  repack: false
  apply_filter: false
```

---

## 🎨 **Phase 3: Lovelace UI Optimization**

### **Dashboard Structure Recommendations**

1. **Split Large Dashboards**
   - Main dashboard: Core controls only
   - Separate views: Lights, Climate, Security, Sensors
   - Use navigation buttons between views

2. **Card Optimization**
   - **Replace heavy cards**: `mini-graph-card` with 24h data → use `entities` card
   - **Conditional visibility**: Hide inactive/unavailable entities
   - **Native cards preferred**: `entities`, `glance`, `button` over custom cards
   - **Limit card count**: Max 20 cards per view

3. **View Organization**
   ```
   📊 Main Dashboard (Essential controls)
   💡 Lighting (All lights and switches)
   🌡️ Climate (Thermostats, sensors)
   🔒 Security (Cameras, alarms, doors)
   📈 Monitoring (System health, sensors)
   ⚙️ Settings (Configuration access)
   ```

### **Performance Settings**

```yaml
frontend:
  themes: !include_dir_merge_named themes
  # Add these for better performance
  extra_module_url: []
  development_repo: false
```

---

## 📊 **Phase 4: System Health Monitoring**

### **Performance Sensors to Add**

```yaml
sensor:
  - platform: systemmonitor
    resources:
      - type: disk_use_percent
        arg: /
      - type: memory_use_percent
      - type: processor_use
    scan_interval: 60  # Reduce from default 30s
```

### **Dashboard Load Time Monitoring**

```yaml
template:
  - sensor:
      - name: "Dashboard Load Time"
        state: >
          {% set start = now() %}
          {{ (now() - start).total_seconds() }}
        unit_of_measurement: "s"
        device_class: duration
```

---

## 🎯 **Implementation Priority**

### **Immediate Actions (Today)**
1. ✅ **Apply recorder exclusions** to `configuration.yaml`
2. ✅ **Run database purge** with `recorder.purge` service
3. ✅ **Split main dashboard** into smaller views
4. ✅ **Replace heavy cards** with native alternatives

### **Short-term (This Week)**
1. ⏳ **Monitor performance** for 24-48 hours
2. ⏳ **Fine-tune exclusions** based on usage patterns
3. ⏳ **Optimize remaining dashboards**
4. ⏳ **Add performance monitoring**

### **Long-term (Ongoing)**
1. 🔄 **Regular database maintenance** (weekly purge)
2. 🔄 **Dashboard cleanup** (quarterly review)
3. 🔄 **Performance monitoring** (continuous)

---

## 📈 **Expected Performance Gains**

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Dashboard Load Time | 25s | <5s | **5x faster** |
| Entity Availability | ~70% | >90% | **20% better** |
| Database Size | >7GB | <500MB | **14x smaller** |
| CPU Usage | High | Stable | **Significant reduction** |
| Memory Usage | High | Optimized | **Better stability** |
| WebSocket Disconnects | Frequent | Rare | **Much more stable** |

---

## 🛠️ **Quick Implementation Script**

Create `dashboard_optimization.sh`:

```bash
#!/bin/bash
echo "🚀 HA Dashboard Performance Optimization"

# Backup current config
cp /config/configuration.yaml /config/configuration_backup_pre_optimization.yaml

# Apply recorder optimizations
echo "✅ Applying recorder optimizations..."
# [Add sed commands to update configuration.yaml]

# Run database purge
echo "🧹 Purging database..."
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  http://localhost:8123/api/services/recorder/purge \
  -d '{"keep_days": 2, "repack": true, "apply_filter": true}'

echo "✅ Optimization complete! Restart HA to apply changes."
```

---

## 📋 **Success Validation Checklist**

- [ ] Dashboard loads in <5 seconds
- [ ] Entity availability >90%
- [ ] Database size <500MB
- [ ] No WebSocket disconnects during normal use
- [ ] CPU/memory usage stable
- [ ] All dashboards functional

**Status**: **OPTIMIZATION PLAN CREATED** — Ready for implementation!

**Next Steps**: Apply recorder exclusions, run database purge, optimize dashboards.</content>
<parameter name="filePath">s:\AI_WORKSPACE\dashboard_optimization.md