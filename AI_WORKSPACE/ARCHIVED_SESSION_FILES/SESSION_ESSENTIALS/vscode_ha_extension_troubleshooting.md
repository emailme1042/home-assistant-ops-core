# VS Code Home Assistant Extension Troubleshooting Guide

**Source**: CP Wiki Research - 2025-10-27  
**Context**: Extension should provide entity dropdown suggestions but often fails

## ✅ What the Extension *Should* Do

When correctly connected to your Home Assistant instance, the extension enables:

- **Entity ID autocompletion**: dropdown suggestions for `entity_id`, `service`, `device_class`, etc.
- **Scene and trigger suggestions**: based on your actual HA config
- **Scoped validation**: even across `!include` files

## 🧠 Why You Might Not See Dropdown Suggestions

### 1. 🔌 No Live Connection to HA
The extension needs to connect to your running Home Assistant instance. If this isn't configured, it can't fetch live entity data.

**Fix**:
- Open VS Code
- Go to **Settings → Extensions → Home Assistant**
- Set your HA URL (e.g., `http://192.168.1.217:8123`)
- Add your **Long-Lived Access Token** from HA (Settings → Profile → Create Token)

### 2. 🧱 YAML File Isn't Recognized
Autocompletion only works in files that match expected schema types:
- `configuration.yaml`
- `automations.yaml`
- `scripts.yaml`
- `ui-lovelace.yaml`

### 3. 🧪 Language Server Not Activated
The extension uses a YAML language server. If it fails to activate, you won't get suggestions.

**Fix**:
- Check VS Code logs (View → Output → Home Assistant)
- Restart VS Code
- Confirm extension version is up to date

### 4. 🧯 Telemetry Disabled
If telemetry is disabled, the extension may not fetch schema updates or entity lists.

## 🧱 What You Can Still Use Without Autocomplete

Even if dropdowns aren't working, you can still:
- Use **snippets** (`Cmd+Shift+P → Home Assistant: Insert Automation Snippet`)
- Validate YAML manually
- Use `Go to Definition` on `!include` paths
- Render templates via HA API

## ✅ Recommended Resources for Home Assistant Schema Standards

### 1. 🧾 [YAML Syntax Guide (Official)](https://www.home-assistant.io/docs/configuration/yaml/)
- Covers **basic YAML rules** used in Home Assistant
- Explains indentation, lists, booleans, and formatting

### 2. 🧠 [YAML Style Guide for Developers](https://developers.home-assistant.io/docs/documenting/yaml-style-guide/)
- Focuses on **best practices** for writing YAML in HA
- **2-space indentation**
- Lowercase `true`/`false` booleans
- Consistent formatting across docs and configs

### 3. 🧱 [Developer Docs: Standards](https://developers.home-assistant.io/docs/documenting/standards/)
- Covers documentation formatting, integration examples, and config variables

## 🧪 Schema Validation Tools

- **VS Code Extension**: Validates YAML blocks and autocompletes entity/service names
- **HA Core Validator**: Built-in checks during HA startup
- **Community Python Scripts**: Validate modular includes and automation syntax

## 🧱 Jamie-Specific Tips

- Use `!include_dir_merge_list` for automations and scripts
- Anchor every automation with unique `id:` and `alias:` for UI parity
- Validate templates using Developer Tools → Template or VS Code's `/template` API

---
**Last Updated**: 2025-10-27  
**Status**: Extension connected but WebSocket auth still failing - entity dropdown not working