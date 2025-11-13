# ⚙️ Automation Patterns — Reusable Templates

## 🤖 GPT Integration Patterns

### Basic GPT Query Pattern
```yaml
- alias: "GPT Query Template"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.gpt_prompt_input
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 5 }}"
  action:
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_status_flag
        value: "Processing..."
    - service: rest_command.ask_openai
      data:
        prompt: "{{ states('input_text.gpt_prompt_input') }}"
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_status_flag
        value: "Complete"
```

### GPT Status Tracking Pattern
```yaml
- alias: "GPT Status Monitor"
  trigger:
    - platform: state
      entity_id: input_text.gpt_result_core
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 5 }}"
  action:
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_status_flag
      data:
        value: "Reply Ready"
```

## 🏠 Motion-Based Automation

### Motion Light Control
```yaml
- alias: "Motion Light Template"
  trigger:
    - platform: state
      entity_id: binary_sensor.ROOM_motion
      to: "on"
  condition:
    - condition: numeric_state
      entity_id: sensor.ROOM_lux
      below: 50
  action:
    - service: light.turn_on
      target:
        entity_id: light.ROOM_main
      data:
        brightness_pct: 80
        transition: 1
```

### Motion Timeout Pattern
```yaml
- alias: "Motion Timeout Template"
  trigger:
    - platform: state
      entity_id: binary_sensor.ROOM_motion
      to: "off"
      for: "00:05:00"
  action:
    - service: light.turn_off
      target:
        entity_id: light.ROOM_main
      data:
        transition: 5
```

## 📊 Validation & Monitoring

### YAML Validation Automation
```yaml
- alias: "YAML Validation Runner"
  trigger:
    - platform: time_pattern
      minutes: "/30"
    - platform: homeassistant
      event: start
  action:
    - service: shell_command.validate_yaml
    - delay: "00:00:05"
    - service: script.process_validation_results
```

### Entity Health Check
```yaml
- alias: "Entity Health Monitor"
  trigger:
    - platform: time_pattern
      hours: "/6"
  action:
    - service: script.run_watchman_scan
    - service: python_script.entity_audit
    - service: notify.admin
      data:
        message: "Entity health check complete"
```

## 🎵 TTS & Notification Patterns

### Alexa TTS Template
```yaml
- alias: "Alexa Announcement Template"
  action:
    - service: notify.alexa_media_DEVICE_NAME
      data:
        message: "{{ announcement_text }}"
        data:
          type: tts
          method: all
```

### Conditional Notification
```yaml
- alias: "Smart Notification Template"
  condition:
    - condition: time
      after: "07:00:00"
      before: "22:00:00"
    - condition: state
      entity_id: input_boolean.notifications_enabled
      state: "on"
  action:
    - service: notify.NOTIFICATION_SERVICE
      data:
        message: "{{ notification_message }}"
```

## 🔄 State Management Patterns

### Input Helper Reset
```yaml
- alias: "Input Reset Template"
  trigger:
    - platform: state
      entity_id: input_text.HELPER_NAME
      to: ""
      for: "00:00:01"
  action:
    - service: python_script.process_input
      data:
        input_value: "{{ trigger.from_state.state }}"
    - service: input_text.set_value
      target:
        entity_id: input_text.HELPER_NAME
      data:
        value: ""
```

### Toggle State Synchronization
```yaml
- alias: "State Sync Template"
  trigger:
    - platform: state
      entity_id: input_boolean.MASTER_TOGGLE
  action:
    - service: input_boolean.turn_{{ trigger.to_state.state }}
      target:
        entity_id: 
          - input_boolean.DEPENDENT_1
          - input_boolean.DEPENDENT_2
```

## 🌦️ Weather-Based Automation

### Rain Detection Pattern
```yaml
- alias: "Rain Response Template"
  trigger:
    - platform: numeric_state
      entity_id: sensor.precipitation
      above: 0.5
  action:
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.irrigation_override
    - service: script.close_garden_covers
```

### Temperature Response
```yaml
- alias: "Temperature Control Template"
  trigger:
    - platform: numeric_state
      entity_id: sensor.ROOM_temperature
      below: 18
  action:
    - service: climate.set_temperature
      target:
        entity_id: climate.ROOM_thermostat
      data:
        temperature: 21
```

## 🔧 System Maintenance Patterns

### Backup Automation
```yaml
- alias: "Auto Backup Template"
  trigger:
    - platform: time
      at: "03:00:00"
  condition:
    - condition: time
      weekday:
        - sun
        - wed
  action:
    - service: hassio.backup_full
      data:
        name: "Auto Backup {{ now().strftime('%Y-%m-%d') }}"
```

### Log Cleanup Pattern
```yaml
- alias: "Log Rotation Template"
  trigger:
    - platform: time
      at: "04:00:00"
  action:
    - service: shell_command.cleanup_logs
    - service: python_script.archive_old_files
```

## 🎮 Interactive Dashboard Patterns

### Dashboard Navigation
```yaml
- alias: "Dashboard Nav Template"
  trigger:
    - platform: state
      entity_id: input_select.dashboard_selection
  action:
    - service: script.show_dashboard
      data:
        dashboard_id: "{{ states('input_select.dashboard_selection') }}"
```

### Dynamic Content Loading
```yaml
- alias: "Content Loader Template"
  trigger:
    - platform: state
      entity_id: input_boolean.load_CONTENT_TYPE
      to: "on"
  action:
    - service: python_script.load_dynamic_content
      data:
        content_type: "CONTENT_TYPE"
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.load_CONTENT_TYPE
```

## 📱 Device Integration Patterns

### Device Status Monitoring
```yaml
- alias: "Device Monitor Template"
  trigger:
    - platform: state
      entity_id: DEVICE_ENTITY
      to: "unavailable"
      for: "00:05:00"
  action:
    - service: notify.admin
      data:
        message: "Device DEVICE_NAME is offline"
    - service: script.attempt_device_recovery
```

### Multi-Device Control
```yaml
- alias: "Device Group Template"
  trigger:
    - platform: state
      entity_id: input_boolean.ROOM_all_lights
  action:
    - service: light.turn_{{ trigger.to_state.state }}
      target:
        entity_id:
          - light.ROOM_main
          - light.ROOM_accent
          - light.ROOM_task
```

---

**Usage Notes**:
- Replace UPPERCASE placeholders with actual entity names
- Adjust timing values for specific needs
- Test patterns in isolation before integration
- Use templates for consistent automation structure

**Last Updated**: 2025-10-26  
**Pattern Count**: 15+ reusable templates  
**Testing Status**: All patterns validated in development