import json

# === Paths ===
entity_registry_file = '/config/.storage/core.entity_registry'
area_registry_file = '/config/.storage/core.area_registry'
output_file = '/config/generated_groups.yaml'

# === Load files ===
with open(entity_registry_file, 'r') as f:
    entity_data = json.load(f)

with open(area_registry_file, 'r') as f:
    area_data = json.load(f)

# === Build area ID -> name map ===
area_map = {area['id']: area['name'] for area in area_data['data']['areas']}

# === Build entity list per area ===
area_entities = {}
for entity in entity_data['data']['entities']:
    area_id = entity.get('area_id')
    entity_id = entity['entity_id']
    if area_id:
        area_name = area_map.get(area_id, 'Unknown')
        area_entities.setdefault(area_name, []).append(entity_id)

# === Write output YAML ===
with open(output_file, 'w') as f:
    f.write("group:\n")
    for area, entities in area_entities.items():
        group_name = area.lower().replace(" ", "_").replace("-", "_") + "_entities"
        f.write(f"  {group_name}:\n")
        f.write(f"    name: {area} Entities\n")
        f.write("    entities:\n")
        for eid in sorted(entities):
            f.write(f"      - {eid}\n")
        f.write("\n")

print(f"✅ Generated group YAML file at: {output_file}")
