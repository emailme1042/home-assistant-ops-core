import sys
import requests
from openai import OpenAI
import yaml

# Logging arguments
with open("/config/python_scripts/chatgpt_debug.log", "w") as f:
    f.write(f"Argv: {sys.argv}\n")

prompt = sys.argv[1] if len(sys.argv) > 1 else "No prompt provided"

with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
    f.write(f"Prompt: {prompt}\n")

# Load secrets.yaml
with open("/config/secrets.yaml") as f:
    secrets = yaml.safe_load(f)

ha_url = secrets.get("ha_url", "http://homeassistant.local:8123")
ha_token = secrets.get("ha_long_lived_token")
openai_api_key = secrets.get("openai_api_key")

if not openai_api_key:
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write("OpenAI API key missing!\n")
    sys.exit(1)

if not ha_token:
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write("HA token missing!\n")
    sys.exit(1)

with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
    f.write("HA URL and token loaded from secrets.yaml\n")
    f.write("OpenAI key loaded from secrets.yaml\n")

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful smart home assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    gpt_reply = response.choices[0].message.content.strip()

    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write(f"GPT reply (full): {gpt_reply}\n")
except Exception as e:
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write(f"OpenAI error: {str(e)}\n")
    sys.exit(1)

# Update HA input_text (still works for short display)
url = f"{ha_url}/api/states/input_text.gpt_text_reply"
headers = {
    "Authorization": f"Bearer {ha_token}",
    "content-type": "application/json",
}
data = {
    "state": gpt_reply[:255]  # HA input_text still limited for fallback
}
try:
    r = requests.post(url, headers=headers, json=data)
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write(f"HA response code: {r.status_code}\n")
        f.write(f"HA response text: {r.text}\n")
except Exception as e:
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write(f"HA update error: {str(e)}\n")
    sys.exit(1)

# Write full reply to file for markdown display
try:
    with open("/config/www/gpt_response.txt", "w") as f:
        f.write(gpt_reply)
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write("Successfully wrote full reply to file.\n")
except Exception as e:
    with open("/config/python_scripts/chatgpt_debug.log", "a") as f:
        f.write(f"File write error: {str(e)}\n")
