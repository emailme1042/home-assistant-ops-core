import yaml
from datetime import datetime

# Define sensors and shell commands
sensors = [

    "sensor.ha_version",
    "sensor.yaml_validation_result",
    "sensor.fix_sheet_last_updated",
    "sensor.mount_point_health"
]

shell_command = "shell_command.validate_yaml"

# Build dashboard structure
dashboard = {
    "title": "System Ops",
    "views": [{
        "title": "Status",
        "path": "status",
        "icon": "mdi:heart-pulse",
        "cards": [
            {
                "type": "markdown",
                "content": "\n".join([
                    "## System Status",
                    f"- Last Sync: `{{{{ states('{sensors[1]}') }}}}`",
                    f"- HA Version: `{{{{ states('{sensors[2]}') }}}}`"
                ])
            },
            {
                "type": "entities",
                "title": "Health Checks",
                "entities": sensors
            },
            {
                "type": "markdown",
                "content": "\n".join([
                    "## YAML Validation Status",
                    f"- Result: `{{{{ states('{sensors[3]}') }}}}`",
                    f"- Last Checked: `{{{{ states('{sensors[4]}') }}}}`"
                ])
            },
            {
                "type": "vertical-stack",
                "cards": [
                    {
                        "type": "button",
                        "name": "Run YAML Validation",
                        "icon": "mdi:file-check",
                        "tap_action": {
                            "action": "call-service",
                            "service": shell_command
                        }
                    },
                    {
                        "type": "entities",
                        "title": "Validation Output",
                        "entities": [sensors[3], sensors[4]]
                    }
                ]
            }
        ]
    }]
}

# Save to file
with open("system_ops.yaml", "w") as f:
    yaml.dump(dashboard, f, sort_keys=False)
print("✅ Dashboard YAML generated: system_ops.yaml")

