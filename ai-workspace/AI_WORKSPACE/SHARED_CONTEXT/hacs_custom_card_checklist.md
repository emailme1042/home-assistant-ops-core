# 📝 HACS Custom Card Installation Checklist

This checklist is generated from your current and previous configuration files. Use it to verify all required HACS custom cards are installed for your dashboards and automations.

## How to Use

- Open HACS in Home Assistant
- Go to "Frontend" and search for each card below
- Click "Install" for any missing cards
- Confirm the `.js` files appear in `www/community/` or your custom path (e.g., `www/smarticards/`)

---

## Required HACS Custom Cards

### Core Cards (from configuration and resources)

- button-card
- lovelace-mushroom
- mini-graph-card
- vertical-stack-in-card
- lovelace-card-mod
- lovelace-auto-entities
- state-switch
- template-entity-row
- config-template-card
- lovelace-layout-card

### Commonly Used Additions

- bar-card
- custom-attributes
- mini-media-player
- simple-weather-card
- decluttering-card
- scheduler-card
- hass-swipe-navigation

### Media & Entertainment

- HA-Firemote
- spotify-card
- maxi-media-player

### Dashboard Enhancements

- Bubble-Card
- clock-weather-card
- light-entity-card
- tabbed-card

### Specialized Cards (Add as needed)

- frigate-hass-card
- atomic-calendar-revive
- formulaone-card

### Utility Cards

- unused-card
- uptime-card
- Summary-Card

---

## Expected File Paths

- `/config/www/community/[card-name]/[card-file].js`
- Or your custom path: `/config/www/smarticards/[card-file].js`

---

## Installation Notes

- All cards must be installed via the HACS UI (not YAML or script)
- If a card is missing, dashboards using it will show errors like "Unknown type encountered"
- After installation, restart Home Assistant if prompted

---

### Tip

Check this list after any dashboard update or HACS reinstall to ensure all cards are present.

---

_Last updated: 2025-11-08 by GitHub Copilot_
