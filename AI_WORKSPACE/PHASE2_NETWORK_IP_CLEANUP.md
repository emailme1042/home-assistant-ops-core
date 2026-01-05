# PHASE 2: Network IP Cleanup - 192.168.1.x → 192.168.0.x Migration
**Date:** 2025-11-13
**Operator:** ⚙️ GitHub Copilot (VSCode)
**Session Owner:** 👤 Jamie

## 🎯 OBJECTIVE
Safely migrate all network references from 192.168.1.x subnet to 192.168.0.x subnet using automated, logged, and reversible batch find/replace operations.

## 📋 IP MAPPING REFERENCE
| Old IP | New IP | Purpose |
|--------|--------|---------|
| 192.168.1.1 | 192.168.0.1 | Router/Gateway |
| 192.168.1.107 | 192.168.0.107 | Device |
| 192.168.1.113 | 192.168.0.113 | Camera/Side |
| 192.168.1.129 | 192.168.0.129 | ESPHome Atom Lite BT Proxy |
| 192.168.1.149 | 192.168.0.149 | Netgear Device |
| 192.168.1.158 | 192.168.0.158 | Device |
| 192.168.1.164 | 192.168.0.164 | Camera/Front |
| 192.168.1.172 | 192.168.0.172 | Device |
| 192.168.1.183 | 192.168.0.183 | ESPHome New ESP |
| 192.168.1.200 | 192.168.0.200 | Fing API Server |
| 192.168.1.203 | 192.168.0.203 | Local Flask/GPT Services |
| 192.168.1.217 | 192.168.0.217 | Home Assistant Core |
| 192.168.1.220 | 192.168.0.220 | Broadlink Device |
| 192.168.1.245 | 192.168.0.245 | Sonos Device |
| 192.168.1.249 | 192.168.0.249 | TP-Link Device |
| 192.168.1.253 | 192.168.0.253 | Sonos Playbar |
| 192.168.1.254 | 192.168.0.254 | Camera/Garden |

## 📁 FILES TO UPDATE

### 🔧 Core Configuration Files
| File | IPs to Change | Priority |
|------|---------------|----------|
| `camera.yaml` | 192.168.1.217 → 192.168.0.217 | HIGH |
| `includes/rest_commands/rest.yaml` | 192.168.1.203, 192.168.1.217 → 192.168.0.203, 192.168.0.217 | HIGH |
| `includes/sensors/fing_local_api.yaml` | 192.168.1.200 → 192.168.0.200 | HIGH |

### 🔌 Device Configuration Files
| File | IPs to Change | Priority |
|------|---------------|----------|
| `esphome/atom-lite-btproxy.yaml` | 192.168.1.129, 192.168.1.1 → 192.168.0.129, 192.168.0.1 | HIGH |
| `esphome/new-esp.yaml` | 192.168.1.183, 192.168.1.1 → 192.168.0.183, 192.168.0.1 | HIGH |
| `go2rtc.yaml` | 192.168.1.164, 192.168.1.254, 192.168.1.113 → 192.168.0.164, 192.168.0.254, 192.168.0.113 | MEDIUM |

### 📜 Scripts & Documentation Files
| File | IPs to Change | Priority |
|------|---------------|----------|
| `AI_WORKSPACE/Scripts/*.ps1` | Various 192.168.1.x → 192.168.0.x | MEDIUM |
| `python_scripts/*.py` | Various 192.168.1.x → 192.168.0.x | MEDIUM |
| `includes/shell_commands/*.yaml` | Various 192.168.1.x → 192.168.0.x | MEDIUM |
| `AI_WORKSPACE/**/*.md` | Various 192.168.1.x → 192.168.0.x | LOW |

## 🔄 EXECUTION PROTOCOL

### Phase 2A: Core Configuration (HIGH Priority)
1. **Update `camera.yaml`**
   - Replace RTSP URLs: `192.168.1.217:8554` → `192.168.0.217:8554`

2. **Update `includes/rest_commands/rest.yaml`**
   - Replace Flask service URLs: `192.168.1.203:5001` → `192.168.0.203:5001`
   - Replace HA API URLs: `192.168.1.217:8123` → `192.168.0.217:8123`

3. **Update `includes/sensors/fing_local_api.yaml`**
   - Replace Fing API URL: `192.168.1.200:49090` → `192.168.0.200:49090`

### Phase 2B: Device Configuration (HIGH Priority)
4. **Update ESPHome Files**
   - `esphome/atom-lite-btproxy.yaml`: Static IP and gateway
   - `esphome/new-esp.yaml`: Static IP and gateway

5. **Update `go2rtc.yaml`**
   - Replace camera RTSP URLs for front, garden, and side cameras

