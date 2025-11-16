#!/usr/bin/env python3
"""
Zigbee Network Map Parser for Home Assistant
Purpose: Parse Zigbee2MQTT network map data and extract routing information
Created: 2025-11-06 by VSCode Mesh Surgery Protocol
"""

import json
import datetime
from pathlib import Path

def zigbee_network_parser(networkmap_data, timestamp):
    """
    Parse Zigbee network map and extract parent-child relationships
    """
    
    # Parse the network map data
    try:
        if isinstance(networkmap_data, str):
            network_data = json.loads(networkmap_data)
        else:
            network_data = networkmap_data
    except (json.JSONDecodeError, TypeError):
        logger.error("Failed to parse network map data")
        return
    
    # Create audit log entry
    audit_log_path = Path("/config/AI_WORKSPACE/zigbee_mesh_audit_log.md")
    
    # Initialize log file if it doesn't exist
    if not audit_log_path.exists():
        with open(audit_log_path, "w") as f:
            f.write("# 🧭 Zigbee Mesh Audit Log\n")
            f.write("## Purpose: Track device routing and parent assignments\n\n")
    
    # Extract device routing information
    routing_info = []
    coordinator_ieee = None
    router_devices = []
    end_devices = []
    
    for node in network_data.get('nodes', []):
        ieee = node.get('ieeeAddr', 'unknown')
        friendly_name = node.get('friendly_name', ieee)
        device_type = node.get('type', 'unknown')
        lqi = node.get('lqi', 0)
        
        # Identify device types
        if device_type == 'Coordinator':
            coordinator_ieee = ieee
        elif device_type == 'Router':
            router_devices.append({
                'name': friendly_name,
                'ieee': ieee,
                'lqi': lqi
            })
        elif device_type == 'EndDevice':
            # Find parent router from links
            parent_ieee = None
            for link in network_data.get('links', []):
                if link.get('target', {}).get('ieeeAddr') == ieee:
                    parent_ieee = link.get('source', {}).get('ieeeAddr')
                    break
            
            end_devices.append({
                'name': friendly_name,
                'ieee': ieee,
                'lqi': lqi,
                'parent_ieee': parent_ieee
            })
    
    # Create detailed audit entry
    with open(audit_log_path, "a") as f:
        f.write(f"\n## 📊 Network Scan: {timestamp}\n\n")
        f.write(f"**Coordinator**: {coordinator_ieee}\n\n")
        
        if router_devices:
            f.write("**Active Routers**:\n")
            for router in router_devices:
                f.write(f"- {router['name']} ({router['ieee']}) - LQI: {router['lqi']}\n")
            f.write("\n")
        
        if end_devices:
            f.write("**End Device Routing**:\n")
            for device in end_devices:
                parent_name = "Unknown"
                if device['parent_ieee']:
                    # Find parent name from routers
                    for router in router_devices:
                        if router['ieee'] == device['parent_ieee']:
                            parent_name = router['name']
                            break
                    if parent_name == "Unknown" and device['parent_ieee'] == coordinator_ieee:
                        parent_name = "Coordinator"
                
                f.write(f"- {device['name']} → {parent_name} (LQI: {device['lqi']})\n")
            f.write("\n")
        
        # Flag potential routing issues
        misrouted_devices = []
        for device in end_devices:
            if device['parent_ieee'] == coordinator_ieee and len(router_devices) > 0:
                misrouted_devices.append(device['name'])
        
        if misrouted_devices:
            f.write("**⚠️ Potential Routing Issues**:\n")
            f.write("Following devices routing through coordinator despite available routers:\n")
            for device_name in misrouted_devices:
                f.write(f"- {device_name}\n")
            f.write("\n")
        
        f.write("---\n")
    
    # Publish summary to MQTT for dashboard display
    summary_data = {
        "timestamp": timestamp,
        "total_devices": len(network_data.get('nodes', [])),
        "routers": len(router_devices),
        "end_devices": len(end_devices),
        "misrouted_count": len(misrouted_devices),
        "coordinator_load": len([d for d in end_devices if d['parent_ieee'] == coordinator_ieee])
    }
    
    # Use the service to publish summary
    service.call('mqtt', 'publish', {
        'topic': 'homeassistant/zigbee_audit/network_summary',
        'payload': json.dumps(summary_data)
    })
    
    logger.info(f"Parsed network map: {len(router_devices)} routers, {len(end_devices)} end devices, {len(misrouted_devices)} potential issues")

# Execute the parser function
zigbee_network_parser(data.get('networkmap_data'), data.get('timestamp'))