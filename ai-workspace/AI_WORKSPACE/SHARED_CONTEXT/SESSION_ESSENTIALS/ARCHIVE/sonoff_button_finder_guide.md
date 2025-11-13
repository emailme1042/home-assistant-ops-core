# 🔘 **SONOFF ZIGBEE BUTTON FINDER**

Since you mentioned it's a **Sonoff Zigbee button** (not Aqara), let me help you find it using these methods:

## 🔍 **METHOD 1: Developer Tools → States**
1. Go to **Settings → Developer Tools → States** 
2. **Search for any of these patterns:**
   - `sensor.` (look for action sensors)
   - `event.` (button press events)
   - Any entity containing "button", "switch", "action", "click"
3. **Press your Sonoff button** and see which entity updates

## 🔍 **METHOD 2: Check MQTT/Zigbee2MQTT**
If using Zigbee2MQTT:
1. Go to **Zigbee2MQTT web interface** (usually port 8080)
2. Look for your Sonoff device in device list
3. Note the IEEE address (like `0x...`) 
4. **Press the button** and see what messages appear

## 🔍 **METHOD 3: Look for These Common Sonoff Button Entity Patterns:**
- `sensor.sonoff_button_action` 
- `sensor.0x[hex_address]_action`
- `event.sonoff_button_press`
- `binary_sensor.sonoff_button`

## 🔍 **METHOD 4: Search by Model**
What's the **exact Sonoff model**? (e.g., SNZB-01, SNZB-01P, etc.)
- **SNZB-01**: Usually creates `sensor.[name]_action` 
- **SNZB-01P**: Usually creates `sensor.[name]_action` with single/double/long press

## 🧪 **METHOD 5: Quick Test with Updated Debug Automation**

Let me update the debug automation to catch **any recently changed entity**:

```yaml
# This will announce ANY entity that changes when you press your button
automation:
  - alias: "Debug - Find ANY Button Press"
    trigger:
      - platform: event
        event_type: state_changed
    condition:
      - condition: template
        value_template: "{{ now() - trigger.event.data.new_state.last_changed < timedelta(seconds=2) }}"
    action:
      - service: tts.google_say
        data:
          message: "Entity changed: {{ trigger.event.data.entity_id }}"
```

## 📝 **WHAT TO DO NEXT:**
1. **Try Method 1 first** (Developer Tools → States)
2. **Press your Sonoff button** 
3. **Look for any entity that changes/updates**
4. **Tell me the entity name** you find
5. **I'll update the downstairs automation** with the correct trigger

**Most likely it will be something like:**
- `sensor.sonoff_button_action` 
- `sensor.0x[something]_action`
- `event.[something]_press`

**Once you find it, let me know and I'll fix the automation immediately!**