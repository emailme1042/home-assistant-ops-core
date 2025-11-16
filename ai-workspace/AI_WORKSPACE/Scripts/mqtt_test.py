#!/usr/bin/env python3
"""MQTT Health Check Script for Home Assistant

Usage:
    python3 mqtt_test.py --host localhost --port 1883 --user mqtt_user --password pass
    
This script:
1. Tests MQTT broker connectivity
2. Publishes test messages
3. Subscribes to test topics
4. Reports broker statistics
"""

import argparse
import json
import paho.mqtt.client as mqtt
import socket
import sys
import time
from typing import Dict, List, Optional

class MQTTTester:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.messages: Dict[str, List[str]] = {}
        self.connected = False
        self.pub_count = 0
        
    def on_connect(self, client, userdata, flags, rc):
        """Callback when client connects to broker"""
        if rc == 0:
            print(f"✅ Connected to broker at {self.host}:{self.port}")
            self.connected = True
        else:
            print(f"❌ Connection failed with code {rc}")
            self.connected = False
            
    def on_message(self, client, userdata, msg):
        """Callback when message is received"""
        topic = msg.topic
        payload = msg.payload.decode()
        if topic not in self.messages:
            self.messages[topic] = []
        self.messages[topic].append(payload)
        print(f"📩 Received on {topic}: {payload}")
        
    def on_publish(self, client, userdata, mid):
        """Callback when message is published"""
        self.pub_count += 1
        
    def test_connection(self) -> bool:
        """Test basic connectivity to broker"""
        try:
            self.client.connect(self.host, self.port, 60)
            self.client.loop_start()
            time.sleep(2)  # Give time to connect
            return self.connected
        except socket.error as e:
            print(f"❌ Connection error: {e}")
            return False
            
    def publish_test_messages(self) -> bool:
        """Publish test messages to verify broker function"""
        if not self.connected:
            return False
            
        test_topics = [
            "homeassistant/test/connection",
            "homeassistant/test/json",
            "homeassistant/test/retained"
        ]
        
        messages = [
            "test_message",
            json.dumps({"test": "value"}),
            "retained_message"
        ]
        
        for topic, msg in zip(test_topics, messages):
            print(f"📤 Publishing to {topic}: {msg}")
            self.client.publish(topic, msg, qos=1)
            
        time.sleep(1)  # Allow time for publishes
        return self.pub_count == len(test_topics)
        
    def subscribe_test_topics(self) -> bool:
        """Subscribe to test topics and verify message receipt"""
        if not self.connected:
            return False
            
        self.client.subscribe("homeassistant/test/#")
        print("👂 Subscribed to homeassistant/test/#")
        
        time.sleep(2)  # Allow time for messages
        return len(self.messages) > 0
        
    def check_broker_stats(self) -> Optional[Dict]:
        """Get broker statistics if available"""
        if not self.connected:
            return None
            
        try:
            self.client.subscribe("$SYS/#")
            time.sleep(2)
            stats = {k: v[-1] for k, v in self.messages.items() if k.startswith("$SYS/")}
            return stats
        except Exception as e:
            print(f"⚠️ Could not get broker stats: {e}")
            return None
            
    def run_tests(self) -> bool:
        """Run all tests and return overall success"""
        success = True
        
        print("\n🔍 Testing MQTT Broker Connection")
        print("-" * 50)
        
        if not self.test_connection():
            print("❌ Connection test failed")
            return False
            
        print("\n📤 Testing Message Publishing")
        print("-" * 50)
        if not self.publish_test_messages():
            print("❌ Publish test failed")
            success = False
            
        print("\n📩 Testing Message Subscription")
        print("-" * 50)
        if not self.subscribe_test_topics():
            print("❌ Subscribe test failed")
            success = False
            
        print("\n📊 Checking Broker Statistics")
        print("-" * 50)
        stats = self.check_broker_stats()
        if stats:
            print("\nBroker Statistics:")
            for k, v in stats.items():
                print(f"  {k}: {v}")
        
        self.client.loop_stop()
        self.client.disconnect()
        
        print("\n📋 Test Summary")
        print("-" * 50)
        print(f"Connection: {'✅' if self.connected else '❌'}")
        print(f"Published Messages: {self.pub_count}")
        print(f"Received Topics: {len(self.messages)}")
        print(f"Overall Status: {'✅ PASS' if success else '❌ FAIL'}")
        
        return success

def main():
    parser = argparse.ArgumentParser(description="Test MQTT broker connectivity")
    parser.add_argument("--host", default="localhost", help="MQTT broker host")
    parser.add_argument("--port", type=int, default=1883, help="MQTT broker port")
    parser.add_argument("--user", required=True, help="MQTT username")
    parser.add_argument("--password", required=True, help="MQTT password")
    
    args = parser.parse_args()
    
    tester = MQTTTester(args.host, args.port, args.user, args.password)
    success = tester.run_tests()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()