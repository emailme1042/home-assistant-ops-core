#!/usr/bin/env python3
"""
Lovelace Resource Validator for Home Assistant
Validates each resource path in resources.yaml against actual files in the filesystem
Designed for HA Green with BusyBox compatibility

Usage:
    python3 lovelace_resource_validator.py [config_path]
    
Example:
    python3 /config/AI_WORKSPACE/Scripts/lovelace_resource_validator.py /config
"""

import yaml
import os
import sys
from pathlib import Path
from datetime import datetime

class LovelaceResourceValidator:
    def __init__(self, config_path="/config"):
        self.config_path = Path(config_path)
        self.resources_yaml_path = self.config_path / "resources.yaml"
        self.hacs_base_path = self.config_path / "www" / "community"
        self.local_base_path = self.config_path / "www"
        
        # Results storage
        self.results = {
            'valid': [],
            'missing': [],
            'skipped': [],
            'errors': []
        }
        
    def load_resources(self):
        """Load resources from resources.yaml file"""
        try:
            with open(self.resources_yaml_path, 'r', encoding='utf-8') as f:
                resources = yaml.safe_load(f)
                return resources if resources else []
        except FileNotFoundError:
            print(f"❌ ERROR: resources.yaml not found at {self.resources_yaml_path}")
            return []
        except yaml.YAMLError as e:
            print(f"❌ ERROR: YAML parsing error in resources.yaml: {e}")
            return []
            
    def validate_hacs_resource(self, url):
        """Validate HACS resource path (/hacsfiles/...)"""
        if not url.startswith('/hacsfiles/'):
            return None
            
        # Extract relative path from /hacsfiles/component/file.js
        relative_path = url.replace('/hacsfiles/', '')
        full_path = self.hacs_base_path / relative_path
        
        if full_path.exists():
            return {'status': 'valid', 'path': str(full_path), 'size': full_path.stat().st_size}
        else:
            return {'status': 'missing', 'path': str(full_path), 'reason': 'File not found'}
            
    def validate_local_resource(self, url):
        """Validate local resource path (/local/...)"""
        if not url.startswith('/local/'):
            return None
            
        # Extract relative path from /local/path/file.js
        relative_path = url.replace('/local/', '')
        full_path = self.local_base_path / relative_path
        
        if full_path.exists():
            return {'status': 'valid', 'path': str(full_path), 'size': full_path.stat().st_size}
        else:
            return {'status': 'missing', 'path': str(full_path), 'reason': 'File not found'}
            
    def validate_resource(self, resource):
        """Validate a single resource entry"""
        if not isinstance(resource, dict) or 'url' not in resource:
            return {'status': 'error', 'reason': 'Invalid resource format'}
            
        url = resource.get('url', '')
        
        # Check HACS resources
        hacs_result = self.validate_hacs_resource(url)
        if hacs_result:
            return hacs_result
            
        # Check local resources
        local_result = self.validate_local_resource(url)
        if local_result:
            return local_result
            
        # Skip external URLs or other formats
        if url.startswith('http'):
            return {'status': 'skipped', 'reason': 'External URL'}
        else:
            return {'status': 'skipped', 'reason': f'Unknown path format: {url}'}
            
    def run_validation(self):
        """Run complete validation process"""
        print(f"🔍 Lovelace Resource Validator")
        print(f"📁 Config path: {self.config_path}")
        print(f"📄 Resources file: {self.resources_yaml_path}")
        print(f"🏠 HACS path: {self.hacs_base_path}")
        print(f"📂 Local path: {self.local_base_path}")
        print("-" * 60)
        
        resources = self.load_resources()
        if not resources:
            print("❌ No resources to validate")
            return
            
        print(f"📋 Validating {len(resources)} resources...")
        print()
        
        for i, resource in enumerate(resources, 1):
            url = resource.get('url', 'UNKNOWN')
            result = self.validate_resource(resource)
            
            # Store results
            if result['status'] == 'valid':
                self.results['valid'].append({'url': url, 'result': result})
            elif result['status'] == 'missing':
                self.results['missing'].append({'url': url, 'result': result})
            elif result['status'] == 'skipped':
                self.results['skipped'].append({'url': url, 'result': result})
            else:
                self.results['errors'].append({'url': url, 'result': result})
                
            # Print status
            status_icon = {
                'valid': '✅',
                'missing': '❌',
                'skipped': '⚠️',
                'error': '🔴'
            }.get(result['status'], '❓')
            
            print(f"{status_icon} [{i:2d}] {url}")
            if result['status'] == 'valid' and 'size' in result:
                print(f"      📁 {result['path']} ({result['size']} bytes)")
            elif result['status'] == 'missing':
                print(f"      📁 Missing: {result['path']}")
            elif result.get('reason'):
                print(f"      💬 {result['reason']}")
            print()
            
    def print_summary(self):
        """Print validation summary"""
        print("=" * 60)
        print("📊 VALIDATION SUMMARY")
        print("=" * 60)
        
        total = sum(len(results) for results in self.results.values())
        print(f"✅ Valid resources:   {len(self.results['valid']):2d} / {total}")
        print(f"❌ Missing resources: {len(self.results['missing']):2d} / {total}")
        print(f"⚠️  Skipped resources: {len(self.results['skipped']):2d} / {total}")
        print(f"🔴 Error resources:   {len(self.results['errors']):2d} / {total}")
        print()
        
        # Detailed missing resources
        if self.results['missing']:
            print("🚨 MISSING RESOURCES (Recommend removal):")
            for item in self.results['missing']:
                print(f"   ❌ {item['url']}")
            print()
            
        # Skipped resources
        if self.results['skipped']:
            print("⚠️  SKIPPED RESOURCES (External or unknown format):")
            for item in self.results['skipped']:
                print(f"   ⚠️  {item['url']} - {item['result']['reason']}")
            print()
            
        # Recommendations
        print("🛠️  RECOMMENDATIONS:")
        if self.results['missing']:
            print(f"   • Remove {len(self.results['missing'])} missing resources from resources.yaml")
            print("   • Check HACS for uninstalled components")
        if len(self.results['valid']) < total * 0.8:
            print("   • Consider reviewing resource usage - many are inactive")
        print("   • Restart Home Assistant after making changes")
        print("   • Check browser console for 404 errors after restart")
        
    def generate_cleanup_script(self, output_path=None):
        """Generate a cleaned resources.yaml with only valid entries"""
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = self.config_path / f"resources_cleaned_{timestamp}.yaml"
            
        valid_resources = []
        for item in self.results['valid']:
            # Find original resource entry
            resources = self.load_resources()
            for resource in resources:
                if resource.get('url') == item['url']:
                    valid_resources.append(resource)
                    break
                    
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(valid_resources, f, default_flow_style=False, allow_unicode=True)
            print(f"📄 Generated cleaned resources.yaml: {output_path}")
            print(f"   Contains {len(valid_resources)} valid resources")
        except Exception as e:
            print(f"❌ Error generating cleanup script: {e}")

def main():
    # Get config path from command line or use default
    config_path = sys.argv[1] if len(sys.argv) > 1 else "/config"
    
    # Run validation
    validator = LovelaceResourceValidator(config_path)
    validator.run_validation()
    validator.print_summary()
    
    # Ask user if they want to generate cleanup file
    missing_count = len(validator.results['missing'])
    if missing_count > 0:
        print()
        print(f"🧹 Found {missing_count} missing resources.")
        print("   Generate cleaned resources.yaml? (y/N): ", end="")
        try:
            response = input().strip().lower()
            if response in ['y', 'yes']:
                validator.generate_cleanup_script()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Validation complete!")

if __name__ == "__main__":
    main()