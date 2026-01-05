# ESPHome Device Sync Troubleshooting Guide
**Date:** January 3, 2026
**Issue:** Can't sync/flash ESPHome to ESP devices - IP addresses wrong from old router

## 🔍 Your Specific Issue: IP Address Migration

**Problem:** Your ESP32 devices have old 192.168.1.x IPs flashed, but your network is now 192.168.0.x. Devices can't connect to update via OTA.

**Solution:** Flash devices via USB with updated YAML configs containing new IPs.

### ✅ Your YAML Files Are Ready
Both configs have been updated with correct IPs:
- **atom-lite-btproxy.yaml**: Static IP `192.168.0.129`
- **new-esp.yaml**: Static IP `192.168.0.183`

**Wi-Fi Settings:** Both use SSID "Bogey Pie WiFi" with your password.

### 📋 Quick Action Plan

1. **Install ESPHome Add-on** (if not already installed)
2. **Open ESPHome Web UI** at `http://your-ha-ip:6052`
3. **Create/Edit Devices** with the updated YAML files
4. **Flash Each ESP32** via USB connection
5. **Verify** devices connect with new IPs

**Status:** YAML files updated ✅ | ESPHome add-on needed | USB flash required for IP update

## 🔧 Recent Compilation Fix
**Issue:** Lambda functions using `optional<string>` causing compilation errors
**Fix:** Updated to `optional<std::string>` for proper C++ namespace resolution
**Files Updated:** `new-esp.yaml` - Scanner Location and Boot Time sensors fixed

## 🛠️ Step-by-Step IP Update Process

## 🏠 HA ESPHome Add-on Method (Easiest)

Since ESPHome isn't installed via pip, use the HA ESPHome add-on:

1. **Go to HA Add-ons:**
   - HA → Settings → Add-ons
   - Find "ESPHome" add-on
   - If not installed: Add repository `https://github.com/esphome/home-assistant-addon`
   - Install and start the add-on

2. **Access ESPHome Dashboard:**
   - Click "Open Web UI" on the ESPHome add-on
   - Or go to: `http://your-ha-ip:6052`

3. **Upload Your YAML Files:**
   - Click "New Device" or "Edit" existing
   - Copy-paste content from:
     - `esphome/atom-lite-btproxy.yaml` (IP: 192.168.0.129)
     - `esphome/new-esp.yaml` (IP: 192.168.0.183)
   - Save and validate

4. **Flash via USB:**
   - Connect ESP32 to computer USB
   - Click "Install" → "Plug into this computer"
   - Select the COM port when prompted
   - Wait for flash to complete

5. **Verify Connection:**
   - Device should connect to Wi-Fi with new IP
   - Check HA for new entities
   - Blue LED should be steady (not blinking)

### Method 2: Command Line (if add-on not available)

1. **Install ESPHome:**
   ```bash
   pip install esphome
   ```

2. **Validate Config:**
   ```bash
   esphome config esphome/atom-lite-btproxy.yaml
   esphome config esphome/new-esp.yaml
   ```

3. **Flash Devices:**
   ```bash
   # For atom-lite-btproxy
   esphome run esphome/atom-lite-btproxy.yaml --device COM3
   
   # For new-esp  
   esphome run esphome/new-esp.yaml --device COM4
   ```
   *Replace COM3/COM4 with your actual COM ports*

## 🔧 Common Issues During IP Update

### Device Won't Connect After Flash
- **Check Wi-Fi Credentials:** Ensure SSID "Bogey Pie WiFi" and password are correct
- **Power Cycle:** Unplug ESP32, wait 10 seconds, plug back in
- **Check Router:** Ensure new IP range (192.168.0.x) is allowed
- **LED Status:** Look for steady blue LED (connected) vs blinking (connecting)

### USB Flash Fails
- **Use USB 2.0 Port:** Avoid USB 3.0 ports/hubs
- **Different Cable:** Try a different USB cable
- **Device Manager:** Check Windows Device Manager for COM port
- **Run as Admin:** Run command prompt as Administrator

### OTA Update (After Initial USB Flash)
Once devices connect with new IPs, future updates can be OTA:
```bash
esphome run esphome/atom-lite-btproxy.yaml --device 192.168.0.129
```

## 📋 Verification Steps

1. **After Flash:** Check HA for new device entities
2. **IP Confirmation:** Devices should appear at 192.168.0.129 and 192.168.0.183
3. **Bluetooth Proxy:** Check if BLE devices are detected
4. **Logs:** Monitor ESPHome logs for connection status

## 🚨 If Still Having Issues

