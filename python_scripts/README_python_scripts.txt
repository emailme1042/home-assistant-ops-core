🗂️ python_scripts — Remaining Scripts Summary
parse_gpt_reply.py
Purpose: Parses responses coming from ChatGPT or other LLM replies.

How it works:

Strips or formats reply text. (JD TEST)

Can extract segments, tidy formatting, or remove special tags if present.

Risk: ✅ Very safe, no file writes or external calls.

reload_assist.py
Purpose: Triggers reload or assist functions in Home Assistant.

How it works:

Usually calls Home Assistant services (e.g., automation.reload, script.reload, etc.).

Could be used for debugging or refreshing configurations dynamically.

Risk: ✅ Safe, but affects runtime state if automations are reloaded.

sort_db_spares.py
Purpose: Sorts or organizes spare database files (e.g., backup .db files).

How it works:

Typically moves or renames DB backups to keep the structure clean.

Might sort by date or file size.

Risk: ✅ Safe, minor risk only if run blindly (no destructive writes expected).

verify_dashboard_mounts.py
Purpose: Verifies dashboard YAML "mount points" and included files.

How it works:

Reads dashboard directories and includes.

Checks references and consistency, prints or logs results.

Risk: ✅ Safe, read-only.