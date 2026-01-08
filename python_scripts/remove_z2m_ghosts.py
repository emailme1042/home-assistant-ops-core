#!/usr/bin/env python3
"""
Z2M Ghost Entity Remover
Removes Zigbee2MQTT ghost entities that remain after Z2M removal
"""

import requests
import json
import sys
import os

# HA API configuration
HA_URL = "http://192.168.0.217:8123"  # Update if different
HA_TOKEN = os.getenv('HA_TOKEN') or input("Enter HA API token: ")

# Headers for API calls
HEADERS = {
    'Authorization': f'Bearer {HA_TOKEN}',
    'Content-Type': 'application/json'
}

# Z2M ghost entities to remove
GHOST_ENTITIES = [
    # Binary sensors
    'binary_sensor.zigbee2mqtt_bridge_connection_state',
    'binary_sensor.zigbee2mqtt_bridge_restart_required',
    'binary_sensor.zigbee2mqtt_running',

    # Buttons
    'button.zigbee2mqtt_bridge_restart',

    # Selects
    'select.zigbee2mqtt_bridge_log_level',

    # Sensors
    'sensor.zigbee2mqtt_bridge_coordinator_version',
    'sensor.zigbee2mqtt_bridge_network_map',
    'sensor.zigbee2mqtt_bridge_version',
    'sensor.zigbee2mqtt_cpu_percent',
    'sensor.zigbee2mqtt_memory_percent',
    'sensor.zigbee2mqtt_newest_version',
    'sensor.zigbee2mqtt_version',

    # Switches
    'switch.zigbee2mqtt',
    'switch.zigbee2mqtt_bridge_permit_join',
    'switch.zigbee2mqtt_networkmap_card_pre_release',

    # Updates
    'update.zigbee2mqtt_networkmap_card_update',
    'update.zigbee2mqtt_update'
]

# Z2M ghost automations to remove
GHOST_AUTOMATIONS = [
    'automation.restart_zigbee2mqtt_if_mesh_fails',
    'automation.zigbee2mqtt_bridge_restart_required_alert',
    'automation.zigbee2mqtt_bridge_connection_lost_alert',
    'automation.zigbee2mqtt_bridge_connection_restored_alert',
    'automation.zigbee2mqtt_bridge_restart_required_alert'
]

def remove_entity(entity_id):
    """Remove a single entity via HA API"""
    url = f"{HA_URL}/api/states/{entity_id}"

    try:
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"✅ Removed: {entity_id}")
            return True
        elif response.status_code == 404:
            print(f"⚠️  Not found: {entity_id}")
            return True
        else:
            print(f"❌ Failed to remove {entity_id}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error removing {entity_id}: {str(e)}")
        return False

def remove_automation(automation_id):
    """Remove a single automation via HA API"""
    url = f"{HA_URL}/api/config/automation/config/{automation_id}"

    try:
        response = requests.delete(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"✅ Removed automation: {automation_id}")
            return True
        elif response.status_code == 404:
            print(f"⚠️  Automation not found: {automation_id}")
            return True
        else:
            print(f"❌ Failed to remove automation {automation_id}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error removing automation {automation_id}: {str(e)}")
        return False

def main():
    print("🧟 Z2M Ghost Entity Remover")
    print("=" * 40)

    # Test API connection
    try:
        response = requests.get(f"{HA_URL}/api/", headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ API connection failed: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Cannot connect to HA API: {str(e)}")
        sys.exit(1)

    print("✅ Connected to HA API")

    # Remove entities
    print(f"\n🗑️  Removing {len(GHOST_ENTITIES)} ghost entities...")
    removed_entities = 0
    for entity_id in GHOST_ENTITIES:
        if remove_entity(entity_id):
            removed_entities += 1

    # Remove automations
    print(f"\n🤖 Removing {len(GHOST_AUTOMATIONS)} ghost automations...")
    removed_automations = 0
    for automation_id in GHOST_AUTOMATIONS:
        if remove_automation(automation_id):
            removed_automations += 1

    print("\n📊 Summary:")
    print(f"   Entities removed: {removed_entities}/{len(GHOST_ENTITIES)}")
    print(f"   Automations removed: {removed_automations}/{len(GHOST_AUTOMATIONS)}")

    if removed_entities == len(GHOST_ENTITIES) and removed_automations == len(GHOST_AUTOMATIONS):
        print("🎉 All Z2M ghosts successfully removed!")
    else:
        print("⚠️  Some entities/automations could not be removed (may not exist)")

    print("\n💡 Next steps:")
    print("   1. Restart Home Assistant to clear any cached references")
    print("   2. Check unavailable entity count reduction")
    print("   3. Monitor MQTT logs for reduced ghost traffic")

if __name__ == "__main__":
    main()