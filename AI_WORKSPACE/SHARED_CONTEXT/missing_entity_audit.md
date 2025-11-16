# Missing Entity Audit - October 27, 2025

## 🔍 **SYSTEM_OVERVIEW Dashboard Entities Required**

### 📝 **Input Text Entities Needed:**
- `input_text.ai_context_note` ✅ **CREATED**
- `input_text.todo_task_1` ✅ **CREATED** 
- `input_text.backup_log_viewer` ❌ **MISSING**
- `input_text.manual_health_report_viewer` ❌ **MISSING**
- `input_text.gpt_text_prompt` ❌ **MISSING**
- `input_text.gpt_text_reply` ❌ **MISSING**
- `input_text.orphaned_file_log` ❌ **MISSING**
- `input_text.recovery_notes` ❌ **MISSING**
- `input_text.preview_tab_log` ❌ **MISSING**

### 🔘 **Input Boolean Entities Needed:**
- `input_boolean.run_validation_test` ✅ **EXISTS** (validation_controls.yaml)
- `input_boolean.gpt_session_active` ❌ **MISSING**
- `input_boolean.ai_script_toggle_1` ✅ **CREATED**

### 📋 **Input Select Entities Needed:**
- `input_select.file_preview` ✅ **EXISTS** (file_preview.yaml)
- `input_select.dashboard_theme` ✅ **EXISTS** (theme_mode.yaml)

### 📊 **Sensor Entities Needed:**
- `sensor.last_restart_time` ❌ **MISSING**
- `sensor.reload_status` ❌ **MISSING**
- `sensor.system_health_summary` ❌ **MISSING**
- `sensor.includes_validation_status` ❌ **MISSING**
- `sensor.copilot_last_snapshot` ❌ **MISSING**
- `sensor.copilot_log_stale` ❌ **MISSING**
- `sensor.file_last_modified` ❌ **MISSING**
- `sensor.system_overview_last_updated` ❌ **MISSING**
- `sensor.wsl_startup_marker` ❌ **MISSING**
- `sensor.last_changelog_entry` ❌ **MISSING**
- `sensor.entity_watchdog_last_run` ❌ **MISSING**
- `sensor.gpt_summary_preview` ❌ **MISSING**
- `sensor.invalid_entities_summary` ❌ **MISSING**
- `sensor.orphaned_file_scan` ❌ **MISSING**

## 🎯 **Priority Creation List**

**HIGH PRIORITY** (Dashboard Breaking):
1. `input_boolean.gpt_session_active`
2. `input_text.gpt_text_prompt`
3. `input_text.gpt_text_reply`
4. `sensor.system_health_summary`
5. `sensor.includes_validation_status`

**MEDIUM PRIORITY** (Feature Breaking):
6. `input_text.backup_log_viewer`
7. `input_text.recovery_notes`
8. `sensor.last_restart_time`
9. `sensor.reload_status`

**LOW PRIORITY** (Nice to Have):
10. Other logging and monitoring sensors

## 📊 **Entity Status Summary**
- **Total Required**: 24 entities
- **Already Exist**: 6 entities (25%)
- **Need Creation**: 18 entities (75%)
- **High Priority Missing**: 5 entities