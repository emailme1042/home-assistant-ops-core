import yaml, os, datetime

# === CONFIG ===
WORKSPACE_ROOT = "S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/"
MERGE_MAP_PATH = os.path.join(WORKSPACE_ROOT, "merge_map.yaml")
WARNING_LOG = os.path.join(WORKSPACE_ROOT, "_merge_warnings.log")

# === FUNCTIONS ===
def log_warning(msg):
    with open(WARNING_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] ⚠️ {msg}\n")
    print(f"⚠️ {msg}")

def append_to_file(target, content):
    with open(target, "a", encoding="utf-8") as f:
        f.write(content + "\n")

def archive_source(filepath, merged_target):
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(
                f"\n\n---\n⚙️ Archived on {datetime.datetime.now().strftime('%Y-%m-%d')} — content merged into {merged_target}\n#archived_{datetime.datetime.now().strftime('%Y%m%d')}\n"
            )
    except Exception as e:
        log_warning(f"Could not archive {filepath}: {e}")

# === MAIN LOGIC ===
def merge_markdown_files():
    print("🔍 Loading merge map...")
    if not os.path.exists(MERGE_MAP_PATH):
        print("❌ merge_map.yaml not found!")
        return

    with open(MERGE_MAP_PATH, "r", encoding="utf-8") as f:
        merge_map = yaml.safe_load(f)

    for target, details in merge_map.get("merge_targets", {}).items():
        output_path = details["output_path"]
        includes = details["includes"]
        target_file = os.path.join(output_path, target)

        print(f"\n🧠 Merging into {target_file}")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        append_to_file(target_file, f"# 🧠 Auto-Merged: {timestamp}\n")

        for src in includes:
            src_path = os.path.join(WORKSPACE_ROOT, src)
            if os.path.exists(src_path):
                print(f"  ✅ Adding {src}")
                with open(src_path, "r", encoding="utf-8") as s:
                    append_to_file(target_file, f"\n\n---\n# 📄 {src}\n\n{s.read()}")
                archive_source(src_path, target)
            else:
                log_warning(f"Missing file: {src}")
                append_to_file(target_file, f"\n\n---\n# ⚠️ Missing file: {src}\n")

    print("\n✅ Merge complete! Check output files and _merge_warnings.log for details.\n")

# === EXECUTE ===
if __name__ == "__main__":
    print("🚀 Starting resilient markdown merge...")
    merge_markdown_files()
