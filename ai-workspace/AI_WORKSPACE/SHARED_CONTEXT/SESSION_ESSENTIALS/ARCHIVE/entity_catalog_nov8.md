## 🧭 Entity Catalog Sync — Status Snapshot (2025-11-07 23:45)

### FROM:
- Catalog included entities removed during dashboard purge
- Ghost devices and unavailable entities present
- MQTT device states not validated

### TO:
- Entity catalog now reflects only active, restart-safe entities
- Ghost devices suppressed and flagged for review
- MQTT device recovery validated and logged

### TODO:
- ✅ Timestamp entity removals and catalog updates
- 🧪 Validate MQTT device health and sync
- 🔄 Review ghost device suppression and update catalog as needed
# 🧠 Entity Catalog — System Reference

This file lists all expected entities, grouped by room, device, and feature for easy tracking and recovery.

---

| Room      | Device/Feature         | Entity ID                        | Domain         | Purpose/Role                | Status        | Notes                |
|-----------|------------------------|----------------------------------|---------------|-----------------------------|---------------|----------------------|
| Lounge    | Temperature Sensor     | sensor.lounge_temperature        | sensor        | Room temperature            | ✅ Available  |                      |
| Lounge    | Main Light             | light.lounge_main                | light         | Main ceiling light          | ✅ Available  |                      |
| Lounge    | Media Player           | media_player.lounge_alexa        | media_player  | Alexa voice assistant       | ✅ Available  |                      |
| Bedroom   | Lamp                   | light.bedroom_lamp               | light         | Bedside lamp                | ✅ Available  |                      |
| Bedroom   | Temperature Sensor     | sensor.bedroom_temperature       | sensor        | Room temperature            | ✅ Available  |                      |
| Kitchen   | Window Sensor          | binary_sensor.kitchen_window     | binary_sensor | Window open/close status    | ❌ Missing    | Needs restore        |
| Kitchen   | Main Light             | light.kitchen_main               | light         | Main ceiling light          | ✅ Available  |                      |
| Bathroom  | Humidity Sensor        | sensor.bathroom_humidity         | sensor        | Humidity monitoring         | ✅ Available  |                      |
| Bathroom  | Light                  | light.bathroom_main              | light         | Main bathroom light         | ✅ Available  |                      |
| Garden    | Pump Switch            | switch.garden_pump               | switch        | Water pump control          | ❌ Missing    | Needs restore        |
| Hall      | Motion Sensor          | binary_sensor.hall_motion        | binary_sensor | Hallway motion detection    | ✅ Available  |                      |
| Office    | Desk Lamp              | light.office_desk_lamp           | light         | Desk lamp                   | ✅ Available  |                      |
| Office    | Temperature Sensor     | sensor.office_temperature        | sensor        | Room temperature            | ✅ Available  |                      |
| Front Door| Door Contact           | binary_sensor.door_contact       | binary_sensor | Door open/close status      | ✅ Available  |                      |
| Global    | Night Shutdown         | automation.night_shutdown        | automation    | Night shutdown sequence     | ❌ Unavailable| Check config         |
| Global    | Boiler Running Status  | input_boolean.boiler_running_status | input_boolean | Boiler status           | ✅ Available  |                      |
| Global    | Boiler Cycles Today    | counter.boiler_cycles_today      | counter       | Boiler cycle count          | ✅ Available  |                      |
| Global    | System Health Score    | sensor.ai_system_health_score    | sensor        | AI system health            | ✅ Available  |                      |
| Global    | Validation Passed      | input_boolean.validation_passed  | input_boolean | Config validation status    | ✅ Available  |                      |
| ...       | ...                    | ...                              | ...           | ...                         | ...           | ...                  |

---

## How to Use

- Add all expected entities to this table, grouped by room and device/feature.
- Mark status as ✅ Available, ❌ Missing, ❌ Unavailable, or ⚠️ Error.
- Add notes for recovery, troubleshooting, or migration.
- Use this as your master reference for entity health and recovery.
