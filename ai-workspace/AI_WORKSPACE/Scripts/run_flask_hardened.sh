#!/bin/bash
cd ~/jit_plugin_runner
source jit_plugin_env/bin/activate
pkill -f jit_plugin.py
nohup python3 jit_plugin.py > flask_output.log 2>&1 &
echo "✅ Flask server running on all interfaces (0.0.0.0:5001)"
