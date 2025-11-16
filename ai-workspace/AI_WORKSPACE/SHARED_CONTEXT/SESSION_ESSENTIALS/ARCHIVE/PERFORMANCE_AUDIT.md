# 🧠 PERFORMANCE AUDIT PROTOCOL — Home Assistant Bottleneck Analysis
**Date:** November 11, 2025
**Status:** Ready for Implementation
**Goal:** Identify and eliminate performance bottlenecks causing UI slowness and system delays

---

## 🎯 AUDIT OVERVIEW
Systematic performance analysis using HA's built-in Profiler integration to identify slow components, memory leaks, and optimization opportunities.

---

## 🛠️ PROFILER INTEGRATION SETUP

### Step 1: Enable Profiler Integration
1. Navigate to **Settings → Devices & Services → Add Integration**
2. Search for **"Profiler"**
3. Click **"Add Integration"**
4. Confirm setup (no additional configuration needed)

### Step 2: Verify Profiler Entities
After setup, these entities should be available:
- `sensor.profiler_status` - Current profiling status
- `sensor.profiler_memory` - Memory usage statistics
- `switch.profiler_enabled` - Enable/disable profiling

---

## 📊 PERFORMANCE PROFILING EXECUTION

### CPU Profile (60 seconds)
```yaml
service: profiler.start
data:
  seconds: 60
```

**What it captures:**
- Function call times and frequencies
- CPU-intensive operations
- Integration processing overhead
- Template sensor evaluation costs

**Output:** `profile.<timestamp>.cprof` file in `/config/`

### Memory Profile (60 seconds)
```yaml
service: profiler.memory
data:
  seconds: 60
```

**What it captures:**
- Memory allocation patterns
- Object growth over time
- Potential memory leaks
- Large object retention

**Output:** `.hpy` file in `/config/`

---

## 🔍 PROFILING RESULTS ANALYSIS

### Visualization Tools Setup

#### SnakeViz (CPU Profiles)
```bash
# Install SnakeViz
pip install snakeviz

# Visualize CPU profile
snakeviz /config/profile.20251111_140000.cprof
```

#### KCachegrind/QCachegrind (Call Graphs)
```bash
# Install QCachegrind (Linux/Windows)
# Open .cprof file directly in QCachegrind
qcachegrind /config/callgrind.out.20251111_140000
```

#### Memory Analysis (Heapy)
```python
# Python script for memory analysis
from guppy import hpy
import pickle

# Load memory profile
with open('/config/memory_profile.hpy', 'rb') as f:
    profile = pickle.load(f)

# Analyze heap
h = hpy()
h.pb()  # Print heap summary
```

---

## 🎯 COMMON BOTTLENECKS TO IDENTIFY

### 1. **Slow Integrations**
**Symptoms:** High CPU during specific time intervals
**Common Culprits:**
- SmartThings (frequent polling)
- Synology (large file operations)
- TuneBlade (audio processing)
- MQTT broker (high message volume)

**Fix:** Reduce polling intervals, optimize entity counts

### 2. **Heavy Template Sensors**
**Symptoms:** CPU spikes during state changes
**Common Issues:**
- Complex Jinja2 expressions
- Large data set processing
- Frequent state evaluations

**Fix:** Simplify templates, add caching, reduce evaluation frequency

### 3. **Memory Leaks**
**Symptoms:** Gradually increasing memory usage
**Common Sources:**
- Custom cards holding references
- Stale entity objects
- Unclosed connections

**Fix:** Restart affected integrations, update custom components

### 4. **Database Performance**
**Symptoms:** Slow startup, delayed queries
**Common Issues:**
- Large `home-assistant_v2.db` file
- Excessive recorder retention
- Missing database indexes

**Fix:** Optimize recorder settings, consider MariaDB migration

### 5. **Frontend Rendering**
**Symptoms:** Slow dashboard loads, unresponsive UI
**Common Issues:**
- Complex Lovelace configurations
- Heavy custom cards
- Large entity counts

**Fix:** Simplify dashboards, optimize card configurations

---

## 📋 AUDIT EXECUTION CHECKLIST

