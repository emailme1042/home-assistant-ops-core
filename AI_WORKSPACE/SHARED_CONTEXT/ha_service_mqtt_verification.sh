# HA Service MQTT Verification (Non-Docker Fallback)
# For HA OS Add-ons or System Services
# Generated: November 13, 2025

# Check HA OS Add-on Status (Mosquitto MQTT)
ha addons info core_mosquitto

# Alternative: Check add-on logs
ha addons logs core_mosquitto --lines 20

# Restart Mosquitto add-on if needed
ha addons restart core_mosquitto

# Check ESPHome add-on status
ha addons info core_esphome

# Restart ESPHome add-on if needed
ha addons restart core_esphome

# System-level MQTT service check (if not using add-on)
sudo systemctl status mosquitto

# Restart system MQTT service
sudo systemctl restart mosquitto

# Check MQTT port listening
netstat -tlnp | grep :1883

# Test MQTT connectivity with mosquitto_pub (if installed)
mosquitto_pub -h localhost -t "test/topic" -m "test message"

# HA API entity count check (replace YOUR_TOKEN)
curl -H "Authorization: Bearer YOUR_LONG_LIVED_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     http://localhost:8123/api/states | jq '. | length'

# Count unavailable entities
curl -H "Authorization: Bearer YOUR_LONG_LIVED_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     http://localhost:8123/api/states | \
     jq '[.[] | select(.state == "unavailable")] | length'