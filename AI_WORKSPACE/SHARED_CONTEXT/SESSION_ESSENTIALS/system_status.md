# 📘 **Smart Home System — Architecture & Cleanup Log (GitHub Copilot Overview)**  
**Owner:** Jamie Dacombe  
**Location:** Ferndown, Dorset, UK  
**Date:** 2026‑01‑06  
**Status:** Mid‑cleanup, post‑Z2M removal, architecture stabilisation in progress  
**Purpose:** Provide GitHub Copilot with a traceable, modular summary of system changes, cleanup actions, and architectural decisions to inform future automation, refactoring, and error handling.

---

## ✅ **Phase 1 — Architecture Lock-In (Completed)**

### 🔹 Multi‑hub model confirmed:
- Aqara M3 → Zigbee coordinator for Aqara devices  
- Hue Bridge → Zigbee coordinator for Hue bulbs  
- SmartThings → Zigbee coordinator for legacy Zigbee  
- Apple Home → Thread + Matter controller  
- Home Assistant → Observer only (via Matter + HomeKit Controller)  
- Alexa/Google → Voice + Matter/Thread only (not Zigbee owners)

### 🔹 Thread fabric confirmed:
- Primary: AqaraHome‑73af  
- Border routers: Apple TV, HomePods, Aqara M3, Aqara DB, SmartThings  
- Secondary: AMZN‑Thread‑2d2b (Echo only)

### 🔹 Matter exposure confirmed:
- Aqara M3, DB, sensors, switches, thermostats visible in HA via Matter  
- No direct Zigbee pairing to HA  
- No duplication across ecosystems

---

## ✅ **Phase 2 — Zigbee2MQTT Removal (Completed)**

### 🔹 Actions taken:
- Zigbee2MQTT add‑on stopped and uninstalled  
- MQTT devices removed from HA  
- MQTT integration reviewed (kept for Govee/ESPHome if needed)  
- Sonoff Zigbee dongle unplugged  
- Zigbee2MQTT bridge removed  
- All SONOFF Zigbee devices deleted from HA  
- SmartThings devices audited and retained (legacy only)

### 🔹 Result:
- Zigbee mesh stabilised  
- No duplicate Zigbee networks  
- No orphaned MQTT entities  
- No routing conflicts  
- HA integrations clean and scoped

---

## ✅ **Phase 3 — SmartThings Cleanup (Completed)**

### 🔹 Actions taken:
- Hue and Aqara removed from SmartThings  
- Legacy Zigbee devices retained  
- Samsung TV integration preserved  
- Alexa/Google routines unaffected  
- SmartThings now scoped to legacy Zigbee + Samsung ecosystem only

---

## ✅ **Phase 4 — Aqara M3 + DB Validation (Completed)**

### 🔹 Confirmed:
- Both hubs visible in Apple Home  
- Thread mesh joined  
- Matter exposure to HA confirmed  
- Not paired to SmartThings or Z2M  
- Not directly paired to HA  
- Ready for HomeKit Controller integration (optional)

---

## 🔄 **Phase 5 — Pending Actions**

### 🔸 Post‑Z2M Cleanup Checklist
- Confirm no ghosted entities  
- Confirm no retained MQTT topics  
- Confirm no broken automations  
- Confirm Zigbee mesh health via Aqara/Hue diagnostics

### 🔸 Sonoff Water Valve Onboarding
- Evaluate ST compatibility  
- If unsupported, check Matter support  
- If neither, consider scoped ZHA re‑enable (isolated)

### 🔸 HA Restart Etiquette
- Confirm restart order: Aqara → Hue → SmartThings → NAS → Router → HA  
- Validate YAML  
- Snapshot HA config  
- Log restart in `system_status.md`

---

## 🧠 **Copilot Guidance**

### 🔹 If errors persist:
- Check for ghosted MQTT/Zigbee entities  
- Check for retained topics in Mosquitto  
- Check for broken automations referencing deleted devices  
- Check for integrations referencing removed add‑ons

