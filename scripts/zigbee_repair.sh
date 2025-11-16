#!/bin/bash
# Zigbee2MQTT Socket Recovery Script
# Usage: ./zigbee_repair.sh

# LQI refresh for all devices
mosquitto_pub -h 127.0.0.1 -u homeassistant -P YOUR_PASSWORD -t zigbee2mqtt/bridge/request/device/lqi -m "{}"

# Interview Sonoff socket Z1
mosquitto_pub -h 127.0.0.1 -u homeassistant -P YOUR_PASSWORD -t zigbee2mqtt/bridge/request/device/interview -m '{"device":"socket Z1"}'

# Interview Sonoff socket Z2
mosquitto_pub -h 127.0.0.1 -u homeassistant -P YOUR_PASSWORD -t zigbee2mqtt/bridge/request/device/interview -m '{"device":"socket Z2"}'

# Permit join for 120 seconds
mosquitto_pub -h 127.0.0.1 -u homeassistant -P YOUR_PASSWORD -t zigbee2mqtt/bridge/request/permit_join -m '{"value":true,"time":120}'

# End permit join
sleep 120
mosquitto_pub -h 127.0.0.1 -u homeassistant -P YOUR_PASSWORD -t zigbee2mqtt/bridge/request/permit_join -m '{"value":false}'

# Log message
logger "Zigbee socket recovery protocol completed."
