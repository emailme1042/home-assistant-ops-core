# HA Crash and Performance Fix Update - 2025-11-13

## Current Situation Summary
Home Assistant (HA) on Nabu Casa's HA Green device has been experiencing repeated crashes, slow performance, and connection issues with HACS. The system shows a misleading "Welcome to Home Assistant" screen instead of the expected dashboard overview. Config is correctly stored locally on the HA Green device (not on network shares), which is the official best practice.

## Root Causes Identified
1. **YAML Configuration Errors**: Duplicate keys in automation and sensor files preventing proper parsing.
2. **Performance Issues**: Expensive template sensors (ha_total_automations, ha_total_scripts) causing high CPU load.
3. **Custom Integrations**: Multiple untested HACS integrations potentially causing instability.
4. **Dashboard Mode**: YAML mode with complex custom dashboards may be contributing to rendering issues.
5. **Network Sync**: Briefcase locks on network-shared config files (though config is local on device).

## Fixes Applied
1. **YAML Fixes**:
   - Removed duplicate `data` keys in `ai_periodic_runner.yaml`.
   - Updated `system_health_template.yaml` to modern template sensor format.
   - Disabled performance-heavy sensors to prevent crashes.

2. **Dashboard Mode Change**:
   - Temporarily switched to `lovelace: mode: storage` to revert to UI-configured dashboards and avoid YAML issues.

3. **Performance Optimizations**:
   - Disabled CPU-intensive template sensors.
   - Recommended removing HACS if stability issues persist.

## Current Status
- HA is configured for YAML mode (user preference).
- Config is local on HA Green device.
- Storage mode applied as temporary fix.
- System ready for restart to apply changes.

## Next Steps and Plans
1. **Immediate Actions**:
   - Restart HA Green device to apply configuration changes.
   - Verify dashboard loads properly (should show previous overview, not welcome screen).
   - Monitor for crashes and performance.

2. **If Issues Persist**:
   - Remove HACS entirely (not official HA, can cause instability).
   - Disable all custom integrations and re-enable one-by-one.
   - Follow official HA troubleshooting: https://www.home-assistant.io/docs/troubleshooting/

3. **Long-term Stability**:
   - Stick to official HA integrations only.
   - Use storage mode for Lovelace if YAML causes issues.
   - Regular backups and updates via official channels.

4. **Official Guidance Adherence**:
   - All changes follow HAOS best practices.
   - Config local to device.
   - Minimize custom components for reliability.

## Files Updated
- `configuration.yaml`: Switched to storage mode.
- `includes/sensors/system_health_template.yaml`: Disabled heavy sensors.
- `includes/automations/ai_routine/ai_periodic_runner.yaml`: Fixed duplicates.

## AI Coordination
This update has been shared with all AIs. Jamie will review and confirm next actions. Focus on official HA docs and community forums for any unresolved issues.

**Priority**: High - Restore stable HA functionality.
**Status**: Fixes applied, pending restart validation.
**Owner**: Jamie + AI Team