- **Share Error Messages:** Exact error from ESPHome commands
- **Device LEDs:** Describe LED behavior (blinking pattern, colors)
- **Network Setup:** Confirm router settings allow static IPs
- **Try One Device:** Start with one ESP32 to isolate issues

## 🚨 ESPHome Timeout Error Fix

**Error:** `TimeoutExpired: Command '['/root/.platformio/penv/bin/uv', 'pip', 'install'...'] timed out after 60 seconds`

**Cause:** ESPHome add-on timing out during dependency installation (esptoolpy package)

### ✅ Quick Fixes to Try

**1. Restart ESPHome Add-on:**
- HA → Settings → Add-ons → ESPHome → Stop
- Wait 10 seconds
- Start again
- Try compilation immediately

**2. Clear ESPHome Cache:**
- In ESPHome dashboard, go to "Secrets" tab
- Click the trash icon to clear cache
- Try compilation again

**3. Check Network:**
- Ensure HA has stable internet connection
- Try restarting HA if network issues suspected

**4. Alternative: Use External ESPHome**
If add-on keeps timing out, use external ESPHome installation:

**Install ESPHome via pip:**
```bash
# In a terminal/command prompt
pip install esphome
```

**Then flash directly:**
```bash
esphome run esphome/new-esp.yaml --device COM3
esphome run esphome/atom-lite-btproxy.yaml --device COM4
```

**5. ESPHome Add-on Configuration:**
- Go to ESPHome add-on configuration
- Try increasing timeout if available
- Or disable "Wait for network" option

### 📊 Expected Results
- **After restart:** Compilation should proceed without timeout
- **After cache clear:** Dependencies reinstall faster
- **External ESPHome:** Bypasses add-on timeout issues entirely

## 🚨 ESPHome Build System Error Fix

**Error:** `esp_netif_lwip.c.o: No such file or directory` + `Error 1`

**Cause:** PlatformIO build cache corruption or missing ESP-IDF components

### ✅ Build System Fixes

**1. Clean ESPHome Build Cache:**
- In ESPHome dashboard, go to device settings (3 dots)
- Click **"Clean Build Files"**
- Try compilation again

**2. Clear PlatformIO Cache (More Thorough):**
- Stop ESPHome add-on
- SSH into HA or use terminal
- Run: `rm -rf /data/cache/platformio`
- Start ESPHome add-on again
- Try compilation (will redownload dependencies)

**3. Restart ESPHome Add-on:**
- HA → Settings → Add-ons → ESPHome → Stop
- Wait 30 seconds
- Start again
- Try compilation immediately

**4. Try Different ESPHome Version:**
- In ESPHome add-on configuration
- Change version to `2025.11.0` (stable version)
- Restart add-on
- Try compilation

**5. Alternative: Use External ESPHome**
If add-on issues persist:
```bash
# Install ESPHome
pip install esphome

# Clean any existing builds
esphome clean esphome/new-esp.yaml

# Try compilation
esphome compile esphome/new-esp.yaml
```

### 📊 Expected Results
- **After cache clean:** Build system redownloads missing components
- **After restart:** Fresh build environment
- **Different version:** May avoid ESP-IDF compatibility issues
- **External ESPHome:** Bypasses add-on build cache issues

## 🚨 ESPHome Clean Build Files Error Fix

**Error:** `ERROR Error deleting build files: [Errno 39] Directory not empty: '/data/build/newesp/.pioenvs/newesp/lwip/lwip/src/netif/ppp'`

**Cause:** Build directory has locked or permission-protected files preventing cleanup

### ✅ Clean Build Directory Fixes

**1. Manual Directory Cleanup (Via SSH/Terminal):**
```bash
# SSH into HA or use terminal
cd /data/build/newesp
rm -rf .pioenvs
# If that fails, try with force
rm -rf .pioenvs/*
rmdir .pioenvs
```

**2. Stop ESPHome Add-on First:**
- HA → Settings → Add-ons → ESPHome → **Stop**
- Wait 10 seconds
- Try cleaning build files again
- Start add-on after cleanup

**3. Force Clean via Terminal:**
```bash
# Stop add-on first
ha addons stop local_esphome

# Force remove build directory
rm -rf /data/build/newesp

# Start add-on
ha addons start local_esphome
```

**4. Alternative: Fresh Device Setup**
If cleanup fails repeatedly:
- In ESPHome dashboard, **delete the device** completely
- **Create new device** with the same YAML
- This gives you a completely clean build environment

**5. External ESPHome Clean:**
```bash
# If using external ESPHome
esphome clean esphome/new-esp.yaml --force
```

