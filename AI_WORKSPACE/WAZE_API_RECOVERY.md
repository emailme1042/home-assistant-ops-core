# Waze Travel Time API Recovery Guide

## Current Status
- Waze Travel Time integration configured with correct coordinates
- Origin: 50.7771748874102, -1.8817954964919519
- Destination: 50.76366525952482, -1.99380844749706
- Region: Europe
- Error: "Failed to connect" - HA cannot reach Waze routing API

## Root Cause Analysis
The "Failed to connect" error indicates HA cannot communicate with Waze's servers, despite correct configuration. Common causes:

1. **No Internet Access**: HA Core lacks internet connectivity (common in Docker/VM setups)
2. **Firewall Blocking**: Outbound connections to waze.com blocked
3. **DNS Issues**: Cannot resolve waze.com domain
4. **Rate Limiting**: Waze API temporarily blocking requests
5. **Integration Bug**: HA Waze integration broken in current version

## Diagnostic Steps

### 1. Test Internet Connectivity
From HA terminal, run:
```bash
curl -I https://www.google.com
```
- Should return HTTP 200 OK
- If fails → No internet access from HA

### 2. Test DNS Resolution
```bash
nslookup www.waze.com
```
- Should return IP addresses
- If fails → DNS issues

### 3. Test Waze Domain Specifically
```bash
curl -I https://www.waze.com
```
- Should return HTTP response
- If fails → Waze domain blocked or unreachable

### 4. Check HA Logs
Look for Waze-related errors in HA logs:
```bash
grep -i waze /config/home-assistant.log
```

## Recovery Options

### Option 1: Restart HA Core
Sometimes a restart resolves temporary connectivity issues:
1. HA Settings → System → Restart Home Assistant
2. Wait 2-3 minutes
3. Test Waze integration again

### Option 2: Alternative Travel Time Integration

#### Google Travel Time (Requires API Key)
```yaml
sensor:
  - platform: google_travel_time
    api_key: !secret google_maps_api_key
    origin: 50.7771748874102, -1.8817954964919519
    destination: 50.76366525952482, -1.99380844749706
    options:
      mode: driving
      units: imperial
      traffic_model: best_guess
```

#### HERE Travel Time (Requires API Key)
```yaml
sensor:
  - platform: here_travel_time
    api_key: !secret here_api_key
    origin: 50.7771748874102, -1.8817954964919519
    destination: 50.76366525952482, -1.99380844749706
    mode: car
```

### Option 3: Template Sensor Fallback
Static ETA based on average travel time:
```yaml
sensor:
  - platform: template
    sensors:
      home_to_work_eta:
        friendly_name: "Home to Work ETA"
        value_template: "25"
        unit_of_measurement: "min"
        device_class: duration
        icon: mdi:car-clock
```

## Implementation Steps

1. **Diagnose Connectivity**: Run the curl/nslookup tests above
2. **Restart HA**: If connectivity works, restart may fix it
3. **Choose Alternative**: If Waze remains broken, implement Google Travel Time
4. **Test Integration**: Verify sensor appears in Developer Tools → States
5. **Update Dashboards**: Replace Waze sensor references with new sensor

## Required Secrets (for alternatives)
Add to `secrets.yaml`:
```yaml
google_maps_api_key: YOUR_GOOGLE_MAPS_API_KEY
here_api_key: YOUR_HERE_API_KEY
```

## Next Steps
1. Run connectivity diagnostics
2. Restart HA if internet works
3. Implement Google Travel Time alternative
4. Test and validate new sensor
5. Update any dashboard references</content>
<parameter name="filePath">s:\AI_WORKSPACE\WAZE_API_RECOVERY.md