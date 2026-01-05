#!/bin/bash

REST_DIR="/includes/rest_commands"
OLD_IP="127.0.0.1"
NEW_IP="192.168.1.203"

echo "🔄 Rewriting REST command URLs in $REST_DIR..."

if [ ! -d "$REST_DIR" ]; then
  echo "❌ ERROR: Directory does not exist: $REST_DIR"
  exit 1
fi

find "$REST_DIR" -type f -name "*.yaml" -print0 | while IFS= read -r -d '' file; do
  if grep -q "$OLD_IP" "$file"; then
    echo "🛠  Patching: $file"
    sed -i "s|http://$OLD_IP|http://$NEW_IP|g" "$file"
  fi
done

echo "✅ All 127.0.0.1 references updated to $NEW_IP"
