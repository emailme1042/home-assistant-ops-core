# validate_lovelace_config.py
import os
import re
import yaml

# --- CONFIGURE THESE PATHS ---
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Navigate to config root (up 4 levels from SESSION_ESSENTIALS)
config_root = os.path.abspath(os.path.join(script_dir, '..', '..', '..', '..'))
DASHBOARD_PATH = os.path.join(config_root, 'dashboards')
AUTOMATIONS_PATH = os.path.join(config_root, 'includes', 'automations')

print(f"🔍 Scanning from config root: {config_root}")
print(f"📊 Dashboard path: {DASHBOARD_PATH}")
print(f"🤖 Automations path: {AUTOMATIONS_PATH}")

RESULTS = []

def load_yaml_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'!include.*', '', content)  # remove HA-specific tags
        return yaml.safe_load(content)
    except Exception as e:
        return {"error": str(e)}

def scan_dashboards():
    if not os.path.exists(DASHBOARD_PATH):
        RESULTS.append(("DASHBOARD_PATH", f"❌ Path not found: {DASHBOARD_PATH}"))
        return
    
    dashboard_count = 0
    for root, _, files in os.walk(DASHBOARD_PATH):
        for file in files:
            if file.endswith('.yaml'):
                dashboard_count += 1
                full = os.path.join(root, file)
                data = load_yaml_safe(full)
                if isinstance(data, dict) and "error" in data:
                    RESULTS.append((full, f"❌ YAML Error: {data['error']}"))
                    continue
                if not isinstance(data, dict) or 'views' not in data:
                    RESULTS.append((full, "❌ Missing or invalid `views:` block"))
                    continue
                for view in data.get('views', []):
                    if 'cards' not in view:
                        RESULTS.append((full, f"❌ View '{view.get('title','Unnamed')}' has no cards"))
                    for card in view.get('cards', []):
                        ctype = card.get('type', '')
                        if 'custom:' in ctype or 'layout' in ctype:
                            RESULTS.append((full, f"⚠️ Custom card used: {ctype}"))
    
    print(f"📊 Found {dashboard_count} dashboard files")

def scan_automations():
    if not os.path.exists(AUTOMATIONS_PATH):
        RESULTS.append(("AUTOMATIONS_PATH", f"❌ Path not found: {AUTOMATIONS_PATH}"))
        return
    
    automation_count = 0
    for root, _, files in os.walk(AUTOMATIONS_PATH):
        for file in files:
            if file.endswith('.yaml'):
                automation_count += 1
                full = os.path.join(root, file)
                data = load_yaml_safe(full)
                if isinstance(data, dict) and "error" in data:
                    RESULTS.append((full, f"❌ YAML Error: {data['error']}"))
                    continue
                if not isinstance(data, list):
                    RESULTS.append((full, "❌ Invalid format (expected list of automations)"))
                    continue
                for a in data:
                    if not isinstance(a, dict): continue
                    if not a.get('id') or not a.get('alias'):
                        RESULTS.append((full, "⚠️ Missing `id:` or `alias:`"))
    
    print(f"🤖 Found {automation_count} automation files")

scan_dashboards()
scan_automations()

print("\n--- VALIDATION REPORT ---")
if not RESULTS:
    print("✅ All checked YAML files passed.")
else:
    print(f"Found {len(RESULTS)} issues:")
    for path, issue in RESULTS:
        print(f"{path} → {issue}")