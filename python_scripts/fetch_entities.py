import requests
import json
import os

# -------- CONFIG --------
ha_url = "http://127.0.0.1:8123"  # Adjust if different (e.g., http://192.168.1.x:8123)
token = "secrets.yaml"
output_file = "/config/ai_suggestions/entities.txt"
# ------------------------

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

print("DEBUG: Fetching entity list from HA API...")

response = requests.get(f"{ha_url}/api/states", headers=headers)
entities = response.json()

entity_ids = [e["entity_id"] for e in entities]
entity_ids.sort()

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(entity_ids))

print(f"DEBUG: Entity list written to {output_file}")
