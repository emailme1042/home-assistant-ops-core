# Zigbee Architecture

This document outlines the Zigbee setup for the smart home, emphasizing reliability through vendor hubs rather than HA dependency.

## Core Principles

- Devices paired to dedicated Zigbee coordinators (hubs).
- Hubs handle local automations, mesh stability, and vendor logic.
- HA integrates locally to observe and extend, but not control the Zigbee network.

## Recommended Hubs

### Sonoff ZBBridge Pro
- Best for Sonoff radars and sensors.
- Local eWeLink integration with HA.
- Stable OTA and mesh.

### Aqara Hub M3
- Great for Aqara devices.
- Thread + Zigbee support.
- HA via HomeKit or Matter.

### Tuya Zigbee Gateway
- Affordable for various sensors.
- Local automations.
- HA via LocalTuya.

## Integration with HA

- Use local APIs to avoid cloud dependencies.
- HA sees all devices but doesn't manage Zigbee pairing or mesh.

## Benefits

- No HA restarts affect Zigbee.
- Vendor-level reliability.
- Local fallbacks.

## Setup Steps

1. Select hub.
2. Pair devices.
3. Configure HA integration.
4. Document mesh layout and recovery steps.