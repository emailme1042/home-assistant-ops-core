#!/usr/bin/env python3
import yaml
import requests
from openai import OpenAI
import os
import shutil

# -----------------------------
# Load secrets
# -----------------------------
secrets_file = "/config/secrets.yaml"
if not os.path.exists(secrets_file):
    secrets_file = "S:/secrets.yaml"  # Windows mapped fallback

with open(secrets_file, "r", encoding="utf-8") as f:
    secrets = yaml.safe_load(f)

ha_token = secrets.get("ha_long_lived_token")
openai_key = secrets.get("openai_api_key")
if not ha_token or not openai_key:
    raise ValueError("❌ Missing ha_long_lived_token or openai_api_key in secrets.yaml")

client = OpenAI(api_key=openai_key)

headers = {
    "Authorization": f"Bearer {ha_token}",
    "Content-Type": "application/json",
}

# -----------------------------
# Fetch HA states
# -----------------------------
response = requests.get("http://192.168.1.217:8123/api/states", headers=headers)
if response.status_code != 200:
    raise ConnectionError(f"❌ Failed to fetch HA states. Status code: {response.status_code}")

entities = response.json()

# -----------------------------
# Build summary
# -----------------------------
summary_text = f"Total entities: {len(entities)}\n"
summary_text += "Examples:\n"
for e in entities[:15]:  # Adjustable
    summary_text += f"- {e['entity_id']}: {e['state']}\n"

summary_text += "\n# Additional context:\n"
summary_text += "- Dynamic dashboards only (auto-entities, no static lists).\n"
summary_text += "- Identify broken or inactive entities.\n"
summary_text += "- Suggest improved automations, helpers, dynamic UI.\n"
summary_text += "- Provide future improvement block as YAML comments.\n"

# -----------------------------
# Load dashboard snippets (optional)
# -----------------------------
dashboards_dir = "/config/dashboards/"
dash_snippets = []

if os.path.exists(dashboards_dir):
    for file_name in os.listdir(dashboards_dir):
        if file_name.endswith(".yaml"):
            with open(os.path.join(dashboards_dir, file_name), "r", encoding="utf-8") as f:
                dash_snippets.append(f.read())

if dash_snippets:
    summary_text += "\n# Example dashboard YAML snippets:\n"
    summary_text += "\n---\n".join(dash_snippets[:2])

# -----------------------------
# Send to GPT
# -----------------------------
messages = [
    {
        "role": "system",
        "content": "You are an expert Home Assistant YAML architect. Suggest dynamic dashboards, helpers, automations, and improvements. Avoid static lists."
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

# -----------------------------
# Save approved.yaml
# -----------------------------
approved_file = "/config/includes/dashboard_suggestions/approved.yaml"
os.makedirs(os.path.dirname(approved_file), exist_ok=True)

with open(approved_file, "w", encoding="utf-8") as f:
    f.write(yaml_suggestion)

print("✅ Saved YAML suggestion to approved.yaml")

# -----------------------------
# Copy to www for UI preview
# -----------------------------
www_target = "/config/www/includes/dashboard_suggestions/approved.yaml"
os.makedirs(os.path.dirname(www_target), exist_ok=True)
shutil.copyfile(approved_file, www_target)
print("✅ Copied approved.yaml to /www for preview")

# -----------------------------
# Update input_text in HA
# -----------------------------
ha_url = "http://192.168.1.217:8123/api/services/input_text/set_value"
payload = {
    "entity_id": "input_text.gpt_result_core",
    "value": yaml_suggestion[:1024]  # Truncate for HA input_text
}

update_resp = requests.post(ha_url, headers=headers, json=payload)

if update_resp.status_code == 200:
    print("✅ input_text.gpt_result_core updated successfully")
else:
    print(f"⚠️ Failed to update input_text.gpt_result_core: {update_resp.status_code}")

print("🎉 Finished: AI YAML generation and deployment pipeline complete.")
