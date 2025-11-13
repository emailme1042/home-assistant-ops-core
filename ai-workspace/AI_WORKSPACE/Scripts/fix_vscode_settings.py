# VSCode Settings Fix Generator
# Purpose: Generate corrected VSCode settings.json with proper HA token placeholder
# Usage: Run after generating HA Long-Lived Access Token

import json
import os
from datetime import datetime

def backup_current_settings():
    """Backup current VSCode settings"""
    settings_path = "S:/.vscode/settings.json"
    backup_path = f"S:/AI_WORKSPACE/ARCHIVED_SESSION_FILES/vscode_settings_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as f:
                content = f.read()
            with open(backup_path, 'w') as f:
                f.write(content)
            print(f"✅ Backup created: {backup_path}")
            return True
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

def generate_fixed_settings(new_ha_token=None):
    """Generate corrected VSCode settings"""
    
    # Template with correct configuration
    fixed_settings = {
        "terminal.integrated.cwd": "${workspaceFolder}",
        "files.defaultLanguage": "yaml",
        "files.autoSave": "afterDelay",
        "files.autoSaveDelay": 5000,
        "editor.formatOnSave": True,
        "editor.formatOnSaveMode": "modifications",
        "workbench.editor.enablePreview": False,
        "files.exclude": {
            "**/.DS_Store": True,
            "**/node_modules": True,
            "**/__pycache__": True
        },
        "files.associations": {
            "*.yaml": "home-assistant",
            "configuration.yaml": "home-assistant",
            "**/includes/**/*.yaml": "home-assistant",
            "**/dashboards/**/*.yaml": "home-assistant",
            "*.md": "markdown"
        },
        "yaml.validate": True,
        "yaml.schemas": {
            "https://json.schemastore.org/home-assistant": "*/includes/**/*.yaml",
            "https://json.schemastore.org/github-workflow": ".github/workflows/*.yaml"
        },
        "yaml.customTags": [
            "!include scalar",
            "!secret scalar",
            "!input scalar",
            "!lambda scalar",
            "!include_dir_merge_list sequence",
            "!include_dir_merge_named mapping",
            "!env_var scalar"
        ],
        "[yaml]": {
            "editor.defaultFormatter": "keesschollaart.vscode-home-assistant",
            "editor.suggest.showWords": False
        },
        "[markdown]": {
            "editor.wordWrap": "on",
            "editor.quickSuggestions": {
                "comments": "on",
                "strings": "on",
                "other": "on"
            }
        },
        "path-intellisense.autoSlashAfterDirectory": True,
        "github.copilot.enable": {
            "*": True
        },
        "github.copilot.inlineSuggest.enable": True,
        "vscode-home-assistant.hostUrl": "https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa",
        "vscode-home-assistant.longLivedAccessToken": new_ha_token or "YOUR_HOME_ASSISTANT_LONG_LIVED_ACCESS_TOKEN_HERE",
        "vscode-home-assistant.languageserver.enable": True,
        "vscode-home-assistant.languageserver.completions.enable": True,
        "vscode-home-assistant.languageserver.definitions.enable": True,
        "vscode-home-assistant.languageserver.hover.enable": True,
        "editor.inlineSuggest.enabled": True,
        "editor.suggest.preview": True,
        "editor.quickSuggestions": {
            "other": True,
            "comments": True,
            "strings": True
        },
        "security.workspace.trust.enabled": False,
        "security.workspace.trust.startupPrompt": "never",
        "security.workspace.trust.untrustedFiles": "open"
    }
    
    return fixed_settings

def write_fixed_settings(settings_dict):
    """Write corrected settings to file"""
    settings_path = "S:/.vscode/settings.json"
    
    try:
        with open(settings_path, 'w') as f:
            json.dump(settings_dict, f, indent=2)
        print(f"✅ Fixed settings written to: {settings_path}")
        return True
    except Exception as e:
        print(f"❌ Failed to write settings: {e}")
        return False

def main():
    print("🔧 VSCode Settings Fix Generator")
    print("="*50)
    
    print("\n📋 Current Issue:")
    print("❌ OpenAI API key used instead of HA Long-Lived Access Token")
    print("❌ This causes 404 errors and extension failures")
    
    # Backup current settings
    print("\n💾 Creating backup...")
    backup_success = backup_current_settings()
    
    if not backup_success:
        print("⚠️ Backup failed, but continuing...")
    
    # Generate fixed settings
    print("\n🔧 Generating fixed settings...")
    fixed_settings = generate_fixed_settings()
    
    # Write fixed settings
    print("📝 Writing corrected settings...")
    write_success = write_fixed_settings(fixed_settings)
    
    if write_success:
        print("\n✅ VSCode settings fixed!")
        print("\n📝 Next Steps:")
        print("1. Generate HA Long-Lived Access Token:")
        print("   - Go to Home Assistant → Profile → Long-Lived Access Tokens")
        print("   - Create token named 'VSCode HA Extension'")
        print("   - Copy the generated token")
        print("\n2. Update settings.json:")
        print("   - Replace 'YOUR_HOME_ASSISTANT_LONG_LIVED_ACCESS_TOKEN_HERE'")
        print("   - Paste your actual HA token")
        print("\n3. Reload VSCode:")
        print("   - Ctrl+Shift+P → 'Developer: Reload Window'")
        print("\n4. Test:")
        print("   - Type 'sensor.' in any YAML file")
        print("   - Should see entity suggestions")
    else:
        print("\n❌ Failed to fix settings")
        print("Manual fix required - see dashboard for instructions")

if __name__ == "__main__":
    main()