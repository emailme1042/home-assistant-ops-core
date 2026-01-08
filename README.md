# Smart Home Automation Project

This project documents and manages a smart home setup using Home Assistant with a focus on reliable, vendor-hub-based Zigbee architecture. The goal is to have devices paired to dedicated Zigbee coordinators (not HA-dependent), with HA observing and extending capabilities for advanced automations.

**Note**: This repository is for planning and documentation. The live Home Assistant configuration is located on the S drive. The `homeassistant/` folder here contains templates and examples for reference.

## Architecture Overview

- **Zigbee devices** paired to vendor hubs (Sonoff ZBBridge Pro, Aqara Hub, etc.) for reliability and local control.
- **Home Assistant** integrates via local APIs (eWeLink LAN, HomeKit, LocalTuya) to observe states and add cross-ecosystem logic.
- **Philosophy**: Reliable first, HA-enhanced second, never HA-dependent.

## Folder Structure

- `docs/`: Documentation
  - `architecture/`: System architecture docs
  - `automations/`: Automation logic and vendor vs HA decisions
  - `radar/`: Device-specific guides (e.g., Sonoff mmWave radars)
- `homeassistant/`: HA configuration templates and examples (live config is on S drive)
- `scripts/`: Scripts for device management and setup
- `.vscode/`: VS Code settings

## Key Components

- Zigbee hubs: Sonoff, Aqara, Tuya
- Presence sensors: Sonoff SNZB-06P, Aqara FP2
- HA integrations: Local, no cloud dependencies

## Getting Started

1. Choose a primary Zigbee hub.
2. Pair devices to the hub.
3. Integrate hub with HA.
4. Use HA for super-automations.

For detailed guides, see `docs/`.