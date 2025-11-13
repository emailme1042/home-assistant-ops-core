# 🚑 HA Recovery Package - Complete Instructions

## 📦 Recovery Package Contents

This package contains everything needed to recover Home Assistant from frontend compilation failures and custom component conflicts.

### 🛠️ Recovery Scripts

#### 1. `rebuild_frontend.bat`
- **Purpose**: Rebuilds HA frontend to fix compilation errors
- **When to use**: When UI won't load despite HA Core running
- **Requirements**: SSH access to Home Assistant
- **Command**: `ha core rebuild`

#### 2. `disable_custom_components.bat`  
- **Purpose**: Temporarily disables ALL custom components
- **When to use**: When HACS/custom integrations cause conflicts
- **Safety**: No data lost - components are renamed, not deleted
- **Effect**: HA runs with core integrations only

#### 3. `restore_custom_components.bat`
- **Purpose**: Restores previously disabled custom components
- **When to use**: After confirming HA works without custom components
- **Process**: Renames disabled folders back to active state

### 📊 Recovery Dashboard

#### `recovery_dashboard.yaml`
- **Purpose**: Minimal fallback UI when main dashboards broken
- **Features**: System health, essential controls, recovery buttons
- **Dependencies**: Zero custom cards - core HA elements only

## 🎯 Recovery Procedure

### Step 1: Quick Diagnosis
```powershell
# Test if HA Core is running
Invoke-WebRequest -Uri "http://192.168.1.217:8123/api/config" -UseBasicParsing

# Test frontend compilation
Invoke-WebRequest -Uri "http://192.168.1.217:8123/frontend_latest/" -UseBasicParsing
```

### Step 2: Frontend Rebuild (Try First)
1. **Access HA via SSH**:
   - Go to: Settings → Add-ons → SSH & Web Terminal
   - Install SSH add-on if needed
   - Click "Open Web UI"

2. **Run Frontend Rebuild**:
   ```bash
   ha core rebuild
   ```

3. **Wait & Test**: 5-10 minutes, then try UI access

### Step 3: Component Isolation (If Rebuild Fails)
1. **Run**: `disable_custom_components.bat`
2. **Restart Home Assistant**
3. **Test UI Access** - should work with core only
4. **Gradually restore** components if needed

### Step 4: Dashboard Recovery
If main dashboards broken:
1. **Copy** `recovery_dashboard.yaml` to `dashboards/` folder
2. **Add to configuration.yaml**:
   ```yaml
   lovelace:
     dashboards:
       recovery:
         mode: yaml
         title: Recovery
         filename: dashboards/recovery_dashboard.yaml
   ```

## 🚨 Emergency Contacts & Resources

### Current System State (2025-11-04 01:27)
- ✅ **HA Core**: Running with minimal config
- ❌ **Frontend**: Compilation broken
- ✅ **Custom Components**: Safely disabled in `custom_components_EMERGENCY_DISABLED/`
- ✅ **Data**: All preserved and backed up

### Recovery Success Criteria
- [ ] UI accessible at http://192.168.1.217:8123
- [ ] No frontend compilation errors
- [ ] Core controls (lights, switches) functional
- [ ] System health indicators working

### Rollback Plan
If recovery fails:
1. All original files backed up with timestamps
2. Custom components preserved in EMERGENCY_DISABLED folder
3. Full configuration backup: `configuration_BROKEN_BACKUP_*.yaml`
4. Can restore exact previous state if needed

---

**Created**: 2025-11-04 01:30  
**Status**: Ready for deployment  
**Success Rate**: High (addresses root frontend compilation issue)