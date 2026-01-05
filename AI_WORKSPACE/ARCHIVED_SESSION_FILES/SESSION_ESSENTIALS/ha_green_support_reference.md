# Home Assistant Green Support Reference

**Source**: https://support.nabucasa.com/hc/en-us/categories/24638797677853-Home-Assistant-Green

## 🔧 Key Troubleshooting Resources

### **Network/Access Issues**
- **Can't access HA Green via http://homeassistant.local:8123**
- **Network performance troubleshooting**
- **Ethernet LED status indicators**

### **Hardware Support**
- **Power supply requirements** (if original lost)
- **Status LED meanings** and control (enable/disable)
- **USB dongle compatibility** (Zigbee, Z-Wave, Wi-Fi)
- **CR2032 battery slot** (optional backup)

### **System Recovery**
- **Resetting Home Assistant Green**
- **SD card reset procedures**
- **Backup and restore processes**
- **Migration between devices**

### **Hardware Specs & Connectivity**
- **Built-in capabilities**: Ethernet, USB ports
- **Missing features**: No built-in Zigbee, Thread, Wi-Fi, or Bluetooth
- **Expansion**: USB dongles required for wireless protocols

## 📋 Relevant to Current Issues

### **Network Performance Analysis**
- HA Green uses **wired Ethernet only** by default
- **USB Wi-Fi dongles** can be connected but may affect performance
- **Switch port configuration** and **cable quality** are critical factors
- **Ethernet LEDs** provide diagnostic information about connection speed/status

### **System Resources**
- **BusyBox environment** with limited shell commands (aligns with our current findings)
- **Container-based architecture** may have resource allocation differences vs PC
- **System monitoring entities** are hardware-specific (explains our entity reference issues)

## 🚨 Current Session Context
This resource helps explain:
1. **Why shell commands need BusyBox compatibility** (HA Green = appliance-style OS)
2. **Network performance differences** vs PC (40% gap we observed)
3. **Entity reference patterns** (HA Green has specific system monitoring entities)
4. **Hardware limitations** affecting network testing approaches

## � Additional Resources

### **Jamie's System URLs**
- **Direct HA Access**: https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa
- **Community Forum**: https://community.home-assistant.io/
- **Developer Standards**: https://github.com/home-assistant/developers.home-assistant/blob/master/docs/documenting/standards.md

### **Support Escalation**
- **Community Forum**: https://community.home-assistant.io/
- **Discord**: https://www.home-assistant.io/join-chat/
- **Nabu Casa Tickets**: https://support.nabucasa.com/hc/en-us/requests/new
- **GitHub Issues**: For development and integration issues

## 🎯 Action Items for Jamie
1. **Check Ethernet LED status** during network performance tests
2. **Verify switch port configuration** (speed/duplex settings)
3. **Consider USB Wi-Fi dongle** for comparison testing
4. **Review power supply specs** if hardware issues suspected