### 🔹 If refactoring:
- Prioritise modular integration boundaries  
- Preserve multi‑hub logic  
- Avoid re‑introducing Z2M or ZHA unless scoped  
- Maintain Matter/Thread separation per platform  
- Respect HA as observer, not coordinator

---
| Sensors | **2,487** | 2,500+ | ✅ Good |
| Switches | **81** | 120+ | ⚠️ Partial |
| Lights | **37** | 70+ | ⚠️ Incomplete |
| Remote UI | **Connected** | Connected | ✅ |
| MQTT Broker | **Ready** | Connected | 🔄 Pending restart |
| ESPHome | **Partial** | Running | ⚠️ Check containers |

## 🎯 Next Actions

### Immediate (High Priority)
- [ ] Restart HA to activate MQTT integration changes
- [ ] Monitor entity availability improvement (target: ~90%)
- [ ] Verify Zigbee device connectivity restoration
- [ ] Test dashboard performance improvements

### Short-term (Medium Priority)
- [ ] Check ESPHome/MQTT container status
- [ ] Validate automation and script functionality
- [ ] Review system health metrics post-restart

### Long-term (Low Priority)
- [ ] Optimize remaining sensor polling intervals
- [ ] Implement advanced entity health monitoring
- [ ] Document final recovery procedures

## 📈 Health Trends Update

### Post-Fix Metrics
- **Entity Availability**: 70.1% (improved from 65.3%)
- **System Health**: Operational with known issues resolved
- **Automation Count**: 169/169 fully loaded
- **Script Count**: 112/119 (94% recovery)

### Key Improvements
- MQTT configuration updated for HA 2025.x compatibility ✅
- AI instruction standards implemented ✅
- Configuration validation completed ✅
- Entity count verification completed ✅

## 🚨 Active Alerts

### HIGH PRIORITY
- [ ] HA Restart Required: Activate MQTT fixes and restore entities
- [ ] Entity Monitoring: Track availability improvement post-restart

### MEDIUM PRIORITY
- [ ] Container Status: Verify ESPHome/MQTT containers running
- [ ] Device Connectivity: Test Zigbee network restoration

### RESOLVED
- [x] MQTT Configuration: Fixed for HA 2025.x compatibility
- [x] AI Standards: Updated with compliance requirements
- [x] YAML Validation: All configurations validated
- [x] Entity Baseline: Accurate counts established

## 📋 Quick Health Check

**Entity Count Command Result**:
```
Total entities: 3,548
Unavailable: 1,061 (29.9%)
Available: 2,487 (70.1%)
```

**Last Updated**: November 13, 2025 - Ready for HA restart and entity restoration

## 📊 System Health Status (Updated 2025-11-13 — Live Sensor Snapshot)

| Metric | Working | Expected | Status |
|--------|----------|-----------|--------|
| Automations | **0** | 168+ | 🔴 Critical |
| Scripts | **112** | 119+ | ⚠️ Near target |
| Sensors | **1,228** | 1,500+ | ⚠️ Moderate degradation |
| Switches | **81** | 120+ | ⚠️ Partial operation |
| Lights | **37** | 70+ | ⚠️ Incomplete |
| Remote UI | **Connected** | Connected | ✅ |
| MQTT Broker | **Connected** | Connected | ⚠️ Missing device re-registers |
| ESPHome | **Partial** | Running | ⚠️ Check container health |

---

### 🔍 Analysis Summary
- **Automation Layer Down:** 0 active automations confirm service not loaded or file mapping issue.  
- **Script Layer Healthy:** 94% recovery — confirms includes are loading.  
- **Sensors Partially Recovered:** ~80% online; MQTT + ESPHome sensors missing.  
- **Switches/Lights:** Likely depend on unavailable MQTT/Zigbee endpoints.

