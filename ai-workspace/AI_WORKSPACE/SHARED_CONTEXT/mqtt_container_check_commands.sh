# MQTT/Container Status Check Command Block
# Generated for HA recovery protocol - November 13, 2025

# Check running containers for ESPHome, MQTT, and Mosquitto
docker ps | grep -E "(esphome|mqtt|mosquitto)"

# Alternative: Check all containers (running and stopped)
docker ps -a | grep -E "(esphome|mqtt|mosquitto)"

# Check container logs for recent activity (last 50 lines)
# Replace CONTAINER_NAME with actual container name
docker logs --tail 50 CONTAINER_NAME

# Check if Mosquitto MQTT broker is listening on port 1883
netstat -tlnp | grep :1883

# Alternative: Use PowerShell to check port
Get-NetTCPConnection -LocalPort 1883 -State Listen

# Check MQTT broker service status (if running as system service)
sudo systemctl status mosquitto

# Restart MQTT broker if needed
sudo systemctl restart mosquitto

# Check ESPHome container restart policy
docker inspect CONTAINER_NAME | grep -A 10 "RestartPolicy"

# View ESPHome logs for restart reasons
docker logs --tail 100 CONTAINER_NAME | grep -i restart