from flask import Flask, request, jsonify
import os
from pathlib import Path
import yaml
import requests

app = Flask(__name__)

BASE_DIR = Path("/home/emailadmin/home-assistant-dashboards/includes")
BLOCKED_KEYWORDS = ["secret"]

def safe_path(subpath):
    full_path = (BASE_DIR / subpath).resolve()
    if BASE_DIR in full_path.parents and not any(kw in str(full_path) for kw in BLOCKED_KEYWORDS):
        return full_path
    return None

def get_ha_headers():
    try:
        with open('/secrets.yaml', 'r') as f:
            secrets = yaml.safe_load(f)
        token = secrets.get("home_assistant_token")
        if not token:
            raise ValueError("Missing home_assistant_token in secrets.yaml")
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    except Exception as e:
        print(f"❌ Failed to load HA token: {e}")
        return {}

@app.route("/jit_plugin/get_file_contents", methods=["GET"])
def get_file_contents():
    path = request.args.get("path")
    full_path = safe_path(path)
    if not full_path or not full_path.exists():
        return jsonify({"error": "Invalid or restricted path."}), 400
    try:
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return jsonify({"filename": str(full_path), "contents": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/jit_plugin/list_folder", methods=["GET"])
def list_folder():
    path = request.args.get("path")
    full_path = safe_path(path)
    if not full_path or not full_path.is_dir():
        return jsonify({"error": "Invalid or restricted folder."}), 400
    files = [f.name for f in full_path.iterdir() if not any(kw in f.name for kw in BLOCKED_KEYWORDS)]
    return jsonify({"folder": str(full_path), "files": files})

@app.route("/jit_plugin/execute_shell", methods=["POST"])
def execute_shell():
    data = request.json
    if not data or "command" not in data:
        return jsonify({"error": "Missing command."}), 400
    command = data["command"]
    confirmation = data.get("confirm", False)
    if confirmation != True:
        return jsonify({"status": "Confirmation required."}), 403
    try:
        output = os.popen(command).read()
        return jsonify({"command": command, "output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/jit_plugin/write_file", methods=["POST"])
def write_file():
    data = request.json
    path = data.get("path")
    content = data.get("content")
    confirm = data.get("confirm", False)
    full_path = safe_path(path)
    if not full_path or confirm != True:
        return jsonify({"error": "Invalid path or no confirmation."}), 403
    try:
        with open(full_path, "w") as f:
            f.write(content)
        return jsonify({"status": "File written", "path": str(full_path)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/jit_plugin/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive"})

@app.route('/api/input_boolean', methods=['POST'])
def toggle_input_boolean():
    data = request.get_json()
    entity_id = data.get("entity_id")
    if not entity_id:
        return jsonify({"error": "Missing entity_id"}), 400

    headers = get_ha_headers()
    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/services/input_boolean/toggle",
            headers=headers,
            json={"entity_id": entity_id}
        )
        return jsonify({"status": "toggled", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/chatgpt_query', methods=['POST'])
def chatgpt_query():
    data = request.get_json()
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    payload = {"state": prompt}
    headers = get_ha_headers()

    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/states/input_text.chatgpt_prompt",
            json=payload,
            headers=headers
        )
        return jsonify({"status": "sent", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/api/reload_automations', methods=['POST'])
def reload_automations():
    headers = get_ha_headers()
    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/services/automation/reload",
            headers=headers
        )
        return jsonify({"status": "reloaded", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reload_scripts', methods=['POST'])
def reload_scripts():
    headers = get_ha_headers()
    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/services/script/reload",
            headers=headers
        )
        return jsonify({"status": "scripts reloaded", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/input_text', methods=['POST'])
def set_input_text():
    data = request.get_json()
    entity_id = data.get("entity_id")
    value = data.get("value")
    if not entity_id or not value:
        return jsonify({"error": "Missing entity_id or value"}), 400

    headers = get_ha_headers()
    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/services/input_text/set_value",
            headers=headers,
            json={"entity_id": entity_id, "value": value}
        )
        return jsonify({"status": "value set", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/entity_state', methods=['GET'])
def get_entity_state():
    entity_id = request.args.get("entity_id")
    if not entity_id:
        return jsonify({"error": "Missing entity_id parameter"}), 400

    headers = get_ha_headers()
    try:
        r = requests.get(
            f"http://192.168.1.217:8123/api/states/{entity_id}",
            headers=headers
        )
        return jsonify({"entity": entity_id, "state": r.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/backup', methods=['POST'])
def create_backup():
    data = request.get_json()
    name = data.get("label", "GPT Triggered Backup")

    headers = get_ha_headers()
    try:
        r = requests.post(
            "http://192.168.1.217:8123/api/services/backup/create",
            headers=headers,
            json={"name": name}
        )
        return jsonify({"status": "backup started", "HA_response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

from flask import send_from_directory

@app.route("/openapi.yaml")
def openapi_spec():
    return send_from_directory("/home/emailadmin", "openapi.yaml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)