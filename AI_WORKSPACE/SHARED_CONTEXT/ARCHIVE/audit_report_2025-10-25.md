# AI System Audit — 2025-10-25

## 🔍 Issues Identified & Fixes Applied

### ✅ Dashboard Links (FIXED)
**Problem**: Links used `/local/ai_context/` which doesn't work with S:/ mapping
**Solution**: Replaced all with `file:///S:/AI_WORKSPACE/...` direct file links
**Affected Files**:
- `dashboards/SYSTEM_OVERVIEW/ai_navigation.yaml`
- `dashboards/ai/ai_workspace_overview.yaml`

### ⚠️ Duplicate Automations
**Problem**: Many automations are duplicated between:
- `automations/*.yaml`
- `includes/automations/*.yaml`
- `includes/automations/kodi.yaml` = `includes/automations/gpt.yaml` (identical GPT automations)

**Recommendation**: Consolidate to one location (keep `includes/automations/` only)

### ⚠️ Shell Commands Referencing Missing Scripts
**Problem**: Several shell_command entries call scripts that may not exist or may fail:
- `run_chatgpt_user_reply` → calls `/config/python_scripts/chatgpt_user_reply.py`
- `run_openai_orphaned_analysis` → calls `/config/scripts/openai_orphaned_analysis.py`
- `mount_ai_workspace` → CIFS mount command (requires secrets.smb_user/smb_pass)
- Validation commands use `/config` paths (should be `S:/` or actual container path)

**Needs Verification**: Check if these scripts exist and secrets are configured

### ⚠️ Missing Entity Definitions
**Problem**: Automations reference entities that may not exist:
- `input_text.gpt_text_prompt`
- `input_text.chatgpt_prompt`
- `input_text.gpt_result_core`
- `input_text.gpt_status_flag`
- `input_boolean.gpt_direct_send_trigger`
- `sensor.gpt_status`
- `binary_sensor.adsb_feed_alive`
- `binary_sensor.jit_plugin_flask_online`

**Action Required**: Create missing input helpers or remove referencing automations

### ⚠️ Notification Targets May Not Exist
**Problem**: Automations send notifications to:
- `notify.alexa_media_your_device` (placeholder name)
- `notify.mobile_app_plop` (may not be registered)

**Action Required**: Update device names or disable automations

### ⚠️ Conflicting Duplicate Automation IDs
**Problem**: Two automations with same ID `update_fix_sheet_timestamp`:
- `includes/automations/validation.yaml`
- `includes/automations/dashboard.yaml`

**Fix Required**: Rename one ID to avoid conflicts

---

## 🛠️ Recommended Fixes (Ready to Apply)

### 1. Remove Duplicate Automation Files
Move all automations to `includes/automations/` and delete from root `automations/`

### 2. Fix Duplicate Automation ID
Rename `update_fix_sheet_timestamp` in `dashboard.yaml` to `update_fix_sheet_timestamp_dashboard`

### 3. Remove/Consolidate kodi.yaml
`includes/automations/kodi.yaml` is 100% duplicate of `gpt.yaml` — delete one

### 4. Create Missing GPT Helpers
Add to `includes/input_texts/` and `includes/input_booleans/`:
```yaml
# includes/input_texts/gpt.yaml
gpt_text_prompt:
  name: GPT Text Prompt
  initial: ""
  max: 1000

chatgpt_prompt:
  name: ChatGPT Prompt
  initial: ""
  max: 1000

gpt_result_core:
  name: GPT Result
  initial: ""
  max: 5000

gpt_status_flag:
  name: GPT Status
  initial: "Idle"
  max: 255

# includes/input_booleans/gpt.yaml
gpt_direct_send_trigger:
  name: GPT Direct Send Trigger
  initial: false
```

### 5. Fix Notification Device Names
Search/replace placeholders:
- `notify.alexa_media_your_device` → actual Alexa device entity
- `notify.mobile_app_plop` → actual mobile app entity or comment out

---

## 🎨 HACS Integration Recommendations

### Already Installed (Good!)
- `custom-sidebar` (custom sidebar YAML)
- `tabbed-card` (used in ai-workspace.yaml)

### Recommended Additions
1. **auto-entities** — Dynamic entity filtering for dashboards
2. **mushroom-cards** — Modern, clean card design
3. **card-mod** — Advanced card styling
4. **layout-card** — Better dashboard layouts
5. **fold-entity-row** — Collapsible entity groups
6. **mini-graph-card** — Compact sensor graphs
7. **button-card** — Advanced button customization (may already have)
8. **decluttering-card** — Reusable card templates
9. **lovelace-state-switch** — Conditional card display
10. **multiple-entity-row** — Show multiple entities per row

### For OpenAI Integration
11. **conversation** (core) — Intent handling for Alexa
12. **assist_pipeline** (core) — Local voice assistant
13. **extended-openai-conversation** (HACS) — Enhanced GPT integration

---

## 📋 Next Steps — What Should I Fix?

1. **Apply all fixes above** (consolidate automations, remove duplicates, create helpers)
2. **Just fix dashboard links** (already done)
3. **Create missing helper entities** for GPT workflows
4. **Clean up shell commands** that reference missing scripts
5. **Audit and fix notification targets**
6. **All of the above** — comprehensive cleanup

Let me know which fixes to apply, or say "fix everything" and I'll do a comprehensive cleanup pass!
