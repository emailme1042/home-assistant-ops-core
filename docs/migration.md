# Migration Plan: From ZHA/Z2M to Vendor Hubs

Steps to transition from HA-managed Zigbee to vendor hubs for better reliability.

## Why Migrate?

- ZHA/Z2M can be unstable with HA updates.
- Vendor hubs provide local control and better mesh.
- HA can still integrate without owning the network.

## Step 1: Assess Current Setup

- List all Zigbee devices in ZHA/Z2M.
- Note automations and dependencies.
- Backup HA config.

## Step 2: Choose New Hub

- Sonoff for Sonoff devices.
- Aqara for Aqara ecosystem.
- Tuya for mixed brands.

## Step 3: Pair Devices to New Hub

- Factory reset devices if needed.
- Pair one by one to avoid conflicts.
- Test local automations on hub.

## Step 4: Integrate with HA

- Remove ZHA/Z2M integration.
- Add new integration (eWeLink LAN, LocalTuya, etc.).
- Update automations to use new entities.

## Step 5: Test and Validate

- Ensure all devices discovered.
- Test presence, motion, controls.
- Verify HA automations work.
- Monitor for 1-2 weeks.

## Step 6: Decommission Old Setup

- Remove ZHA/Z2M add-on.
- Document new architecture.

## Risks

- Device re-pairing may take time.
- Some devices may not be compatible with new hub.
- Temporary loss of functionality during transition.

## Timeline

- Planning: 1 day
- Migration: 1-2 days
- Testing: 1 week