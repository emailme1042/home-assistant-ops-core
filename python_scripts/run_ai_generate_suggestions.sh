#!/bin/bash

echo "DEBUG: Wrapper script started."
echo "DEBUG: Arg1 (dashboard_target): $1"
echo "DEBUG: Arg2 (request_type): $2"

python3 /config/python_scripts/ai_generate_suggestions.py "$1" "$2"
