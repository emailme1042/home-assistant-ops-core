# 🆘 EMERGENCY: HA Unresponsive - Recovery Protocol

## 🚨 **SITUATION**: Home Assistant Unresponsive
- **Web UI**: Timeout after 10+ seconds
- **API**: Not responding
- **Logs**: Show HA running but with device timeouts
- **Last Activity**: 20:37 (aircraft/device automations)

## 🔧 **IMMEDIATE RECOVERY OPTIONS**

### Option 1: **SSH Terminal Access** (RECOMMENDED)
1. Open browser to: `http://192.168.1.217:8123`
2. If any part loads, navigate to: **Settings → Add-ons → SSH & Web Terminal**
3. Click **"Open Web UI"** button
4. In terminal, run: `ha core restart`

### Option 2: **Power Cycle HA Green**
1. **Unplug power** from HA Green device
2. **Wait 30 seconds**
3. **Plug back in**
4. **Wait 3-5 minutes** for full boot

### Option 3: **Network Reset**
1. **Restart router** (192.168.1.1)
2. **Wait 2 minutes** for network stabilization
3. **Test HA access**: `http://192.168.1.217:8123`

## 🧬 **LIKELY CAUSES**

### Configuration Load Issues:
- **Emergency dashboard** added during conflict resolution
- **Duplicate entries** in configuration.yaml
- **Resource conflicts** from Lovelace changes

### System Resource Exhaustion:
- **Kasa device timeouts** suggest network stress
- **Nabu Casa connection issues** indicate connectivity problems
- **Device polling overload** from new configurations

## 🛡️ **FALLBACK CONFIGURATION READY**

If HA restarts but still has issues:

### Restore Minimal Config:
```powershell
# Emergency config restore
Copy-Item 'configuration_minimal_SAVED.yaml' 'configuration.yaml' -Force
# Then restart HA
```

### Emergency Dashboard Available:
- **File**: `emergency_working_dashboard.yaml`
- **Purpose**: Core cards only, no custom dependencies
- **Access**: Should appear as "🚨 Emergency Recovery" after restart

## 📊 **POST-RECOVERY VALIDATION**

After HA becomes responsive:

1. **Test Web UI**: Load home dashboard
2. **Check Logs**: `ha core logs` for new errors  
3. **Validate Config**: `ha core check` for YAML issues
4. **Test Emergency Dashboard**: Verify it loads correctly

## 🔍 **ROOT CAUSE ANALYSIS**

**Likely Issue**: 
- Configuration changes created resource conflicts
- Multiple dashboard definitions confused Lovelace renderer
- System became unresponsive due to frontend compilation failure

**Evidence**:
- Network timeouts in logs
- Kasa device communication failures
- Web UI completely unresponsive despite HA core running

## ✅ **SUCCESS CRITERIA**

HA recovery successful when:
- [ ] Web UI loads within 5 seconds
- [ ] Emergency Recovery dashboard accessible
- [ ] No YAML configuration errors in logs
- [ ] System responsive to configuration reloads

---

**🚨 IMMEDIATE ACTION**: Try SSH terminal access first, then power cycle if needed.

**Next Steps**: Once HA responsive, validate emergency dashboard and assess configuration conflicts.