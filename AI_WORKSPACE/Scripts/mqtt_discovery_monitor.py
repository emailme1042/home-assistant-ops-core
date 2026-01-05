#!/usr/bin/env python3
"""MQTT Discovery Monitor for Home Assistant

This script:
1. Monitors MQTT auto-discovery topics
2. Validates entity registration
3. Reports sync status and missing topics
4. Maintains watchdog state
"""

import json
import paho.mqtt.client as mqtt
import sys
import time
from datetime import datetime
from typing import Dict, List, Set

class MQTTDiscoveryMonitor:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        
        # Track discovered entities
        self.discovered_entities: Set[str] = set()
        self.active_topics: Dict[str, float] = {}
        self.last_activity: Dict[str, datetime] = {}
        
    def on_connect(self, client, userdata, flags, rc):
        """Subscribe to discovery and state topics on connect"""
        if rc == 0:
            print(f"✅ Connected to broker at {self.host}:{self.port}")
            # Subscribe to discovery topics
            self.client.subscribe("homeassistant/+/+/config")
            # Subscribe to state topics for discovered entities
            self.client.subscribe("homeassistant/+/+/state")
        else:
            print(f"❌ Connection failed with code {rc}")
            
    def on_message(self, client, userdata, msg):
        """Process incoming MQTT messages"""
        topic = msg.topic
        now = datetime.now()
        
        if topic.endswith("/config"):
            try:
                config = json.loads(msg.payload)
                if "unique_id" in config:
                    self.discovered_entities.add(config["unique_id"])
                    print(f"📝 Discovered entity: {config['unique_id']}")
            except json.JSONDecodeError:
                print(f"⚠️ Invalid discovery payload on {topic}")
                
        elif topic.endswith("/state"):
            # Extract entity ID from topic
            parts = topic.split("/")
            if len(parts) >= 4:
                entity_id = f"{parts[1]}_{parts[2]}"
                self.last_activity[entity_id] = now
                print(f"🔄 State update: {entity_id}")
                
    def check_entity_sync(self) -> Dict[str, List[str]]:
        """Check sync status of discovered entities"""
        now = datetime.now()
        active_entities = []
        inactive_entities = []
        
        for entity_id in self.discovered_entities:
            last_seen = self.last_activity.get(entity_id)
            if last_seen and (now - last_seen).total_seconds() < 300:  # 5 min timeout
                active_entities.append(entity_id)
            else:
                inactive_entities.append(entity_id)
                
        return {
            "active": active_entities,
            "inactive": inactive_entities
        }
        
    def check_watchdog(self) -> Dict[str, List[str]]:
        """Check for missing topics and watchdog status"""
        now = datetime.now()
        missing_topics = []
        active_topics = []
        
        for topic, last_seen in self.last_activity.items():
            if (now - last_seen).total_seconds() > 300:  # 5 min timeout
                missing_topics.append(topic)
            else:
                active_topics.append(topic)
                
        return {
            "missing": missing_topics,
            "active": active_topics
        }
        
    def run(self, runtime: int = 300):
        """Run the monitor for specified duration"""
        try:
            self.client.connect(self.host, self.port, 60)
            self.client.loop_start()
            
            start_time = time.time()
            while time.time() - start_time < runtime:
                time.sleep(60)  # Check every minute
                
                # Check entity sync
                sync_status = self.check_entity_sync()
                print("\n📊 Entity Sync Status:")
                print(f"Active: {len(sync_status['active'])}")
                print(f"Inactive: {len(sync_status['inactive'])}")
                
                # Check watchdog
                watchdog = self.check_watchdog()
                print("\n🔍 Topic Watchdog Status:")
                print(f"Active Topics: {len(watchdog['active'])}")
                print(f"Missing Topics: {len(watchdog['missing'])}")
                
                if watchdog['missing']:
                    print("Missing Topics:")
                    for topic in watchdog['missing']:
                        print(f"  - {topic}")
                        
            self.client.loop_stop()
            self.client.disconnect()
            
        except KeyboardInterrupt:
            print("\n⚠️ Monitoring interrupted")
            self.client.loop_stop()
            self.client.disconnect()
            
def main():
    if len(sys.argv) != 5:
        print("Usage: discovery_monitor.py host port username password")
        sys.exit(1)
        
    host = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]
    
    monitor = MQTTDiscoveryMonitor(host, port, username, password)
    monitor.run()

if __name__ == "__main__":
    main()