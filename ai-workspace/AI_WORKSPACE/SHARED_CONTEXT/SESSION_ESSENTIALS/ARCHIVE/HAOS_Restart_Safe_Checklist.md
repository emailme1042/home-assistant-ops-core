# 🧠 Home Assistant Restart-Safe Checklist
**DATE:** 2025-11-01  
**TAG:** #restart_safe #merge_complete #dashboard_validated  
**AUTHOR:** 👤 Jamie | ⚙️ GitHub Copilot (VSCode) | 🧠 GPT (Smart Home Ops Assistant)

---

## ✅ PRE-RESTART VALIDATION

### 1️⃣ Merge Integrity
- [x] `merge_map.yaml` executed successfully  
- [x] 3 master markdowns created:  
  - AI_OPERATIONS_REFERENCE.md  
  - AI_DASHBOARD_GUIDE.md  
  - VSCode_Edge_Integration_Guide.md  
- [x] All source files tagged `#archived_20251101`  
- [x] `copilot_session_notes_merge.md` log confirmed  

### 2️⃣ Dashboard Validation
- [x] `ai_insight.yaml` rendering verified  
- [x] `dashboard_ai_insight_fix.yaml` applied (entity mappings repaired)  
- [x] `entity_validation.yaml` validated (no missing entities)  
- [x] Sidebar titles and dashboard names aligned  

### 3️⃣ Configuration Audit
- [x] YAML check passes (`Developer Tools → Check Configuration`)  
- [x] No “invalid option for lovelace” warnings present  
- [x] Template sensors and shell commands load correctly  
- [x] Automations and scripts enabled  

### 4️⃣ Logging and Archiving
- [x] `copilot_session_notes.md` updated with #restart_safe  
- [x] `_merge_warnings.log` reviewed (empty / acknowledged)  
- [x] `AI_VALIDATION_SUMMARY.md` confirmed created  

### 5️⃣ Snapshot and Restart
- [ ] Take HAOS backup (Supervisor → Backups → Create Full Backup)  
- [ ] Reboot Home Assistant (Settings → System → Restart)  
- [ ] Verify dashboards reload without errors  
- [ ] Check AI Workspace dashboard last-updated timestamp  

---

## 🧩 POST-RESTART CHECKS
| Area | Verification | Status |
|------|---------------|--------|
| AI Workspace | Dashboard and heatmap load | ☐ |
| AI Navigation | Sidebar navigation functional | ☐ |
| AI System Insight | All entity groups populated | ☐ |
| Weekly Digest Automation | Scheduled & runs successfully | ☐ |
| Sensors & Scripts | Values & outputs normal | ☐ |
| Logs | No new errors in Supervisor log | ☐ |

---

## 🗃️ FILES INVOLVED
- merge_map.yaml  
- merge_markdown_files_resilient.py  
- dashboard_ai_insight_fix.yaml  
- entity_validation.yaml  
- copilot_session_notes.md  
- AI_VALIDATION_SUMMARY.md  

---

> **Completion Directive:**  
> Once all boxes are checked, mark this document as **Completed ✅** and archive with tag `#restart_confirmed_20251101`.
