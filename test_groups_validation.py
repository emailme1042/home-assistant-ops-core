#!/usr/bin/env python3
"""
Validation script for groups.yaml - Apple TV/tvOS compatibility check
Tests group structure, entity format, and icon validity
"""

import yaml
import sys

def validate_groups():
    """Validate groups.yaml structure and content"""
    
    errors = []
    warnings = []
    
    try:
        with open('groups.yaml', 'r') as f:
            groups = yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Failed to load groups.yaml: {e}")
        return False
    
    if not groups:
        print("❌ groups.yaml is empty or invalid")
        return False
    
    print("=" * 60)
    print("🔍 GROUPS.YAML VALIDATION REPORT")
    print("=" * 60)
    print()
    
    # Validate each group
    for group_id, group_data in groups.items():
        print(f"📦 Validating: {group_id}")
        
        # Check required fields
        if 'name' not in group_data:
            errors.append(f"  ❌ Missing 'name' field in {group_id}")
        else:
            print(f"  ✅ Name: {group_data['name']}")
        
        if 'icon' not in group_data:
            warnings.append(f"  ⚠️  No icon specified for {group_id}")
        else:
            icon = group_data['icon']
            if not icon.startswith('mdi:'):
                errors.append(f"  ❌ Invalid icon format in {group_id}: {icon}")
            else:
                print(f"  ✅ Icon: {icon}")
        
        if 'entities' not in group_data:
            errors.append(f"  ❌ Missing 'entities' field in {group_id}")
        else:
            entities = group_data['entities']
            if not isinstance(entities, list):
                errors.append(f"  ❌ Entities must be a list in {group_id}")
            elif len(entities) == 0:
                warnings.append(f"  ⚠️  Empty entities list in {group_id}")
            else:
                print(f"  ✅ Entities: {len(entities)}")
                
                # Validate entity format
                valid_domains = [
                    'light', 'switch', 'cover', 'media_player', 'remote',
                    'siren', 'climate', 'fan', 'humidifier', 'sensor',
                    'binary_sensor', 'lock', 'alarm_control_panel'
                ]
                
                for entity in entities:
                    if isinstance(entity, str):
                        if '.' not in entity:
                            errors.append(f"    ❌ Invalid entity format: {entity}")
                        else:
                            domain = entity.split('.')[0]
                            if domain not in valid_domains:
                                warnings.append(f"    ⚠️  Uncommon domain: {entity}")
                    else:
                        errors.append(f"    ❌ Entity must be string: {entity}")
        
        print()
    
    # Summary
    print("=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total groups: {len(groups)}")
    print(f"Total entities: {sum(len(g.get('entities', [])) for g in groups.values())}")
    print()
    
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(error)
        print()
    
    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(warning)
        print()
    
    if not errors and not warnings:
        print("✅ All checks passed! Groups are properly configured.")
        print("🍎 Ready for Apple TV/tvOS Home Assistant app")
    elif not errors:
        print("✅ No critical errors found.")
        print("⚠️  Please review warnings above.")
    else:
        print("❌ Validation failed. Please fix errors above.")
        return False
    
    print()
    return True

if __name__ == "__main__":
    success = validate_groups()
    sys.exit(0 if success else 1)