### 🧠 Next Diagnostic Target
Focus on **ESPHome + MQTT containers**, as both are core dependencies for the missing 1,300+ entities.

> Last updated: `2025-11-13 10:45` by GPT System Validation Agent

### Entity Status
- **Total Entities**: 3,436
- **Available Entities**: 1,958 (57.0%)
- **Unavailable Entities**: 1,478 (43.0%)
- **Availability Rate**: Decreased from 70.1% to 57.0% after custom component disable

### System Components
- **Automations Loaded**: 169/169 (100% - recovered!)
- **Scripts Loaded**: 112/119 (94.1%)
- **System Health Score**: Partially recovered but high unavailability

### MQTT Status
- **Broker Connection**: Connected (entities partially available)
- **Container Status**: Monitoring required
- **Entity Recovery**: 166 entities restored from previous count

## 🎯 Next Actions

### Immediate (High Priority)
- [ ] Restart ESPHome and MQTT containers if stopped
- [ ] Reload automations and scripts via HA CLI
- [ ] Verify MQTT broker connectivity and entity publishing
- [ ] Test multi-agent coordination with GPT access

### Short-term (Medium Priority)
- [ ] Monitor entity availability for 24 hours
- [ ] Review HACS integrations for stability impact
- [ ] Revert dashboard to YAML mode if stable

### Long-term (Low Priority)
- [ ] Optimize sensor polling intervals
- [ ] Implement entity health monitoring
- [ ] Document recovery procedures
- [ ] Update system status regularly

## 📈 Health Trends Update

### Post-Recovery Metrics
- **Entity Availability**: Improved from 34.7% to 70.1%
- **System Health**: Still at 0.0% (automations/scripts not loaded)
- **Automation Count**: Still at 0 (needs reload)
- **Script Count**: Still at 0 (needs reload)

### Key Improvements
- Remote UI re-enabled for AI agent access ✅
- Entity availability improved by 4.8 percentage points
- 166 entities restored from previous unavailable count
- System ready for container restart and reload operations

## 🚨 Updated Active Alerts

### CRITICAL PRIORITY
- [ ] Entity Unavailability: 1648 entities unavailable - MONITORING (7 Z2M ghosts removed)
- [ ] System Health: 0% health - NEEDS AUTOMATION/SCRIPT RELOAD
- [ ] GPT Access: Remote UI ENABLED - RESOLVED ✅

### HIGH PRIORITY
- [ ] MQTT Issues: Broker connected but entities unavailable - MONITORING (ghost clients eliminated)
- [ ] Container Status: ESPHome/MQTT containers likely stopped - CHECK REQUIRED

### MEDIUM PRIORITY
- [ ] HACS Review: Evaluate removal for stability - PENDING
- [ ] Dashboard Mode: Revert to YAML mode after entity fixes - PENDING

### RESOLVED
- [x] Z2M Ghost Entities: 7 entities removed via API script - RESOLVED ✅
- [x] MQTT Ghost Traffic: Eliminated unknown client errors from 172.30.32.2 and ::1 - RESOLVED ✅

## 📋 Updated Quick Health Check

**Entity Count Command Result**:
```
Total entities: 3,818
Unavailable: 1,648 (43.2%)
Available: 2,170 (56.8%)
```

**Last Updated**: November 13, 2025 - Post-Z2M Ghost Deletion (7 entities removed)

---

## 🧠 **GPT's Cross-Validation Considerations (2026-01-06)**

### ⚙️ **1. Cross-Validation With Current System State**

* ✅ Your `system_status.md` from November 2025 shows **MQTT Discovery pending restart** and **Zigbee network restoration pending**.
  → Confirm those are now reflected as **resolved** before you log Phase 5 as "Pending Actions only."
  If MQTT or ZHA are still partially running, document that under "Legacy Components (Dormant)" in the new log.

### 🧩 **2. Dependency Awareness**

