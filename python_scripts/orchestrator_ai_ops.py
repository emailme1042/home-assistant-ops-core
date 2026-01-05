import yaml
import requests
from openai import OpenAI
import os
import shutil

# Load secrets
secrets_file = "/config/secrets.yaml"
with open(secrets_file, "r", encoding="utf-8") as f:
    secrets = yaml.safe_load(f)

ha_token = secrets.get("ha_long_lived_token")
openai_key = secrets.get("openai_api_key")
client = OpenAI(api_key=openai_key)

headers = {
    "Authorization": f"Bearer {ha_token}",
    "Content-Type": "application/json",
}

# -------------------------
# 1️⃣ Get all states
# -------------------------
response = requests.get("http://192.168.1.217:8123/api/states", headers=headers)
entities = response.json()

summary_text = f"Total entities: {len(entities)}\n"
summary_text += "Entity examples:\n"

for e in entities[:10]:
    summary_text += f"- {e['entity_id']}: {e['state']}\n"

summary_text += "\n# Additional context for AI (advanced):\n"
summary_text += "- Focus on dynamic dashboards (auto-entities, no static lists).\n"
summary_text += "- Identify broken or inactive entities for fixing or removal.\n"
summary_text += "- Suggest improved helpers, automations, and dynamic UI.\n"
summary_text += "- Provide future improvement block in YAML comments.\n"

# -------------------------
# 2️⃣ Send to GPT
# -------------------------
messages = [
    {
        "role": "system",
        "content": "You are an expert Home Assistant YAML designer. Suggest improvements, dynamic dashboards, helpers, automations, and future enhancements using the provided system data."
    },
    {
        "role": "user",
        "content": summary_text,
    },
]

ai_response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
)

yaml_suggestion = ai_response.choices[0].message.content

# -------------------------
# 3️⃣ Save to approved.yaml
# -------------------------
approved_file = "/config/includes/dashboard_suggestions/approved.yaml"
with open(approved_file, "w", encoding="utf-8") as f:
    f.write(yaml_suggestion)

print("✅ New YAML suggestion saved to approved.yaml")

# -------------------------
# 4️⃣ Copy to www for UI access
# -------------------------
www_target = "/config/www/includes/dashboard_suggestions/approved.yaml"
os.makedirs(os.path.dirname(www_target), exist_ok=True)
shutil.copyfile(approved_file, www_target)

print("✅ Copied approved.yaml to /www for UI preview.")
print("✅ Orchestrator finished successfully.")
