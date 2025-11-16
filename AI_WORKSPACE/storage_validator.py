#!/usr/bin/env python3
"""
🔍 Home Assistant Entity & Automation Validator
Uses .storage files to validate entity references and diagnose automation issues
"""

import json
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

def load_entity_registry():
    """Load entity registry from .storage"""
    try:
        with open('.storage/core.entity_registry', 'r') as f:
            registry = json.load(f)
        return {entry['entity_id']: entry for entry in registry['data']['entities']}
    except Exception as e:
        print(f"❌ Error loading entity registry: {e}")
        return {}

def load_device_registry():
    """Load device registry from .storage"""
    try:
        with open('.storage/core.device_registry', 'r') as f:
            registry = json.load(f)
        return {entry['id']: entry for entry in registry['data']['devices']}
    except Exception as e:
        print(f"❌ Error loading device registry: {e}")
        return {}

def load_restore_state():
    """Load last known states from .storage"""
    try:
        with open('.storage/core.restore_state', 'r') as f:
            data = json.load(f)
        return {entry['state']['entity_id']: entry['state'] for entry in data['data']}
    except Exception as e:
        print(f"❌ Error loading restore state: {e}")
        return {}

def extract_entities_from_yaml(file_path):
    """Extract all entity references from a YAML file"""
    entities = set()
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Entity ID patterns
        patterns = [
            r'entity_id:\s*([a-z_]+\.[a-z0-9_]+)',
            r'entity_id:\s*["\']([a-z_]+\.[a-z0-9_]+)["\']',
            r'states\(["\']([a-z_]+\.[a-z0-9_]+)["\']',
            r'target:\s*\n\s*entity_id:\s*([a-z_]+\.[a-z0-9_]+)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE | re.MULTILINE)
            entities.update(matches)
            
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
    
    return entities

def validate_office_automation():
    """Specifically validate office motion automation"""
    print("\n🏢 OFFICE AUTOMATION ANALYSIS")
    print("=" * 50)
    
    # Load storage data
    entities = load_entity_registry()
    states = load_restore_state()
    
    # Check critical office entities
    office_entities = {
        'binary_sensor.office_motion': 'Motion Sensor',
        'light.office': 'Office Light',
        'light.office_3': 'Office Light (alt)',
        'sensor.office_motion_sensor_battery': 'Motion Battery'
    }
    
    print("📊 Office Entity Status:")
    for entity_id, description in office_entities.items():
        if entity_id in entities:
            entity_info = entities[entity_id]
            state = states.get(entity_id, {}).get('state', 'unknown')
            print(f"✅ {entity_id} ({description})")
            print(f"   State: {state}")
            print(f"   Platform: {entity_info.get('platform', 'unknown')}")
            print(f"   Device ID: {entity_info.get('device_id', 'none')}")
        else:
            print(f"❌ {entity_id} ({description}) - NOT FOUND")
    
    # Check automation file
    automation_file = Path('includes/automations/office_motion_lighting.yaml')
    if automation_file.exists():
        entities_used = extract_entities_from_yaml(automation_file)
        print(f"\n🤖 Automation uses these entities:")
        for entity in sorted(entities_used):
            status = "✅ EXISTS" if entity in entities else "❌ MISSING"
            print(f"   {entity} - {status}")

def main():
    """Main validation function"""
    print("🔍 HOME ASSISTANT STORAGE VALIDATOR")
    print(f"📅 Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Load all storage data
    entities = load_entity_registry()
    devices = load_device_registry()
    states = load_restore_state()
    
    print(f"📊 Storage Summary:")
    print(f"   Entities: {len(entities)}")
    print(f"   Devices: {len(devices)}")
    print(f"   States: {len(states)}")
    
    # Validate office automation specifically
    validate_office_automation()
    
    # Find all automation files
    automation_dir = Path('includes/automations')
    if automation_dir.exists():
        automation_files = list(automation_dir.glob('*.yaml'))
        
        print(f"\n🤖 AUTOMATION VALIDATION")
        print("=" * 50)
        
        total_entities_used = set()
        missing_entities = set()
        
        for file_path in automation_files[:5]:  # Check first 5 files
            entities_used = extract_entities_from_yaml(file_path)
            total_entities_used.update(entities_used)
            
            file_missing = entities_used - set(entities.keys())
            if file_missing:
                print(f"❌ {file_path.name}:")
                for entity in sorted(file_missing):
                    print(f"   Missing: {entity}")
                missing_entities.update(file_missing)
            else:
                print(f"✅ {file_path.name}: All entities found")
        
        print(f"\n📋 SUMMARY:")
        print(f"   Total entities referenced: {len(total_entities_used)}")
        print(f"   Missing entities: {len(missing_entities)}")
        
        if missing_entities:
            print(f"\n❌ MISSING ENTITIES:")
            for entity in sorted(missing_entities):
                print(f"   {entity}")
    
    # Entity naming pattern analysis
    print(f"\n📝 ENTITY NAMING PATTERNS")
    print("=" * 50)
    
    patterns = {}
    for entity_id in entities.keys():
        domain, name = entity_id.split('.', 1)
        if domain not in patterns:
            patterns[domain] = []
        patterns[domain].append(name)
    
    for domain, names in sorted(patterns.items()):
        if len(names) <= 10:  # Only show domains with few entities
            print(f"{domain}: {', '.join(sorted(names))}")

if __name__ == "__main__":
    main()