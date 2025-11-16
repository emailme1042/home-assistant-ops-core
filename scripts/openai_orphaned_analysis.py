# openai_orphaned_analysis.py
# Purpose: Read orphaned file scan from flat file, send to OpenAI, save response

import requests
import datetime
import os
import yaml

# === Load secrets from secrets.yaml ===
with open("/config/secrets.yaml", "r") as f:
    secrets = yaml.safe_load(f)

HA_TOKEN = secrets.get("ha_token")
OPENAI_KEY = secrets.get("openai_api_key")
HA_URL = secrets.get("ha_url")

SCAN_FILE = "/config/sensors/orphaned_file_scan.txt"
OUTPUT_DIR = "/config/www/context_snapshots"

def write_error(msg):
    error_path = os.path.join(OUTPUT_DIR, "orphaned_analysis_error.txt")
    with open(error_path, "w", encoding="utf-8") as f:
        f.write(msg)

# === Precheck: Secrets ===
if not HA_TOKEN or not OPENAI_KEY or not HA_URL:
    write_error("Missing HA token, OpenAI key, or HA URL in secrets.yaml")
    exit()

# === Precheck: Scan File ===
if not os.path.exists(SCAN_FILE):
    write_error("Scan file not found: orphaned_file_scan.txt")
    exit()

with open(SCAN_FILE, "r", encoding="utf-8") as f:
    orphaned_data = f.read().strip()

if not orphaned_data:
    write_error("Scan file exists but is empty.")
    exit()

# === Create Prompt ===
prompt = f"""Analyze the following orphaned Home Assistant files. Recommend cleanup or recovery:
{orphaned_data}"""

# === Call OpenAI ===
payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.5
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    },
    json=payload
)

if response.status_code != 200:
    write_error(f"OpenAI call failed: {response.status_code}\n{response.text}")
    exit()

reply = response.json()["choices"][0]["message"]["content"]

# === Save Response ===
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
filename = f"orphaned_analysis_{timestamp}.txt"
filepath = os.path.join(OUTPUT_DIR, filename)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(reply)

print("Analysis saved:", filepath)
