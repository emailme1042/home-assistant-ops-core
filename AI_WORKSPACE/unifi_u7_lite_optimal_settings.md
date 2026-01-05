# Unifi U7-Lite WiFi Configuration Guide
## Optimal Settings for Jamie's Home Network

### 🎯 Network Configuration Overview
**Main Network**: "Bogey Pie Wifi" - Primary WiFi for all devices
**IoT Network**: "Smart Devices" - Dedicated 2.4GHz for IoT devices
**Security**: WPA3 where possible, WPA2 for compatibility
**Performance**: Optimized for home automation and streaming

### 📡 WiFi Network Settings

#### Main Network: "Bogey Pie Wifi"
```
SSID: Bogey Pie Wifi
Security: WPA3-Personal (if all devices support) or WPA2-Personal
Password: [Your current password]
Bands: 2.4GHz + 5GHz + 6GHz (U7-Lite supports WiFi 7)
Channel Width: Auto (160MHz on 5GHz/6GHz, 40MHz on 2.4GHz)
Transmit Power: Auto
Band Steering: Enabled
Airtime Fairness: Enabled
Fast Roaming: Enabled (802.11k/v/r)
```

#### IoT Network: "Smart Devices"
```
SSID: Smart Devices
Security: WPA2-Personal (for maximum IoT compatibility)
Password: [Different from main network]
Bands: 2.4GHz only
Channel Width: 20MHz (for better range and compatibility)
Transmit Power: Medium-High
Band Steering: Disabled
Client Isolation: Optional (for security)
Guest Network: Disabled
```

### ⚙️ U7-Lite Device Settings

#### Radio Configuration
```
2.4GHz Radio:
- Channel: Auto (avoid interference)
- Transmit Power: 20-23 dBm
- Minimum RSSI: -85 dBm

5GHz Radio:
- Channel: Auto (DFS channels enabled)
- Transmit Power: 20-23 dBm
- Channel Width: 160MHz
- Minimum RSSI: -75 dBm

6GHz Radio:
- Channel: Auto
- Transmit Power: 20-23 dBm
- Channel Width: 160MHz
- Minimum RSSI: -75 dBm
```

#### Advanced Settings
```
Device Name: U7-Lite Living Room
LED: Auto (bright during setup, dim after)
SSH: Disabled (unless needed for troubleshooting)
NTP: Enabled (time sync)
Syslog: Disabled (unless monitoring needed)
```

### 🏠 Home Automation Optimizations

#### For Smart Home Devices
- **Zigbee Devices**: Use "Smart Devices" 2.4GHz network
- **WiFi Cameras**: Use main "Bogey Pie Wifi" for bandwidth
- **Smart TVs/Streaming**: Main network for 5GHz/6GHz speeds
- **Mobile Devices**: Main network with band steering

#### Performance Settings
```
Multicast Enhancement: Enabled
IGMP Snooping: Enabled
Fast Roaming: Enabled
Band Steering: Smart (aggressive)
Airtime Fairness: Enabled
```

### 🔒 Security Recommendations

#### Network Security
- **Firewall**: Enabled on router
- **Device Isolation**: Consider for IoT network
- **Client Isolation**: Optional for guest devices
- **MAC Filtering**: Disabled (too restrictive for smart home)

#### Access Control
- **Admin Access**: HTTPS only, strong password
- **Remote Access**: Via Unifi Cloud (secure)
- **Firmware Updates**: Auto-update enabled
- **Backup**: Regular configuration backups

### 📊 Monitoring & Maintenance

#### What to Monitor
- **Client Count**: Per radio band
- **Channel Utilization**: Should be <50%
- **Signal Strength**: >-65dBm for good performance
- **Uptime**: Track device reliability
- **Temperature**: Monitor for overheating

#### Maintenance Schedule
- **Weekly**: Check for firmware updates
- **Monthly**: Review client connections and performance
- **Quarterly**: Physical inspection and cleaning
- **Annually**: Cable testing and replacement if needed

### 🚨 Troubleshooting

#### Common Issues
- **Slow Speeds**: Check channel interference, reduce channel width
- **Dropouts**: Adjust transmit power, check for interference
- **Poor Range**: Increase transmit power, reposition AP
- **Device Compatibility**: Use WPA2 for older IoT devices

#### Performance Testing
- **Speed Test**: Use main network on 5GHz/6GHz
- **Range Test**: Walk around with device, check signal
- **Interference Check**: Use WiFi analyzer app
- **Client Count**: Monitor per radio band

### 🎯 Expected Performance

#### WiFi 7 Capabilities (U7-Lite)
- **Theoretical Speeds**: Up to 19Gbps
- **Real-World**: 1-3Gbps depending on client devices
- **Range**: 150-200ft indoors, 300-400ft outdoors
- **Client Capacity**: 200+ concurrent devices

#### Network Segmentation Benefits
- **Main Network**: High-speed for streaming, gaming, work
- **IoT Network**: Reliable 2.4GHz for smart home devices
- **Security**: Isolated networks reduce attack surface
- **Performance**: Reduced interference between device types

### 📋 Setup Checklist

#### Phase 1: Physical Setup ✅
- [x] PoE cable connected
- [x] LED shows white pulsing (discovery mode)
- [x] Ethernet cable is Cat6+

#### Phase 2: Device Adoption 🔄
- [ ] Access Unifi Controller at 192.168.0.1
- [ ] Navigate to Devices → Pending Adoption
- [ ] Adopt U7-Lite device
- [ ] Wait for firmware download
- [ ] Confirm steady white LED

#### Phase 3: Configuration 🔄
- [ ] Set device name: "U7-Lite Living Room"
- [ ] Configure WiFi networks as specified
- [ ] Set radio settings for optimal performance
- [ ] Enable advanced features (roaming, steering)
- [ ] Test client connections

#### Phase 4: Testing & Optimization 🔄
- [ ] Connect test devices to both networks
- [ ] Verify speeds and range
- [ ] Check HA integration (uptime, clients, temperature)
- [ ] Monitor performance over 24-48 hours
- [ ] Adjust settings if needed

### 🤝 Integration with Home Assistant

#### Expected HA Sensors (after adoption)
```
sensor.u7_lite_living_room_uptime
sensor.u7_lite_living_room_temperature
sensor.u7_lite_living_room_clients_2g
sensor.u7_lite_living_room_clients_5g
sensor.u7_lite_living_room_clients_6g
sensor.u7_lite_living_room_channel_utilization_2g
sensor.u7_lite_living_room_channel_utilization_5g
sensor.u7_lite_living_room_channel_utilization_6g
```

#### Automation Opportunities
- **Performance Alerts**: Notify if utilization >70%
- **Temperature Monitoring**: Alert if >50°C
- **Client Count Tracking**: Monitor device connections
- **Channel Optimization**: Auto-adjust on interference

---

**Ready for Phase 2: Device Adoption**
Navigate to your Unifi Cloud Gateway Ultra at `https://192.168.0.1` and look for the U7-Lite in pending devices. Once adopted, apply these optimal settings for your home network!</content>
<parameter name="filePath">s:\AI_WORKSPACE\unifi_u7_lite_optimal_settings.md