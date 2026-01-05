# 🧠 system_sync_snapshot.md
📅 Timestamp: 2025-09-03  
📍 Source: SYSTEM_OVERVIEW, diagnostics, entity snapshots, and script audits

---

## 🔴 Entity Status Summary  
- Over 100+ entities marked `unavailable` or `unknown`  
- Key failures:  
  - `sensor.kitchen_temp`  
  - `switch.lounge_lamp`  
  - `sensor.boys_room_humidity`  
  - `scene.bedroom_relax`  
  - `script.data`  
  - `person.teddy`  
  - `tts.google_translate_en_com`

---

## ⚠️ YAML Diagnostics  
- ❌ `configuration.yaml`: `!include_dir_merge_named` error  
- ❌ `email_notify.yaml`: `!secret` constructor failure  
- ❌ `approved.yaml`: alias scan error  
- ❌ `automations.yaml`: duplicate `action` key  
- ✅ All other includes validated and modular

---

## 🧭 Dashboard Recovery Map  
- Fallback views confirmed for:  
  - `fire_tv.yaml`  
  - `garden_flow.yaml`  
  - `admin_automations.yaml`  
  - `wizard_bootstrap.yaml`  
  - `teddys_den.yaml`  
- Recovery logic surfaced for:  
  - `admin_nav`, `admin_rooms`, `admin_presence`, `admin_scripts`, `admin_security`

---

## 🧰 Script & Automation Summary  
- Active scripts:  
  - `run_chatgpt_user_reply`  
  - `fix_sheet_logger`  
  - `python_script.add_todo`  
  - `save_email_subject`, `save_email_body`, `save_email_from`  
- Automations confirmed:  
  - ESP alerts  
  - GPT triggers  
  - WSL startup checks  
  - YAML validation  
- Audit targets:  
  - `gpt_context_file`  
  - `dashboard_urls`  
  - `sensor.wsl_startup_marker`

---

## 🧠 AI Execution & Folder Logic  
- Canonical root: `S:` confirmed  
- AI zone: `media\\AI_Zone\\AI_WORKSPACE`  
- All folder roles modular and locked  
- No silent edits—visual keys enforced:  
  - 🟦 Confirmed  
  - 🌸 Pending  
  - 🟥 Deprecated

---

## 📂 Context File Index  
- All key `.md` files confirmed and surfaced  
- `backup_log.txt` still missing  
- `session_prompt.s.md` active and schema-safe  
- SYSTEM_OVERVIEW sync confirmed
