# 🛡️ Emergency Access Setup Guide
**Date**: 2025-11-04  
**Purpose**: Prevent future lockouts from frontend compilation issues

## 🎯 **SSH Terminal Add-on Setup**

### **Step 1: Install SSH & Web Terminal**
1. **Navigate**: Settings → Add-ons → Add-on Store
2. **Search**: "SSH & Web Terminal" 
3. **Install**: Official Home Assistant add-on
4. **Configure**: See configuration below

### **Step 2: SSH Terminal Configuration**
```yaml
# Add-on Configuration (via Add-on UI)
apks: []
init_commands: []
packages: []
share_sessions: false
ssh:
  allow_agent_forwarding: false
  allow_remote_port_forwarding: false
  allow_tcp_forwarding: false
  authorized_keys: []
  compatibility_mode: false
  host_keys: []
  password: ""
  sftp: false
  username: hassio
zsh: true
```

### **Step 3: Enable Web Terminal**
- **Start the add-on**: Click "Start" 
- **Enable**: "Start on boot" and "Watchdog"
- **Open Web UI**: Click "Open Web UI" for terminal access

## 🔧 **Emergency Commands Reference**

### **Frontend Issues**
```bash
# Rebuild frontend compilation
ha core rebuild

# Restart HA Core  
ha core restart

# Full system restart
ha host reboot

# Check core status
ha core info
```

### **Diagnostic Commands**
```bash
# Check logs
ha core logs

# System information
ha info

# Add-on status
ha addons

# Check disk space
df -h
```

### **Recovery Commands**
```bash
# Safe mode boot
ha core options --safe-mode

# Check configuration
ha core check

# Backup creation
ha backups new --name "Emergency_$(date +%Y%m%d_%H%M)"
```

## 🚨 **Hardware Emergency Access**

### **HA Green Physical Controls**
- **Power Button**: Hold 5 seconds for hard restart
- **LED Indicators**: 
  - Blue: Booting
  - Green: Running normally
  - Yellow: Starting up
  - Red: Error state

### **Network Access Alternatives**
- **Direct IP**: http://192.168.1.217:8123
- **Local hostname**: http://homeassistant.local:8123
- **SSH Port 22222**: (if configured) `ssh root@192.168.1.217 -p 22222`

## 📋 **Recovery Protocols**

### **Frontend Compilation Failure**
1. **First**: Hard browser refresh (Ctrl+Shift+R)
2. **Second**: Incognito browser test
3. **Third**: SSH terminal → `ha core rebuild`
4. **Last resort**: Hardware restart button

### **Complete System Lockout**
1. **Hardware restart**: Hold power button 5 seconds
2. **Wait for boot**: Watch LED indicators
3. **SSH access**: Use terminal add-on when available
4. **Safe mode**: Boot with `--safe-mode` if needed

## ✅ **Post-Setup Verification**

### **Test SSH Access**
1. Go to Settings → Add-ons → SSH & Web Terminal
2. Click "Open Web UI"
3. Run: `ha core info`
4. Verify command executes successfully

### **Test Emergency Commands**
```bash
# Quick system check
ha info
ha core check
ha addons --installed
```

## 📊 **Emergency Contact Card**

| Issue Type | First Action | Backup Action |
|------------|--------------|---------------|
| Frontend broken | Browser refresh | SSH rebuild |
| UI lockout | Incognito test | Hardware restart |
| API timeout | Check logs | Full reboot |
| Entity errors | Configuration check | Safe mode |

**Status**: Emergency access protocols ready for implementation!