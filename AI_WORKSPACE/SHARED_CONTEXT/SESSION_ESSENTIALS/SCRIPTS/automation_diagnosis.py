#!/usr/bin/env python3
"""
Automation Diagnosis Script
Analyzes all automation YAML files vs entity registry to find unavailable automations
"""

import json
import yaml
import os
import glob
from pathlib import Path

def load_entities():
    """Load current entity states from REST API snapshot"""
    try:
        with open('entities.json', 'r', encoding='utf-8') as f:
            entities = json.load(f)
        return {e['entity_id']: e for e in entities}
    except FileNotFoundError:
        print("❌ entities.json not found. Run Windows REST snapshot first.")
        return {}

def scan_automation_files():
    """Scan all automation YAML files"""
    automation_files = []
    
    # Check includes/automations/
    includes_path = "../includes/automations/"
    if os.path.exists(includes_path):
        for root, dirs, files in os.walk(includes_path):
            for file in files:
                if file.endswith('.yaml') or file.endswith('.yml'):
                    automation_files.append(os.path.join(root, file))
    
    # Check root automations.yaml
    if os.path.exists("../automations.yaml"):
        automation_files.append("../automations.yaml")
    
    return automation_files

def analyze_automation_file(file_path):
    """Analyze a single automation YAML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        
        if not content:
            return []
        
        automations = []
        if isinstance(content, list):
            automations = content
        elif isinstance(content, dict) and 'automation' in content:
            automations = content['automation']
        elif isinstance(content, dict) and 'alias' in content:
            # Single automation
            automations = [content]
        
        results = []
        for auto in automations:
            if isinstance(auto, dict):
                auto_id = auto.get('id', 'no_id')
                alias = auto.get('alias', 'no_alias')
                entity_id = f"automation.{auto_id}" if auto_id != 'no_id' else None
                
                results.append({
                    'file': file_path,
                    'id': auto_id,
                    'alias': alias,
                    'entity_id': entity_id,
                    'automation': auto
                })
        
        return results
        
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return []

def main():
    print("🔍 AUTOMATION DIAGNOSIS REPORT")
    print("=" * 50)
    
    # Load current entities
    entities = load_entities()
    if not entities:
        print("⚠️ No entity data available. Running basic file scan only.")
    
    # Find automation entities
    automation_entities = {k: v for k, v in entities.items() if k.startswith('automation.')}
    unavailable_automations = {k: v for k, v in automation_entities.items() if v['state'] == 'unavailable'}
    
    print(f"📊 ENTITY SUMMARY:")
    print(f"   Total automation entities: {len(automation_entities)}")
    print(f"   Unavailable automations: {len(unavailable_automations)}")
    print()
    
    # Scan automation files
    automation_files = scan_automation_files()
    print(f"📁 AUTOMATION FILES FOUND: {len(automation_files)}")
    
    all_file_automations = []
    for file_path in automation_files:
        file_automations = analyze_automation_file(file_path)
        all_file_automations.extend(file_automations)
    
    print(f"📋 AUTOMATIONS IN FILES: {len(all_file_automations)}")
    print()
    
    # Analysis
    print("🚨 UNAVAILABLE AUTOMATIONS:")
    print("-" * 40)
    
    if unavailable_automations:
        for entity_id in sorted(unavailable_automations.keys()):
            # Find corresponding file
            file_found = None
            for file_auto in all_file_automations:
                if file_auto['entity_id'] == entity_id:
                    file_found = file_auto['file']
                    break
            
            status = f"📁 {file_found}" if file_found else "❌ NO FILE FOUND"
            print(f"   {entity_id} → {status}")
    else:
        print("   ✅ No unavailable automations found!")
    
    print()
    print("🔍 AUTOMATIONS IN FILES BUT NOT IN ENTITIES:")
    print("-" * 50)
    
    file_entity_ids = {auto['entity_id'] for auto in all_file_automations if auto['entity_id']}
    entity_entity_ids = set(automation_entities.keys())
    
    missing_from_entities = file_entity_ids - entity_entity_ids
    if missing_from_entities:
        for entity_id in sorted(missing_from_entities):
            for file_auto in all_file_automations:
                if file_auto['entity_id'] == entity_id:
                    print(f"   {entity_id} → 📁 {file_auto['file']}")
                    break
    else:
        print("   ✅ All file automations found in entity registry!")
    
    print()
    print("📊 SUMMARY:")
    print(f"   Files with automations: {len(automation_files)}")
    print(f"   Automations in files: {len(all_file_automations)}")
    print(f"   Automation entities: {len(automation_entities)}")
    print(f"   Unavailable entities: {len(unavailable_automations)}")
    print(f"   Missing from entities: {len(missing_from_entities)}")

if __name__ == "__main__":
    main()