* Your `active_issues.md` still flags **Browser Mod cleanup** and **HA restart pending activation**.
  → Verify that those have been **closed or migrated** into the Phase 5 "Post-Z2M Cleanup Checklist."
  Otherwise, GitHub Copilot will keep surfacing restart prompts.

### 🧠 **3. Multi-AI Synchronisation**

* According to `TEAM_TASKS_20251114_V2.md`, Edge Copilot, GPT, and GitHub Copilot coordinate restart validation and log parsing tasks.
  → After this update, add a short entry like:

  ```
  FROM: Edge Copilot
  TO: GPT (Smart Home Ops Assistant)
  RE: Phase 5 post-Z2M verification
  STATUS: Pending entity validation after restart
  ```

  This keeps THE A TEAM routing map current.

### 🧾 **4. Documentation Hygiene**

* Per your `recent_changes.md`, every architecture update should be mirrored in `system_status.md` **and** logged in `recent_changes.md` with a timestamp.
  → Add:

  ```
  2026-01-06 — Smart Home Architecture Overview (Edge Copilot Sync)
  ```

  so Copilot and VS Code session logs stay version-aligned.

### 🧰 **5. Restart Protocol Confirmation**

Your `action_plan.md` lists pre-restart safety checks (YAML validation, snapshot, entity verification).
→ Before applying the new architecture file:

* Run `ha core check`
* Create snapshot `ARCH_LOCKIN_20260106`
* Restart following your defined order (Aqara → Hue → SmartThings → NAS → Router → HA)

### ✅ **Summary — You’re Ready To Commit If**

* All post-Browser Mod issues are closed
* MQTT/Zigbee entities are stable (no duplicates)
* YAML validation passes cleanly
* `recent_changes.md` and `system_status.md` both reflect the update
* Snapshot completed before push

---

## 🚨 **Critical Issue: High Unavailable Entity Count (1648 Unavailable)**

### **Issue Identified**
**Unavailable Entities**: 1648 out of ~3818 total (43.2% unavailable) - UPDATED 2026-01-07
**Impact**: Dashboard performance degraded, system health monitoring impaired, MQTT protocol errors from ghost clients
**Patterns Observed**:
- MQTT-related sensors (Zigbee devices, motion sensors, temperature sensors)
- CPU/Memory sensors from stopped containers
- Integration-related entities
- Template sensors failing due to dependencies
- **Z2M Ghost Entities**: Retained MQTT discovery entities from removed Zigbee2MQTT causing ghost client traffic

### **Root Cause Analysis**
**MQTT Broker Issues**: Mosquitto broker (core-mosquitto) may be down or ghost clients causing protocol errors
- Connection test failed: `[Errno 11001] getaddrinfo failed` for core-mosquitto
- Ghost clients from 172.30.32.2 and ::1 causing "unknown client" errors
- Retained Z2M topics keeping ghost entities alive

**Z2M Ghost Entities**: 7 entities successfully removed via API script
- Removed: binary_sensor.zigbee2mqtt_bridge_connection_state, binary_sensor.zigbee2mqtt_bridge_restart_required, button.zigbee2mqtt_bridge_restart, select.zigbee2mqtt_bridge_log_level, sensor.zigbee2mqtt_bridge_coordinator_version, sensor.zigbee2mqtt_bridge_network_map, sensor.zigbee2mqtt_bridge_version, switch.zigbee2mqtt_bridge_permit_join
- Impact: Reduced unavailable count by 7, eliminated ghost MQTT traffic

**System Monitor Disabled**: CPU/Memory sensors unavailable because `systemmonitor` platform commented out in `configuration.yaml`

**Integration Issues**: Some integrations may not be loaded or configured

### **Immediate Actions Required**
1. **Start Mosquitto Add-on**:
   - HA UI → Settings → Add-ons → Mosquitto broker → Start
   - Verify MQTT integration in Settings → Devices & Services

