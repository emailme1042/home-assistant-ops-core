import os
import yaml

DASHBOARD_ROOT = "S:/dashboards"
CONFIG_PATH = "S:/configuration.yaml"

def load_yaml(path):
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.constructor.ConstructorError:
        print(f"⚠ Skipping unsupported tags in: {path}")
        return {}
    except Exception as e:
        print(f"⚠ Error reading {path}: {e}")
        return {}

def collect_dashboard_files(base_dir):
    dashboards = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, DASHBOARD_ROOT)
                dashboards[relative.replace("\\", "/")] = full_path
    return dashboards

def extract_dashboard_metadata(file_path):
    content = load_yaml(file_path)
    title = content.get("title", "Unknown")
    path = content.get("path", "N/A")
    icon = content.get("icon", "N/A")
    return title, path, icon

def verify_mounts():
    config = load_yaml(CONFIG_PATH)
    declared = config.get("lovelace", {}).get("dashboards", {})

    file_map = collect_dashboard_files(DASHBOARD_ROOT)
    print(f"\n{'Slug':<25} {'File':<50} {'Admin':<6} {'Status':<20} {'Title':<30} {'Path':<15}")
    print(f"{'-'*150}")

    declared_paths = []

    for slug, entry in declared.items():
        path = entry.get("filename", "")
        is_admin = entry.get("require_admin", False)
        normalized = os.path.normcase(path.replace("/", "\\"))
        declared_paths.append(normalized)

        matched = next((f for f in file_map if os.path.normcase(f.replace("/", "\\")) == normalized), None)

        if matched:
            title, dash_path, icon = extract_dashboard_metadata(file_map[matched])
            status = "✅ OK"
            # Additional checks
            if ("admin" in matched.lower() and not is_admin):
                status = "⚠ Wrong folder for non-admin"
            elif ("users" in matched.lower() and is_admin):
                status = "⚠ User folder but requires admin"
        else:
            title, dash_path, icon = "Missing", "-", "-"
            status = "❌ Missing file"

        print(f"{slug:<25} {path:<50} {str(is_admin):<6} {status:<20} {title:<30} {dash_path:<15}")

    # Undeclared files
    for rel_path in file_map:
        norm_rel = os.path.normcase(rel_path.replace("/", "\\"))
        if norm_rel not in declared_paths:
            title, dash_path, icon = extract_dashboard_metadata(file_map[rel_path])
            print(f"{'-':<25} {rel_path:<50} {'-':<6} ⚠ Unmounted dashboard   {title:<30} {dash_path:<15}")

if __name__ == "__main__":
    verify_mounts()

input("\n✅ Script complete. Press Enter to close...")
