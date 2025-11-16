# 🏠 Jamie’s Home Assistant System Blueprint — 2025 Edition

## 🔧 Core Setup
- **Install Type**: Home Assistant OS (HAOS) on SSD-backed hardware
- **Mode**: YAML mode (manual dashboard control)
- **Backup**: Automated snapshots + manual Git sync of `AI_WORKSPACE/config`

## 🧩 Integrations (Core + Custom)
| Type         | Integration Name         | Purpose                                      |
|--------------|--------------------------|----------------------------------------------|
| Core         | MQTT                     | Device telemetry, sensor updates             |
| Core         | ESPHome                  | ESP-based sensors and relays                 |
| Core         | Zigbee2MQTT              | Zigbee mesh control                          |
| Core         | Matter Server            | Future-proofing for Matter devices           |
| Core         | Terminal & SSH           | Remote CLI access                            |
| Core         | Glances                  | System metrics                               |
| Core         | go2rtc                   | Camera stream routing                        |
| Core         | Log Viewer               | Live log inspection                          |
| Core         | Safe UI                  | Frontend recovery                            |
| Custom (HACS)| Alexa Devices            | Voice assistant integration (post-migration) |
| Custom (HACS)| Button Card              | Custom UI buttons                            |
| Custom (HACS)| Mod Card                 | UI layout control                            |
| Custom (HACS)| Mushroom Chips Card      | Compact UI elements                          |
| Custom (HACS)| Auto Entities            | Dynamic entity lists                         |
| Custom (HACS)| Gap Card                 | UI spacing                                   |
| Custom (HACS)| Lottie Card              | Animated UI elements                         |
| Custom (HACS)| Config Template Card     | Jinja-style templating in YAML dashboards    |

## 🧠 AI Agent Roles
| Agent            | Role                                      | Scope                                                  |
|------------------|-------------------------------------------|--------------------------------------------------------|
| **Edge Copilot** | DevTools inspector + frontend validator   | JS module loading, dashboard render, console errors    |
| **GPT (me)**     | System architect + YAML validator         | Recovery protocols, markdown logging, config refactor  |
| **M365 Copilot** | SOP writer + task planner                 | Meeting notes, SOPs, task assignment                   |
| **Siri/Alexa**   | Voice trigger + automation relay          | Local control, status queries                          |
| **OneNote Agent**| Knowledge extractor + routing agent       | Extracts tasks from shared notebooks                   |

## 📦 Devices in Use
- **Zigbee Mesh**: 200+ devices (lights, sensors, switches)
- **ESPHome**: Door sensors, ambient light, motion detectors
- **MQTT**: Battery sensors, message age monitors
- **Alexa**: Voice control, notification triggers
- **Custom Dashboards**: SMARTi, JD Dev Board, fallback dashboards

## 🎯 Final Goal
- Fully modular, restart-safe Home Assistant system
- All dashboards validated and renderable in YAML mode
- All HACS cards registered in `resources.yaml`
- All markdown blocks refactored for Jinja compatibility
- AI agents assigned and logged in `SESSION_RECALL.md`
- Remote UI enabled for GPT access (optional)
- OneNote routing active for shared task extraction
