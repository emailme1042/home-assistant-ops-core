# 🔄 AI System Restart Validation Checklist
**DATE:** {{ now().strftime('%Y-%m-%d') }}  
**OPERATOR:** 👤 Jamie  
**AGENTS:** 🧠 GPT | ⚙️ GitHub Copilot | 💬 Edge Copilot  

---

## ✅ Step 1 — Pre-Restart
- [ ] Backup configuration (snapshot or Git copy)
- [ ] Check YAML syntax: Developer Tools → YAML → **Check Configuration**
- [ ] Review `AI_Monitoring_Report.md` for any warnings
- [ ] Confirm no pending automation edits in VS Code

---

## 🧠 Step 2 — Restart Home Assistant
Restart via: **Settings → System → Restart**

Wait until:
- [ ] Sidebar dashboards reload (AI Workspace, AI Routine, AI Insight)
- [ ] Green system health indicator returns
- [ ] No “failed to load” messages in Supervisor log

---

## 🧩 Step 3 — Dashboard Verification
**AI Routine Dashboard**
- [ ] Current phase displayed correctly (Morning / Focus / Evening / Sleep)
- [ ] Phase gauges show non-zero values
- [ ] Daily summary markdown renders correctly
- [ ] Mood scene buttons respond instantly

**AI System Insight Dashboard**
- [ ] Sync status = `online`
- [ ] Merge warnings = `0`
- [ ] Validation summary populated
- [ ] Session log markdown loads without error

---

## ⚙️ Step 4 — Automation Health
- [ ] `ai_routine_phase_timer.yaml` triggers on state change
- [ ] `ai_routine_summary_digest.yaml` scheduled at 23:59
- [ ] Notifications delivered successfully
- [ ] Log file `/config/www/ai_routine_summary.md` updated

---

## 📡 Step 5 — Agent & Log Sync
- [ ] `copilot_session_notes.md` last updated < 10 min ago
- [ ] `sensor.ai_workspace_status` = “Healthy”
- [ ] Edge Copilot connection confirmed
- [ ] GitHub Copilot log: `#final_validation` tag present

---

## 🧾 Step 6 — Final Confirmation
- [ ] Create a quick note in `copilot_session_notes_merge.md`:
  > ✅ Restart validation completed — all dashboards green  
- [ ] Notify GPT: “Restart complete, validation green”

---

**Notes:**
- If any dashboard fails to load, open *System Insight → Logs* for details.
- To rerun diagnostics manually:

```
python S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/validate_merge_sources.py
```

---

📍 **Location Suggestion:**  
Save at  
`S:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\AI_RESTART_VALIDATION_CHECKLIST.md`
