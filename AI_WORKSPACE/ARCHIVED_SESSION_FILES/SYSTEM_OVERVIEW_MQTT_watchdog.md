# SYSTEM_OVERVIEW — MQTT Sensors & Watchdog Scaffold

This scaffold outlines MQTT sensor monitoring and a simple watchdog automation to mark stale sensors.

## Monitored MQTT sensors
- mqtt.sensor.motion_lounge
- mqtt.sensor.temperature_hall
- mqtt.sensor.door_front

## Watchdog logic (concept)
- A template sensor `sensor.mqtt_last_message_age_<name>` computes seconds since last message.
- An automation triggers when age > threshold (e.g., 3600s) and writes a `binary_sensor.mqtt_<name>_stale` or sends notification.

Example `template` snippet to include in `includes/sensors/`:

```yaml
- platform: template
  sensors:
    mqtt_last_message_age_motion_lounge:
      friendly_name: "MQTT Last Message Age - Motion Lounge"
      value_template: "{{ (as_timestamp(now()) - as_timestamp(states.sensor.motion_lounge.last_changed)) | int }}"
      unit_of_measurement: seconds
```

Example automation (place in `includes/automations/`):

```yaml
- alias: MQTT Sensor Stale Alert - Motion Lounge
  trigger:
    - platform: numeric_state
      entity_id: sensor.mqtt_last_message_age_motion_lounge
      above: 3600
  action:
    - service: notify.admin
      data:
        message: "Motion Lounge MQTT sensor stale (>1h)"
```

Notes:
- Add sensors to dashboards `dashboards/SYSTEM_OVERVIEW/` after validation.
- Consider rate-limiting notifications and auto-archive old alerts.
