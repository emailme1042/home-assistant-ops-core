# 🧠 Frontend Resource Fix Plan - November 3, 2025

## 🎯 Issue Analysis from Console Errors

### 🔹 1. CustomElementRegistry Conflicts
**Problem**: Cards like `mini-graph-card`, `button-card`, `auto-entities` being registered multiple times
**Root Cause**: Likely duplicate resource declarations or cards being loaded by multiple views
**Impact**: Failed card loading, frontend instability

### 🔹 2. Missing Module Files  
**Problem**: 404 errors for scoped-custom-element-registry.ts and other modules
**Root Cause**: Broken HACS installations or outdated card references
**Impact**: Console errors, potential card failures

### 🔹 3. Broken Card Dependencies
**Problem**: simple-weather-card.js and mini-media-player.js throwing TypeErrors
**Root Cause**: Cards not compatible with current HA version or missing dependencies
**Impact**: Specific cards not rendering

## 🔧 Fix Actions Required

### 📋 Phase 1: Validate Current Resources (IMMEDIATE)
```bash
# Check which cards are actually installed
ls /config/www/community/
# Check HACS files
ls /config/www/community/hacsfiles/
```

### 📋 Phase 2: Remove Problematic Cards (SAFE)
Cards to temporarily disable from configuration.yaml resources:
- `simple-weather-card` (causing TypeErrors)
- `mini-media-player` (causing constructor errors)  
- `scoped-custom-element-registry` (404 error)

### 📋 Phase 3: Validate Remaining Cards
Keep only verified working cards:
- ✅ `button-card` (core, widely compatible)
- ✅ `lovelace-mushroom` (modern, stable)
- ✅ `mini-graph-card` (stable, popular)
- ✅ `vertical-stack-in-card` (simple, stable)
- ✅ `card-mod` (essential for styling)

### 📋 Phase 4: Clear Browser Cache
- Hard refresh (Ctrl+Shift+R)
- Clear browser cache completely
- Test in incognito mode

## 🎯 Minimal Resource Configuration

```yaml
lovelace:
  mode: yaml
  resources:
    # CORE CARDS ONLY (verified working)
    - url: /hacsfiles/button-card/button-card.js
      type: module
    - url: /hacsfiles/lovelace-mushroom/mushroom.js
      type: module
    - url: /hacsfiles/mini-graph-card/mini-graph-card-bundle.js
      type: module
    - url: /hacsfiles/vertical-stack-in-card/vertical-stack-in-card.js
      type: module
    - url: /hacsfiles/lovelace-card-mod/card-mod.js
      type: module
    - url: /hacsfiles/auto-entities/auto-entities.js
      type: module
    
    # CUSTOM SIDEBAR (already in frontend.extra_module_url)
    # - url: /hacsfiles/custom-sidebar/custom-sidebar-yaml.js
    #   type: module
```

## 🚨 Cards to Temporarily Remove

Comment out these problematic cards:
```yaml
# TEMPORARILY DISABLED - CAUSING ERRORS
# - url: /hacsfiles/Switch-and-Timer-Bar-Card/switch-and-timer-bar-card.js
#   type: module
# - url: /local/community/simple-weather-card/simple-weather-card-bundle.js  
#   type: module
# - url: /hacsfiles/home-assistant-flightradar24-card/flightradar24-card.js
#   type: module
# - url: /hacsfiles/floor3d-card/floor3d-card.js
#   type: module
```

## 🎯 Testing Protocol

### Step 1: Apply Minimal Config
1. Comment out problematic cards in configuration.yaml
2. Restart Home Assistant
3. Check browser console for errors

### Step 2: Verify Core Functionality  
1. Test System Triage dashboard loads
2. Test automation control toggles work
3. Verify no CustomElementRegistry conflicts

### Step 3: Gradual Re-enable
1. Add back one card at a time
2. Test after each addition
3. Identify specific problematic cards

## 📊 Expected Results

After applying minimal config:
- ✅ No more CustomElementRegistry conflicts
- ✅ Reduced 404 errors
- ✅ Core dashboards load properly
- ✅ Automation control system functional
- ⚠️ Some fancy cards temporarily unavailable (can re-enable later)

## 🔄 Recovery Plan

If issues persist:
1. Use fallback dashboard with basic entities cards only
2. Disable all custom cards temporarily
3. Test core HA functionality
4. Re-enable cards one by one to isolate problems

This approach prioritizes **system stability** over **advanced UI features** during the stabilization phase.