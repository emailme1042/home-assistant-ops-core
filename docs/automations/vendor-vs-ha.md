# Vendor Automations vs HA Automations

This guide explains what logic runs on vendor hubs vs Home Assistant.

## Vendor Hub Logic (Local)

- Presence detection and state management.
- Idle timers and sensitivity settings.
- Basic automations (e.g., turn on light when motion detected).
- Mesh routing and device pairing.
- OTA updates and firmware management.

## HA Logic (Enhanced)

- Cross-device automations (radar + camera + door sensor).
- Presence fusion from multiple sources.
- Notifications and alerts.
- Energy monitoring and overrides.
- Complex logic combining Zigbee with Wi-Fi/Thread devices.

## Why This Separation?

- Reliability: Core functions work without HA.
- Performance: Local responses are faster.
- Simplicity: HA focuses on orchestration, not basics.

## Examples

- **Vendor**: Radar detects motion → local light on.
- **HA**: Radar + door open + time of day → custom scene.

## Failure Modes

- HA down: Vendor logic continues.
- Hub issues: HA can alert or use alternatives.
- Restart-safe: No state loss on HA reboots.