# 🧱 PHASE 1 STABILIZATION PATCH — 2026-01-01

## 🎯 GOAL
Resolve UTF-8, template loop, missing logbook service, Alexa desync, and DLNA SSL timeout.

---

### 🔧 1. Fix UTF-8 Encoding

**Files:**
/config/includes_scripts_validation.yaml
/config/includes_automations_validation.yaml
/config/includes_sensors_validation.yaml
/config/config/fix_sheet.yaml

**VS Code Command:**
```
> Reopen With Encoding → UTF-8
> Save
```

---

### 🧮 2. Patch Template Loop (`sensor.system_health_score`)
**File:** `includes/templates/system_triage_sensors.yaml`

```yaml
    - name: "System Health Score"
      unique_id: system_health_score
      state: >
        {% set total_entities = states | selectattr('domain','defined') | list | count %}
        {% set unavailable = states | selectattr('state','in',['unavailable','unknown']) | list | count %}
        {% if total_entities > 0 %}
          {{ (((total_entities - unavailable) / total_entities) * 100) | round(1) }}
        {% else %}
          0
        {% endif %}
      unit_of_measurement: "%"
      attributes:
        total_entities: "{{ states | count }}"
        unavailable_entities: "{{ states | selectattr('state','in',['unavailable','unknown']) | list | count }}"
        healthy_entities: "{{ states | rejectattr('state','in',['unavailable','unknown']) | list | count }}"
        unavailable_entities: >
          {{ states | selectattr('state','in',['unavailable','unknown']) | list | count }}
        entity_id:
          - sensor.unavailable_entity_count
```

---

### 🪶 3. Restore Logbook Logging

**File:** `includes/scripts/capture_health_snapshot.yaml`

```yaml
alias: Capture Health Snapshot
sequence:
  - service: logbook.log
    data:
      name: "System Health Snapshot"
      message: "Captured restart snapshot at {{ now() }}"
      entity_id: sensor.system_health_score
  - service: persistent_notification.create
    data:
      title: "System Snapshot"
      message: "Health snapshot captured and logged."
mode: single
```

---

### 🗣️ 4. Alexa Re-Sync Automation

**File:** `includes/automations/alexa_entity_sync.yaml`

```yaml
automation:
  - alias: Alexa Entity Sync Monthly
    trigger:
      - platform: time
        at: "02:30:00"
    action:
      - service: cloud.alexa_sync_entities
    mode: single
```

---

### 📺 5. DLNA/TV SSL Patch

UI → Integrations → DLNA Media Renderer → Configure → **Uncheck "Use SSL"**

---

### 🔄 6. Validate & Restart

```bash
ha core check
git add -A
git commit -m "2026-01-01 | Phase 1 Stabilization Patch Applied"
ha core restart
```

**Verify After Restart**

* No UTF-8 or template warnings in logs
* "System Health Snapshot" appears in Logbook
* Alexa devices respond
* DLNA player stable (no SSL error)

---

</content>
<parameter name="filePath">s:\AI_WORKSPACE\copilot_session_notes\PHASE1_STABILIZATION_PATCH.md