import requests
import os

print("DEBUG: AI Python script started.")

# -------- CONFIG --------
ha_url = "secrets.yaml"  # Update if different
token = "secrets.yaml"
api_key = "secrets.yaml"

# ------------------------

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# Fetch dashboard_target
resp_target = requests.get(f"{ha_url}/api/states/input_text.ai_dashboard_target", headers=headers)
dashboard_target = resp_target.json().get("state", "NoTarget")
print(f"DEBUG: Dashboard target: {dashboard_target}")

# Fetch request_type
resp_type = requests.get(f"{ha_url}/api/states/input_select.ai_request_type", headers=headers)
request_type = resp_type.json().get("state", "NoType")
print(f"DEBUG: Request type: {request_type}")

# Read context snapshot
context_file = "/config/ai_suggestions/context_snapshot.txt"
if os.path.exists(context_file):
    with open(context_file, "r", encoding="utf-8") as f:
        context_data = f.read()
else:
    context_data = "No context snapshot found."

print("DEBUG: Context snapshot loaded.")

# Build prompt
prompt = f"""
Here is my full Home Assistant context snapshot:

{context_data}

You are an expert Home Assistant developer. Using these details, help me improve or create a {request_type.lower()} for {dashboard_target}.
Please provide YAML code suggestions, fully formatted, using only valid entity IDs, helpers, and correct references where possible.
"""

api_key = "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"

headers_openai = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

json_data = {
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.7
}

print("DEBUG: Sending request to OpenAI...")

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers_openai, json=json_data)
response_json = response.json()
print("DEBUG: Full OpenAI response:", response_json)

if "choices" in response_json:
    response_text = response_json["choices"][0]["message"]["content"]
else:
    print("ERROR: OpenAI response missing 'choices' key. Full response above.")
    exit(1)


output_dir = "/config/ai_suggestions"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = os.path.join(output_dir, "last_suggestion.yaml")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(response_text)

print(f"DEBUG: Suggestion written to {file_path}")
