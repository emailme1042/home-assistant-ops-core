import json
import os

# 👉 Edit this to your Home Assistant config path
storage_path = 'S:/.storage'

# Load area registry
with open(os.path.join(storage_path, 'core.area_registry'), 'r') as f:
    area_data = json.load(f)['data']['areas']

# Load entity registry
with open(os.path.join(storage_path, 'core.entity_registry'), 'r') as f:
    entity_data = json.load(f)['data']['entities']

# Map area_id → area name
area_id_to_name = {a['id']: a['name'] for a in area_data}

# Map area name → list of entities
area_to_entities = {}

for entity in entity_data:
    area_id = entity.get('area_id')
    entity_id = entity.get('entity_id')

    if area_id and entity_id:
        area_name = area_id_to_name.get(area_id, 'Unknown')
        area_to_entities.setdefault(area_name, []).append(entity_id)

# Generate HomeKit YAML blocks
base_port = 21064
print("homekit:")

for i, (area_name, entities) in enumerate(sorted(area_to_entities.items()), start=0):
    port = base_port + i
    print(f"  - name: {area_name}")
    print(f"    port: {port}")
    print(f"    filter:")
    print(f"      include_entities:")
    for entity in sorted(entities):
        print(f"        - {entity}")
    print("")  # blank line between bridges
