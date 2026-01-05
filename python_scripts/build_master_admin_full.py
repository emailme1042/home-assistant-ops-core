import os
import glob
import yaml
import openai

# Load the OpenAI API key from secrets.yaml
with open("S:/secrets.yaml", 'r', encoding='utf-8') as f:
    secrets = yaml.safe_load(f)

openai.api_key = secrets.get('openai_api_key')

# Paths
ROOT_PATH = "S:/"
BACKUP_PATH = "S:/_archived_backups/ai_fixes"
FINAL_ADMIN_PATH = "S:/DASHBOARDS/master-admin.yaml"

os.makedirs(BACKUP_PATH, exist_ok=True)

# Final categories
categories = [
    "Dashboards",
    "Automations",
    "Scripts",
    "Scenes",
    "Helpers & Includes",
    "UI & Views",
    "Blueprints",
    "Custom Components",
    "OpenAI / GPT Hybrid",
    "Other"
]

def categorize_file(file_path, content):
    # Use OpenAI to suggest category
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a Home Assistant YAML expert. Categorize this YAML file into one of the following categories: "
                    "Dashboards, Automations, Scripts, Scenes, Helpers & Includes, UI & Views, Blueprints, Custom Components, OpenAI / GPT Hybrid, or Other. "
                    "Reply ONLY with the exact category name."
                )
            },
            {"role": "user", "content": content}
        ]
    )
    suggestion = response.choices[0].message['content'].strip()
    return suggestion if suggestion in categories else "Other"

def build_master_admin(views_dict):
    master_admin = {
        "title": "Master Admin",
        "path": "admin-root",
        "icon": "mdi:shield-crown",
        "show_in_sidebar": True,
        "require_admin": True,
        "views": []
    }

    for category, files in views_dict.items():
        if not files:
            continue

        view = {
            "title": category,
            "path": category.lower().replace(" ", "-"),
            "icon": "mdi:view-dashboard",
            "cards": []
        }

        for file_path in files:
            filename = os.path.basename(file_path)
            display_name = filename.replace(".yaml", "").replace(".yml", "").replace("_", " ").title()

            button_card = {
                "type": "button",
                "name": display_name,
                "icon": "mdi:file-document-outline",
                "tap_action": {
                    "action": "navigate",
                    "navigation_path": f"/lovelace/{filename.replace('.yaml','').replace('.yml','')}"
                }
            }
            view["cards"].append(button_card)

        master_admin["views"].append(view)

    # Add dedicated GPT Hybrid view
    gpt_view = {
        "title": "OpenAI / GPT Hybrid",
        "path": "openai-gpt",
        "icon": "mdi:robot",
        "cards": [
            {
                "type": "markdown",
                "content": "## 🤖 OpenAI & GPT Hybrid Tools\nUse these tools to build, tweak, and fix your setup live."
            },
            {
                "type": "button",
                "name": "Dashboard Builder",
                "icon": "mdi:hammer-wrench",
                "tap_action": {"action": "call-service", "service": "script.dashboard_builder"}
            },
            {
                "type": "button",
                "name": "Dashboard Tweaker",
                "icon": "mdi:tune",
                "tap_action": {"action": "call-service", "service": "script.dashboard_tweaker"}
            },
            {
                "type": "button",
                "name": "Entity Fixer",
                "icon": "mdi:bug-check",
                "tap_action": {"action": "call-service", "service": "script.entity_fixer"}
            },
            {
                "type": "button",
                "name": "Ask AI",
                "icon": "mdi:chat-question",
                "tap_action": {"action": "call-service", "service": "script.ask_ai"}
            },
            {
                "type": "button",
                "name": "Admin AI Tools",
                "icon": "mdi:robot-industrial",
                "tap_action": {"action": "call-service", "service": "script.admin_ai_tools"}
            }
        ]
    }
    master_admin["views"].append(gpt_view)

    # Save draft
    draft_path = os.path.join(BACKUP_PATH, "master-admin-draft.yaml")
    with open(draft_path, 'w', encoding='utf-8') as f:
        yaml.dump(master_admin, f, default_flow_style=False, allow_unicode=True)

    print(f"📝 Draft Master Admin YAML saved at: {draft_path}")

    confirm = input("✅ Type 'yes' to finalize and write to Master Admin YAML: ").strip().lower()
    if confirm == "yes":
        with open(FINAL_ADMIN_PATH, 'w', encoding='utf-8') as f:
            yaml.dump(master_admin, f, default_flow_style=False, allow_unicode=True)
        print(f"✅ Master Admin YAML saved at: {FINAL_ADMIN_PATH}")
    else:
        print("⚠️ Final write skipped. Draft is saved for review.")

def process_files():
    yaml_files = glob.glob(os.path.join(ROOT_PATH, '**', '*.yaml'), recursive=True)
    yaml_files += glob.glob(os.path.join(ROOT_PATH, '**', '*.yml'), recursive=True)

    views_dict = {category: [] for category in categories}

    for file in yaml_files:
        if os.path.basename(file).lower() in ["master-admin.yaml", "main-dashboard.yaml"]:
            continue

        print(f"🔎 Processing: {file}")
        try:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            category = categorize_file(file, content)
            print(f"📂 Categorized as: {category}")

            views_dict[category].append(file)

        except Exception as e:
            print(f"⚠️ Error processing {file}: {e}")

    build_master_admin(views_dict)

if __name__ == "__main__":
    process_files()
    print("✅ All files analyzed and Master Admin draft (FULL CONFIG MODE) generated.")
