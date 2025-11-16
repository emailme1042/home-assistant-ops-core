# Edge Copilot File Drop Strategy for HA Validation

## 🧠 How to Use Edge Copilot for YAML Validation

### 📁 **Files to Drop into Edge Copilot Tabs:**

1. **Dashboard Files** (Primary targets):
   ```
   dashboards/ai/main.yaml
   dashboards/system_overview/system_overview_main.yaml
   dashboards/users/users_main.yaml
   dashboards/users/room_template.yaml
   ```

2. **Automation Files** (Secondary targets):
   ```
   includes/automations/admin/automation_control.yaml
   includes/automations/monitoring/dashboard_ai_audit.yaml
   Any files showing errors in VSCode
   ```

3. **Configuration Context**:
   ```
   configuration.yaml (for reference)
   ```

### 🔍 **Prompts to Use with Edge Copilot:**

#### For Dashboard Validation:
> "Scan these YAML files for Home Assistant errors — especially missing `views:` blocks in dashboards, or dashboards without proper `cards:` sections. Look for any `custom:` card usage and flag YAML structure issues."

#### For Automation Validation:
> "Check these automation YAML files for missing `id:` or `alias:` fields, and identify any YAML structure problems that would prevent Home Assistant from loading them."

#### For General Analysis:
> "Analyze these Home Assistant YAML files for syntax errors, missing required fields, and compatibility issues. Focus on dashboard `views:` blocks and automation `id:`/`alias:` requirements."

### 💡 **What Edge Copilot Can Help With:**

- ✅ YAML syntax validation
- ✅ Missing required fields detection
- ✅ Home Assistant structure compliance
- ✅ Custom card usage analysis
- ✅ Explanation of validator scripts
- ✅ Suggested fixes for common issues

### 📋 **Expected Output:**
Edge Copilot should identify the same issues our validator finds:
- Missing `views:` blocks in dashboards
- Automation files missing `id:` or `alias:`
- Invalid YAML structure
- Custom card dependencies

### 🎯 **Best Practice:**
Drop 2-3 files at a time for focused analysis, rather than overwhelming with too many files at once.