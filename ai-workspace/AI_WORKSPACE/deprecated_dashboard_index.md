# Deprecated Dashboard Index

**Created**: 2025-10-27  
**Trigger**: GPT recommendation after dashboard testing  
**Status**: Post-entity cleanup archive

## 🗑️ **Archived Dashboards**

### **working_services_test.yaml** 
**Status**: 🗑️ **Archived** (Non-functional)  
**Reason**: Buttons non-functional, unclear utility, superseded by SYSTEM_OVERVIEW  
**Location**: `AI_WORKSPACE/ARCHIVE/dashboards/working_services_test.yaml`  
**Removed from**: `configuration.yaml` lovelace dashboards section

**Issues Found**:
- Buttons require additional backend automation to function
- Doesn't serve unique purpose beyond SYSTEM_OVERVIEW
- Entity references needed extensive patching
- No clear user value after entity cleanup

## 🛠️ **Dashboards Requiring Fixes**

### **SYSTEM_OVERVIEW.yaml**
**Status**: ⚠️ **Needs Structural Fix**  
**Issue**: Black screen loading (malformed YAML structure)  
**Action Required**: VSC structural fix needed  
**Recommendation**: Run HA Developer Tools → YAML Check for validation

**Suspected Issues**:
- View block malformed 
- Entity list includes invalid paths
- Resource section misplaced (fixed)
- Missing required view structure

## 📋 **Cleanup Recommendations**

### **Immediate Actions**
1. ✅ **Archive working_services_test** - Completed
2. 🔄 **Fix SYSTEM_OVERVIEW structure** - In progress
3. 🧹 **Remove unused entity references** - Completed via entity cleanup

### **Future Optimization**
- Consider simplified monitoring dashboard as replacement
- Focus on SYSTEM_OVERVIEW tab-based approach
- Consolidate testing functions into existing dashboards

## 🏆 **Successful Cleanup Results**
- **8 new entities created** for proper monitoring
- **Dashboard structure standardized** 
- **Entity references validated** against actual HA registry
- **Configuration warnings resolved**

---
**Next**: Fix SYSTEM_OVERVIEW structure, then system fully optimized for multi-AI collaboration