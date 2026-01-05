# VS Code Extension Fallback - Manual Entity Autocomplete

**Purpose**: Manual entity lookup when VS Code HA extension dropdown fails  
**Created**: 2025-10-27 per CP recommendation  
**Usage**: Reference for typing entity names manually in YAML files

## 🏠 **Quick Entity Autocomplete Reference**

### **Lights** 
```yaml
entity_id: light.office         # Office automation
entity_id: light.lounge         # Front door automation  
```

### **Media Players**
```yaml
entity_id: media_player.lounge_alexa    # TTS announcements
entity_id: media_player.office_speaker  # Office media
```

### **Binary Sensors**
```yaml
entity_id: binary_sensor.office_motion      # Motion detection
entity_id: binary_sensor.front_door_contact # Door monitoring
entity_id: binary_sensor.192_168_1_1        # Router ping
entity_id: binary_sensor.mqtt_connection    # 🆕 MQTT health
```

### **Input Controls**
```yaml
entity_id: input_text.openai_query      # AI input
entity_id: input_text.openai_response   # AI output
entity_id: input_boolean.test_voice_openai   # Test trigger
entity_id: input_boolean.debug_mode     # Debug toggle
```

### **System Monitoring (New)**
```yaml
entity_id: sensor.system_health_status     # 🆕 CPU/memory/disk
entity_id: sensor.yaml_validation_status   # 🆕 Config validation
entity_id: sensor.mqtt_watch_status        # 🆕 MQTT watchdog
entity_id: sensor.network_latency          # 🆕 Network ping
```

### **SpeedTest Sensors**
```yaml
entity_id: sensor.speedtest_download    # 🆕 Download speed
entity_id: sensor.speedtest_upload      # 🆕 Upload speed  
entity_id: sensor.speedtest_ping        # 🆕 Ping latency
```

### **Test Controls**
```yaml
entity_id: switch.openai_voice_test         # 🆕 Manual AI test
entity_id: switch.system_validation_toggle  # 🆕 Manual validation
```

## 🔧 **Common Service Calls**

### **Notifications**
```yaml
service: notify.alexa_media_lounge_alexa
data:
  message: "Your message here"
  data:
    type: tts
```

### **Shell Commands**
```yaml
service: shell_command.validate_yaml        # YAML validation
service: shell_command.test_network         # Network test
service: shell_command.clear_dns_cache      # DNS cache clear
```

### **Light Control**
```yaml
service: light.turn_on
target:
  entity_id: light.office
data:
  brightness: 255
```

## 📋 **VS Code Extension Workaround Tips**

1. **For Entity Names**: Copy from this reference instead of relying on dropdown
2. **For Service Calls**: Use the service templates above
3. **For Validation**: Extension's red/green schema validation still works
4. **For Navigation**: Use Ctrl+F to find entity usage instead of F12
5. **For Testing**: Use the Entity Reference dashboard to verify entities exist

## 🔍 **How to Find More Entities**

- **HA UI**: Developer Tools → States → Browse all entities
- **Entity Reference Dashboard**: `/entity-reference` in HA
- **Registry File**: `.storage/core.entity_registry` (advanced)
- **Manual Search**: Use grep/findstr in includes/ folders

---
**Note**: This reference covers the most commonly used entities. For complete lists, use HA Developer Tools or the Entity Reference dashboard.