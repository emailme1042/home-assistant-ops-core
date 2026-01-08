# iOS Apps for Matter Device Setup Codes

## 🏠 Native iOS/HomeKit Apps
**Apple Home App** (Built-in)
- ✅ **Matter QR Code Scanning**: Can scan Matter device QR codes
- ✅ **Setup Code Display**: Shows codes when adding devices
- ✅ **Bulk Capability**: Can scan multiple devices quickly
- 📱 **How to Use**:
  1. Open Home app → + → Add Accessory
  2. Scan QR code on device
  3. Note the setup code displayed
  4. Don't complete pairing (cancel to keep code)

## 🔧 Manufacturer Apps (Device-Specific)

**Tapo App** (for Tapo Plugs)
- ✅ **Setup Codes**: Shows Matter codes for all Tapo devices
- ✅ **Device Management**: Lists all devices with codes
- 📱 **How to Get Codes**:
  1. Open Tapo app → Device list
  2. Select device → Settings → Matter → Setup Code

**Aqara Home App** (for Aqara Devices)
- ✅ **Matter Pairing**: Shows setup codes for Matter-enabled devices
- ✅ **Bulk View**: Can view codes for multiple devices
- 📱 **How to Get Codes**:
  1. Open Aqara Home → Device → More → Matter
  2. Setup code displayed for pairing

**Tado App** (for Tado Thermostat)
- ✅ **Matter Setup**: Provides setup code for Matter pairing
- 📱 **How to Get Codes**:
  1. Open Tado app → Device → Settings → Matter Setup

## 📱 QR Code & Matter Apps

**Matter QR Scanner** (Third-party)
- ✅ **Code Extraction**: Scans and decodes Matter QR codes
- ✅ **Bulk Scanning**: Can scan multiple devices quickly
- 📱 **Features**: Shows discriminator, setup PIN, and other details

**QR Code Reader by QR Code Team**
- ✅ **Matter Compatible**: Can decode Matter QR codes
- ✅ **Batch Scanning**: Scan multiple codes in sequence

## 🏡 Smart Home Hub Apps

**Google Home App**
- ✅ **Matter Support**: Can scan Matter QR codes
- ✅ **Code Display**: Shows setup codes during pairing
- 📱 **Alternative to Apple Home for code extraction**

## 📋 Recommended Workflow for Bulk Code Collection

### Method 1: Apple Home App (Fastest)
1. Open Apple Home app
2. Tap + → Add Accessory
3. Scan each device's QR code
4. Note the setup code displayed
5. Cancel pairing (don't complete)
6. Repeat for all devices

### Method 2: Manufacturer Apps
1. Open each brand's app (Tapo, Aqara, Tado)
2. Navigate to device settings
3. Find Matter setup section
4. Record codes for each device

### Method 3: QR Scanner App
1. Use Matter QR Scanner app
2. Scan QR codes on devices
3. App decodes and displays setup codes

## 💡 Pro Tips
- **QR Codes**: Most devices have QR codes on the device itself or in manual
- **Setup Codes**: 8-11 digit codes (e.g., 12345678 or 123-45-678)
- **Discriminators**: Usually 0x0000 for most devices
- **Save Codes**: Update `matter_device_codes.yaml` as you collect them

## 📱 App Download Links
- **Apple Home**: Pre-installed on iOS
- **Tapo**: App Store - "Tapo" by TP-Link
- **Aqara Home**: App Store - "Aqara Home" by Lumi United
- **Tado**: App Store - "Tado" by Tado GmbH
- **Google Home**: App Store - "Google Home"
- **Matter QR Scanner**: Search App Store for "Matter QR" or "CHIP QR"