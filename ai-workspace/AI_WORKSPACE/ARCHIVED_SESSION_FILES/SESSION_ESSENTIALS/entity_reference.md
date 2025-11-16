# Entity List Reference for GPT

**Generated**: 2025-10-27  
**Source**: Home Assistant Entity Registry  
**Purpose**: Quick reference for entity cleanup and dashboard work

## 🏠 **Key Working Entities (Verified)**

### **Alexa/Media**
- `media_player.lounge_alexa` ✅ Working (TTS target)
- `media_player.office_speaker` ✅ Exists

### **Lights**
- `light.office` ✅ Working (office automation)
- `light.lounge` ✅ Working (front door automation)

### **Motion/Binary Sensors**
- `binary_sensor.office_motion` ✅ Fixed entity name
- `binary_sensor.front_door_contact` ✅ Exists
- `binary_sensor.192_168_1_1` ✅ Network ping sensor

### **Input Controls**
- `input_boolean.test_voice_openai` ✅ Created for testing
- `input_boolean.debug_mode` ✅ Exists
- `input_text.openai_query` ✅ OpenAI integration
- `input_text.openai_response` ✅ OpenAI integration

### **System Monitoring (Created Today)**
- `sensor.system_health_status` 🆕 CPU/memory/disk aggregate
- `sensor.yaml_validation_status` 🆕 YAML validation tracking  
- `sensor.mqtt_watch_status` 🆕 MQTT watchdog status
- `binary_sensor.mqtt_connection` 🆕 MQTT connectivity
- `sensor.network_latency` 🆕 Network ping monitoring

### **SpeedTest (Template Sensors)**
- `sensor.speedtest_download` 🆕 Template sensor
- `sensor.speedtest_upload` 🆕 Template sensor  
- `sensor.speedtest_ping` 🆕 Template sensor

### **Test Controls (Created Today)**
- `switch.openai_voice_test` 🆕 Manual OpenAI test trigger
- `switch.system_validation_toggle` 🆕 Manual YAML validation

## 📊 **Entity Count Summary**
- **Total Entities**: ~2577 (from HA startup log)
- **Created Today**: 8 new entities for monitoring/testing
- **Fixed Today**: Office motion entity reference corrected

## 🔍 **How to Get Full Entity List**

**Via HA UI**: Developer Tools → States → View all entities  
**Via File**: `.storage/core.entity_registry` (JSON format)  
**Via API**: `GET /api/states` endpoint

## ⚠️ **Known Missing/Placeholder Entities**
- `sensor.gpt_status` - Referenced in SYSTEM_OVERVIEW but not created
- `sensor.device_map_status` - Referenced but may not exist
- Various `sensor.dashboard_*` entities - May be placeholders

---
**Note**: This is a working reference. For complete entity audit, use HA Developer Tools or entity registry file.