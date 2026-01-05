# Unifi U7 Lite Access Point Setup Guide
# For Unifi Cloud Ultra Network with Home Assistant Integration

## 🎯 Device Overview
**Unifi U7 Lite**: WiFi 7 access point for high-performance wireless networking
- **WiFi 7 Support**: Latest 802.11be standard with multi-gig speeds
- **PoE Support**: 802.3af/at/bt Power over Ethernet
- **Mesh Support**: EasyMesh compatible for seamless roaming
- **Management**: Cloud-managed via Unifi Cloud Ultra

## 📋 Pre-Installation Checklist

### Network Requirements
- ✅ **Unifi Cloud Ultra**: Controller running and accessible
- ✅ **PoE Switch**: Available PoE port (802.3af/at/bt compatible)
- ✅ **Ethernet Cable**: Cat6 or better for multi-gig speeds
- ✅ **Power Source**: PoE injector or PoE switch port
- ✅ **IP Address**: DHCP available or static IP planned

### Controller Preparation
- ✅ **Firmware Updated**: Unifi Cloud Ultra on latest firmware
- ✅ **Adoption Ready**: Controller set to "Adopt" mode
- ✅ **Site Configuration**: Correct site selected for device adoption
- ✅ **Admin Access**: Super admin credentials ready

## 🛠️ Installation Steps

### Phase 1: Physical Setup
1. **Power Off Device**: Ensure U7 Lite is powered off
2. **Connect Ethernet**: Plug PoE cable into LAN port
3. **Power On**: Device will boot and enter adoption mode
4. **LED Status**: Watch for white pulsing LED (discovery mode)

### Phase 2: Device Adoption
1. **Access Controller**: Log into Unifi Cloud Ultra (192.168.0.1)
2. **Navigate to Devices**: Go to Devices → Pending Adoption
3. **Adopt Device**: Click "Adopt" for the U7 Lite
4. **Wait for Provisioning**: Device downloads firmware and configures
5. **LED Confirmation**: LED turns steady white when adopted

### Phase 3: Configuration
1. **Device Settings**: Click on adopted U7 Lite in device list
2. **Network Settings**:
   - **Name**: U7 Lite (Living Room) or appropriate location
   - **IP Assignment**: DHCP (recommended) or static IP
3. **Radio Settings**:
   - **2.4GHz**: Enable with appropriate channel width
   - **5GHz**: Enable with 160MHz channel width if supported
   - **6GHz**: Enable for WiFi 7 capabilities
4. **Advanced Settings**:
   - **Transmit Power**: Auto or manual adjustment
   - **Band Steering**: Enable for optimal client distribution

### Phase 4: Placement & Testing
1. **Optimal Location**: Central location, away from interference
2. **Cable Management**: Secure Ethernet cable routing
3. **Client Testing**: Connect test devices and verify speeds
4. **Coverage Testing**: Walk around and check signal strength

## 📊 Performance Optimization

### WiFi 7 Features
- **4K QAM**: Higher data rates for modern devices
- **Multi-Link Operation**: Simultaneous band usage
- **1024-QAM**: Enhanced modulation for better throughput
- **320MHz Channels**: Wider channels for higher speeds

### Mesh Configuration (if using multiple APs)
- **EasyMesh**: Enable for seamless roaming
- **Backhaul**: Use wired backhaul for best performance
- **Smart Steering**: Automatic client band steering

## 🔍 Troubleshooting

### Adoption Issues
- **LED not pulsing**: Power cycle device, check PoE power
- **Not appearing in pending**: Check network connectivity, firewall rules
- **Adoption fails**: Verify controller credentials, check device compatibility

### Connectivity Problems
- **No wireless clients**: Check radio settings, channel interference
- **Slow speeds**: Verify cable quality, check for interference
- **Client disconnects**: Adjust roaming settings, check mesh configuration

### Performance Issues
- **Low throughput**: Check channel width, transmit power, interference
- **Coverage gaps**: Reposition AP, add additional APs
- **Compatibility**: Ensure client devices support WiFi 7 features

## 📈 Expected Performance
- **WiFi 7 Speeds**: Up to 19Gbps theoretical maximum
- **Real-world**: 2-5Gbps depending on client capabilities
- **Range**: 150-300 feet depending on environment
- **Concurrent Clients**: 100+ devices supported

## 🔗 Home Assistant Integration
Once adopted, the U7 Lite will automatically appear in HA via the Unifi integration:
- **Device Entity**: unifi_u7_lite_living_room (or custom name)
- **Sensors Available**:
  - WiFi clients connected
  - Uptime and status
  - Performance metrics
  - Temperature monitoring

## ⚡ Power Requirements
- **PoE Standard**: 802.3bt (Type 4) recommended for full performance
- **Power Consumption**: ~25W maximum
- **PoE Injector**: 60W+ injector if not using PoE switch

## 🏆 Success Checklist
- [ ] Device adopted successfully in Unifi controller
- [ ] LED shows steady white light
- [ ] Wireless networks broadcasting
- [ ] Client devices can connect and achieve expected speeds
- [ ] Device appears in Home Assistant
- [ ] Performance monitoring active

## 📞 Support Resources
- **Unifi Documentation**: https://help.ui.com/hc/en-us
- **Community Forums**: https://community.ui.com/
- **Firmware Updates**: Automatic via cloud management
- **Technical Support**: Available through Unifi account

---
**Ready for U7 Lite installation! Follow the steps above for successful deployment.**</content>
<parameter name="filePath">s:\AI_WORKSPACE\unifi_u7_lite_setup_guide.md