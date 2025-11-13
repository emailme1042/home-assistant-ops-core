# Quickstart for AI coding agents (project-specific)

- Workspace type: Home Assistant YAML config with an AI staging area at `AI_WORKSPACE/` (mapped to `AI_Zone/`).
- Always prefer `AI_Zone/` paths (see `AI_WORKSPACE/mount_map.yaml`) instead of `S:/` or `/config`.
- Do not edit `secrets.yaml` or files under `.storage/`.

Core rules (short):
- Log every edit to `AI_WORKSPACE/ai_exec_log.md` and append a session summary to `AI_WORKSPACE/copilot_session_notes.md` using `AI_WORKSPACE/copilot_session_template.md`.
- Files in `AI_WORKSPACE/` are informational unless explicitly marked for action — archive, don't delete.
- Do not push production dashboard or one-way git sync changes without Jamie's approval.

Where to look first (high value files):
- `configuration.yaml` — shell_command entries (e.g. `run_ai_generate_suggestions`, `validate_yaml`, `check_flask_status`) and allowlisted OpenAI URLs.
- `includes/rest_commands/rest.yaml` — concrete REST endpoints (OpenAI, local JIT services at 192.168.1.203:5001, 127.0.0.1:5001/5005) and example payloads.
- `AI_WORKSPACE/README.md`, `AI_WORKSPACE/mount_map.yaml` — mapping and AI agent protocol (must follow path rules and notify on contradictions).
- `AI_WORKSPACE/copilot_session_template.md` — required session logging format.
- `dashboards/AI/ai-workspace.yaml` and `dashboards/SYSTEM_OVERVIEW/` — where changes are surfaced in Home Assistant.

Integration patterns and examples:
- Local services: several REST calls target local helper services (e.g. `http://192.168.1.203:5001` and `http://127.0.0.1:5001`) — prefer reading `includes/rest_commands/rest.yaml` for exact endpoints and auth headers.
- Shell commands: `shell_command.run_gpt_via_flask` posts to `http://localhost:5006/run_command` and `shell_command.check_flask_status` checks that endpoint. Use `curl` in PowerShell to validate.
- Validation workflows: run `shell_command.validate_yaml` and `shell_command.validate_includes_yaml` before proposing config changes; they generate `fix_sheet.yaml` and validation logs.

Safe autonomous actions (allowed):
- Run non-destructive validators and health checks listed above.
- Append logs and diagnostic files under `AI_WORKSPACE/` (follow logging templates).

Prohibited or require-approval actions:
- Never change secrets or `.storage/` entries.
- Do not delete or permanently modify `AI_WORKSPACE/`, `SYSTEM_OVERVIEW/`, or `dashboards/` without approval.
- Do not perform one-way git syncs or push production dashboard edits without Jamie's consent.

Quick copyable PowerShell checks (examples):

```powershell
# check Flask health
curl -s -o $null -w "%{http_code}" http://localhost:5006/run_gpt

# run AI preview (non-destructive)
python3 /config/python_scripts/ai_generate_suggestions.py

# run YAML validator and write fix sheet (explicit root)
python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml 2>> /config/fix_errors.log; echo "$(Get-Date) - YAML validation complete." >> /config/fix_sheet.yaml
```

When uncertain: append a short summary to `AI_WORKSPACE/copilot_session_notes.md` and request guidance from Jamie. If a file appears stale, report it rather than editing.

References: `configuration.yaml`, `includes/rest_commands/rest.yaml`, `AI_WORKSPACE/README.md`, `AI_WORKSPACE/mount_map.yaml`, `AI_WORKSPACE/copilot_session_template.md`
