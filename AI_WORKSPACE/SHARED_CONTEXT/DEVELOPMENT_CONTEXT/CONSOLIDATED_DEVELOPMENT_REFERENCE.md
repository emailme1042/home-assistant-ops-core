# CONSOLIDATED DEVELOPMENT CONTEXT

## 🏗️ System Architecture Overview

### **Home Assistant Green Hardware**
- **OS**: Home Assistant OS 16.2 (BusyBox environment)
- **Core**: 2025.10.4, Supervisor 2025.10.0, Frontend 20251001.4
- **Network**: Ethernet-only, IPv6 enabled, 96.36 Mbps performance
- **Shell Limitations**: BusyBox commands only (no systemctl, limited curl)

---

## 🔌 Key Integration Endpoints

### **OpenAI API Integration**
```yaml
ask_openai:
  url: "https://api.openai.com/v1/chat/completions"
  model: "gpt-4o-mini" (optimized for speed)
  headers: "Bearer {{ secrets.openai_api_key }}"
```

### **Local Flask Services**
- **GPT Service**: `http://192.168.1.203:5001/api/chatgpt_query`
- **Backup Service**: `http://192.168.1.203:5001/api/backup`
- **JIT Plugin**: `http://127.0.0.1:5001/jit_plugin/{{ endpoint }}`
- **NAS Scripts**: `http://127.0.0.1:5005/run_nas_script`

### **External APIs**
- **Voice Monkey**: TTS notifications
- **Dropbox**: File uploads
- **Notion**: Page updates
- **Azure CV**: Image analysis

---

## 🎛️ Critical Entity Catalog

### **System Monitoring Entities (VERIFIED WORKING)**
- `sensor.home_assistant_core_cpu_percent` - HA Core CPU usage
- `sensor.home_assistant_core_memory_percent` - HA Core memory usage  
- `sensor.home_assistant_host_disk_used` - Host disk usage
- `sensor.uptime` - System uptime
- `sensor.system_monitor_last_boot` - Last boot timestamp

### **Network Monitoring Entities (CONFIRMED)**
- `sensor.speedtest_download` - Internet download speed
- `sensor.speedtest_upload` - Internet upload speed
- `sensor.speedtest_ping` - Internet latency
- `binary_sensor.192_168_1_1` - Router ping status
- `binary_sensor.192_168_1_217` - HA system ping status

### **Motion & Lighting (FIXED)**
- `binary_sensor.office_motion` - Office motion sensor (corrected entity name)
- `light.office` - Office light control
- `automation.office_light_on_when_occupied_yaml` - Motion trigger (renamed to avoid conflicts)
- `automation.office_light_off_after_no_motion_yaml` - Motion timeout (renamed)

### **Voice Integration (OPERATIONAL)**
- `input_text.openai_query` - Voice query input
- `input_text.openai_response` - AI response storage
- `input_text.tts_message` - TTS message buffer
- `input_boolean.test_voice_openai` - Voice test trigger

---

## 🔧 Validation Workflows

### **YAML Validation Commands**
```bash
# Full system validation
shell_command.validate_yaml: python3 /config/scripts/validate_yaml.py /config

# Automation-specific validation  
shell_command.validate_automations: AUTOMATIONS_PATH=/config/automations.yaml python3 /config/python_scripts/validate_automations.py

# Includes validation (fallback)
shell_command.validate_includes_yaml: python3 /config/python_scripts/validate_includes_yaml.py /config/includes
```

### **Network Diagnostics (BusyBox Compatible)**
```bash
# Network connectivity test
shell_command.test_network: ping -c 4 8.8.8.8

# DNS cache clear (network interface reset)
shell_command.clear_dns_cache: ip link set eth0 down && ip link set eth0 up

# Performance check
shell_command.check_network_performance: wget -O /dev/null --timeout=10 http://httpbin.org/get

# Interface status
shell_command.network_interface_check: ip addr show && ip route show
```

---

## 📊 Dashboard Structure

