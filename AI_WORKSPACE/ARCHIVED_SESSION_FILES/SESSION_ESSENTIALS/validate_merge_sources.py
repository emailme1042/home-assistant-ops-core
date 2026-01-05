"""
🧠 AI Workspace Pre-Merge Validation Script (Cross-Platform)
Validates all source files listed in merge_map.yaml before consolidation.
"""

import yaml
from pathlib import Path

# Define paths
base_path = Path(r"S:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS")
merge_map = base_path / "merge_map.yaml"

# Load merge map
if not merge_map.exists():
    print(f"❌ merge_map.yaml not found at {merge_map}")
    exit(1)

with open(merge_map, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

missing_files = []

# Parse includes from all merge targets
for target, details in data.get("merge_targets", {}).items():
    includes = details.get("includes", [])
    print(f"\n🔍 Checking files for target: {target}")
    for inc in includes:
        file_path = base_path / inc
        if file_path.exists():
            print(f"✅ Found: {inc}")
        else:
            print(f"⚠️ Missing: {inc}")
            missing_files.append(inc)

# Summary
if missing_files:
    print("\n❌ Validation failed. Missing files detected:")
    for file in missing_files:
        print(f" - {file}")
    exit(1)
else:
    print("\n✅ All required files found. Safe to proceed with Copilot merge.")
