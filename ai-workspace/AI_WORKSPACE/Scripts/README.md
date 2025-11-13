# MQTT Broker Test Script

This folder contains `mqtt_test.py`, a comprehensive MQTT broker testing script for Home Assistant. The script performs:

1. Connection testing to verify broker availability
2. Message publishing tests across multiple topics
3. Subscription verification 
4. Broker statistics collection

## Usage

```powershell
python3 mqtt_test.py --host localhost --port 1883 --user mqtt_user --password your_password
```

## Features

- Tests basic connectivity to MQTT broker
- Publishes test messages with different formats (plain text, JSON, retained)
- Subscribes to test topics to verify message receipt
- Collects broker statistics from $SYS topics
- Provides detailed test report with emojis for visual status

## Example Output

```
🔍 Testing MQTT Broker Connection
--------------------------------------------------
✅ Connected to broker at localhost:1883

📤 Testing Message Publishing
--------------------------------------------------
📤 Publishing to homeassistant/test/connection: test_message
📤 Publishing to homeassistant/test/json: {"test": "value"}
📤 Publishing to homeassistant/test/retained: retained_message

📩 Testing Message Subscription  
--------------------------------------------------
👂 Subscribed to homeassistant/test/#
📩 Received on homeassistant/test/connection: test_message
📩 Received on homeassistant/test/json: {"test": "value"}
📩 Received on homeassistant/test/retained: retained_message

📊 Checking Broker Statistics
--------------------------------------------------
Broker Statistics:
  $SYS/broker/version: 2.0.15
  $SYS/broker/uptime: 1234567
  $SYS/broker/clients/total: 5
  ...

📋 Test Summary
--------------------------------------------------
Connection: ✅
Published Messages: 3
Received Topics: 3
Overall Status: ✅ PASS
```

## Parameters

- `--host`: MQTT broker hostname (default: localhost)
- `--port`: MQTT broker port (default: 1883)
- `--user`: MQTT username (required)
- `--password`: MQTT password (required)

## Integration with Home Assistant

This script is part of the MQTT monitoring infrastructure. It can be called from:

1. Shell commands in `configuration.yaml`
2. The MQTT status dashboard
3. Automation scripts

## Dependencies

Requires `paho-mqtt` package. Install with:

```powershell
pip install paho-mqtt
```