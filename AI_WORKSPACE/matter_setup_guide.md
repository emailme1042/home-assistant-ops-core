# Matter Integration Setup Guide
# Add Matter devices once in Home Assistant, control them everywhere!

## 🎯 What is Matter?
Matter is a smart home protocol that allows devices to work across different ecosystems:
- ✅ Add device once in Home Assistant
- ✅ Control from HA, Apple Home, Google Home, Alexa, Samsung SmartThings
- ✅ Secure, reliable, and future-proof

## 📋 Setup Steps

### 1. Enable Matter Integration
Add to configuration.yaml:
```yaml
matter:
  # Optional: Thread border router for Thread-enabled Matter devices
  # thread:
  #   - usb_device: /dev/ttyACM0
```

### 2. Add Matter Devices
- Go to HA Settings → Devices & Services
- Click "Add Integration" → Search "Matter"
- Follow setup wizard to commission devices

### 3. Enable Cross-Platform Control

#### Apple HomeKit
```yaml
homekit:
  - name: "Home Assistant Matter Bridge"
    port: 21063
    filter:
      include_entities:
        - light.matter_*
        - switch.matter_*
        - climate.matter_*
```

#### Google Assistant
```yaml
google_assistant:
  project_id: !secret google_assistant_project_id
  service_account: !secret google_assistant_service_account
```

#### Amazon Alexa
```yaml
alexa:
  smart_home: {}
```

### 4. Control from Multiple Platforms

#### iOS Home App
- Add HA as Home Hub in iOS Settings
- Matter devices appear automatically
- Control with Siri: "Hey Siri, turn on the Matter light"

#### Google Home App
- Link HA account in Google Home
- Matter devices appear in Google Home
- Control with Google Assistant: "Hey Google, dim the Matter bulb"

#### Alexa App
- Enable HA skill in Alexa app
- Matter devices appear in Alexa
- Control with Alexa: "Alexa, turn off the Matter switch"

## 🔧 Matter Device Types Supported
- Lights (bulbs, strips, controllers)
- Switches & outlets
- Thermostats & climate control
- Door locks
- Window coverings
- Fans
- Sensors (motion, contact, temperature)

## 📱 Multi-Platform Control Flow

```
Matter Device
     ↓
Home Assistant (Primary Hub)
     ↓
Multiple Ecosystems:
• Apple HomeKit → iOS devices
• Google Assistant → Google Home/Nest
• Amazon Alexa → Echo devices
• Samsung SmartThings → Samsung devices
```

## ⚙️ Configuration Options

### Thread Support (for Thread-enabled Matter devices)
```yaml
matter:
  thread:
    - usb_device: /dev/ttyACM0  # Your Thread border router
```

### Device Filtering
```yaml
homekit:
  filter:
    include_domains:
      - light
      - switch
    include_entities:
      - light.matter_*
```

## 🔍 Troubleshooting

### Device Not Appearing
1. Check Matter integration status in HA
2. Ensure device is in pairing mode
3. Try different USB port for border router
4. Check HA logs for Matter errors

### Cross-Platform Sync Issues
1. Restart HA after adding devices
2. Re-link accounts in each platform app
3. Check device permissions in each ecosystem

## 📊 Benefits
- **Single Point of Control**: Add devices once, use everywhere
- **Future-Proof**: Matter is industry standard
- **Secure**: End-to-end encryption
- **Reliable**: Local control with cloud backup
- **Compatible**: Works with 200+ brands

## 🚀 Getting Started
1. Add `matter:` to configuration.yaml
2. Restart HA
3. Go to Settings → Devices & Services → Add Matter
4. Commission your first Matter device
5. Set up cross-platform integrations (HomeKit, Google, Alexa)
6. Control from any assistant!</content>
<parameter name="filePath">s:\AI_WORKSPACE\matter_setup_guide.md