import os
import yaml

# Folder to scan
INCLUDE_DIR = "/includes"

def extract_includes(yaml_data):
    """Find all !include paths in the loaded YAML."""
    includes = []
    if isinstance(yaml_data, dict):
        for key, value in yaml_data.items():
            includes.extend(extract_includes(value))
    elif isinstance(yaml_data, list):
        for item in yaml_data:
            includes.extend(extract_includes(item))
    elif isinstance(yaml_data, str):
        if "!include" in yaml_data:
            includes.append(yaml_data.replace("!include", "").strip())
    return includes

def validate_includes(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r") as stream:
                        content = stream.read()
                        yaml_data = yaml.load(content, Loader=yaml.SafeLoader)
                        includes = extract_includes(yaml_data)
                        for inc in includes:
                            inc_path = os.path.join(os.path.dirname(path), inc)
                            if not os.path.exists(inc_path):
                                print(f"❌ {file} → {inc} not found")
                except Exception as e:
                    print(f"⚠️ Error in {file}: {e}")

# Run
print(f"🔍 Scanning includes in {INCLUDE_DIR}...")
validate_includes(INCLUDE_DIR)
print("✅ Scan complete.")
