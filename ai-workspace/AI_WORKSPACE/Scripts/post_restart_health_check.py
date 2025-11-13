# Post-Restart Validation Script
# Run this after HA restart to check if our fixes worked

import requests
import json
from datetime import datetime

def check_ha_health():
    print("🏥 Post-Restart Health Check")
    print("=" * 40)
    print(f"⏰ Check Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Check if HA is responding
        response = requests.get('http://localhost:8123', timeout=5)
        if response.status_code == 200:
            print("✅ Home Assistant is responding")
        else:
            print(f"⚠️ HA response code: {response.status_code}")
    except Exception as e:
        print(f"❌ HA not responding: {e}")
        return False
    
    # Check for our new sensors
    expected_sensors = [
        'sensor.ha_total_entities',
        'sensor.ha_unavailable_entities_count', 
        'sensor.ha_system_health_percentage',
        'sensor.ha_system_health_grade'
    ]
    
    print("\n📊 New Health Sensors:")
    print("-" * 25)
    
    for sensor in expected_sensors:
        try:
            # This would need HA API token in real implementation
            print(f"🔍 {sensor}: Check manually in Developer Tools")
        except:
            pass
    
    print("\n🎯 Manual Validation Steps:")
    print("1. Visit Developer Tools → States")
    print("2. Search for 'ha_system_health' entities")
    print("3. Check System Fixes dashboard in sidebar")
    print("4. Look for 'Entity not found' errors")
    print("5. Check browser console for CustomElementRegistry errors")
    
    print("\n✅ If all sensors show values (not 'unknown'), fixes worked!")
    print("❌ If still 'Entity not found', check HA logs for template errors")

if __name__ == "__main__":
    check_ha_health()