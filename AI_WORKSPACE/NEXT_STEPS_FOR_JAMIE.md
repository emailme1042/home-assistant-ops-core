# Next Steps for Jamie - Cleanup & System Maintenance

## Generated: November 15, 2025

## 🎯 Immediate Actions (Today)

### Phase 1: Safe Junction Removal

Execute these commands to remove broken symbolic links:

```powershell
# Remove broken junctions (safe - no data loss)
Remove-Item "S:\snapshots" -Force
Remove-Item "S:\ui_lovelace_minimalist_DISABLED_ROOT" -Force
Remove-Item "S:\validation_logs" -Force
Remove-Item "S:\venv" -Force
Remove-Item "S:\yaml_validation_logs" -Force
```

**Expected Result**: Free up directory namespace, eliminate VS Code confusion
**Status**: ✅ COMPLETED - venv/ removed, others not found (already cleaned or never existed)

### File & Folder Cleanup Audit (From GPT Analysis)

#### Safe-to-Delete Files (Confirmed from GPT)

| File | Reason |
|------|--------|
| `home-assistant.log.old` | Rotated log, safe to delete if not needed for diagnostics |
| `includes_automations_errors.log` | Old error log, safe to archive or delete |
| `fix_errors.log` | If already resolved and logged in markdown, safe to delete |
| `core_stats.txt` | If snapshot already logged in `system_status.md`, safe to delete |
| `host_info.txt` | If contents are logged elsewhere, safe to delete |

#### Folders Worth Exploring for Cleanup

| Folder | Notes |
|--------|-------|
| `custom_components_disabled` / `disabled_custom_components` | Likely contain deprecated or broken integrations — safe to archive or delete after validation |
| `validation_logs` / `yaml_validation_logs` | If older than 2 weeks and not referenced in `NEXT_STEPS_FOR_JAMIE.md`, safe to archive |
| `venv` | If not actively used for Python scripts or OpenAI, consider archiving or deleting |
| `ui_lovelace_minimalist_DISABLED_ROOT` | Redundant if `ui_lovelace_minimalist` is active — validate and delete if unused |
| `snapshots` | Review for outdated backups — delete older than 30 days if space is needed |

#### Archive Protocol

If unsure, move candidates to `/ARCHIVE_2025_CLEANUP/` and log each move in:

- `recent_changes.md`
- `system_status.md`
- `ARCHIVE_LOG_20251115.md` (optional)

### Git Repository Decision

**Question**: Do you want to:

- **Option A**: Use existing `github_repo/` for HA config version control
- **Option B**: Initialize new git repo in root `S:\`
- **Option C**: Keep current setup (no version control)

**Recommendation**: Option A - leverage existing structured repo

## 📋 This Week's Tasks

### Tuesday: Directory Access Resolution

- [ ] Troubleshoot why most directories show "file not available" errors
- [ ] Verify network drive connectivity or permissions
- [ ] Test access to `AI_WORKSPACE/`, `config/`, `includes/`

### Wednesday: Content Audit (When Accessible)

- [ ] Review `custom_components/` for deprecated integrations
- [ ] Audit `backups/` for redundant configurations
- [ ] Check `deps/` and `python_scripts/` for stale content
- [ ] Validate `snapshots/` for outdated backups (>30 days)

### Thursday: Log Management Setup

- [ ] Implement automated log rotation policy
- [ ] Create `/ARCHIVE_2025_LOGS/` directory
- [ ] Configure HA external logging if needed

## 🎯 Long-term Goals (This Month)

### System Health

- [ ] Achieve stable HA operation with <1% crash rate
- [ ] Resolve remaining 6,038 unavailable entities
- [ ] Enable functional Nabu Casa remote access
- [ ] Complete MQTT supervisor connection fix

### Development Environment

- [ ] Finalize VS Code extension configuration
- [ ] Set up proper git workflow for HA config
- [ ] Implement automated backup procedures

### File Hygiene

- [ ] Establish quarterly cleanup audits
- [ ] Create automated cleanup scripts
- [ ] Implement archive rotation policies

## 📊 Success Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| System Stability | Intermittent crashes | <1 crash/week | 2 weeks |
| Entity Availability | 6,038 unavailable | <100 unavailable | 1 week |
| Remote Access | Not connected | Fully functional | 3 days |
| Disk Usage | 1.11 GB | <1 GB | 1 week |
| File Organization | Broken junctions | Clean structure | Today |

## 🚨 Critical Path Items

1. **Today**: Remove broken junctions
2. **Tomorrow**: Resolve directory access issues
3. **This Week**: Complete content audit
4. **Next Week**: Implement log management
5. **This Month**: Achieve full system stability

## 📞 Support Resources

- **HA Community**: forums.home-assistant.io
- **VS Code**: code.visualstudio.com/docs
- **Git**: git-scm.com/doc
- **PowerShell**: docs.microsoft.com/powershell

---
*Next review: November 22, 2025*
*Escalation: If directory access issues persist >48 hours*