### Phase 2C: Scripts & Documentation (MEDIUM/LOW Priority)
6. **Update PowerShell Scripts**
   - `AI_WORKSPACE/Scripts/*.ps1`: HA API URLs and service endpoints

7. **Update Python Scripts**
   - `python_scripts/*.py`: HA API URLs and service endpoints

8. **Update Shell Commands**
   - `includes/shell_commands/*.yaml`: Network references

9. **Update Documentation**
   - `AI_WORKSPACE/**/*.md`: IP references in documentation

## 🛡️ SAFETY MEASURES

### Pre-Execution Validation
- **YAML Syntax Check**: Run `python3 /config/scripts/validate_yaml.py /config` before each file change
- **Backup Creation**: Create timestamped backups of all modified files
- **Git Staging**: Stage changes incrementally for easy rollback

### Rollback Protocol
- **Immediate Revert**: `git checkout -- <file>` for individual file rollback
- **Batch Revert**: `git reset --hard HEAD~1` for complete phase rollback
- **Network Restore**: Router configuration backup available

### Testing Protocol
- **Connectivity Test**: Ping all updated IPs after changes
- **Service Validation**: Test HA API, Flask services, camera streams
- **Integration Check**: Verify MQTT, REST commands, device discovery

## 📊 VALIDATION CHECKLIST

### Phase 2A Validation
- [ ] HA Web UI accessible at `http://192.168.0.217:8123`
- [ ] Camera streams working in HA dashboard
- [ ] REST commands functional (Flask services, HA API)
- [ ] Fing network monitoring working

### Phase 2B Validation
- [ ] ESPHome devices online and responsive
- [ ] Camera RTSP streams accessible via go2rtc
- [ ] Device static IPs reachable on network

### Phase 2C Validation
- [ ] PowerShell scripts execute without errors
- [ ] Python scripts connect to correct endpoints
- [ ] Shell commands reference valid IPs
- [ ] Documentation reflects current network config

## 🚀 EXECUTION COMMANDS

### Batch Find/Replace Commands
```bash
# Phase 2A: Core files
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.217/192.168.0.217/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.203/192.168.0.203/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.200/192.168.0.200/g' {} \;

# Phase 2B: Device files
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.129/192.168.0.129/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.183/192.168.0.183/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.164/192.168.0.164/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.254/192.168.0.254/g' {} \;
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\.113/192.168.0.113/g' {} \;

# Phase 2C: Remaining IPs
find /config -name "*.yaml" -exec sed -i 's/192\.168\.1\./192.168.0./g' {} \;
find /config -name "*.ps1" -exec sed -i 's/192\.168\.1\./192.168.0./g' {} \;
find /config -name "*.py" -exec sed -i 's/192\.168\.1\./192.168.0./g' {} \;
find /config -name "*.md" -exec sed -i 's/192\.168\.1\./192.168.0./g' {} \;
```

### Manual Copilot Commands
```bash
# Execute in VSCode terminal for each file
sed -i 's/192\.168\.1\.217/192.168.0.217/g' camera.yaml
sed -i 's/192\.168\.1\.203/192.168.0.203/g' includes/rest_commands/rest.yaml
sed -i 's/192\.168\.1\.200/192.168.0.200/g' includes/sensors/fing_local_api.yaml
# ... continue for each file
```

## 📈 SUCCESS METRICS

### Network Connectivity
- [ ] All devices pingable on 192.168.0.x subnet
- [ ] Router DHCP serving correct range
- [ ] No IP conflicts detected

### Service Functionality
- [ ] Home Assistant fully operational
- [ ] All cameras streaming correctly
- [ ] Flask/GPT services responding
- [ ] Fing network monitoring active
- [ ] ESPHome devices connected

### System Stability
- [ ] HA restart successful without errors
- [ ] All automations functional
- [ ] Dashboard loads without issues
- [ ] No broken entity references

## 🎯 NEXT STEPS AFTER EXECUTION

1. **HA Restart**: `ha core restart` to apply network changes
2. **Connectivity Test**: Verify all services reachable on new IPs
3. **Device Reconnection**: Update device static IPs if necessary
4. **Integration Testing**: Test all HA integrations and automations
5. **Documentation Update**: Update network diagrams and IP references

## 🏆 ACHIEVEMENT TARGET
**NETWORK INFRASTRUCTURE MODERNIZATION**: Complete migration from legacy 192.168.1.x subnet to standardized 192.168.0.x subnet with zero service disruption and full system compatibility.

**Tags:** `#phase2_ip_cleanup` `#network_migration` `#192_168_1_to_0` `#automated_replacement` `#safe_rollback` `#comprehensive_validation`