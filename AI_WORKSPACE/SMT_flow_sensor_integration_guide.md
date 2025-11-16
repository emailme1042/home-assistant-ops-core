# 🔧 SMT-100/200 Flow Sensor Integration Guide

## 📋 **Supplier Device Compatibility**

**Your SMT-100/200 sensors are RS485/SDI-12/Modbus output** - not natively Zigbee. Integration requires a bridge device.

## 🎯 **Integration Options (Ranked by Ease)**

### 1. 🥇 **Tuya ZPMETER 214C-Z** (Easiest - £25-35)
**Why Best:** Built-in Zigbee, ultrasonic measurement, includes valve control
- **No DIY required** - plug-and-play Zigbee device
- **Direct ZHA integration** in Home Assistant
- **Built-in valve** for water control
- **Battery powered** (2x AA batteries)

**Setup:**
1. Pair with Zigbee coordinator (ZHA integration)
2. Configure in Home Assistant
3. Replace SMT-100/200 with ZPMETER on pipe

### 2. 🥈 **ESP32 + ESPHome Bridge** (Most Flexible - £15-25)
**Why Good:** Full control, restart-safe, expandable
- **Hardware:** ESP32 dev board + RS485 adapter (£5)
- **Software:** ESPHome firmware (free)
- **Integration:** Native ESPHome device in HA

**Setup:**
1. Flash ESPHome firmware to ESP32
2. Connect RS485 adapter to SMT-100/200
3. Configure UART/Modbus in ESPHome
4. Adopt device in Home Assistant

### 3. 🥉 **Zigbee Pulse Adapter (MC241)** (If SMT has pulse output)
**Why:** Direct Zigbee if sensor supports pulses
- **Hardware:** MC241 adapter (£10-15)
- **Check:** Confirm SMT-100/200 has pulse output mode
- **Integration:** ZHA pulse counter in HA

## 📊 **Expected Performance**

| Integration | Accuracy | Installation | Cost | Maintenance |
|-------------|----------|--------------|------|-------------|
| **Tuya ZPMETER** | ±2% | 15 min | £25-35 | Low |
| **ESPHome Bridge** | ±1% | 45 min | £15-25 | Low |
| **Pulse Adapter** | ±5% | 30 min | £10-15 | Medium |

## 🔄 **Migration Path**

### Phase 1: Test Integration (1-2 days)
- Choose integration method
- Install bridge device
- Validate flow readings in HA dashboard
- Monitor accuracy over 24 hours

### Phase 2: Replace Sensor (30 min)
- Remove SMT-100/200 from pipe
- Install new sensor/bridge
- Update HA configuration
- Test hot water detection

### Phase 3: Enhanced Monitoring (Ongoing)
- Separate heating vs hot water runtime
- Flow rate monitoring
- Leak detection alerts
- Energy usage correlation

## 📁 **Configuration Files Ready**

- `esphome_flow_sensor_bridge.yaml` - ESPHome configuration
- `zigbee_pulse_adapter_config.yaml` - Pulse adapter setup
- Boiler sensors updated to use flow data automatically

## 🎯 **Next Steps**

1. **Choose Integration:** Tuya ZPMETER recommended for simplicity
2. **Order Hardware:** Available on AliExpress/Amazon
3. **Test Setup:** When MQTT is available, we'll configure entities
4. **Monitor Results:** 24h validation period

**Ready to proceed with flow sensor integration?** 🚀