# 🧹 **MQTT Recovery Checklist** — GitHub-Ready

**Repository:** home-assistant-ops-core  
**Branch:** main  
**Date:** January 7, 2026  
**Operator:** ⚙️ GitHub Copilot (VSCode)  
**Session Owner:** 👤 Jamie  

---

## 🎯 **Mission Objective**
Complete MQTT broker recovery after Mosquitto restart, eliminating ghost clients, protocol errors, and unavailable entities while maintaining Govee2MQTT and HA connectivity.

## 📊 **Pre-Recovery Status**
- **Mosquitto Status:** ✅ Running (v2.0.22)
- **Connected Clients:** ✅ `govee2mqtt`, `homeassistant`
- **Unavailable Entities:** ⚠️ 1,655/3,818 (43.3%)
- **Ghost Issues:** ⚠️ `Client <unknown>` from `172.30.32.2` and `::1`
- **Retained Topics:** ⚠️ Stale Z2M topics present
- **Z2M Entities:** ⚠️ Still present in HA

## ✅ **Recovery Steps**

### **Phase 1: Ghost Client Identification**
- [ ] **Access HA Developer Tools:** Settings → Developer Tools → States
- [ ] **Filter MQTT Entities:** Search `mqtt` in entity filter
- [ ] **Document Ghost Entities:**
  - `zigbee2mqtt_bridge_*`
  - `mqtt_sensor_stale_alert_*`
  - `mqtt_connection_watchdog`
  - `restart_zigbee2mqtt_if_mesh_fails`
  - `clear_stale_mqtt_topics`
- [ ] **Log Count:** _____ ghost entities identified

### **Phase 2: Retained Topic Cleanup**
- [ ] **Install MQTT Explorer:** (if not available)
- [ ] **Connect to Mosquitto:** Host: `core-mosquitto`, Port: `1883`, User: `homeassistant`
- [ ] **Browse Topics:** Navigate to retained topics
- [ ] **Delete Stale Topics:**
  - `zigbee2mqtt/`
  - `homeassistant/sensor/zigbee2mqtt_*`
  - `bridge/state`
  - `bridge/config`
- [ ] **Confirm Deletion:** Topics removed from broker

### **Phase 3: Entity Removal**
- [ ] **Access MQTT Integration:** Settings → Devices & Services → MQTT → Configure
- [ ] **Delete Ghost Devices:**
  - Any Z2M devices
  - Ghosted SONOFF sensors
  - Bridge entities
  - Stale automations referencing MQTT topics
- [ ] **Verify Removal:** Entities no longer appear in States

### **Phase 4: HA Restart**
- [ ] **Pre-Restart Validation:** Run `python3 /config/scripts/validate_yaml.py /config`
- [ ] **Restart HA:** Settings → System → Restart Home Assistant
- [ ] **Wait:** 2-3 minutes for full startup
- [ ] **Check Logs:** Confirm only valid clients in MQTT logs

### **Phase 5: Post-Restart Validation**
- [ ] **Entity Count Check:** Developer Tools → States → Total entities
- [ ] **Unavailable Count:** Compare before/after
- [ ] **MQTT Logs:** Check for ghost client errors
- [ ] **Client Connections:** Verify `govee2mqtt` and `homeassistant` connected
- [ ] **Govee Functionality:** Test Govee device control

## 📈 **Success Metrics**

| Metric | Pre-Recovery | Target | Post-Recovery |
|--------|-------------|--------|---------------|
| Total Entities | 3,818 | 3,818 | _____ |
| Unavailable Entities | 1,655 | <200 | _____ |
| MQTT Clients | 2 valid + ghosts | 2 valid only | _____ |
| Ghost Errors | Present | None | _____ |
| Z2M Entities | Present | None | _____ |

## 🔍 **Troubleshooting**

### **If 172.30.32.2 Keeps Reconnecting:**
- Check Supervisor container logs: `ha supervisor logs`
- Review add-ons using MQTT (Ring MQTT, watchdogs)
- Inspect automations restarting Z2M or monitoring MQTT health

### **If Entities Remain Unavailable:**
- Verify Mosquitto add-on is running
- Check MQTT integration configuration
- Restart affected containers (ESPHOME, etc.)

### **If Protocol Errors Persist:**
- Review MQTT client configurations
- Check username/password settings
- Verify TLS/PSK settings if used

## 📝 **Documentation Updates Required**

### **system_status.md**
```markdown
## MQTT Recovery Status
- **Recovery Completed:** [Date]
- **Ghost Entities Removed:** [Count]
- **Unavailable Entities Reduced:** [Before] → [After]
- **Mosquitto Status:** Stable
- **Connected Clients:** govee2mqtt, homeassistant
```

### **recent_changes.md**
```markdown
## MQTT Broker Recovery — COMPLETED
- Ghost clients eliminated
- Retained topics cleared
- Z2M entities removed
- HA restart successful
- Entity availability improved: [Metrics]
```

### **multi_hub_architecture_diagram.md**
- Update MQTT scope: Govee devices only
- Confirm no Z2M references
- Document recovery completion

## 🏆 **Completion Checklist**
- [ ] Phase 1: Ghost identification complete
- [ ] Phase 2: Retained topics cleared
- [ ] Phase 3: Entities removed
- [ ] Phase 4: HA restart successful
- [ ] Phase 5: Validation passed
- [ ] Documentation updated
- [ ] Metrics logged

## 📎 **Related Files**
- `configuration.yaml` - MQTT integration config
- `includes/sensors/mqtt_*` - MQTT sensor definitions
- `includes/automations/mqtt_*` - MQTT-related automations
- `AI_WORKSPACE/copilot_session_notes.md` - Recovery log entry

---

**Next Action:** Begin Phase 1 ghost client identification in HA UI.