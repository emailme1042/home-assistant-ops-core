# 🔄 Session Startup Checklist — GitHub Copilot Protocol

## ✅ **Required Actions at Every Session Start**

### 1. 📁 **SHARED_CONTEXT Structure Verification**
- [ ] Verify all folders exist: `SESSION_ESSENTIALS`, `DEVELOPMENT_CONTEXT`, `AI_PROTOCOLS`, `JD_KEY_DOCS`, `ARCHIVE`
- [ ] Check folder permissions and accessibility
- [ ] Confirm Windows Explorer path works: `S:\AI_WORKSPACE\SHARED_CONTEXT\`

### 2. 📋 **SESSION_ESSENTIALS Update Check**
- [ ] Update `current_session.md` with today's goals and context
- [ ] Refresh `system_status.md` with latest health indicators
- [ ] Review `active_issues.md` for outstanding problems
- [ ] Check `recent_changes.md` reflects latest modifications
- [ ] Verify `NEXT_STEPS_FOR_JAMIE.md` is current

### 3. 🔧 **JD_KEY_DOCS Synchronization**
- [ ] Copy latest `fix_sheet.yaml` from root if newer
- [ ] Update validation logs from `validation_logs/` folder
- [ ] Ensure `JD_PLAY.yaml` is current version
- [ ] Check all operational files are accessible

### 4. 📊 **System Health Validation**
- [ ] Run quick YAML validation check
- [ ] Verify external services (OpenAI, Flask) are responsive
- [ ] Check entity availability and dashboard functionality
- [ ] Confirm no critical errors in logs

### 5. 🧠 **AI Collaboration Readiness**
- [ ] Confirm all AI agents have updated context files
- [ ] Verify multi-AI handoff protocols are clear
- [ ] Check session tagging system is ready
- [ ] Ensure logging templates are current

## 🚀 **Automated Session Startup Commands**

### File Sync Commands
```bash
# Update JD_KEY_DOCS with latest operational files
Copy-Item "S:\fix_sheet.yaml" "S:\AI_WORKSPACE\SHARED_CONTEXT\JD_KEY_DOCS\" -Force
Copy-Item "S:\validation_logs\*" "S:\AI_WORKSPACE\SHARED_CONTEXT\JD_KEY_DOCS\" -Force

# Refresh system status
python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml
```

### Health Check Commands  
```bash
# Verify OpenAI connectivity
$headers = @{ "Authorization" = "Bearer $(Get-Content S:\secrets.yaml | Select-String 'openai_bearer' | ForEach-Object { $_.Line.Split(':')[1].Trim() })" }
Invoke-RestMethod -Uri "https://api.openai.com/v1/models" -Headers $headers -Method GET | Select-Object -First 1

# Check Flask services
curl -s -o /dev/null -w "%{http_code}" http://localhost:5006/run_gpt
```

## 📝 **Session Start Template**

### Standard Session Opening Message
```
#session_start [DATE] [TIME]

✅ **System Status Check Complete**
- SHARED_CONTEXT folders: All present and accessible  
- SESSION_ESSENTIALS: Updated for today's work
- JD_KEY_DOCS: Synchronized with latest operational files
- System Health: [VALIDATION_RESULT]
- External Services: [SERVICE_STATUS]

🎯 **Today's Goals**: [JAMIE_SPECIFIED_GOALS]

📁 **Context Ready for Multi-AI Sharing**: 
All files in S:\AI_WORKSPACE\SHARED_CONTEXT\ are current and ready for drag-and-drop to GPT and Edge Copilot.

⚠️ **Issues Requiring Attention**: [IF_ANY]

🤝 **Ready for Collaboration**
```

## 🔄 **If Issues Found During Startup**

### Critical Issues (Session Cannot Proceed)
- Missing SHARED_CONTEXT folders → Recreate structure
- YAML validation failures → Fix before continuing
- External service failures → Diagnose and repair

### Warning Issues (Can Proceed with Caution)
- Outdated files → Update during session
- Minor entity errors → Note for resolution
- Performance issues → Monitor and optimize

### Documentation Issues (Fix During Session)
- Stale session notes → Update as we work
- Missing documentation → Create as needed
- Inconsistent file organization → Reorganize

## 🎯 **Success Criteria for Session Start**

### ✅ **Ready to Proceed When:**
- All SHARED_CONTEXT folders accessible
- Key operational files are current
- System validation passes
- External AI services can access context files
- No critical blocking issues

### 🔄 **Session Handoff Protocol**
Once startup check complete:
1. Update Jamie with any issues found
2. Confirm today's work priorities  
3. Ensure context files are ready for other AIs
4. Begin productive work with clean foundation

---

**Execution**: This checklist runs automatically at every new session start  
**Duration**: ~2-3 minutes for complete verification  
**Purpose**: Ensure perfect multi-AI collaboration foundation  
**Owner**: GitHub Copilot (VSCode)