# Frontend Resource Cleanup Plan
**Date**: 2025-01-08
**Issue**: Missing HACS card files causing 404 errors and CustomElementRegistry conflicts

## 🔍 Root Cause Analysis

### Missing Files (404 Errors)
```
❌ /local/community/simple-weather-card/simple-weather-card-bundle.js
❌ /local/community/mini-media-player/mini-media-player-bundle.js  
❌ /local/community/light-entity-card/light-entity-card.js
❌ /local/community/config-template-card/config-template-card.js
❌ /local/community/flex-horseshoe-card/flex-horseshoe-card.js
❌ /local/community/hass-swipe-navigation/swipe-navigation.js
```

### Duplicate References
- `custom-sidebar-yaml.js` appears twice (extra_module_url + resources)
- Multiple cards referencing missing file paths

## 🛠️ Surgical Fix Plan

### Step 1: Remove Missing Card References
Remove these lines from `configuration.yaml` resources:
```yaml
# REMOVE THESE - Files don't exist:
- url: /local/community/simple-weather-card/simple-weather-card-bundle.js
- url: /local/community/mini-media-player/mini-media-player-bundle.js
- url: /local/community/light-entity-card/light-entity-card.js
- url: /local/community/config-template-card/config-template-card.js
- url: /local/community/flex-horseshoe-card/flex-horseshoe-card.js
- url: /local/community/hass-swipe-navigation/swipe-navigation.js
```

### Step 2: Fix Duplicate custom-sidebar Reference
Remove duplicate from resources (keep only in extra_module_url):
```yaml
# REMOVE THIS DUPLICATE:
- url: /hacsfiles/custom-sidebar/custom-sidebar-yaml.js
```

### Step 3: Install Missing Cards via HACS
If you need these cards, install them properly:
1. Go to HACS → Frontend
2. Search for: simple-weather-card, mini-media-player, light-entity-card
3. Install and restart HA
4. Files will appear in correct `/hacsfiles/` paths

## ✅ Expected Results After Fix
- ❌ → ✅ No more 404 errors in browser console
- ❌ → ✅ No CustomElementRegistry conflicts  
- ❌ → ✅ Faster dashboard loading
- ❌ → ✅ Clean browser console output

## 📋 Implementation Status
- [ ] Remove missing file references from resources
- [ ] Remove duplicate custom-sidebar entry
- [ ] Restart Home Assistant
- [ ] Verify clean browser console
- [ ] Install missing cards via HACS if needed