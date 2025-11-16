import os
import yaml

summary = {}

folders = [
    '/config/includes/input_booleans',
    '/config/includes/input_texts',
    '/config/includes/input_numbers',
    '/config/includes/input_datetimes',
    '/config/includes/input_selects',
    '/config/includes/scripts',
    '/config/includes/sensors',
    '/config/includes/scenes',
    '/config/includes/templates',
    '/config/dashboards/aimagic'
]

files_to_scan = [
    '/config/configuration.yaml',
    '/config/automations.yaml'
]


# Process folders
for folder in folders:
    if not os.path.exists(folder):
        continue

    folder_summary = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        if content:
                            folder_summary.append({
                                'file': os.path.relpath(file_path, folder),
                                'entities': list(content.keys()) if isinstance(content, dict) else ['unknown_structure']
                            })
                except Exception as e:
                    folder_summary.append({
                        'file': os.path.relpath(file_path, folder),
                        'error': str(e)
                    })

    summary[os.path.basename(folder)] = folder_summary

# Process individual files
for file_path in files_to_scan:
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                summary[os.path.basename(file_path)] = {
                    'entities': list(content.keys()) if isinstance(content, dict) else ['unknown_structure']
                }
        except Exception as e:
            summary[os.path.basename(file_path)] = {
                'error': str(e)
            }

# Write markdown summary
output_file = '/config/www/ha_summary.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 🟢 Home Assistant Configuration Summary\n\n")
    for section, items in summary.items():
        f.write(f"## {section}\n\n")
        if isinstance(items, list):
            for file_info in items:
                file = file_info.get('file')
                entities = file_info.get('entities', [])
                error = file_info.get('error', None)
                if error:
                    f.write(f"- **{file}**: ⚠️ Error: {error}\n")
                else:
                    f.write(f"- **{file}**: {', '.join(entities)}\n")
        elif isinstance(items, dict):
            error = items.get('error')
            entities = items.get('entities', [])
            if error:
                f.write(f"- ⚠️ Error: {error}\n")
            else:
                f.write(f"- Entities: {', '.join(entities)}\n")
        f.write("\n")
print("⚙️ Script finished writing file at", output_file)
print("✅ HA summary file generated at /config/www/ha_summary.md")
print("✅ HA summary file generated at", output_file)

import requests

ha_url = "http://homeassistant.local:8123/api/services/input_text/set_value"
token = "YOUR_LONG_LIVED_TOKEN"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

data = {
    "entity_id": "input_text.last_chatgpt_prompt",
    "value": "Scan completed. Summary is available at /local/ha_summary.md."
}

requests.post(ha_url, headers=headers, json=data)
print("✅ input_text.last_chatgpt_prompt updated via API.")
