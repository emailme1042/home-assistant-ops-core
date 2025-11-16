#!/bin/bash
# Zigbee Full Recovery Script
# Usage: ./zigbee_full_repair.sh

# Credentials
MQTT_HOST="127.0.0.1"
MQTT_USER="homeassistant"
MQTT_PASS="YOUR_PASSWORD"

# Devices
DEVICES=("socket Z1" "socket Z2" "socket Z3")

# Step 1: Trigger full LQI refresh
mosquitto_pub -h $MQTT_HOST -u $MQTT_USER -P $MQTT_PASS -t zigbee2mqtt/bridge/request/device/lqi -m "{}"

# Step 2: Interview each socket
for DEVICE in "${DEVICES[@]}"; do
  mosquitto_pub -h $MQTT_HOST -u $MQTT_USER -P $MQTT_PASS -t "zigbee2mqtt/bridge/request/device/interview/$DEVICE" -m "{}"
done

# Step 3: Enable permit join for 60 seconds
mosquitto_pub -h $MQTT_HOST -u $MQTT_USER -P $MQTT_PASS -t zigbee2mqtt/bridge/request/permit_join -m "true"
sleep 60
mosquitto_pub -h $MQTT_HOST -u $MQTT_USER -P $MQTT_PASS -t zigbee2mqtt/bridge/request/permit_join -m "false"

# Optional: Log entry trigger or dashboard refresh
echo "Zigbee recovery protocol executed at $(date)" >> /config/logs/zigbee_repair.log
