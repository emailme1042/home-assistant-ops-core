#!/usr/bin/env python3
"""Simple and fast resource validator for Home Assistant"""

import yaml
import os
from pathlib import Path

def check_resources():
    """Quick check of resources.yaml"""
    print("🔍 Simple Resource Validator")
    print("-" * 40)
    
    # Load resources.yaml
    resources_file = Path("s:/resources.yaml")
    if not resources_file.exists():
        print("❌ resources.yaml not found!")
        return
    
    with open(resources_file, 'r', encoding='utf-8') as f:
        resources = yaml.safe_load(f)
    
    print(f"📋 Found {len(resources)} resources to check")
    print()
    
    valid_count = 0
    missing_count = 0
    skipped_count = 0
    
    for i, resource in enumerate(resources, 1):
        url = resource.get('url', '')
        
        if url.startswith('/hacsfiles/'):
            # Check HACS resource
            file_path = url.replace('/hacsfiles/', 's:/www/community/')
            if os.path.exists(file_path):
                print(f"✅ [{i:2d}] {url}")
                valid_count += 1
            else:
                print(f"❌ [{i:2d}] {url} (MISSING)")
                missing_count += 1
                
        elif url.startswith('/local/'):
            # Check local resource
            file_path = url.replace('/local/', 's:/www/')
            if os.path.exists(file_path):
                print(f"✅ [{i:2d}] {url}")
                valid_count += 1
            else:
                print(f"❌ [{i:2d}] {url} (MISSING)")
                missing_count += 1
                
        else:
            print(f"⚠️  [{i:2d}] {url} (SKIPPED - external/unknown)")
            skipped_count += 1
    
    print()
    print("📊 SUMMARY:")
    print(f"✅ Valid:   {valid_count}")
    print(f"❌ Missing: {missing_count}")
    print(f"⚠️  Skipped: {skipped_count}")
    
    if missing_count > 0:
        print(f"\n🚨 Found {missing_count} missing resources!")
        print("   Recommend removing these from resources.yaml")

if __name__ == "__main__":
    check_resources()