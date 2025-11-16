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

api_key = "secrets.yaml"

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

try:
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers_openai, json=json_data, timeout=30)
    print(f"DEBUG: OpenAI response status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        suggestions = result["choices"][0]["message"]["content"]
        print("DEBUG: Suggestions received from OpenAI")
        
        # Send suggestions back to HA
        suggestion_data = {"suggestions": suggestions}
        resp_suggest = requests.post(f"{ha_url}/api/services/input_text/set_value", 
                                   headers=headers, 
                                   json={"entity_id": "input_text.ai_suggestions", "value": suggestions[:255]})
        print(f"DEBUG: Suggestions sent to HA: {resp_suggest.status_code}")
        
    else:
        print(f"DEBUG: OpenAI error: {response.status_code} - {response.text}")
        
except Exception as e:
    print(f"DEBUG: Error: {e}")

print("DEBUG: AI Python script completed.")</content>
<parameter name="filePath">s:\python_scripts\ai_generate_suggestions.py
