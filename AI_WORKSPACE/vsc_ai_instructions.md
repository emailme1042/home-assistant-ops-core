# 🧠 HAOS/HACS AI Instruction Standards (2025.x)

## ✅ YAML Validation Rules

- Use dictionary format for integrations (e.g. `mqtt:` must not be a list)
- Validate all YAML with `validate_yaml.py` before restart
- Flag deprecated keys: `broker`, `discovery`, `discovery_prefix`
- Enforce 2-space indentation, no tabs

## ✅ MQTT Integration Schema

```yaml
mqtt:
  host: core-mosquitto
  port: 1883
  username: homeassistant
  password: Donkey123
```

## ✅ HACS Component Standards

- No YAML config allowed — setup must be UI-only
- Require `manifest.json` with `domain`, `name`, `version`, `codeowners`
- Optional `hacs.json` for metadata
- One integration per repo under `/custom_components/`

## ✅ Recorder/Logbook Optimization

```yaml
recorder:
  exclude:
    domains: [automation, script, mqtt]
    entities: [sensor.cpu_temp, sensor.mqtt_last_message_age_*]

logbook:
  exclude:
    domains: [automation, script, mqtt]

history:
  exclude:
    domains: [automation, script, mqtt]
```

## ✅ Restart Safety

- Run `ha core check` before restart
- Log all config errors to `active_issues.md`
