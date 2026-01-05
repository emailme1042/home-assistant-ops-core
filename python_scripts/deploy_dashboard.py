import shutil
import os

source_file = "/config/includes/dashboard_suggestions/approved.yaml"
target_file = "/config/dashboards/ops_dashboard.yaml"

if os.path.exists(source_file):
    shutil.copyfile(source_file, target_file)
    print("✅ Dashboard YAML deployed to:", target_file)
else:
    print("⚠️ No approved YAML draft found.")
