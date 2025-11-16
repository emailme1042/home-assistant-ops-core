#!/usr/bin/env python3
"""
Entity Reference Cleanup Analysis
Compares entity references in dashboards with actual entity registry
"""

import json
import re
import os
from pathlib import Path

def load_entity_registry():
    """Load actual entities from entity registry"""
    registry_path = Path("s:\.storage\core.entity_registry")
    
    if not registry_path.exists():
        print(f"❌ Entity registry not found at {registry_path}")
        return set()
    
    entities = set()
    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract entity_id values using regex
            entity_matches = re.findall(r'"entity_id":"([^"]+)"', content)
            entities.update(entity_matches)
    except Exception as e:
        print(f"❌ Error reading entity registry: {e}")
        return set()
    
    print(f"✅ Loaded {len(entities)} entities from registry")
    return entities

def find_dashboard_entities():
    """Find all entity references in dashboard files"""
    dashboard_root = Path("s:\dashboards")
    entity_refs = {}
    
    # Patterns to match entity references
    patterns = [
        r'entity:\s*([a-z_]+\.[a-z_0-9]+)',  # entity: sensor.something
        r'entity_id:\s*([a-z_]+\.[a-z_0-9]+)',  # entity_id: sensor.something
        r'states\([\'"]([a-z_]+\.[a-z_0-9]+)[\'"]',  # states('sensor.something')
        r'([a-z_]+\.[a-z_0-9]+)',  # Direct entity references in lists
    ]
    
    for yaml_file in dashboard_root.rglob("*.yaml"):
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                file_entities = set()
                for pattern in patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for match in matches:
                        # Filter for actual entity patterns
                        if '.' in match and not match.startswith('www.') and not match.startswith('http'):
                            file_entities.add(match.lower())
                
                if file_entities:
                    entity_refs[str(yaml_file)] = file_entities
                    
        except Exception as e:
            print(f"⚠️ Error reading {yaml_file}: {e}")
    
    return entity_refs

def analyze_entity_references():
    """Main analysis function"""
    print("🔍 Entity Reference Cleanup Analysis")
    print("=" * 50)
    
    # Load actual entities
    actual_entities = load_entity_registry()
    if not actual_entities:
        return
    
    # Find dashboard entity references
    dashboard_entities = find_dashboard_entities()
    
    # Analysis results
    missing_entities = {}
    suggestions = {}
    
    total_refs = 0
    missing_count = 0
    
    for file_path, entities in dashboard_entities.items():
        file_missing = []
        file_suggestions = []
        
        for entity in entities:
            total_refs += 1
            if entity not in actual_entities:
                file_missing.append(entity)
                missing_count += 1
                
                # Find similar entities for suggestions
                similar = []
                entity_domain = entity.split('.')[0] if '.' in entity else ''
                entity_name = entity.split('.')[1] if '.' in entity else entity
                
                for actual in actual_entities:
                    if actual.startswith(entity_domain + '.'):
                        actual_name = actual.split('.')[1]
                        # Simple similarity check
                        if entity_name in actual_name or actual_name in entity_name:
                            similar.append(actual)
                
                if similar:
                    file_suggestions.append({
                        'missing': entity,
                        'suggestions': similar[:3]  # Top 3 suggestions
                    })
        
        if file_missing:
            missing_entities[file_path] = file_missing
            suggestions[file_path] = file_suggestions
    
    # Generate report
    report_lines = []
    report_lines.append(f"# 🧩 Entity Reference Cleanup Report")
    report_lines.append(f"")
    report_lines.append(f"**Analysis Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"**Total Entity References**: {total_refs}")
    report_lines.append(f"**Missing Entities**: {missing_count}")
    report_lines.append(f"**Success Rate**: {((total_refs - missing_count) / total_refs * 100):.1f}%")
    report_lines.append(f"")
    
    if missing_entities:
        report_lines.append(f"## 🚨 Missing Entities by File")
        report_lines.append(f"")
        
        for file_path, missing in missing_entities.items():
            file_name = Path(file_path).name
            report_lines.append(f"### 📄 `{file_name}`")
            report_lines.append(f"**Path**: `{file_path}`")
            report_lines.append(f"**Missing Entities**: {len(missing)}")
            report_lines.append(f"")
            
            for entity in missing:
                report_lines.append(f"- ❌ `{entity}`")
            
            # Add suggestions if available
            file_suggestions = suggestions.get(file_path, [])
            if file_suggestions:
                report_lines.append(f"")
                report_lines.append(f"**🔧 Suggested Replacements**:")
                for suggestion in file_suggestions:
                    report_lines.append(f"- `{suggestion['missing']}` → **Suggestions**:")
                    for alt in suggestion['suggestions']:
                        report_lines.append(f"  - `{alt}`")
            
            report_lines.append(f"")
    
    else:
        report_lines.append(f"## ✅ All Entity References Valid!")
        report_lines.append(f"")
        report_lines.append(f"No missing entities found in dashboard files.")
    
    # Write report
    report_path = Path("s:\AI_WORKSPACE\entity_reference_cleanup.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"📋 Report saved to: {report_path}")
    print(f"📊 Summary: {missing_count}/{total_refs} entities missing ({((total_refs - missing_count) / total_refs * 100):.1f}% success rate)")

if __name__ == "__main__":
    analyze_entity_references()