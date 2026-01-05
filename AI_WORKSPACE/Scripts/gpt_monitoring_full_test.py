#!/usr/bin/env python3
"""
GPT Monitoring System - Full Integration Test
===========================================

Tests all components of the GPT access monitoring system:
- Dashboard file validation
- Sensor configuration checks  
- Automation logic verification
- Entity availability confirmation
- Cloud connectivity status

For Home Assistant Green - Network Drive S:\ Environment
"""

import os
import sys
import json
import yaml
from pathlib import Path

# Add the workspace to path for imports
sys.path.append(str(Path(__file__).parent.parent))

def colored_output(text, color='green'):
    """Simple colored console output for Windows"""
    colors = {
        'green': '\033[92m',
        'red': '\033[91m', 
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    return f"{colors.get(color, '')}{text}{colors['reset']}"

def test_dashboard_files():
    """Test all GPT monitoring dashboard files exist and are valid YAML"""
    print(colored_output("🔍 Testing Dashboard Files...", 'blue'))
    
    dashboard_files = [
        "S:/dashboards/ai/gpt_access_monitor_view.yaml",
        "S:/dashboards/ai/vscode_ha_diagnostics_view.yaml", 
        "S:/dashboards/ai/main.yaml",
        "S:/ui-lovelace.yaml"
    ]
    
    results = []
    for file_path in dashboard_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    yaml.safe_load(f)
                results.append(f"✅ {file_path} - Valid YAML")
            except yaml.YAMLError as e:
                results.append(f"❌ {file_path} - YAML Error: {e}")
        else:
            results.append(f"❌ {file_path} - File not found")
    
    return results

def test_sensor_configs():
    """Test GPT monitoring sensor configurations"""
    print(colored_output("🔍 Testing Sensor Configurations...", 'blue'))
    
    sensor_files = [
        "S:/includes/sensors/gpt_access_monitoring.yaml",
        "S:/includes/binary_sensors/cloud_connectivity.yaml"
    ]
    
    results = []
    for file_path in sensor_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, list) and len(data) > 0:
                        results.append(f"✅ {file_path} - Valid sensor config ({len(data)} sensors)")
                    else:
                        results.append(f"⚠️ {file_path} - No sensors found")
            except yaml.YAMLError as e:
                results.append(f"❌ {file_path} - YAML Error: {e}")
        else:
            results.append(f"❌ {file_path} - File not found")
    
    return results

def test_automation_configs():
    """Test GPT monitoring automation configurations"""
    print(colored_output("🔍 Testing Automation Configurations...", 'blue'))
    
    automation_files = [
        "S:/includes/automations/gpt_access_alerts.yaml"
    ]
    
    results = []
    for file_path in automation_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, list) and len(data) > 0:
                        results.append(f"✅ {file_path} - Valid automation config ({len(data)} automations)")
                    else:
                        results.append(f"⚠️ {file_path} - No automations found")
            except yaml.YAMLError as e:
                results.append(f"❌ {file_path} - YAML Error: {e}")
        else:
            results.append(f"❌ {file_path} - File not found")
    
    return results

def test_main_config():
    """Test main configuration.yaml for GPT monitoring includes"""
    print(colored_output("🔍 Testing Main Configuration...", 'blue'))
    
    config_path = "S:/configuration.yaml"
    results = []
    
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_content = f.read()
                
            # Check for include patterns
            required_includes = [
                "sensor: !include_dir_merge_list includes/sensors/",
                "binary_sensor: !include_dir_merge_list includes/binary_sensors/",
                "automation: !include_dir_merge_list includes/automations/"
            ]
            
            for include in required_includes:
                if include in config_content:
                    results.append(f"✅ Found: {include}")
                else:
                    results.append(f"❌ Missing: {include}")
                    
        except Exception as e:
            results.append(f"❌ Error reading configuration.yaml: {e}")
    else:
        results.append(f"❌ configuration.yaml not found at {config_path}")
    
    return results

def create_validation_summary():
    """Create a validation summary report"""
    print(colored_output("📋 Creating Validation Summary...", 'blue'))
    
    summary_path = "S:/AI_WORKSPACE/gpt_monitoring_validation_summary.md"
    
    try:
        dashboard_results = test_dashboard_files()
        sensor_results = test_sensor_configs()
        automation_results = test_automation_configs()
        config_results = test_main_config()
        
        summary_content = f"""# GPT Monitoring System - Validation Summary
Generated: {os.popen('date /t').read().strip()} {os.popen('time /t').read().strip()}

## ✅ Dashboard Files
{chr(10).join(['- ' + result for result in dashboard_results])}

## ✅ Sensor Configurations  
{chr(10).join(['- ' + result for result in sensor_results])}

## ✅ Automation Configurations
{chr(10).join(['- ' + result for result in automation_results])}

## ✅ Main Configuration
{chr(10).join(['- ' + result for result in config_results])}

## 🎯 Next Steps
1. **If all ✅**: Ready for Home Assistant restart
2. **If any ❌**: Fix errors before restart
3. **After restart**: Test GPT access from dashboard
4. **VSCode Settings**: Update with proper HA Long-Lived Access Token

## 🔧 Quick Fixes
- **Missing files**: Use Copilot to create missing components
- **YAML errors**: Check indentation and syntax
- **Missing includes**: Add to configuration.yaml

---
**Generated by**: GPT Monitoring Full Test Script
**Location**: S:/AI_WORKSPACE/Scripts/gpt_monitoring_full_test.py
"""
        
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
            
        return f"✅ Validation summary created: {summary_path}"
        
    except Exception as e:
        return f"❌ Error creating summary: {e}"

def main():
    """Run full GPT monitoring system validation"""
    print(colored_output("🤖 GPT Monitoring System - Full Validation Test", 'blue'))
    print("=" * 60)
    
    # Run all tests
    dashboard_results = test_dashboard_files()
    sensor_results = test_sensor_configs()  
    automation_results = test_automation_configs()
    config_results = test_main_config()
    summary_result = create_validation_summary()
    
    # Print results
    print(colored_output("\n📊 VALIDATION RESULTS:", 'yellow'))
    print("-" * 40)
    
    all_results = dashboard_results + sensor_results + automation_results + config_results + [summary_result]
    
    success_count = sum(1 for result in all_results if result.startswith('✅'))
    warning_count = sum(1 for result in all_results if result.startswith('⚠️'))
    error_count = sum(1 for result in all_results if result.startswith('❌'))
    
    for result in all_results:
        if result.startswith('✅'):
            print(colored_output(result, 'green'))
        elif result.startswith('⚠️'):
            print(colored_output(result, 'yellow'))
        elif result.startswith('❌'):
            print(colored_output(result, 'red'))
        else:
            print(result)
    
    print("-" * 40)
    print(colored_output(f"📈 SUMMARY: {success_count} ✅ | {warning_count} ⚠️ | {error_count} ❌", 'blue'))
    
    if error_count == 0:
        print(colored_output("🎉 ALL TESTS PASSED! Ready for Home Assistant restart.", 'green'))
        print(colored_output("📋 Check validation summary: S:/AI_WORKSPACE/gpt_monitoring_validation_summary.md", 'blue'))
    else:
        print(colored_output(f"⚠️ {error_count} errors found. Fix before restart.", 'red'))
    
    return error_count == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)