import os
import glob
import yaml
import shutil
from openai import OpenAI

# ✅ Embedded final mission statement as system prompt
MISSION_PROMPT = (
    "You are a Home Assistant YAML dashboard architect. "
    "Analyze and improve YAML dashboards under dashboards/aimagic and exploratory folders. "
    "Follow my refined mission: modular, minimal, dynamically updated, admin-first. "
    "Suggest structure fixes, remove outdated parts, ensure no drift. "
    "Propose future improvements. Always generate backups and summaries. "
    "Use dynamic cards (e.g., auto-entities, tabbed-card, mushroom) and advanced Lovelace features."
)

# Load OpenAI API key from secrets.yaml
with open("/secrets.yaml", 'r', encoding='utf-8') as f:
    secrets = yaml.safe_load(f)

client = OpenAI(api_key=secrets.get('openai_api_key'))

# Paths
DASHBOARD_ROOT = "S:/dashboards/aimagic"
BACKUP_PATH = "S:/_archived_backups/ai_fixes"
CLEAN_PATH = "S:/_archived_backups/final_auto_fixes"
EXPLORATORY_FOLDERS = ["S:/dashboards/lateradmin", "S:/dashboards/lateradmin/lastconsider"]

os.makedirs(BACKUP_PATH, exist_ok=True)
os.makedirs(CLEAN_PATH, exist_ok=True)

def validate_and_fix_dashboard(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": MISSION_PROMPT},
            {"role": "user", "content": content}
        ]
    )

    suggestion = response.choices[0].message.content

    base_name = os.path.basename(file_path)
    suggestion_file = os.path.join(BACKUP_PATH, f"{base_name}_AI_SUGGESTION.txt")
    with open(suggestion_file, 'w', encoding='utf-8') as f:
        f.write(suggestion)

    print(f"✅ AI suggestion saved: {suggestion_file}")

def auto_clean_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        if 'entity:' in line and ('null' in line or line.strip().endswith(':')):
            continue
        cleaned_lines.append(line)

    base_name = os.path.basename(file_path)
    cleaned_file = os.path.join(CLEAN_PATH, base_name)
    with open(cleaned_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

    print(f"✅ Auto-cleaned and saved: {cleaned_file}")

def move_cleaned_back():
    cleaned_files = glob.glob(os.path.join(CLEAN_PATH, '*.yaml'))
    for cleaned_file in cleaned_files:
        file_name = os.path.basename(cleaned_file)
        for root, dirs, files in os.walk(DASHBOARD_ROOT):
            if file_name in files:
                original_path = os.path.join(root, file_name)
                backup_orig = original_path + ".bak_before_replace"
                shutil.copy2(original_path, backup_orig)
                shutil.copy2(cleaned_file, original_path)
                print(f"✅ Replaced: {original_path} (backup saved as .bak_before_replace)")
                break

def collect_all_yaml_files():
    yaml_files = glob.glob(os.path.join(DASHBOARD_ROOT, '**', '*.yaml'), recursive=True)
    for folder in EXPLORATORY_FOLDERS:
        yaml_files += glob.glob(os.path.join(folder, '**', '*.yaml'), recursive=True)
        yaml_files += glob.glob(os.path.join(folder, '**', '*.bak'), recursive=True)
    return yaml_files

if __name__ == "__main__":
    yaml_files = collect_all_yaml_files()

    for file in yaml_files:
        print(f"🔎 Validating: {file}")
        validate_and_fix_dashboard(file)

    for file in yaml_files:
        print(f"🧹 Auto-cleaning: {file}")
        auto_clean_yaml(file)

    move = input("⚠️ Do you want to move cleaned dashboards back into live folders now? (y/n): ")
    if move.lower() == 'y':
        move_cleaned_back()
        print("✅ All dashboards validated, auto-cleaned, and live replacements done!")
    else:
        print("ℹ️ Cleaned dashboards are ready. You can review them before replacing.")
