# System Status Update Block Template
# Replace the CRITICAL ISSUES section in system_status.md with this block
# Fill in the [PLACEHOLDER] values with actual numbers from your entity count command

## 🔴 CRITICAL ISSUES

- **Entity Availability**: [TOTAL_UNAVAILABLE]/[TOTAL_ENTITIES] entities unavailable ([PERCENTAGE]%) 🔴
- **System Health**: [SYSTEM_HEALTH_PERCENTAGE]% 🔴
- **Automations**: [AUTOMATION_COUNT] (expected >168) 🔴
- **Scripts**: [SCRIPT_COUNT] (expected >119) 🔴
- **GPT Access**: Remote UI [ENABLED/DISABLED] 🔴

## 📊 Recovery Progress

### Entity Status
- **Total Entities**: [TOTAL_ENTITIES]
- **Available Entities**: [AVAILABLE_ENTITIES]
- **Unavailable Entities**: [TOTAL_UNAVAILABLE]
- **Availability Rate**: [AVAILABILITY_PERCENTAGE]%

### System Components
- **Automations Loaded**: [AUTOMATION_COUNT]/168 ([AUTOMATION_PERCENTAGE]%)
- **Scripts Loaded**: [SCRIPT_COUNT]/119 ([SCRIPT_PERCENTAGE]%)
- **System Health Score**: [SYSTEM_HEALTH_PERCENTAGE]%

### MQTT Status
- **Broker Connection**: [CONNECTED/DISCONNECTED]
- **Container Status**: [RUNNING/STOPPED]
- **Entity Recovery**: [RECOVERED_ENTITIES] entities restored

## 🎯 Next Actions

### Immediate (High Priority)
- [ ] Enable Nabu Casa Remote UI if not already enabled
- [ ] Restart ESPHome and MQTT containers if stopped
- [ ] Reload automations and scripts via HA CLI
- [ ] Verify MQTT broker connectivity and entity publishing

### Short-term (Medium Priority)
- [ ] Monitor entity availability for 24 hours
- [ ] Test multi-agent coordination with GPT access
- [ ] Review HACS integrations for stability impact
- [ ] Revert dashboard to YAML mode if stable

### Long-term (Low Priority)
- [ ] Optimize sensor polling intervals
- [ ] Implement entity health monitoring
- [ ] Document recovery procedures
- [ ] Update system status regularly

## 📈 Health Trends Update

### Post-Recovery Metrics
- **Entity Availability**: Improved from 34.7% to [NEW_AVAILABILITY_PERCENTAGE]%
- **System Health**: Increased from 0.0% to [NEW_SYSTEM_HEALTH]%
- **Automation Count**: Restored from 0 to [AUTOMATION_COUNT]
- **Script Count**: Restored from 0 to [SCRIPT_COUNT]

### Key Improvements
- Remote UI re-enabled for AI agent access
- MQTT containers restarted and connectivity restored
- Automation and script entities repopulated
- System health monitoring reactivated

## 🚨 Updated Active Alerts

### CRITICAL PRIORITY
- [ ] Entity Unavailability: [TOTAL_UNAVAILABLE] entities unavailable - [RESOLVED/MONITORING]
- [ ] System Health: [SYSTEM_HEALTH_PERCENTAGE]% health - [RESOLVED/MONITORING]
- [ ] GPT Access: Remote UI [ENABLED/DISABLED] - [RESOLVED/MONITORING]

### HIGH PRIORITY
- [ ] MQTT Issues: Broker [CONNECTED/DISCONNECTED] - [RESOLVED/MONITORING]
- [ ] Container Status: ESPHome/MQTT containers [RUNNING/STOPPED] - [RESOLVED/MONITORING]

### MEDIUM PRIORITY
- [ ] HACS Review: Evaluate removal for stability - [PENDING/IN_PROGRESS]
- [ ] Dashboard Mode: Revert to YAML mode after entity fixes - [PENDING/IN_PROGRESS]

## 📋 Updated Quick Health Check

**Entity Count Command Result**:
```
Total entities: [TOTAL_ENTITIES]
Unavailable: [TOTAL_UNAVAILABLE] ([PERCENTAGE]%)
```

**Last Updated**: November 13, 2025 - Post-Recovery