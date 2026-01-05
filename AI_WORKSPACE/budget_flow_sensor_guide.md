# CHEAPER FLOW SENSOR ALTERNATIVES (£20-50 range)
# Since Tuya ZPMETER is £160, here are budget options:

## 🔥 TOP BUDGET RECOMMENDATION: DIGITEN Water Flow Sensor (£15-25)
- **Price**: £15-25 on Amazon/AliExpress
- **Type**: Hall effect turbine sensor (G1/2" threads)
- **Output**: Pulse output (needs ESP32/Zigbee adapter)
- **Accuracy**: ±2-3% (acceptable for usage detection)
- **Installation**: Easy - BSP threads, hot water pipe

## 🏗️ INTEGRATION OPTIONS:

### Option A: ESP32 Pulse Counter (£20 total)
```
ESP32 + DIGITEN Sensor = £35 total
- ESP32 Dev Board: £5
- DIGITEN Flow Sensor: £15
- ESPHome firmware: Free
- Zigbee/WiFi integration
```

### Option B: Zigbee Pulse Adapter (£30 total)
```
DIGITEN Sensor + MC241 Adapter = £35 total
- DIGITEN Flow Sensor: £15
- Sonoff/MC241 Zigbee Adapter: £20
- Direct ZHA integration
```

## 📊 EXPECTED PERFORMANCE:
- ✅ **Hot Water Detection**: 95%+ accuracy (much better than estimation)
- ✅ **Flow Rate Monitoring**: Real-time usage intensity
- ✅ **Leak Detection**: Basic monitoring capability
- ⚠️ **Total Volume**: Less accurate than ultrasonic sensors

## 🛠️ INSTALLATION:
1. **Pipe Prep**: Turn off water, drain pipe section
2. **Sensor Mount**: Install on hot water outlet from boiler
3. **Adapter Setup**: Configure ESP32/MC241 with pulse counting
4. **HA Integration**: Add as sensor with flow rate calculations

## 💰 COST COMPARISON:
- **Tuya ZPMETER**: £160 (ultrasonic, built-in Zigbee, valve)
- **DIGITEN + ESP32**: £35 (turbine, needs adapter, no valve)
- **DIGITEN + MC241**: £35 (turbine, Zigbee adapter, no valve)

## 🎯 RECOMMENDATION:
**Go with DIGITEN + ESP32** - £35 total gives you 95% of the functionality at 1/5 the cost!