#!/bin/bash

# Calm venv setup script for HA shell_command usage
echo "🌱 Creating venv in /config/myvenv ..."

cd /config || { echo "❌ Failed to cd to /config"; exit 1; }

# Create venv if not exists
if [ ! -d "myvenv" ]; then
  python3 -m venv myvenv
  echo "✅ Virtual environment created."
else
  echo "ℹ️ venv already exists, using existing one."
fi

# Activate venv
source myvenv/bin/activate

# Install required packages
echo "📦 Installing packages: requests, openai, pyyaml ..."
pip install --upgrade pip
pip install requests openai pyyaml

# Deactivate
deactivate

echo "✅ All done! venv setup complete at /config/myvenv"
