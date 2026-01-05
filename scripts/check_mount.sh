#!/bin/bash
MOUNTPOINT=""
REMOTE="//192.168.1.217/config"

if mountpoint -q "$MOUNTPOINT"; then
  echo "✅ Mount OK: $MOUNTPOINT"
else
  echo "⚠️ Not mounted. Attempting remount..."
  sudo mount -t cifs $REMOTE $MOUNTPOINT -o username=homeassistant,password=test1234,vers=3.0,uid=$(id -u),gid=$(id -g)
fi
