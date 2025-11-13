# ⚠️ Icon Injection Protocol — Home Assistant Workspace

- `pyyaml_validator.py` does NOT add or remove `icon:`/`icon_template:` keys.
- Any icon suggestions in `script:` or `template:` YAML blocks must be removed manually.
- Icons are only safe in `template:` sensors, dashboards, or non-critical blocks.
- No icon drift detected in restart-critical scripts or automations.
- Patch protocol: Do not add icons unless explicitly requested.

_Last sweep: 2025-11-05 — Workspace is restart-safe and clean._

---

## 🧩 Optional Additions
- Add a validator sensor to surface icon drift in real time
- Use this grep command for future sweeps:
  ```bash
  grep -r "icon:" includes/
  ```
- Link this protocol in your `README.md` or `CONTRIBUTING.md`

---

**This protocol documents the boundaries of the validator, the risk of icon injection, and the results of the latest sweep. Future collaborators should reference this file before making YAML changes.**