### **Network Diagnostics** (`dashboards/ops/network_diagnostics.yaml`)
- **System Performance**: Real HA system monitoring entities
- **SpeedTest Integration**: Download/upload/ping monitoring
- **Ping Status**: Router and system connectivity
- **Troubleshooting Tools**: BusyBox-compatible shell commands

### **AI Navigation** (`dashboards/ai/ai_navigation.yaml`)
- **Voice Testing**: OpenAI integration controls
- **File Access**: Direct links to AI workspace files
- **Session Management**: Current status and next steps

### **Working Services** (`dashboards/ops/working_services_test.yaml`)
- **Verified Commands**: Known-working service calls
- **Debug Tools**: Office motion and network diagnostics
- **Performance Testing**: Network and system resource monitoring

---

## 🔨 Automation Patterns

### **Motion-Based Lighting**
```yaml
# Pattern: binary_sensor trigger → light control with timeout
trigger:
  - platform: state
    entity_id: binary_sensor.office_motion
    to: "on"
action:
  - service: light.turn_on
    target:
      entity_id: light.office
```

### **Voice Integration Workflow**
```yaml
# Pattern: input_boolean trigger → REST call → TTS response
trigger:
  - platform: state
    entity_id: input_boolean.test_voice_openai
    to: "on"
action:
  - service: rest_command.ask_openai
  - service: notify.alexa_media_lounge_alexa
```

### **Network Monitoring**
```yaml
# Pattern: SpeedTest automation with configurable frequency
trigger:
  - platform: time_pattern
    minutes: "/30"  # Every 30 minutes
action:
  - service: homeassistant.update_entity
    target:
      entity_id: sensor.speedtest_download
```

---

## 🧰 HACS Components (Key Active)

### **Dashboard & UI**
- `custom-sidebar` - Sidebar customization
- `mini-graph-card` - Network performance graphs
- `auto-entities` - Dynamic entity filtering

### **Device Integration**
- `alexa_media` - TTS and notification
- `tapo_control` - TP-Link device control  
- `speedtestdotnet` - Network performance monitoring
- `bermuda` - Bluetooth tracking

### **System & Automation**
- `watchman` - Entity usage monitoring
- `scheduler` - Advanced automation timing
- `entity_controller` - Motion-based lighting

---

## 🚨 Common Troubleshooting

### **Entity Not Found Errors**
- **Cause**: Dashboard references non-existent entities
- **Solution**: Use `.storage/core.entity_registry` to find actual entity names
- **Prevention**: Validate entity references before deployment

### **Shell Command Failures**
- **Cause**: Non-BusyBox commands (systemctl, advanced curl)
- **Solution**: Use basic commands (ip, ping, wget)
- **Testing**: Developer Tools → Services after HA restart

### **Automation Conflicts**
- **Cause**: Duplicate automation IDs between UI and YAML
- **Solution**: Rename YAML automation IDs with `_yaml` suffix
- **Detection**: Check logs for "skipping duplicate" warnings

### **Network Performance Issues**
- **IPv6 Status**: Ensure enabled for optimal performance
- **Switch Ports**: Verify speed/duplex settings
- **HA Green Hardware**: 40% performance gap vs PC normal

---

## 🎯 Development Best Practices

### **Entity Management**
1. **Validate entities exist** before dashboard deployment
2. **Use consistent naming** (`_yaml` suffix for YAML automations)
3. **Monitor entity usage** with Watchman integration
4. **Clean up unused entities** regularly

### **Shell Commands**
1. **Test BusyBox compatibility** before deployment
2. **Use absolute paths** for file operations
3. **Include error handling** and output redirection
4. **Restart HA** to register new commands

### **Network Monitoring**
1. **SpeedTest frequency**: Balance accuracy vs resource usage
2. **Ping targets**: Include router, internet, and critical devices
3. **Performance baselines**: Document normal vs degraded performance
4. **IPv6 optimization**: Maintain enabled for best performance

**Last Updated**: 2025-10-27 - Entity fixes and BusyBox compatibility