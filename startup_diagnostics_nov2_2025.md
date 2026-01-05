# 🧠 Home Assistant Startup Diagnostics — Nov 2, 2025

## ✅ Startup Summary
- **Total entities loaded**: 2648
- **Automations enabled**: 107
- **Scripts loaded**: 90
- **IP Address**: `192.168.1.217`
- **Uptime**: 2025-11-02T21:59:04+00:00
- **Unavailable entities**: 1053 (39.8% of total)

---

## ⚠️ Entity Availability Issues

### ❌ Unavailable Entities (1053 total)
**Common pattern**: `sensor.<integration>_cpu_percent`, `sensor.<integration>_memory_percent`

#### Critical Examples:
- `sensor.grafana_cpu_percent` / `sensor.grafana_memory_percent`
- `sensor.vlc_cpu_percent` / `sensor.vlc_memory_percent`
- `sensor.motioneye_cpu_percent` / `sensor.motioneye_memory_percent`
- `sensor.studio_code_server_cpu_percent` / `sensor.studio_code_server_memory_percent`
- `sensor.sharptools_io_cpu_percent` / `sensor.sharptools_io_memory_percent`
- **...and 1043 more**

### 🔍 Suspected Causes:
- Integration containers not running or misconfigured
- Missing MQTT topics or stale entity registry entries
- Restart drift or invalid `via_device` references

---

## 🧩 Frontend Resource Failures

### ❌ JS Errors from HACS Cards
- `simple-weather-card.js`: `TypeError: Cannot convert undefined or null to object`
- `mini-media-player.js`: `TypeError: Class extends value undefined`
- `light-entity-card.js.map`: 404 error (missing source map)

### ❌ Custom Element Registry Collisions
- `"button-card-action-handler" already used`
- `"mini-graph-card" already used`

### ❌ DOMException
- `Failed to execute 'define' on 'CustomElementRegistry'`

### 🔍 Causes:
- Duplicate card imports via `configuration.yaml`, `resources.yaml`, and HACS
- Missing or outdated `.js` files in `/www/community/`
- Theme or layout conflicts with scoped registry

---

## 🖼️ Branding Asset 404s
- `broadlink_manager/dark_icon.png`
- `entity_controller/dark_icon.png`

> **Status**: Cosmetic only — no functional impact

---

## 🧠 Tuple Index Errors
- `hui-button-entity-row`: `Uncaught (in promise) {code: 'unknown_error', message: 'tuple index out of range'}`
- **Source**: Broken `call_service` action or invalid `via_device` reference

---

## 🔧 Fix Plan Summary

### ✅ Entity Recovery
- Validate MQTT and container status
- Remove stale entities from registry
- Re-pair Broadlink device and re-learn RF commands

### ✅ Frontend Cleanup
- Remove duplicate card imports
- Reinstall broken HACS cards
- Validate JS file paths and map files
- Fix broken `call_service` YAML blocks

### ✅ Optional Enhancements
- Create `dashboard_card_health.md`
- Build `element_registry_conflicts.md`
- Prep `button_card_debug.yaml` for service testing

---

## 📊 System Health Baseline
**Health Score**: 60.2% (entity availability)
**Priority**: Medium-High (high unavailable entity count)
**Action Required**: Entity cleanup and frontend resource validation

---

**Audit Generated**: {{ now().strftime('%Y-%m-%d %H:%M:%S') }}
**Next Review**: After entity cleanup and resource fixes