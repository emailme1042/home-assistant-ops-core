#!/usr/bin/env python3
"""
Matter Bulk Commissioning Script for Home Assistant
Commission multiple Matter devices using their setup codes
"""

import requests
import json
import time
import sys

# HA Configuration
HA_URL = "http://192.168.0.217:8123"
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI3N2M5ZDBjYmZlZDg0OTQ5YmRjYjhjZDBhM2IzN2JiYiIsImlhdCI6MTc2MjQ3OTI3NSwiZXhwIjoyMDc3ODM5Mjc1fQ.x_kVxgkEbTtmkDMahBG7ypaduRPiZtZHGEhX-6TIHHo"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

# Matter Device Setup Codes (Add your device codes here)
MATTER_DEVICES = {
    "Tapo_Plug_Node5": {"code": "12345678", "discriminator": "0x1234"},
    "Aqara_Hub_Node10": {"code": "87654321", "discriminator": "0x5678"},
    "Aqara_Doorbell_Node17": {"code": "11223344", "discriminator": "0x9ABC"},
    "Tapo_Plug_Node18": {"code": "44332211", "discriminator": "0xDEF0"},
    "Tapo_Plug_Node19": {"code": "55667788", "discriminator": "0x1234"},
    "Tapo_Plug_Node20": {"code": "88776655", "discriminator": "0x5678"},
    "Aqara_Temp_Node24": {"code": "99887766", "discriminator": "0x9ABC"},
    "Aqara_Motion_Node37": {"code": "66778899", "discriminator": "0xDEF0"},
    "Aqara_Contact_Node44": {"code": "33445566", "discriminator": "0x1234"},
    "Tado_Thermostat_Node45": {"code": "77889900", "discriminator": "0x5678"}
}

def commission_device(device_name, setup_code, discriminator):
    """Commission a single Matter device"""
    print(f"🔄 Commissioning {device_name}...")

    payload = {
        "device_id": None,  # Let HA discover the device
        "code": setup_code,
        "discriminator": discriminator
    }

    try:
        response = requests.post(
            f"{HA_URL}/api/services/matter/commission",
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            print(f"✅ {device_name} commissioned successfully")
            return True
        else:
            print(f"❌ Failed to commission {device_name}: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error commissioning {device_name}: {str(e)}")
        return False

def main():
    print("🏠 Matter Bulk Commissioning Script")
    print("=" * 40)

    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("🔍 DRY RUN MODE - No devices will be commissioned")
        dry_run = True
    else:
        print("⚠️  LIVE MODE - Devices will be commissioned!")
        dry_run = False

    print(f"📋 Found {len(MATTER_DEVICES)} devices to commission")
    print()

    successful = 0
    failed = 0

    for device_name, device_info in MATTER_DEVICES.items():
        if dry_run:
            print(f"🔍 Would commission {device_name} (Code: {device_info['code']}, Discriminator: {device_info['discriminator']})")
            successful += 1
        else:
            if commission_device(device_name, device_info['code'], device_info['discriminator']):
                successful += 1
            else:
                failed += 1

            # Small delay between commissions to avoid overwhelming the controller
            time.sleep(2)

    print()
    print("📊 Commissioning Results:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")

    if dry_run:
        print("\n💡 To run actual commissioning, remove --dry-run flag")
        print("⚠️  Make sure all devices are in pairing mode first!")

if __name__ == "__main__":
    main()