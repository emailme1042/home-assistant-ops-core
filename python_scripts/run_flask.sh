#!/bin/bash
cd ~/jit_plugin_runner
source ~/jit_plugin_runner/jit_plugin_env/bin/activate
pkill -f jit_plugin.py
nohup python3 jit_plugin.py > /dev/null 2>&1 &
# Create WSL startup marker
touch /startup_marker

