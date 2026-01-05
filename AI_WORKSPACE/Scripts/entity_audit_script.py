#!/usr/bin/env python3
"""
Entity Reference Audit Script
Scans all dashboard YAML files for missing entity references
"""

import os
import yaml
import re
from pathlib import Path

def scan_yaml_for_entities(file_path):
    """Extract entity references from YAML file"""
    entities = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find entity references
        entity_patterns = [
            r'entity:\s+([a-z_]+\.[a-z0-9_]+)',
            r'entities:\s*\n\s*-\s+([a-z_]+\.[a-z0-9_]+)',
            r'states\([\'"]([a-z_]+\.[a-z0-9_]+)[\'"]',
            r'sensor\.([a-z0-9_]+)',
            r'binary_sensor\.([a-z0-9_]+)',
            r'input_boolean\.([a-z0-9_]+)',
            r'input_text\.([a-z0-9_]+)',
        ]
        
        for pattern in entity_patterns:
            matches = re.findall(pattern, content, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                if '.' in match:
                    entities.add(match)
                else:
                    # Add domain prefix for partial matches
                    if 'sensor' in pattern:
                        entities.add(f'sensor.{match}')
                    elif 'binary_sensor' in pattern:
                        entities.add(f'binary_sensor.{match}')
                    elif 'input_boolean' in pattern:
                        entities.add(f'input_boolean.{match}')
                    elif 'input_text' in pattern:
                        entities.add(f'input_text.{match}')
                        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        
    return entities

def audit_dashboard_entities():
    """Audit all dashboard files for entity references"""
    
    dashboard_dirs = [
        'dashboards/ai',
        'dashboards/SYSTEM_OVERVIEW', 
        'dashboards/users',
        'dashboards/integrations',
        'dashboards/hacs',
        'dashboards/admin',
        'dashboards/ops'
    ]
    
    all_entities = {}
    
    for dashboard_dir in dashboard_dirs:
        dir_path = Path(dashboard_dir)
        if dir_path.exists():
            print(f"\n🔍 Scanning {dashboard_dir}:")
            
            for yaml_file in dir_path.glob('*.yaml'):
                entities = scan_yaml_for_entities(yaml_file)
                if entities:
                    all_entities[str(yaml_file)] = entities
                    print(f"  📄 {yaml_file.name}: {len(entities)} entities")
                    
    return all_entities

def generate_entity_audit_report(all_entities):
    """Generate comprehensive entity audit report"""
    
    report = []
    report.append("# 🔍 ENTITY REFERENCE AUDIT REPORT")
    report.append(f"Generated: {os.popen('date').read().strip()}")
    report.append("")
    
    # Group entities by domain
    entity_domains = {}
    
    for file_path, entities in all_entities.items():
        for entity in entities:
            domain = entity.split('.')[0]
            if domain not in entity_domains:
                entity_domains[domain] = set()
            entity_domains[domain].add(entity)
            
    report.append("## 📊 ENTITIES BY DOMAIN")
    for domain, entities in sorted(entity_domains.items()):
        report.append(f"- **{domain}**: {len(entities)} entities")
        
    report.append("")
    report.append("## 📋 ENTITIES BY FILE")
    
    for file_path, entities in all_entities.items():
        report.append(f"\n### 📄 {os.path.basename(file_path)}")
        for entity in sorted(entities):
            report.append(f"- {entity}")
            
    report.append("")
    report.append("## 🚨 LIKELY MISSING ENTITIES")
    report.append("Check these entities in Developer Tools → States:")
    
    # Common problematic patterns
    suspicious_entities = []
    for entities in all_entities.values():
        for entity in entities:
            if any(pattern in entity for pattern in [
                'workspace_sync', 'validation_', 'session_', 'integration_health',
                'mqtt_broker', 'adguard_', 'unifi_controller', 'hacs_'
            ]):
                suspicious_entities.append(entity)
                
    for entity in sorted(set(suspicious_entities)):
        report.append(f"- ⚠️ {entity}")
        
    return "\n".join(report)

if __name__ == "__main__":
    print("🔍 Starting Entity Reference Audit...")
    
    # Change to Home Assistant config directory
    os.chdir('S:/')
    
    all_entities = audit_dashboard_entities()
    
    if all_entities:
        report = generate_entity_audit_report(all_entities)
        
        # Save report
        with open('AI_WORKSPACE/REPORTS/entity_audit_report.md', 'w') as f:
            f.write(report)
            
        print(f"\n✅ Audit complete! Report saved to AI_WORKSPACE/REPORTS/entity_audit_report.md")
        print(f"📊 Found {sum(len(entities) for entities in all_entities.values())} entity references across {len(all_entities)} files")
        
    else:
        print("❌ No dashboard files found or no entities detected")