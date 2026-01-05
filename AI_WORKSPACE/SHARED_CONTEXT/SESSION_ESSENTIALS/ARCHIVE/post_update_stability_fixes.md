# STABILITY FIXES TO APPLY AFTER HA UPDATE
# Prepared fixes for critical issues causing crashes and noise

## 🔇 ISSUE 1: Noisy TTS Debug Automations
**Problem**: debug_sonoff_button.yaml causing repeated Alexa/Google announcements
**Fix**: Disable debug automations that are no longer needed

### Files to disable/rename:
- includes/automations/debug_sonoff_button.yaml → DISABLED
- includes/automations/debug_sonoff_button_detection.yaml → DISABLED  
- includes/automations/debug_office_motion.yaml → DISABLED

## 🚨 ISSUE 2: 1519 Unavailable Entities
**Problem**: Container services not starting properly
**Fix**: Exclude noisy container CPU/memory sensors from recorder

### Already added to configuration.yaml:
```yaml
recorder:
  exclude:
    entity_globs:
      - sensor.*_cpu_percent
      - sensor.*_memory_percent
```

## 🔧 ISSUE 3: Backup Manager Busy
**Problem**: create_backup busy error blocking updates
**Fix**: Wait for current backup/update to complete before new operations

## 📊 ISSUE 4: Add-ons Not Loading
**Problem**: ESPHome, VLC, MotionEye containers failing to start
**Fix**: Check Supervisor logs after update, restart individual add-ons if needed

## ⚠️ IMMEDIATE ACTIONS AFTER UPDATE:
1. Check if debug automations are still triggering TTS noise
2. Disable debug_sonoff_button.yaml if still causing issues
3. Test OneNote sync button (should work now)
4. Monitor new Stability Dashboard for crash risk patterns
5. Use SSH terminal if frontend becomes unresponsive

## 🛡️ EMERGENCY ACCESS:
- SSH Terminal: Settings → Add-ons → SSH & Web Terminal
- Stability Monitor: New dashboard should appear in sidebar
- Nuclear Disable: AI_WORKSPACE/emergency_nuclear_disable.bat (if needed)

**Status**: Ready to apply fixes once HA update completes and system stabilizes!