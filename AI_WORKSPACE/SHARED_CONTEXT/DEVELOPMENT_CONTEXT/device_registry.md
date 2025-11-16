# 🔧 Device Registry — Home Assistant Integrations

## 🏠 Physical Devices

### Lighting & Smart Switches
- **Hue Integration** — Phillips Hue lights throughout house
  - `light.lounge` — Main lounge lighting
  - `binary_sensor.hall_sensor_motion` — Hall motion sensor
  - Various Hue switches with button events
- **Smart Switches** — Multiple button devices
  - `event.teddy_switch_button_1` — Teddy's room controls
  - `event.lounge_hue_switch_button_1` — Lounge switch
  - `event.bedroom_switch_button_3` — Bedroom controls

### Climate & Environment
- **Temperature Sensors** — Environmental monitoring
  - `sensor.temperature_and_humidity_sensor_egg_temperature` — Kitchen sensor
  - Various climate monitoring devices
- **Boiler System** — Heating control integration
  - `sensor.boiler_runtime_today` — Daily operation tracking
  - Smart thermostat integration

### Security & Access
- **Door Sensors** — Entry monitoring
  - `binary_sensor.front_door_contact` — Front door status
- **Motion Detection** — Movement tracking
  - Multiple motion sensors throughout house

## 📱 Media & Entertainment

### Voice Assistants
- **Alexa Media Integration** — Voice control and TTS
  - `media_player.lounge_alexa` — Main lounge Alexa device
  - `notify.alexa_media_lounge_alexa` — TTS service
  - Multiple Alexa devices for whole-house audio

### Media Players
- **Kodi Integration** — Media center control
  - Multiple Kodi instances
  - Integration with automation system
- **Fire TV** — Streaming device control
  - Remote control integration
  - Dashboard control interface

### Audio Systems
- **TTS Integration** — Text-to-speech services
  - Google Translate TTS
  - Alexa media TTS
  - Multi-device audio routing

## 🌐 Network & Communication

### MQTT Broker
- **Local MQTT Server** — Device communication hub
  - Host: `localhost` (configurable)
  - Port: `1883` (configurable)
  - Authentication enabled
  - Discovery monitoring active

### External Services
- **OpenAI Integration** — GPT services
  - API endpoint: `https://api.openai.com/v1/chat/completions`
  - Bearer token authentication
  - Model: `gpt-4o`
- **Flask Services** — Local API endpoints
  - `http://192.168.1.203:5001` — JIT plugin services
  - `http://localhost:5006` — GPT command runner
  - `http://127.0.0.1:5005` — NAS script runner

## 📧 Communication Services

### Email Integration
- **IMAP Monitoring** — Email sensor
  - `sensor.imap_emailme1042_gmail_com_messages` — Unread count
- **SMTP Notifications** — Outbound email
- **Voice Monkey** — Alexa announcement service

### Notification Services
- **Alexa Media** — Voice announcements
- **Email Notifications** — SMTP alerts
- **Dashboard Notifications** — UI alerts

## 🏡 Home Management

### Irrigation System
- **Smart Irrigation** — Garden watering control
  - Timer-based scheduling
  - Weather integration
  - Manual override controls
  - Rain detection integration

### Pokemon Card Scanner
- **Custom Integration** — Card recognition system
  - Card scanning capability
  - Rarity detection
  - Value estimation
  - Feature extraction

## 🔍 Monitoring & Diagnostics

### System Health
- **Home Assistant Core** — System monitoring
  - CPU usage tracking
  - Memory utilization
  - Supervisor status
- **Network Monitoring** — Connectivity checks
  - Device tracking
  - Service availability
  - Performance metrics

### iBeacon Tracking
- **Location Services** — Device presence
  - `device_tracker.tv_lounge_tv_ad07` — TV tracking
  - Signal strength monitoring
  - Distance estimation
  - Vendor identification

## 🎯 Integration Capabilities

### HACS Components
- **Custom Integrations** — Enhanced functionality
  - Auto-entities
  - Browser mod
  - Custom icons
  - Scheduler
  - Watchman
  - Many others (see HACS registry)

### Custom Components
- **AI Automation Suggester** — Machine learning automation
- **Entity Controller** — Smart device control
- **Magic Areas** — Room-based automation
- **Bermuda** — Bluetooth tracking
- **BLE Monitor** — Bluetooth sensor integration

## 🔧 Device Configuration Notes

### Network Settings
- **IP Range**: `192.168.1.0/24`
- **Trusted Networks**: Local LAN access
- **External URLs**: OpenAI, Voice Monkey, others whitelisted

### Integration Status
- **Stable**: Hue, Alexa, MQTT, Core sensors
- **Active Development**: AI integration, Dashboard builders
- **Monitoring**: All devices health-checked via Watchman

### Device Access Methods
- **Local API**: REST commands, shell commands
- **Cloud Services**: OpenAI, Voice Monkey, email
- **Direct Integration**: Hue, Alexa, MQTT devices

---

**Last Updated**: 2025-10-26  
**Device Count**: 50+ active devices  
**Integration Types**: Local, Cloud, Hybrid  
**Primary Protocols**: WiFi, Bluetooth, MQTT, REST