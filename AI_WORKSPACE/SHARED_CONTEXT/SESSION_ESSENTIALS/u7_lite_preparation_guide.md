# U7 Lite Preparation Guide — Complete Setup Checklist
**Created:** 2026-01-03
**For:** Jamie's Home Assistant + Unifi Network
**Status:** Ready for U7 Lite arrival tomorrow

## 🎯 EXECUTIVE SUMMARY
Complete preparation guide for U7 Lite installation with Unifi Cloud Ultra controller. Includes settings verification, backup procedures, physical setup planning, and post-installation verification.

## 📋 PRE-ARRIVAL CHECKLIST

### ✅ UNIFI ULTRA CONTROLLER ACCESS
**URL:** https://192.168.0.1:443
**Credentials:** Your existing admin credentials
**SSL Certificate:** ✅ Successfully added to HA (green tick confirmed)

### ✅ CURRENT SYSTEM STATUS
**HA Integration:** ✅ Working (devices visible in entity registry)
**Network Coverage:** 3 WLANs detected (Bogey Pie WiFi, Smart Devices, Ultra)
**Device Count:** Multiple APs and switches already configured
**SSL Certificate:** ✅ Added and tested successfully

## 🔍 ULTRA CONTROLLER SETTINGS VERIFICATION

### 📡 NETWORK SETTINGS
- [ ] **VLANs**: Check existing VLAN configurations
  - Note: VLAN IDs, names, and purposes
  - Document: Which devices use which VLANs
- [ ] **DHCP**: Review DHCP server settings
  - Note: IP ranges, lease times, reservations
  - Document: Static IP assignments
- [ ] **DNS**: Check DNS server configuration
  - Note: Primary/secondary DNS servers
  - Document: Custom DNS entries

### 🔐 SECURITY SETTINGS
- [ ] **Firewall Rules**: Document existing rules
- [ ] **Port Forwarding**: Note current port forwards
- [ ] **VPN Settings**: Check VPN configuration if used
- [ ] **Guest Network**: Verify guest network settings

### 📶 WIRELESS NETWORKS
- [ ] **SSID Configuration**: Document all 3 WLANs
  - Bogey Pie WiFi (main network)
  - Smart Devices (IoT network)
  - Ultra (additional network)
- [ ] **Security Settings**: WPA3, WPA2 settings
- [ ] **Channel Settings**: Current channel configurations
- [ ] **Transmit Power**: Current power levels

## 💾 BACKUP PROCEDURES

### 📤 CREATE FRESH BACKUP
1. **Login to Ultra Controller**: https://192.168.0.1:443
2. **Navigate to Settings** → **System** → **Backup**
3. **Create New Backup**:
   - Click "Download Backup"
   - Name: `pre_u7_lite_backup_20260103`
   - Include: All settings and configurations
4. **Save Backup File**: Store in secure location
5. **Verify Backup**: Confirm file size and creation timestamp

### 📁 BACKUP CONTENTS TO INCLUDE
- [ ] **Network Settings**: VLANs, DHCP, DNS
- [ ] **Device Configurations**: All APs, switches, gateways
- [ ] **Wireless Settings**: SSIDs, security, channels
- [ ] **Firewall Rules**: All security configurations
- [ ] **User Accounts**: Admin and user accounts
- [ ] **Site Settings**: Controller-specific settings

## 🛠️ U7 LITE PHYSICAL SETUP PLANNING

### ⚡ POWER PLANNING
- [ ] **Power Source**: Identify PoE+ injector or PoE switch port
- [ ] **Cable Run**: Plan Ethernet cable route to installation location
- [ ] **Power Budget**: Verify PoE switch can handle additional device
- [ ] **Backup Power**: Consider UPS protection for critical network device

### 📍 MOUNTING LOCATION
- [ ] **Central Location**: Choose central position for optimal coverage
- [ ] **Cable Access**: Ensure Ethernet cable can reach location
- [ ] **Ventilation**: Good airflow for cooling
- [ ] **Aesthetics**: Consider visibility and home decor

### 🔌 CABLE MANAGEMENT
- [ ] **Ethernet Cable**: Cat6 or better, appropriate length
- [ ] **Cable Routing**: Plan path that avoids interference
- [ ] **Labeling**: Label cables for future maintenance
- [ ] **Protection**: Use cable protectors if needed

## 🌐 NETWORK PLANNING

### 📧 IP ADDRESS ASSIGNMENT
- [ ] **DHCP Reservation**: Plan static IP for U7 Lite
- [ ] **IP Range**: Choose from existing DHCP range
- [ ] **VLAN Assignment**: Determine which VLAN for management
- [ ] **DNS Registration**: Plan hostname for device

