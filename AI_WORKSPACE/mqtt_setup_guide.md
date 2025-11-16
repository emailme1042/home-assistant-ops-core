# Mosquitto Add-on Setup Guide

## Quick Install Steps
1. Open Home Assistant → Supervisor → Add-on Store
2. Search for "Mosquitto broker"
3. Click "Install"
4. Use configuration below after install

## Recommended Add-on Configuration

### Basic Setup (localhost only)
```yaml
logins:
  - username: mqtt_user
    password: strong_unique_password_here
customize:
  active: false
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
```

### Advanced Setup (network accessible)
```yaml
logins:
  - username: mqtt_user
    password: strong_unique_password_here
  - username: readonly_user          # Optional read-only user for external tools
    password: another_strong_pass
    readonly: true
customize:
  active: true
  folder: mosquitto
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false
```

### Full Configuration with All Options
```yaml
# Logins - at least one required
logins:
  - username: mqtt_user
    password: strong_unique_password_here
    readonly: false    # false = read/write (default)
  - username: readonly_user
    password: another_strong_pass
    readonly: true     # true = read-only access

# Custom config
customize:
  active: true
  folder: mosquitto     # folder in /share for custom configs

# SSL/TLS certificates (optional but recommended)
certfile: fullchain.pem
keyfile: privkey.pem
require_certificate: false

# Network settings
anonymous: false        # Never enable anonymous access
```

## Network Access Configuration

### Option A: Local Network Only (recommended)
1. Set network mode to "host" in add-on Network tab
2. Port 1883 will be available on your HA host IP
3. Configure firewall to limit access to trusted IPs

### Option B: Isolated Mode
1. Leave network settings as default
2. Only Home Assistant will be able to connect
3. Perfect for simple setups where external access isn't needed

## After Installation

1. Start the add-on and check logs for successful startup
2. Add the MQTT integration:
   - Go to Configuration → Integrations
   - Add Integration → MQTT
   - Use these settings:
     ```yaml
     Broker: localhost  # or 127.0.0.1
     Port: 1883
     Username: mqtt_user
     Password: [password from add-on config]
     ```

## Security Recommendations

1. Always use strong unique passwords
2. Never enable anonymous access
3. Use readonly users for monitoring tools
4. Enable SSL/TLS if exposing to network
5. Consider network isolation (Option B) if external access isn't needed

## Testing the Installation

### 1. Via Home Assistant UI
- Check add-on logs for successful startup
- Watch States page after adding MQTT integration
- Enable MQTT discovery and verify auto-discovery works

### 2. Via Command Line (if network access enabled)
```powershell
# Install mosquitto_pub/sub tools first
# Test publishing:
mosquitto_pub -h YOUR_HA_IP -p 1883 -u mqtt_user -P your_password -t "test/topic" -m "test message"

# Test subscribing:
mosquitto_sub -h YOUR_HA_IP -p 1883 -u mqtt_user -P your_password -t "test/#" -v
```

## Common Issues & Solutions

### 1. Connection Refused
- Check username/password in integration matches add-on
- Verify broker host is correct (use `localhost` for add-on)
- Confirm port 1883 isn't blocked

### 2. Add-on Won't Start
- Check logs for permission errors
- Verify custom config syntax if enabled
- Ensure no port conflicts

### 3. Clients Can't Connect
- Verify network mode is "host" if needed
- Check firewall rules
- Confirm client credentials

## Support Files

### Example mosquitto.conf
Create this at `/share/mosquitto/mosquitto.conf` if using custom config:
```conf
listener 1883
protocol mqtt

# Uncomment to enable websockets
# listener 9001
# protocol websockets

persistence true
persistence_location /data/

# Logging (adjust as needed)
log_dest stdout
log_type error
log_type warning
connection_messages true

# Security
allow_anonymous false
password_file /data/auth
```

## References
- [Official Mosquitto Documentation](https://mosquitto.org/documentation/)
- [Home Assistant MQTT Integration](https://www.home-assistant.io/integrations/mqtt/)
- [Mosquitto Add-on Documentation](https://github.com/home-assistant/hassio-addons/tree/master/mosquitto)