# Sonoff mmWave Radar Best Practices

Guide for setting up and optimizing Sonoff SNZB-06P and SNZB-03P radars.

## Device Overview

- mmWave technology for accurate presence detection.
- Zigbee paired to Sonoff hub for reliability.
- HA sees occupancy, motion, distance, light level.

## Pairing

- Use Sonoff ZBBridge Pro or ZBDongle-P with eWeLink.
- Ensure firmware is latest for best performance.

## Sensitivity Settings

- Adjust via eWeLink app:
  - Sensitivity: Medium for general use.
  - Idle time: 30-60 seconds to avoid false triggers.
  - Detection range: Based on room size.

## HA Integration

- Use eWeLink LAN integration.
- Entities: occupancy, motion, distance, confidence.

## Best Practices

- Place 2-3m high, avoid metal obstructions.
- Test for false positives (pets, fans).
- Combine with PIR for redundancy.
- Use HA for advanced logic (e.g., presence fusion).

## Known Quirks

- May detect through walls; adjust sensitivity.
- Battery life: 1-2 years with Zigbee.
- OTA updates via hub.

## Troubleshooting

- If unresponsive, re-pair to hub.
- Check mesh signal strength.
- Monitor HA logs for integration issues.