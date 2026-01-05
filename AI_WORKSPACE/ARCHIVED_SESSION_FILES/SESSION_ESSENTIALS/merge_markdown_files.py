"""
🧠 AI Workspace Markdown Merge Script
Reads merge_map.yaml and consolidates listed markdown files into target outputs.
Tags each source file as archived after merging.
"""

import yaml
from pathlib import Path
from datetime import datetime

# Paths
base_path = Path(r"S:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS")
merge_map = base_path / "merge_map.yaml"
archive_tag = f"\n⚙️ Archived on {datetime.now().strftime('%Y-%m-%d')} — content merged into [Target_File_Name]\n#archived_{datetime.now().strftime('%Y%m%d')}\n"

# Load merge map
with open(merge_map, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

for target, details in data.get("merge_targets", {}).items():
    output_file = base_path / target
    includes = details.get("includes", [])
    merged_content = []
    archived_sources = []
    for inc in includes:
        src_path = base_path / inc
        if src_path.exists():
            # Add section header and content
            merged_content.append(f"\n_Merged from: {inc}_\n")
            with open(src_path, "r", encoding="utf-8") as src:
                merged_content.append(src.read())
            # Tag source file as archived
            with open(src_path, "a", encoding="utf-8") as src:
                src.write(archive_tag.replace('[Target_File_Name]', target))
            archived_sources.append(inc)
        else:
            merged_content.append(f"\n_Missing source: {inc}_\n")
    # Append archived sources list
    merged_content.append("\n---\n**Archived Sources:**\n" + "\n".join(archived_sources))
    # Write merged output
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(merged_content))
    print(f"✅ Merged {len(archived_sources)} files into {target}")

print("\n✅ All merges complete. Check SESSION_ESSENTIALS for output files.")