### 📶 WIRELESS CONFIGURATION
- [ ] **SSID Adoption**: Which WLANs should U7 Lite broadcast
- [ ] **Channel Planning**: Coordinate with existing APs
- [ ] **Transmit Power**: Set appropriate power levels
- [ ] **Band Steering**: Configure 2.4GHz/5GHz/6GHz handling

### 🔄 DEVICE ADOPTION
- [ ] **Adoption Process**: Plan device discovery and adoption
- [ ] **Firmware Update**: Prepare for automatic firmware update
- [ ] **Configuration Sync**: Ensure consistent settings across APs
- [ ] **Mesh Formation**: Plan integration with existing mesh

## ✅ POST-INSTALLATION VERIFICATION

### 🔌 PHYSICAL VERIFICATION
- [ ] **Power Status**: Confirm PoE power delivery
- [ ] **LED Indicators**: Check device status lights
- [ ] **Ethernet Connection**: Verify link status and speed
- [ ] **Mounting Security**: Ensure device is securely mounted

### 🌐 NETWORK VERIFICATION
- [ ] **Device Adoption**: Confirm device appears in Ultra controller
- [ ] **IP Assignment**: Verify DHCP lease or static IP
- [ ] **Firmware Update**: Allow time for firmware update if needed
- [ ] **Configuration Sync**: Confirm settings match other APs

### 📡 WIRELESS VERIFICATION
- [ ] **SSID Broadcasting**: Confirm WLANs are broadcasting
- [ ] **Signal Strength**: Test coverage in target areas
- [ ] **Client Connections**: Test device connections to new AP
- [ ] **Roaming**: Test seamless roaming between APs

### 🤖 HOME ASSISTANT INTEGRATION
- [ ] **Device Discovery**: Check HA for new Unifi device entities
- [ ] **Entity Registration**: Verify sensors and controls appear
- [ ] **SSL Certificate**: Confirm continued connectivity
- [ ] **Performance Monitoring**: Check network performance metrics

## ⚠️ PRECAUTIONS & BEST PRACTICES

### 🔄 BACKUP-FIRST APPROACH
- **ALWAYS CREATE BACKUP BEFORE CHANGES**
- Test backup restoration capability
- Store backups in multiple secure locations
- Document backup contents and procedures

### ⚡ POWER CONSIDERATIONS
- Use PoE+ for reliable power delivery
- Consider power redundancy for critical devices
- Monitor power consumption and switch capacity
- Plan for future expansion

### 🔧 FIRMWARE COMPATIBILITY
- Check Unifi OS version compatibility
- Plan firmware update windows
- Monitor for security updates
- Document firmware versions

### 📊 MONITORING & MAINTENANCE
- Set up performance monitoring
- Plan regular backup schedule
- Document network changes
- Maintain configuration documentation

## 📞 SUPPORT RESOURCES

### 📚 DOCUMENTATION
- **Unifi Documentation**: https://help.ui.com/hc/en-us
- **U7 Lite Datasheet**: Check Unifi product specifications
- **HA Unifi Integration**: https://www.home-assistant.io/integrations/unifi/

### 🆘 TROUBLESHOOTING
- **Ultra Controller Logs**: Check system logs for issues
- **Device LED Status**: Reference LED indicator guide
- **HA Integration Logs**: Monitor HA logs for connectivity issues
- **Network Testing**: Use ping, traceroute for connectivity verification

## 🎯 SUCCESS CRITERIA

### ✅ MINIMUM SUCCESS REQUIREMENTS
- [ ] U7 Lite adopted by Ultra controller
- [ ] Device appears in HA entity registry
- [ ] Wireless networks broadcasting correctly
- [ ] Client devices can connect and roam
- [ ] No network performance degradation

### 🚀 OPTIMAL SUCCESS REQUIREMENTS
- [ ] Seamless integration with existing mesh
- [ ] Improved coverage in target areas
- [ ] Enhanced network performance metrics
- [ ] Automatic firmware updates completed
- [ ] Full HA sensor integration working

## 📝 POST-INSTALLATION NOTES
*Record any issues encountered, configuration changes made, or lessons learned during the installation process.*

---

**Preparation Complete** ✅
**Ready for U7 Lite Arrival** ✅
**Backup Status**: ⏳ Requires manual execution
**Ultra Access**: ⏳ Requires manual verification

*This guide ensures a smooth, well-documented U7 Lite installation with minimal risk to your existing network infrastructure.*