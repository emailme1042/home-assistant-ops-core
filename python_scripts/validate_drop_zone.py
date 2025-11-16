import os, yaml, time

DROP_ZONE = "/config/ai_workspace"
REQUIRED_KEYS = ["alias", "trigger", "action"]

def validate_yaml(file_path):
    try:
        with open(file_path) as f:
            data = yaml.safe_load(f)
        missing = [k for k in REQUIRED_KEYS if k not in data]
        return "✅ Valid" if not missing else f"⚠️ Missing keys: {missing}"
    except Exception as e:
        return f"❌ YAML error: {str(e)}"

def scan_drop_zone():
    for fname in os.listdir(DROP_ZONE):
        if fname.endswith(".yaml"):
            fpath = os.path.join(DROP_ZONE, fname)
            age = time.time() - os.path.getmtime(fpath)
            status = validate_yaml(fpath)
            print(f"{fname}: {status} (Age: {int(age)}s)")

if __name__ == "__main__":
    scan_drop_zone()
