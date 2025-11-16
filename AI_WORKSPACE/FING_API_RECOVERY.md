# Fing Local API Recovery Guide

## Current Status

- Fing Local API enabled on 192.168.1.200:49090
- API Key: fing_loc_api123
- HA sensor configured in `includes/sensors/fing_local_api.yaml`
- Port connectivity confirmed (TcpTestSucceeded: True)
- API endpoint test failed with protocol violation error

## Diagnostic Steps

### 1. Verify Fing Agent Status

- Confirm Fing Desktop/Fingbox is running on 192.168.1.200
- Check Fing logs for API startup messages
- Ensure Local API is enabled in Settings → Advanced

### 2. Test Endpoint from Fing Host

From the machine running Fing (192.168.1.200), open browser to:

```bash
http://localhost:49090/1/devices?auth=fing_loc_api123
http://localhost:49090/1/people?auth=fing_loc_api123
```

- Should return JSON data
- If not, check Fing configuration

### 3. Network Connectivity

- HA (192.168.1.217) can reach 192.168.1.200:49090 (confirmed)
- No firewall blocking port 49090 on Fing host
- Both devices on same subnet (192.168.1.0/24)

### 4. HA Sensor Configuration

Current config uses REST sensor with auth parameter.
If API test fails, try alternative config:

```yaml
sensor:
  - platform: rest
    name: Fing Devices
    resource: http://192.168.1.200:49090/1/devices?auth=fing_loc_api123
    method: GET
    value_template: "{{ value_json.networkId }}"
    json_attributes_path: "$.devices"
    json_attributes:
      - mac
      - ip
      - name
      - state
```

## Fallback Options

### Mock Data Sensor (for testing)

```yaml
sensor:
  - platform: template
    sensors:
      fing_devices_mock:
        friendly_name: "Fing Devices (Mock)"
        value_template: "3"
        attribute_templates:
          devices: >
            [{"mac": "AA:BB:CC:DD:EE:FF", "ip": "192.168.1.100", "name": "Mock Device", "state": "online"}]
```

### Alternative Integration

- Consider MQTT bridge if Fing supports it
- Use Fing mobile app webhooks
- Implement via Node-RED or custom script

## Next Steps

1. Test endpoint from Fing host directly
2. Check Fing agent logs
3. If API works locally but not remotely, investigate network/firewall
4. Update HA sensor config if needed
5. Restart HA after changes
