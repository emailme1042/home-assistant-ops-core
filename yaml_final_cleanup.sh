#!/bin/bash
# yaml_final_cleanup.sh
# Safe targeted cleanup for Home Assistant YAML files

BACKUP_DIR="/HA_BACKUPS/yaml_final_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "📦 Backing up YAML files to: $BACKUP_DIR"
find /dashboards /includes -type f -name "*.yaml" -exec cp --parents {} "$BACKUP_DIR" \;

echo "🔹 Removing '---' from file starts..."
find /dashboards /includes -type f -name "*.yaml" -exec sed -i '1{/^---$/d}' {} \;

echo "🔹 Fixing specific indentations..."
# These are exact fixes from lint results
sed -i '98s/^  \{4\}/  /' /includes/input_booleans/all_input_booleans_combined.yaml
sed -i '2s/^  //' /includes/templates/jit_plugin_sensor.yaml
sed -i '2s/^  //' /includes/input_selects/input_select.mood.yaml
sed -i '215s/^  \{4\}/      /' /dashboards/users/home.yaml

echo "🔹 Replacing YAML truthy/falsey values..."
find /dashboards /includes -type f -name "*.yaml" -exec \
  sed -i -E 's/\b([Yy]es|[Oo]n)\b/true/g; s/\b([Nn]o|[Oo]ff)\b/false/g' {} \;

echo "✅ Cleanup complete. Backup stored at: $BACKUP_DIR"
echo "💡 Run: yamllint -f parsable /dashboards /includes"
