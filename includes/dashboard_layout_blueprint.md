# 🗺️ Admin Dashboard Layout Blueprint

## 🌟 Overview

All admin dashboards live under `dashboards/aimagic`, defined via `ui-lovelace.yaml` or direct YAML mode.

---

## 🏠 Root Dashboard

- **Title**: Admin Root
- **Sections**:
  - Quick summary (Uptime, current issues)
  - Global controls (shutdown, restart, updates)
  - High-level cards: overall system health

---

## 📋 Entities Dashboard

- **Sections**:
  - Chips header (Devices, Unavailable, Diagnostics)
  - Markdown summary (audit results, suggestions)
  - Tabbed cards:
    - Devices
    - Unavailable entities
    - Diagnostics
  - Advanced filters using `auto-entities`

---

## 🛠️ Maintenance Dashboard

- **Sections**:
  - Recent logs
  - Update controls
  - Advanced cleanup or migration tools

---

## ⚙️ System Dashboard

- **Sections**:
  - System vitals (CPU, disk, network)
  - Core configurations overview
  - Automation status summary

---

## 🧩 Helpers Dashboard

- **Sections**:
  - Inputs grouped by type:
    - `input_boolean`
    - `input_number`
    - `input_text`
    - `input_select`
  - Control toggles or direct edit
  - Helper audit summary

---

## 🌐 Topology Dashboard

- **Sections**:
  - Visual map (zones, rooms)
  - Device tree
  - Area assignments
  - Missing/unknown devices

---

## 🔁 AutoPatch Preview Dashboard

- **Sections**:
  - AI-generated fixes preview
  - Backup diffs
  - Approval controls before merge

---

### 🧑‍🤝‍🧑 **User Dashboards**

- Auto-generated from above dashboards
- Only show relevant views (filtered entities, no admin controls)

---

## 💙 Core Principles

- Modular: each YAML view can be updated alone
- Hierarchical: Admin → User cascade
- Auditable: all changes backed up before merge
- Auto-entities and dynamic lists for future-proofing

## 🧑‍💻 Add-ons & Integrations Dashboard

- Version overview
- Update status
- Health state
- Quick update/disable

## 🚨 Device & Issue Dashboard

- Problematic devices
- Orphaned entities
- Auto-clean toggle

## 🖥️ Dashboard Control Center

- Live/disabled status
- User vs. admin access
- Feature toggles per dashboard
- Global or per-dashboard theme

## 🎛️ Helper & Entity Toggles

- Individual control over helpers
- Switch between auto/manual
- Override buttons

## 🎨 Visual Overrides Dashboard

- Global theme control
- Preview changes
- Per-dashboard style options
