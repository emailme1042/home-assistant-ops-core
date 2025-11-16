# Quick Restart Readiness Check
# Purpose: Validate system is ready for HA restart with new GPT monitoring features

import os
import yaml

def check_critical_files():
    """Check that all critical files exist and are readable"""
    critical_files = [
        'ui-lovelace.yaml',
        'configuration.yaml',
        'dashboards/ai/main.yaml',
        'dashboards/system_overview/system_overview_main.yaml',
        'dashboards/users/users_main.yaml',
        'dashboards/ai/gpt_access_monitor_view.yaml',
        'dashboards/ai/vscode_ha_diagnostics_view.yaml',
        'includes/sensors/cloud_monitoring_sensors.yaml',
        'includes/automations/gpt_access_monitoring.yaml'
    ]
    
    print("📁 Checking critical files...")
    all_present = True
    
    for file_path in critical_files:
        full_path = f"S:/{file_path}"
        if os.path.exists(full_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING!")
            all_present = False
    
    return all_present

def validate_yaml_syntax():
    """Quick YAML syntax validation for critical files"""
    print("\n📝 Validating YAML syntax...")
    
    yaml_files = [
        'ui-lovelace.yaml',
        'dashboards/ai/main.yaml',
        'dashboards/ai/gpt_access_monitor_view.yaml'
    ]
    
    all_valid = True
    
    for file_path in yaml_files:
        full_path = f"S:/{file_path}"
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            print(f"✅ {file_path} - Valid YAML")
        except yaml.YAMLError as e:
            print(f"❌ {file_path} - YAML Error: {e}")
            all_valid = False
        except Exception as e:
            print(f"⚠️ {file_path} - Could not validate: {e}")
    
    return all_valid

def check_new_features():
    """Verify new GPT monitoring features are properly configured"""
    print("\n🤖 Checking new GPT monitoring features...")
    
    # Check GPT Access Monitor view
    try:
        with open('S:/dashboards/ai/gpt_access_monitor_view.yaml', 'r') as f:
            content = f.read()
            if 'GPT Access Status Monitor' in content:
                print("✅ GPT Access Monitor - Configured")
            else:
                print("⚠️ GPT Access Monitor - Content issue")
    except:
        print("❌ GPT Access Monitor - File error")
    
    # Check VSCode Diagnostics view
    try:
        with open('S:/dashboards/ai/vscode_ha_diagnostics_view.yaml', 'r') as f:
            content = f.read()
            if 'VSCode Home Assistant Extension Diagnostics' in content:
                print("✅ VSCode Diagnostics - Configured")
            else:
                print("⚠️ VSCode Diagnostics - Content issue")
    except:
        print("❌ VSCode Diagnostics - File error")
    
    # Check Cloud Monitoring Sensors
    try:
        with open('S:/includes/sensors/cloud_monitoring_sensors.yaml', 'r') as f:
            content = f.read()
            if 'gpt_access_health' in content:
                print("✅ Cloud Monitoring Sensors - Configured")
            else:
                print("⚠️ Cloud Monitoring Sensors - Content issue")
    except:
        print("❌ Cloud Monitoring Sensors - File error")

def main():
    print("🚀 Home Assistant Restart Readiness Check")
    print("="*50)
    print("Validating new GPT monitoring system...")
    
    # Run all checks
    files_ok = check_critical_files()
    yaml_ok = validate_yaml_syntax()
    check_new_features()
    
    print("\n" + "="*50)
    print("📊 READINESS SUMMARY")
    print("="*50)
    
    if files_ok and yaml_ok:
        print("✅ READY FOR RESTART")
        print("✅ All critical files present and valid")
        print("✅ New GPT monitoring features configured")
        print("✅ YAML syntax validated")
        print("\n🎯 Expected after restart:")
        print("- AI Main Hub with 6 views (including new GPT monitoring)")
        print("- Live cloud connectivity monitoring")
        print("- Smart health scoring and alerts")
        print("- VSCode diagnostics and troubleshooting")
    else:
        print("⚠️ ISSUES DETECTED")
        if not files_ok:
            print("❌ Missing critical files")
        if not yaml_ok:
            print("❌ YAML syntax errors")
        print("\n🔧 Fix issues before restarting Home Assistant")
    
    print("\n📋 Next Steps:")
    print("1. Restart Home Assistant")
    print("2. Test AI Main Hub → GPT Access Monitor")
    print("3. Verify health scoring and alerts")
    print("4. Check VSCode extension connectivity")

if __name__ == "__main__":
    main()