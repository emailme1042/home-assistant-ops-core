# Z2M Setup Guide - Vibration Sensor Away from Aqara Hub
# Run these commands in sequence:

# 1. Install Zigbee2MQTT as Docker container
docker run -d \
  --name zigbee2mqtt \
  --restart unless-stopped \
  --device /dev/ttyUSB0 \
  -p 8099:8080 \
  -v /config/zigbee2mqtt:/app/data \
  -e TZ=Europe/London \
  koenkk/zigbee2mqtt:latest

# 2. Check if container is running
docker ps | grep zigbee2mqtt

# 3. Access Z2M web interface at http://localhost:8099
# Default login: admin/admin (change immediately)

# 4. Permit join for 5 minutes to add vibration sensor
# In Z2M web UI: Settings → Permit Join → Enable for 300 seconds

# 5. Factory reset vibration sensor (if needed)
# Press and hold reset button for 5+ seconds until LED flashes rapidly

# 6. Add sensor away from Aqara hub for better mesh routing
# Place vibration sensor:
# - At least 3-5 meters from Aqara hub
# - Line-of-sight if possible
# - Away from metal objects/large appliances
# - Near thermostats for vibration detection

# 7. Verify pairing in Z2M web UI
# Should appear as "Aqara_Vibration_Sensor" or similar

# 8. Update HA configuration to use Z2M entities instead of Aqara integration
# Replace entity IDs in boiler monitoring sensors</content>
<parameter name="filePath">S:\AI_WORKSPACE\z2m_vibration_sensor_setup.md