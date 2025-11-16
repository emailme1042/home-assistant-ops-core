# 🔧 Entity Unavailability Fix Plan - 2025-11-05

## 📊 **CURRENT STATUS**
- **Unavailable Entities:** 1,175 (down from 1,239 - some improvement)
- **System Health:** 59.1% (needs improvement to 80%+)
- **Main Culprits:** Container sensors from stopped/removed add-ons

## 🔍 **PATTERN ANALYSIS RESULTS**

### **🔴 Container CPU/Memory Sensors (16 entities)**
These are auto-discovered from Home Assistant add-ons that are no longer running:
- `sensor.grafana_cpu_percent` / `sensor.grafana_memory_percent`
- `sensor.vlc_cpu_percent` / `sensor.vlc_memory_percent`  
- `sensor.motioneye_cpu_percent` / `sensor.motioneye_memory_percent`
- `sensor.studio_code_server_cpu_percent` / `sensor.studio_code_server_memory_percent`
- `sensor.sharptools_io_cpu_percent` / `sensor.sharptools_io_memory_percent`
- `sensor.frigate_full_access_cpu_percent` / `sensor.frigate_full_access_memory_percent`
- `sensor.influxdb_cpu_percent` / `sensor.influxdb_memory_percent`
- `sensor.node_red_cpu_percent` / `sensor.node_red_memory_percent`

### **🔴 MQTT Sensors (12 entities)**
MQTT-related sensors showing unavailable status:
- `sensor.mqtt_last_message_age_temperature_hall`
- Various MQTT connectivity and status sensors

### **🔴 Template/AI Sensors (5 entities)**
Custom sensors that may have dependency issues:
- `sensor.recent_automation_triggers`
- `sensor.nabu_casa_url_status`
- `sensor.ha_domain_summary`

## 🛠️ **CURRENT MITIGATION IN PLACE**

### **✅ Configuration.yaml - Hide Container Sensors**
```yaml
homeassistant:
  customize_glob:
    "sensor.*_cpu_percent":
      hidden: true
    "sensor.*_memory_percent": 
      hidden: true
```

### **✅ Recorder.yaml - Exclude from Database**
```yaml
recorder:
  exclude:
    entity_globs:
      - sensor.*_cpu_percent
      - sensor.*_memory_percent
      - sensor.*_active_notification_count
      - binary_sensor.*_connected
```

## 🎯 **ACTION PLAN**

### **Phase 1: Enhanced Entity Exclusions**
Add more aggressive exclusions to prevent entity creation:

```yaml
# Additional customize_glob entries
"sensor.*_motioneye*":
  hidden: true
"sensor.*_grafana*":
  hidden: true
"sensor.*_vlc*":
  hidden: true
"sensor.*_studio_code*":
  hidden: true
"sensor.*_sharptools*":
  hidden: true
"sensor.*_frigate*":
  hidden: true
"sensor.*_influxdb*":
  hidden: true
"sensor.*_node_red*":
  hidden: true
```

### **Phase 2: MQTT Validation**
- Check MQTT broker connectivity
- Validate ESP32/Zigbee device status
- Review temperature sensor configurations

### **Phase 3: Template Sensor Fixes**
- Fix dependency chains in template sensors
- Add defensive defaults where missing
- Validate all entity references exist

### **Phase 4: System Health Monitoring**
- Monitor entity health score improvement
- Target 80%+ system health (currently 59.1%)
- Track unavailable entity count reduction

## 📈 **EXPECTED RESULTS**
- **Container Sensors:** 16 entities hidden/excluded (immediate)
- **MQTT Sensors:** 12 entities validated/fixed
- **Template Sensors:** 5 entities fixed with defensive defaults
- **Target Health Score:** 80%+ (up from 59.1%)
- **Target Unavailable Count:** <200 (down from 1,175)

## 🚀 **IMPLEMENTATION STATUS**
- [ ] Enhanced customize_glob exclusions
- [ ] MQTT integration validation
- [ ] Template sensor defensive coding
- [ ] System health score monitoring
- [ ] Entity count reduction verification

**Last Updated:** 2025-11-05 23:58
**Next Action:** Implement enhanced entity exclusions