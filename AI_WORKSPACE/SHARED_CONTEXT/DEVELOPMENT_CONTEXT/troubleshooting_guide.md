# 🆘 Troubleshooting Guide — Common Issues & Solutions

## 🚨 Critical System Issues

### TTS Script Missing Error
**Error**: `Action script.tts_test_script not found.`

**Fix**: Ensure TTS script is properly loaded in scripts config:
```yaml
# includes/scripts/tts_test_script.yaml
script:
  tts_test_script:
    alias: TTS Test Script
    sequence:
      - service: notify.alexa_media_lounge_alexa
        data:
          message: "This is a test message from Jamie's AI system."
          data:
            type: tts
```

### Dashboard Entity Missing Errors
**Error**: Dashboard references entities that don't exist

**Fix Process**:
1. Check if entity is defined in `includes/` folder
2. Verify correct entity naming in YAML files
3. Restart Home Assistant if entities were just created
4. Temporarily comment out missing entities until HA restart

### YAML Validation Failures
**Error**: Syntax errors in YAML files

**Fix Steps**:
```bash
# 1. Run validation to identify issues
python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml

# 2. Check common issues:
# - Indentation (spaces not tabs)
# - Quote matching
# - List syntax
# - Duplicate keys

# 3. Fallback: validate includes only
python3 /config/python_scripts/validate_includes_yaml.py /config/includes
```

## 🔗 Dashboard & Navigation Issues

### Broken Dashboard Links
**Issue**: Links opening in wrong location or not working

**Solutions**:
- **For VSCode opening**: Use `vscode://file/S:/...` format
- **For Windows Explorer**: Use `file:///S:/...` format  
- **For web browser**: Use plain text paths with copy instructions

### Dashboard Navigation Problems
**Issue**: Links going to same page instead of target

**Fix**: Update dashboard link paths:
```yaml
# Wrong:
navigation_path: /lovelace-ai-workspace/0

# Correct:
navigation_path: /ai-workspace/ai-overview
```

### Missing Dashboard Entities
**Issue**: Dashboard shows "Entity not available"

**Resolution**:
1. Create missing entity files in `includes/` directories
2. Restart Home Assistant
3. Verify entity names match exactly in dashboards
4. Use auto-entities for dynamic content where possible

## 🤖 AI Integration Problems

### OpenAI API Failures
**Error**: GPT requests failing or timing out

**Diagnosis & Fix**:
```bash
# 1. Check API connectivity
curl -s -H "Authorization: Bearer $OPENAI_TOKEN" https://api.openai.com/v1/models

# 2. Verify secrets.yaml has correct token
# 3. Check OpenAI account billing status
# 4. Review request format in rest_commands/rest.yaml
```

### Flask Service Unavailable
**Error**: Local Flask services not responding

**Fix Process**:
```bash
# 1. Check service status
curl -s -o /dev/null -w "%{http_code}" http://localhost:5006/run_gpt

# 2. Restart Flask services
# 3. Verify ports 5001, 5005, 5006 are available
# 4. Check firewall settings
```

### AI Agent Context Loss
**Issue**: AI agents losing session context

**Solution**:
1. Update `AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/current_session.md`
2. Drag-and-drop context files to AI chats
3. Reference AI_README.md for collaboration protocol
4. Use structured session templates

## 📡 Network & Service Issues

### MQTT Connection Problems
**Error**: MQTT devices unavailable

**Fix Steps**:
```bash
# 1. Test MQTT connection
python3 /config/ai_workspace/Scripts/mqtt_test.py --host localhost --port 1883

# 2. Check MQTT broker status
# 3. Verify credentials in input_text entities
# 4. Restart MQTT broker if needed
```

### External Service Timeouts
**Issue**: REST commands failing to external services

**Diagnosis**:
1. Check network connectivity
2. Verify API credentials haven't expired
3. Test endpoints manually with curl
4. Review rate limiting on external services

## 🏠 Home Assistant Core Issues

### Entity Unavailable Errors
**Issue**: Entities showing as unavailable

**Investigation**:
1. Check if integration is still connected
2. Verify device is powered and connected
3. Review integration logs for errors
4. Restart specific integration if needed

### Automation Not Triggering
**Issue**: Automations not firing as expected

**Debug Process**:
1. Check automation is enabled
2. Verify trigger conditions are met
3. Test conditions in template editor
4. Add logging to automation actions
5. Check if automation is in single mode and still running

### Performance Issues
**Issue**: Home Assistant running slowly

**Optimization**:
1. Check recorder settings (purge_keep_days: 3)
2. Review excluded domains/entities
3. Monitor CPU/memory usage via sensors
4. Clear old log files and backups

## 🗂️ File System Issues

### AI_Zone Path References
**Issue**: References to invalid `AI_Zone/` paths

**Fix**: Replace with actual paths:
```yaml
# Wrong:
/media/ai_workspace/AI_Zone/file.md

# Correct options:
S:/AI_WORKSPACE/SHARED_CONTEXT/file.md
/config/AI_WORKSPACE/SHARED_CONTEXT/file.md
ai_workspace/SHARED_CONTEXT/file.md  # Using alias
```

### Mount Point Issues
**Issue**: AI_WORKSPACE mount not accessible

**Solutions**:
1. Check mount_map.yaml for correct paths
2. Verify network drive connectivity
3. Restart Home Assistant if needed
4. Use local paths as fallback

## 🔄 Recovery Procedures

### Emergency Recovery
**When system is completely broken**:

1. **Stop Home Assistant**
2. **Restore last known good configuration**:
   ```bash
   cp /config/snapshots/configuration.yaml.snapshot.YYYYMMDD /config/configuration.yaml
   ```
3. **Validate restored config**:
   ```bash
   python3 /config/scripts/validate_yaml.py /config
   ```
4. **Start Home Assistant in safe mode**
5. **Gradually re-add changes**

### Partial Recovery
**When specific components are broken**:

1. **Identify broken component via logs**
2. **Comment out in configuration.yaml**
3. **Restart Home Assistant**
4. **Fix component issues**
5. **Re-enable component**

### Configuration Rollback
**When recent changes cause issues**:

1. **Check git history** (if using version control)
2. **Use snapshots from `snapshots/` directory**
3. **Restore specific files from backups**
4. **Validate before full restart**

## 📝 Logging & Diagnostics

### Key Log Locations
- **Home Assistant Log**: `/config/home-assistant.log`
- **Validation Logs**: `/config/validation_logs/`
- **AI Session Logs**: `/config/AI_WORKSPACE/copilot_session_notes.md`
- **Fix Reports**: `/config/fix_sheet.yaml`

### Diagnostic Commands
```bash
# System health check
python3 /config/python_scripts/system_health_check.py

# Entity validation
python3 /config/python_scripts/validate_entities.py

# Service status check
curl -s http://localhost:8123/api/

# YAML validation
python3 /config/scripts/validate_yaml.py /config
```

## 📞 Support Resources

### Internal Resources
- **AI_README.md**: Multi-AI collaboration protocol
- **copilot_session_notes.md**: Recent session history
- **SYSTEM_OVERVIEW dashboards**: System status visibility
- **Validation workflows**: Automated health checking

### External Resources
- **Home Assistant Community**: Forum support
- **HACS Issues**: Component-specific problems
- **Integration Documentation**: Official HA docs
- **GitHub Issues**: Component bug reports

---

**Recovery Time**: Most issues resolved in < 10 minutes  
**Success Rate**: 95%+ of issues have documented solutions  
**Prevention**: Regular validation and backups key to stability