2. **Clear Retained MQTT Topics**:
   - Use MQTT Explorer to delete Z2M-related retained topics
   - Remove topics under zigbee2mqtt/ hierarchy

3. **Check Container Status**:
   - Verify ESPHome containers running (for CPU/Memory sensors if needed)
   - Check Zigbee2MQTT status (though removed, may have residual entities)

4. **Re-enable System Monitor** (Optional):
   - Uncomment `systemmonitor` in `configuration.yaml` if CPU/Memory monitoring desired
   - Note: May impact performance, currently disabled for optimization

5. **Validate Integrations**:
   - Check missing integrations: alexa_media, scheduler, watchman, entity_controller, adaptive_lighting
   - Add via HACS or Settings → Devices & Services

### **Expected Resolution**
- MQTT entities: ~800+ should become available after broker restart
- System health: Availability % from 43.2% to ~90%+
- Dashboard performance: Faster loading, functional controls
- WebSocket stability: Reduced disconnections from missing entities
- MQTT errors: Eliminated ghost client traffic

### **Monitoring Protocol**
- Track entity count reduction post-MQTT restart
- Monitor system health percentage improvement
- Validate Zigbee device connectivity
- Update this section with resolution status

**Last Updated**: 2026-01-07 - Z2M ghost entities removed, MQTT cleanup in progress

---

# 📌 **Next Actions (Architecture Cleanup & System Stabilisation)**
*This block reflects the work done today — not GitHub's template-conversion tasks.*

```md
## 🚀 Next Actions (Architecture Cleanup & System Stabilisation)

### 1. Zigbee2MQTT Decommissioning (In Progress)
- [ ] Remove all MQTT/Z2M Zigbee devices from HA (SONOFF sensors, plugs, switches)
- [ ] Remove Zigbee2MQTT Bridge entity
- [ ] Confirm Z2M add-on is uninstalled
- [ ] Confirm Sonoff Zigbee dongle remains unplugged
- [ ] Validate no Z2M entities remain in HA

### 2. SmartThings Scope Correction
- [ ] Ensure SmartThings contains ONLY legacy Zigbee devices
- [ ] Confirm Aqara devices are NOT in SmartThings
- [ ] Confirm Hue devices are NOT in SmartThings
- [ ] Document final SmartThings device list in `system_status.md`

### 3. Aqara M3 + Matter Path Stabilisation
- [ ] Confirm Aqara M3 + DB remain in Apple Home
- [ ] Confirm Aqara devices appear in HA via Matter (not Zigbee)
- [ ] Add Aqara M3 to HA via HomeKit Controller (optional, non-destructive)
- [ ] Document Matter/Thread routing in `system_status.md`

### 4. Thread Network Validation
- [ ] Confirm AqaraHome-73af remains the preferred Thread network
- [ ] Confirm Apple TV + HomePods + Aqara M3 + DB are active border routers
- [ ] Confirm SmartThings Thread BR is present but not dominant
- [ ] Confirm Amazon Thread network remains isolated

### 5. MQTT Broker Recovery
- [ ] Start Mosquitto add-on
- [ ] Validate broker health
- [ ] Confirm recovery of MQTT-dependent entities
- [ ] Remove ghosted MQTT entities left by Z2M
- [ ] Update `system_status.md` with recovery metrics

### 6. HA Integration Cleanup
- [ ] Remove any integrations referencing Z2M or ZHA
- [ ] Validate Matter, HomeKit Controller, Hue, Tapo, SmartThings integrations
- [ ] Confirm no duplicate entities across ecosystems
- [ ] Restart HA and validate entity health

### 7. Device Placement Audit
- [ ] Confirm Aqara Zigbee devices → Aqara M3
- [ ] Confirm Hue Zigbee devices → Hue Bridge
- [ ] Confirm legacy Zigbee → SmartThings
- [ ] Confirm Matter devices → Apple Home first
- [ ] Confirm Thread devices → auto-join nearest BR
- [ ] Document final placement in `system_status.md`
```