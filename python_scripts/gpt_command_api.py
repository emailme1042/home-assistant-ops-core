from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Replace this with your real token
API_TOKEN = os.getenv("GPT_API_TOKEN", "your_strong_token_here")

# Define allowed commands (prefix match or full command)
ALLOWED_COMMANDS = [
    "echo ",
    "ls ",
    "git ",
    "cp ",
    "cat ",
    "python3 ",
]

@app.route("/run_command", methods=["POST"])
def run_command():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing Bearer token"}), 401

    token = auth_header.split("Bearer ")[-1]
    if token != API_TOKEN:
        return jsonify({"error": "Invalid token"}), 403

    data = request.get_json()
    command = data.get("command")

    if not command or not any(command.startswith(prefix) for prefix in ALLOWED_COMMANDS):
        return jsonify({"error": "Command not allowed or missing"}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
