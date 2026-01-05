#!/usr/bin/env python3
"""
UniFi API Script to Add Firewall Rule for HA Access to CGU Ports 80/443
Uses UniFi Network API v8.0+
"""

import requests
import json
import sys

# Configuration - Update these with your UniFi controller details
UNIFI_CONTROLLER_IP = "192.168.0.1"  # Replace with your CGU/UDM IP
UNIFI_USERNAME = "HomeAssistant67"     # Replace with your UniFi admin username
UNIFI_PASSWORD = "HomeAssistant67"     # Replace with your UniFi admin password
UNIFI_SITE = "default"               # Replace with your site name if not default
HA_IP = "192.168.0.217"              # HA server IP

# API endpoints
LOGIN_URL = f"https://{UNIFI_CONTROLLER_IP}:443/api/auth/login"
FIREWALL_RULE_URL = f"https://{UNIFI_CONTROLLER_IP}:443/api/s/{UNIFI_SITE}/rest/firewallrule"

def login_and_get_session():
    """Login to UniFi controller and return session with cookies"""
    payload = {
        "username": UNIFI_USERNAME,
        "password": UNIFI_PASSWORD,
        "remember": True
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Disable SSL verification for self-signed certs (remove in production)
    response = requests.post(LOGIN_URL, json=payload, headers=headers, verify=False)

    if response.status_code != 200:
        print(f"Login failed: {response.status_code} - {response.text}")
        sys.exit(1)

    # Return session with cookies
    session = requests.Session()
    session.cookies.update(response.cookies)
    session.verify = False  # Disable SSL verification

    print("Successfully logged in to UniFi controller")
    return session

def add_firewall_rule(session):
    """Add firewall rule allowing HA IP to access CGU ports 80 and 443"""

    # Firewall rule payload for LAN_LOCAL ruleset (allowing internal access to controller)
    rule_payload = {
        "action": "accept",
        "dst_port": "80,443",
        "enabled": True,
        "ip_version": "ipv4",
        "logging": False,
        "name": "Allow HA to CGU Web",
        "protocol": "tcp",
        "ruleset": "LAN_LOCAL",  # LAN_LOCAL for internal network rules
        "src_ip": HA_IP,
        "src_network": "",  # Leave empty for specific IP
        "dst_network": "",  # Leave empty for any
        "priority": 2000  # Set appropriate priority
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = session.post(FIREWALL_RULE_URL, json=rule_payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("meta", {}).get("rc") == "ok":
            print("Firewall rule added successfully!")
            print(f"Rule ID: {data.get('data', [{}])[0].get('_id', 'Unknown')}")
            return True
        else:
            print(f"API returned error: {data}")
            return False
    else:
        print(f"Failed to add firewall rule: {response.status_code} - {response.text}")
        return False

def main():
    print("UniFi Firewall Rule Addition Script")
    print("=" * 40)
    print(f"Allowing HA IP {HA_IP} to access CGU ports 80,443")
    print()

    try:
        session = login_and_get_session()
        success = add_firewall_rule(session)

        if success:
            print("\n✅ Firewall rule added successfully!")
            print("HA should now be able to connect to the UniFi CGU on ports 80/443")
            print("\nNext steps:")
            print("1. Test HA UniFi integration setup")
            print("2. Check HA logs for connectivity")
            print("3. Restart HA if needed")
        else:
            print("\n❌ Failed to add firewall rule")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()</content>
<parameter name="filePath">s:\python_scripts\unifi_add_firewall_rule.py