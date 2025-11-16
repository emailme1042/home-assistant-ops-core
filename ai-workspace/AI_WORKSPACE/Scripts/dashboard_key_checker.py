import yaml

with open('s:/configuration.yaml', 'r') as f:
    config = yaml.safe_load(f)

dashboards = config['lovelace']['dashboards']
print("Dashboard keys analysis:")
print("-" * 40)

no_hyphen = []
has_hyphen = []

for key in dashboards.keys():
    if '-' in key:
        has_hyphen.append(key)
    else:
        no_hyphen.append(key)

print(f"✅ Keys WITH hyphens ({len(has_hyphen)}):")
for key in has_hyphen:
    print(f"   {key}")

print(f"\n❌ Keys WITHOUT hyphens ({len(no_hyphen)}):")
for key in no_hyphen:
    print(f"   {key}")

print(f"\nTotal dashboard keys: {len(dashboards)}")