# 🧹 Configuration Cleanup Audit Script
# Identifies deprecated, unnecessary, and problematic entries in Home Assistant configuration
# Safe analysis - no modifications made automatically

import yaml
import os
import json
from datetime import datetime
from pathlib import Path

class ConfigurationAuditor:
    def __init__(self, config_root="/config/"):
        self.config_root = config_root
        self.log_dir = "/config/AI_WORKSPACE/logs/"
        self.ensure_log_dir()
        self.deprecated_entries = []
        self.unnecessary_entries = []
        self.problematic_entries = []
        self.recommendations = []
    
    def ensure_log_dir(self):
        """Ensure log directory exists"""
        os.makedirs(self.log_dir, exist_ok=True)
    
    def audit_configuration_yaml(self):
        """Audit main configuration.yaml for deprecated/unnecessary entries"""
        config_file = os.path.join(self.config_root, "configuration.yaml")
        
        if not os.path.exists(config_file):
            return {"error": "configuration.yaml not found"}
        
        try:
            with open(config_file, 'r') as f:
                content = f.read()
                
            # Parse YAML safely
            config = yaml.safe_load(content)
            
            # Check for deprecated entries
            self._check_deprecated_integrations(config)
            self._check_unnecessary_entries(config)
            self._check_problematic_patterns(content)
            
        except Exception as e:
            self.problematic_entries.append(f"YAML parsing error in configuration.yaml: {e}")
    
    def _check_deprecated_integrations(self, config):
        """Check for deprecated integrations that should be UI-configured"""
        deprecated_integrations = {
            'discovery': 'Deprecated - Home Assistant now uses automatic discovery',
            'updater': 'Deprecated - Updates managed via Supervisor',
            'introduction': 'Deprecated - No longer needed',
            'map': 'Deprecated - Use device_tracker instead',
            'config': 'Deprecated - Built into Home Assistant',
            'zeroconf': 'Deprecated - Built into Home Assistant',
            'ssdp': 'Deprecated - Built into Home Assistant',
            'cloud': 'Should be configured via UI in Settings → Home Assistant Cloud',
            'mobile_app': 'Automatically configured - YAML config not needed',
            'met': 'Should be configured via UI in Settings → Integrations',
            'radio_browser': 'Should be configured via UI',
            'shopping_list': 'Built-in - no configuration needed',
            'sun': 'Built-in - no configuration needed',
            'system_health': 'Built-in - no configuration needed',
            'energy': 'Configured via UI in Settings → Energy',
        }
        
        for integration, reason in deprecated_integrations.items():
            if integration in config:
                self.deprecated_entries.append(f"'{integration}': {reason}")
    
    def _check_unnecessary_entries(self, config):
        """Check for unnecessary or redundant entries"""
        # Check for empty configurations
        empty_configs = ['api', 'python_script', 'frontend', 'history', 'logbook', 'recorder']
        for entry in empty_configs:
            if entry in config and (config[entry] == {} or config[entry] is None):
                self.unnecessary_entries.append(f"'{entry}: {{}}' - Empty config can be removed or simplified to '{entry}:'")
        
        # Check for default_config conflicts
        if 'default_config' in config:
            conflicting_entries = [
                'automation', 'config', 'frontend', 'history', 'logbook', 'media_source',
                'mobile_app', 'person', 'script', 'ssdp', 'sun', 'system_health', 'updater',
                'webhook', 'zeroconf', 'zone', 'discovery', 'map'
            ]
            for entry in conflicting_entries:
                if entry in config and entry != 'automation' and entry != 'script':
                    self.unnecessary_entries.append(f"'{entry}' - Redundant with default_config (unless customized)")
    
    def _check_problematic_patterns(self, content):
        """Check for problematic patterns in YAML content"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for resources.yaml include (no longer auto-loaded)
            if 'resources:' in line and '!include' in line:
                self.problematic_entries.append(f"Line {i}: 'resources: !include' - Frontend resources must be added via UI (Settings → Dashboards → Resources)")
            
            # Check for commented visualcrossing (already fixed)
            if line.strip().startswith('# visualcrossing:'):
                self.recommendations.append(f"Line {i}: visualcrossing commented out - good! Remove entirely if not using UI integration")
            
            # Check for deprecated YAML integrations
            if line.strip().startswith('discovery:'):
                self.deprecated_entries.append(f"Line {i}: 'discovery:' - Remove, now automatic")
            
            if line.strip().startswith('updater:'):
                self.deprecated_entries.append(f"Line {i}: 'updater:' - Remove, managed by Supervisor")
    
    def audit_resources_yaml(self):
        """Audit resources.yaml for broken or unnecessary entries"""
        resources_file = os.path.join(self.config_root, "resources.yaml")
        
        if not os.path.exists(resources_file):
            self.recommendations.append("resources.yaml not found - this is actually GOOD since resources should be managed via UI")
            return
        
        try:
            with open(resources_file, 'r') as f:
                resources = yaml.safe_load(f)
            
            # Common problematic resources
            problematic_resources = [
                '/hacsfiles/entity-registry-card/entity-registry-card.js',  # Often broken
                '/hacsfiles/custom-attributes/custom-attributes.js',        # Deprecated
                '/local/community/config-template-card/config-template-card.js',  # Wrong path
            ]
            
            resource_count = len(resources) if resources else 0
            self.recommendations.append(f"resources.yaml contains {resource_count} entries - Consider migrating to UI management")
            
            if resources:
                for resource in resources:
                    url = resource.get('url', '')
                    if url in problematic_resources:
                        self.problematic_entries.append(f"Problematic resource: {url} - likely broken or deprecated")
                    
                    # Check for /local/community paths (should be /hacsfiles)
                    if '/local/community/' in url:
                        self.problematic_entries.append(f"Outdated path: {url} - should probably be /hacsfiles/")
        
        except Exception as e:
            self.problematic_entries.append(f"Error reading resources.yaml: {e}")
    
    def audit_dwains_dashboard(self):
        """Check for empty or problematic Dwains Dashboard config"""
        config_file = os.path.join(self.config_root, "configuration.yaml")
        
        try:
            with open(config_file, 'r') as f:
                content = f.read()
            
            if 'dwains_dashboard:' in content and content.count('dwains_dashboard:') == content.count('dwains_dashboard:\n'):
                self.unnecessary_entries.append("'dwains_dashboard:' - Empty config block, remove if not using Dwains Dashboard")
        
        except Exception as e:
            pass
    
    def generate_cleanup_recommendations(self):
        """Generate actionable cleanup recommendations"""
        cleanup_actions = []
        
        # High priority: Remove deprecated entries
        if self.deprecated_entries:
            cleanup_actions.append({
                'priority': 'HIGH',
                'category': 'Remove Deprecated Integrations',
                'actions': self.deprecated_entries
            })
        
        # Medium priority: Fix problematic entries
        if self.problematic_entries:
            cleanup_actions.append({
                'priority': 'MEDIUM', 
                'category': 'Fix Problematic Configurations',
                'actions': self.problematic_entries
            })
        
        # Low priority: Remove unnecessary entries
        if self.unnecessary_entries:
            cleanup_actions.append({
                'priority': 'LOW',
                'category': 'Remove Unnecessary Entries',
                'actions': self.unnecessary_entries
            })
        
        # Recommendations
        if self.recommendations:
            cleanup_actions.append({
                'priority': 'INFO',
                'category': 'General Recommendations', 
                'actions': self.recommendations
            })
        
        return cleanup_actions
    
    def audit_all(self):
        """Run complete configuration audit"""
        print("🧹 Starting Configuration Audit...")
        
        # Audit main areas
        self.audit_configuration_yaml()
        self.audit_resources_yaml()
        self.audit_dwains_dashboard()
        
        # Generate recommendations
        cleanup_actions = self.generate_cleanup_recommendations()
        
        # Create summary
        summary = {
            'timestamp': datetime.now().isoformat(),
            'deprecated_count': len(self.deprecated_entries),
            'problematic_count': len(self.problematic_entries),
            'unnecessary_count': len(self.unnecessary_entries),
            'recommendations_count': len(self.recommendations),
            'cleanup_actions': cleanup_actions,
            'total_issues': len(self.deprecated_entries) + len(self.problematic_entries) + len(self.unnecessary_entries)
        }
        
        return summary
    
    def save_audit_log(self, summary):
        """Save audit results to log file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(self.log_dir, f'config_cleanup_audit_{timestamp}.log')
        
        with open(log_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Also save as latest
        latest_file = os.path.join(self.log_dir, 'latest_config_audit.json')
        with open(latest_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        return log_file

def main():
    """Main execution function"""
    auditor = ConfigurationAuditor()
    summary = auditor.audit_all()
    
    # Save results
    log_file = auditor.save_audit_log(summary)
    
    # Print summary
    print(f"\n🧹 Configuration Cleanup Audit Complete")
    print(f"Timestamp: {summary['timestamp']}")
    print(f"Total Issues Found: {summary['total_issues']}")
    print(f"  - Deprecated Entries: {summary['deprecated_count']}")
    print(f"  - Problematic Entries: {summary['problematic_count']}")
    print(f"  - Unnecessary Entries: {summary['unnecessary_count']}")
    print(f"  - Recommendations: {summary['recommendations_count']}")
    
    # Print actionable cleanup
    print(f"\n📋 Cleanup Actions:")
    for action_group in summary['cleanup_actions']:
        print(f"\n{action_group['priority']} PRIORITY: {action_group['category']}")
        for action in action_group['actions']:
            print(f"  • {action}")
    
    print(f"\n📄 Full report saved to: {log_file}")
    print(f"🔧 Use this audit to clean up configuration.yaml and improve system stability")

if __name__ == "__main__":
    main()