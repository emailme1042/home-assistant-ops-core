# Fallback Automation Best Practices
*Created: 2025-10-28 | Multi-AI Collaboration Project*

## 🎯 Purpose
Ensure Home Assistant system resilience when primary automations fail or encounter network/hardware issues.

## 🔧 Implementation Patterns

### **Trigger Conditions for Fallback Activation**
- Primary automation fails to execute within expected timeframe
- Entity state remains unchanged beyond expected window (use `for:` condition)
- Network connectivity timeout detected (ping sensors, API calls)
- Hardware sensor becomes unavailable or unresponsive

### **Recommended Fallback Actions**
1. **Activate Secondary Logic**: Use alternate entities or services with reduced scope
2. **Event Logging**: Record failure with timestamp and session ID for debugging
3. **User Notification**: Alert via persistent notification or dashboard tile
4. **Graceful Degradation**: Maintain core functionality with minimal features

### **BusyBox-Safe Shell Commands (HA Green Compatible)**
```yaml
# ✅ SAFE: Basic connectivity test
shell_command:
  safe_ping: 'ping -c 2 8.8.8.8 || echo "Network unavailable"'
  
# ✅ SAFE: Simple interface check  
  interface_status: 'ip addr show | head -10'
  
# ✅ SAFE: DNS resolution test
  dns_test: 'nslookup google.com || echo "DNS resolution failed"'

# ❌ AVOID: Complex timeout commands
# timeout_ping: 'timeout 5 ping -c 4 192.168.1.1'  # timeout may not exist

# ❌ AVOID: Advanced networking tools
# traceroute_test: 'traceroute 8.8.8.8'  # traceroute may not be available
```

### **Network Fallback Patterns**

#### **IPv6 to IPv4 Fallback**
```yaml
automation:
  - alias: Network Protocol Fallback
    trigger:
      - platform: state
        entity_id: binary_sensor.ipv6_connectivity
        to: 'off'
        for:
          minutes: 5
    action:
      - service: shell_command.test_ipv4_connectivity
      - condition: state
        entity_id: binary_sensor.ipv4_connectivity  
        state: 'on'
      - service: notify.persistent_notification
        data:
          title: "Network Fallback Activated"
          message: "Switched to IPv4 due to IPv6 connectivity issues"
```

#### **API Service Fallback**
```yaml
automation:
  - alias: API Service Fallback
    trigger:
      - platform: state
        entity_id: sensor.openai_api_status
        to: 'unavailable'
        for:
          minutes: 2
    action:
      - service: input_text.set_value
        target:
          entity_id: input_text.fallback_mode
        data:
          value: "local_processing"
      - service: script.activate_offline_mode
```

### **Entity Fallback Strategy**
```yaml
# Primary automation with built-in fallback
automation:
  - alias: Motion Light with Fallback
    trigger:
      - platform: state
        entity_id: binary_sensor.office_motion
        to: 'on'
    action:
      - choose:
          # Primary: Smart light with scene
          - conditions:
              - condition: state
                entity_id: light.office_smart_bulb
                state: 'available'
            sequence:
              - service: scene.turn_on
                target:
                  entity_id: scene.office_work_mode
        # Fallback: Basic light toggle
        default:
          - service: light.turn_on
            target:
              entity_id: light.office_basic_light
            data:
              brightness: 180
```

## 🏷️ **Tagging & Monitoring**

### **Session Tags for Multi-AI Tracking**
```yaml
tags:
  - fallback_automation
  - multi_ai_project
  - session_2025_10_28
  - resilience_pattern
```

### **Status Entities for Dashboard Monitoring**
```yaml
# Template sensors to track fallback status
template:
  - sensor:
      - name: "Fallback Mode Status"
        state: >
          {% if states('input_text.fallback_mode') == 'active' %}
            Fallback Active
          {% else %}
            Normal Operation
          {% endif %}
        icon: >
          {% if states('input_text.fallback_mode') == 'active' %}
            mdi:alert-circle
          {% else %}
            mdi:check-circle
          {% endif %}
```

## 📊 **Dashboard Integration**

### **Fallback Status Card**
```yaml
type: entities
title: System Resilience Status
entities:
  - sensor.fallback_mode_status
  - binary_sensor.network_connectivity
  - sensor.api_service_status
  - input_text.last_fallback_trigger
show_header_toggle: false
```

## 🔄 **Testing & Validation**

### **Fallback Test Automation**
```yaml
automation:
  - alias: Monthly Fallback Test
    trigger:
      - platform: time
        at: '02:00:00'
      - platform: event
        event_type: call_service
        event_data:
          domain: script
          service: test_fallback_systems
    action:
      - service: script.simulate_network_failure
      - delay: '00:02:00'
      - service: script.restore_network_connectivity
      - service: notify.alexa_media_lounge_alexa
        data:
          message: "Fallback system test completed successfully"
```

---

## 🎯 **Implementation Checklist**

- [ ] **Identify Critical Automations**: List automations that need fallback logic
- [ ] **Define Fallback Triggers**: Set appropriate timeout and failure conditions  
- [ ] **Create Fallback Actions**: Design reduced-scope alternatives
- [ ] **Add Status Monitoring**: Create entities to track fallback activation
- [ ] **Dashboard Integration**: Add fallback status to system overview
- [ ] **Test Regularly**: Schedule periodic fallback system validation

---

*This documentation supports the Multi-AI Collaboration Project (2025-10-28)*  
*Contributors: Smart Home Ops Assistant, Edge Copilot, GitHub Copilot*