# Quick Fix Summary - Nov 3, 2025

## 🎯 Analysis Results

### Total Problem Scope
- **678/2,684 entities unavailable (25.3%)**
- **75/194 automations unavailable (38.7%)**
- **Container sensors already hidden** ✅

### Top Problem Domains
1. **sensor** - 306 unavailable (mostly container CPU/memory sensors)
2. **binary_sensor** - 99 unavailable
3. **automation** - 75 unavailable (❗ HIGH PRIORITY - 38% failure rate)
4. **switch** - 57 unavailable (mostly Alexa Media Player)
5. **media_player** - 38 unavailable 
6. **light** - 36 unavailable

### Critical Automation Failures
Sample broken automations include:
- Git sync related automations (can be disabled - no git sync)
- GPT/AI integration automations 
- Dashboard optimization automations
- Email/Kodi automations

## 🛠️ Stabilizers Applied

### ✅ Container Sensors (Already Hidden)
```yaml
homeassistant:
  customize_glob:
    "sensor.*_cpu_percent": { hidden: true }
    "sensor.*_memory_percent": { hidden: true }
recorder:
  exclude:
    entity_globs: [sensor.*_cpu_percent, sensor.*_memory_percent]
logbook:
  exclude:
    entity_globs: [sensor.*_cpu_percent, sensor.*_memory_percent]
```

### ✅ Automation Analysis Complete
- Created `automations_unavailable.csv` with 75 broken automations
- Many are AI/GPT related and may need entity reference fixes
- Git sync automations can be safely disabled

## 📤 Files Ready for GPT Analysis
1. **unavailable_entities.csv** (44.7 KB) - Complete breakdown
2. **entity_analysis_summary.md** (1.6 KB) - Executive summary 
3. **automations_unavailable.csv** (5.3 KB) - Broken automations list

## 🎯 Next Actions for GPT
1. **Triage by integration** - identify which to fix vs. disable
2. **Automation priority** - which 75 automations are critical
3. **Entity cleanup plan** - safe removal candidates
4. **Integration restart needs** - which need reconfiguration

## 💡 Quick Wins Identified
- Disable Git-related automations (no longer using Git)
- Fix Alexa Media Player integration (many switches unavailable)
- Check ESPHome devices for power/connectivity issues
- Review AI/GPT automations for entity reference mismatches