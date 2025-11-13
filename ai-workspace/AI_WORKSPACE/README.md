AI_WORKSPACE — quick developer README
==================================

This folder contains helper scripts and tools for validating and previewing Home Assistant configuration during AI-assisted edits.

Quick notes
- The scripts accept an optional root directory as their first argument. If omitted they use the current working directory.
- Examples in this README assume you run commands from the repository root.

Install dependencies (one-time):

```powershell
python -m pip install -r AI_WORKSPACE\requirements.txt
```

Validator commands
- Strict PyYAML validator (recommended):

```powershell
python .\AI_WORKSPACE\pyyaml_validator.py .
```

- Quick validator (uses safe_load, prints root):

```powershell
python .\AI_WORKSPACE\tmp_ha_yaml_check.py .
```

Examples for Home Assistant shell_command usage
- In HA shell_command entries we now pass explicit roots so the validator runs against the intended folder:

```yaml
shell_command:
  validate_yaml: >
    python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml 2>> /config/fix_errors.log && echo "$(date) - YAML validation complete." >> /config/fix_sheet.yaml

  validate_includes_yaml: >
    python3 /config/python_scripts/validate_includes_yaml.py /config/includes
```

VS Code behavior
- There's a workspace setting in `.vscode/settings.json` that sets the integrated terminal CWD to the workspace root (`${workspaceFolder}`). That means running `python .\AI_WORKSPACE\pyyaml_validator.py .` from the integrated terminal checks the repo root and avoids needing `s:\` drive prefixes.

If you want me to add small wrappers or tasks (e.g., `.vscode/tasks.json`) to run these validators with one click, say the word and I'll add them.
## 🔍 Purpose & AI Sync Rules

This folder anchors all AI sessions (Copilot, GPT, OpenAI) and exposes the full context stack required for accurate reasoning, diagnostics, and dashboard sync. All markdowns and YAMLs surfaced here are **informational only** unless explicitly marked for action.

### 🧠 AI Agent Protocol
- AI must **always reference files in `ai_workspace/`** before acting.
- If any file appears **stale, missing, or contradictory**, the agent must **notify Jamie immediately**.
- No assumptions or silent edits allowed—**explicit confirmation is required** before any change.
- All updates must be logged in `ai_exec_log.md` and surfaced in `copilot_session_notes.md`.

### 🚫 Path Reference Rules
- **Never reference `S:/`, `mnt/s`, or `/config`** directly.
- These paths introduce ambiguity and legacy bleed.
- Instead, use mapped drive logic from `mount_map.yaml`:
  - `ai_workspace/` and `SYSTEM_OVERVIEW/` are **parallel roots**.
  - Both support identical scripts, commands, and sync logic.
  - This ensures mirrored execution and low cognitive load.

### 🔄 Sync Logic
- `SYSTEM_OVERVIEW/` holds finalized structure and dashboard logic.
- `ai_workspace/` stages context, scripts, and session logs.
- All files are versioned—**never deleted**, only replaced or archived.
- Git sync is one-way unless manually triggered (see `mount_map.yaml`).

## ⚠️ No Git Sync (Default Policy)

This AI workspace is configured by default to avoid being synced to a remote Git repository.

- Rationale: preventing accidental disclosure of runtime files, backups, or environment-specific secrets.
- If you *do* choose to migrate any part of this workspace into Git later, follow the safety checklist:
  - Ensure `secrets.yaml`, `.storage/`, `snapshots/`, and `backups/` are excluded in `.gitignore`.
  - Prefer exporting only sanitized, non-sensitive YAML and markdown files (for example, `AI_WORKSPACE/SHARED_CONTEXT/` items).
  - Document the exact files included in the repo and obtain explicit approval before pushing to a remote.

This file documents the default, conservative policy used during AI-assisted editing: keep local, avoid automatic Git sync.

