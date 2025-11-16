#!/bin/bash

cd ~/jit_plugin_runner || exit 1
source jit_plugin_env/bin/activate || exit 1

# Kill any previous Flask if needed
pkill -f jit_plugin.py

# Launch Flask safely and log output
nohup python3 jit_plugin.py > /flask_output.log 2>&1 &
echo "✅ Flask launched in background. Logs: /flask_output.log"
touch /startup_marker