### 📊 Expected Results
- **Manual cleanup:** Removes stuck build files
- **Stop/start add-on:** Releases file locks
- **Force remove:** Completely cleans build directory
- **Fresh device:** Eliminates all build cache issues

## 🔍 WiFi/AP Connection Issues

**Problem:** Device shows SSID but you can't connect to it

### ✅ AP vs Main WiFi Explanation

**Your atom-lite-btproxy.yaml has TWO networks:**

1. **Main WiFi (what you should connect TO):**
   - SSID: `"Bogey Pie WiFi"`
   - Password: `"Fartbum10.11"`
   - Static IP: `192.168.0.129`

2. **Fallback AP (captive portal - device CREATES this when WiFi fails):**
   - SSID: `"Atom-Lite-Btproxy"`
   - Password: `"iaAGiqhQ0A67"`

### 🔍 Which SSID Are You Seeing?

**If you see "Bogey Pie WiFi":**
- This is your main router WiFi
- Device should connect to this automatically
- If you can't connect, check your device WiFi settings

**If you see "Atom-Lite-Btproxy":**
- Device is in AP/captive portal mode
- Can't connect to main WiFi (probably due to IP issues)
- Connect to this AP to access device captive portal
- Password: `"iaAGiqhQ0A67"`

### 📋 Troubleshooting Steps

1. **Check which SSID appears** when device powers on
2. **If "Atom-Lite-Btproxy" appears:** Device can't reach main WiFi
3. **Connect to AP** and go to `192.168.4.1` in browser
4. **Check WiFi settings** in captive portal
5. **Verify main WiFi credentials** match your router

**If you see "Atom-Lite-Btproxy" but can't connect:**

### 🔧 Captive Portal Connection Issues

**Problem:** Can see AP SSID but can't connect even with correct password

**Possible Causes:**
1. **Wrong Password Attempts** - Too many failed attempts lock out connections
2. **Device Power Cycle** - Device needs restart to properly enter AP mode
3. **WiFi Interference** - Other networks interfering
4. **Device Hardware Issue** - ESP32 WiFi module problem

**Fix Steps:**
1. **Power cycle device:** Unplug ESP32 for 30 seconds, plug back in
2. **Wait for AP to appear** (may take 30-60 seconds)
3. **Try different device:** Connect with phone instead of computer
4. **Check password:** `"iaAGiqhQ0A67"` (case-sensitive)
5. **Forget network:** On your device, forget "Atom-Lite-Btproxy" and reconnect

**If AP connection works:**
- Open browser to `192.168.4.1`
- Should see ESPHome captive portal
- Check WiFi settings and try reconnecting to main WiFi

**If AP still doesn't work:**
- Device may have hardware issues
- Try USB flashing directly (bypass WiFi entirely)

---

## 🌐 IP CHANGE RECOVERY: Devices Already Flashed

**Your Situation:** 2 ESP32 devices already flashed, but IP subnet changed from 192.168.1.x to 192.168.0.x

### Step 1: Find Current Device IPs
**Method A - Router Admin:**
- Log into router: `192.168.0.1`
- Check connected devices list
- Look for devices with names like "atom-lite-btproxy", "newesp", or ESP-handshake

**Method B - Network Scan:**
```bash
# Install nmap if needed
# Scan for ESP devices
nmap -sn 192.168.0.0/24 | findstr "esp"
```

**Method C - Check HA Logs:**
- HA → Settings → System → Logs
- Look for ESPHome connection attempts
- Note any IP addresses mentioned

### Step 2: Check if Devices are in AP Mode
If devices can't connect to WiFi (due to wrong static IP), they create a hotspot:
- Look for WiFi networks: "Atom-Lite-Btproxy" or "Newesp"
- Connect to the hotspot (password in YAML)
- Access device at: `192.168.4.1`
- Update WiFi settings via web interface

### Step 3: OTA Update (If Device IP Found)
```bash
# Update atom-lite-btproxy
esphome run esphome/atom-lite-btproxy.yaml --device 192.168.0.129

# Update new-esp
esphome run esphome/new-esp.yaml --device 192.168.0.183
```

### Step 4: USB Flash (If OTA Fails)
```bash
# Find COM port in Device Manager
# Flash atom-lite-btproxy
esphome run esphome/atom-lite-btproxy.yaml --device COM3

# Flash new-esp
esphome run esphome/new-esp.yaml --device COM4
```

### Step 5: Verify Success
- Check HA for new device entities
- Confirm devices show "Online" status
- Test Bluetooth proxy functionality

**Your YAML files are already updated for the new IP subnet (192.168.0.x), so once you connect to the devices, the OTA update should work.**