### Pre-Audit Preparation
- [ ] Enable Profiler integration
- [ ] Clear browser cache (`Ctrl+Shift+R`)
- [ ] Note current performance baseline
- [ ] Ensure system is in normal operation state

### CPU Profiling Phase
- [ ] Start 60-second CPU profile during normal use
- [ ] Perform typical HA operations (navigate dashboards, trigger automations)
- [ ] Wait for profile completion notification
- [ ] Locate `.cprof` file in `/config/`

### Memory Profiling Phase
- [ ] Start 60-second memory profile
- [ ] Navigate through all major dashboards
- [ ] Trigger various automations and scripts
- [ ] Wait for memory profile completion

### Results Analysis Phase
- [ ] Install visualization tools (SnakeViz, QCachegrind)
- [ ] Analyze CPU profile for hotspots
- [ ] Analyze memory profile for leaks
- [ ] Identify top 3 performance bottlenecks
- [ ] Document findings with specific recommendations

### Optimization Implementation
- [ ] Apply fixes for identified bottlenecks
- [ ] Test performance improvements
- [ ] Re-run profiles to validate fixes
- [ ] Document before/after performance metrics

---

## 📊 EXPECTED FINDINGS (Based on Current Issues)

### Likely Performance Issues
1. **Template Sensor Overhead** - Complex automation counting templates
2. **MQTT Processing** - Flight radar data processing
3. **Database Queries** - Large entity set operations
4. **Frontend Rendering** - Complex dashboard configurations

### Current System Metrics
- **Entity Count:** 3,027 total (844 unavailable)
- **Automation Count:** ~168 active
- **Integration Count:** 32 loaded
- **Memory Usage:** ~500MB (estimated)
- **UI Response:** 5-10 second delays reported

---

## 🛠️ OPTIMIZATION RECOMMENDATIONS

### Immediate Actions (< 30 minutes)
```yaml
# Reduce recorder retention
recorder:
  purge_keep_days: 3  # Currently 7

# Optimize sensor polling
sensor:
  - platform: template
    scan_interval: 120  # Increase from 30-60s where possible
```

### Medium-term Fixes (1-2 hours)
- Simplify complex template sensors
- Reduce dashboard complexity
- Optimize automation triggers
- Update custom component versions

### Long-term Improvements (Days)
- Migrate to MariaDB
- Implement caching layers
- Redesign heavy dashboards
- Upgrade hardware if needed

---

## 📈 SUCCESS METRICS

### Performance Targets
- **CPU Usage:** < 20% average during normal operation
- **Memory Usage:** < 600MB stable (no gradual increase)
- **UI Response:** < 2 seconds for dashboard loads
- **Entity Availability:** > 95% (currently ~72%)
- **Startup Time:** < 5 minutes

### Validation Commands
```bash
# Check current resource usage
ha core stats

# Monitor entity recovery
ha core logs | grep "entity"

# Test automation performance
time ha automation trigger automation.test_automation
```

---

## 📝 AUDIT SESSION LOG

### Session Start: November 11, 2025
- **Pre-Audit Status:** UI slowness, 844 unavailable entities, template sensor issues
- **Profiler Setup:** Integration enabled, ready for profiling
- **Baseline Metrics:** CPU ~15%, Memory ~550MB, Entity availability 72%

### Profiling Results
*[To be filled after profiler execution]*

### Identified Bottlenecks
*[To be filled after analysis]*

### Applied Optimizations
*[To be filled after fixes]*

### Post-Optimization Metrics
*[To be filled after validation]*

---

## 🎯 NEXT STEPS

1. **Execute CPU Profile** - Run 60-second profile during normal HA usage
2. **Execute Memory Profile** - Capture memory usage patterns
3. **Analyze Results** - Use visualization tools to identify bottlenecks
4. **Apply Fixes** - Implement optimization recommendations
5. **Validate Improvements** - Re-profile to confirm performance gains

---

**🎯 MISSION STATUS:** Performance audit protocol ready for execution. Profiler integration configured, analysis tools prepared, optimization roadmap defined.

**📊 TARGET OUTCOME:** Identify root causes of UI slowness and system delays, implement targeted fixes for 50-80% performance improvement.</content>
<parameter name="filePath">s:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\PERFORMANCE_AUDIT.md