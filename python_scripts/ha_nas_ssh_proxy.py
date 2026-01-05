from flask import Flask, request, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route('/run_nas_script', methods=['POST'])
def run_nas_script():
    data = request.json
    prompt = data.get('prompt', '')
    
    # Call your local script directly inside HA
    try:
        result = subprocess.run(
            ["python3", "/config/python_scripts/chatgpt_user_reply.py", prompt],
            capture_output=True, text=True, timeout=90
        )
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
