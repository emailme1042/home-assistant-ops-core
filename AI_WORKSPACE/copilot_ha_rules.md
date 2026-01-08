# Home Assistant YAML Rules for Copilot

## Overview
This file contains the definitive rules for Home Assistant YAML configuration that GitHub Copilot must follow. These rules ensure compatibility with HA 2025+ and prevent format mixing that causes startup failures.

## Template Sensors (HA 2025+ Modern Format)
**Always use this exact format for template sensors:**

```yaml
template:
  - sensor:
      name: "Sensor Name"
      unique_id: sensor_unique_id
      state: >
        {% set value = states('sensor.source') %}
        {{ value | default('unknown') }}
      attributes:
        friendly_name: "Sensor Name"
        unit_of_measurement: "units"
```

**Never use these deprecated formats:**
- `platform: template` with `sensors:` block
- Mixed old and new formats in the same file
- `value_template` instead of `state`

## File Sensors
**Always use this format for file-based sensors:**

```yaml
sensor:
  - platform: file
    name: "File Sensor Name"
    file_path: "/config/path/to/file.txt"
    value_template: >
      {% set content = value %}
      {{ content | regex_findall('pattern') | first | default('unknown') }}
```

**Never convert file sensors to template sensors unless explicitly requested.**

## Binary Sensors (Template)
**Use this format for template binary sensors:**

```yaml
template:
  - binary_sensor:
      name: "Binary Sensor Name"
      unique_id: binary_sensor_unique_id
      state: >
        {{ states('sensor.source') | float > 10 }}
```

## Automations
**Standard automation format:**

```yaml
automation:
  - alias: "Automation Name"
    trigger:
      - platform: state
        entity_id: sensor.example
    condition: []
    action:
      - service: notify.mobile_app_device
        data:
          message: "Alert"
```

## Scripts
**Standard script format:**

```yaml
script:
  script_name:
    alias: "Script Name"
    sequence:
      - service: light.turn_on
        target:
          entity_id: light.example
```

## Includes System
- Use `!include_dir_merge_named` for directories with named files
- Use `!include_dir_merge_list` for directories with list items
- Do not mix formats in the same file
- If a file starts with `template:`, everything inside must follow the modern format

## General Rules
- **Never mix old and new formats in the same file** (causes YAML parsing errors)
- **Never remove indentation** (YAML is indentation-sensitive)
- **Never add stray characters** like '?' or malformed content
- **Never rewrite an entire file unless explicitly asked**
- **Always add unique_id to template sensors** (required in HA 2025+)
- **Use state instead of value_template** in modern template sensors
- **Preserve existing entity IDs and names** unless changing functionality
- **Test YAML validation after any changes**

## File Organization
- Template sensors go in `includes/templates/` (modern format)
- Legacy sensors stay in `includes/sensors/` (if still using old format)
- Automations in `includes/automations/`
- Scripts in `includes/scripts/`
- Use modular includes to avoid large configuration files

## HA 2025+ Specific Rules
- Template integration requires modern `template:` format
- Deprecated `platform: template` causes "Invalid config" errors
- All template sensors must have unique_id
- Use `state` instead of `value_template`
- Use `name` instead of `friendly_name` in modern format

## Copilot Behavior Rules
- Read this file before making any YAML changes
- Ask for confirmation before rewriting entire files
- Follow the exact formats shown above
- Never assume or guess formats
- When in doubt, preserve existing working format
- Use Copilot Chat for complex changes to see diffs first

## Emergency Rules
- If a file is working, do not change it unless there's a specific issue
- Always validate YAML after changes using HA's check config
- Never mix template sensor formats (old + new = broken)
- Comment out problematic sections instead of deleting them
- Keep backups of working configurations

## Examples

### Correct Template Sensor
```yaml
template:
  - sensor:
      name: "System Health"
      unique_id: system_health_status
      state: >
        {{ 'healthy' if states('binary_sensor.system_ok') == 'on' else 'unhealthy' }}
```

### Incorrect (Deprecated)
```yaml
sensor:
  - platform: template
    sensors:
      system_health:
        value_template: "{{ 'healthy' if states('binary_sensor.system_ok') == 'on' else 'unhealthy' }}"
```

### Correct File Sensor
```yaml
sensor:
  - platform: file
    name: "Log Errors"
    file_path: "/config/home-assistant.log"
    value_template: >
      {% set content = value %}
      {{ content.count('ERROR') if content else 0 }}
```

## Validation Checklist
- [ ] YAML syntax valid (no indentation errors)
- [ ] No mixed formats in same file
- [ ] All template sensors have unique_id
- [ ] File sensors use platform: file format
- [ ] HA config check passes
- [ ] No stray characters or malformed content
- [ ] Includes system properly structured

---

**Last Updated:** January 7, 2026  
**Purpose:** Prevent Copilot from breaking HA YAML by providing definitive formatting rules  
**Usage:** Copilot reads this file automatically when working in the repository