# Entity Recovery Plan - October 27, 2025

## 🎯 **MISSION: Dashboard Entity Recovery**
**Goal**: Fix all broken dashboard entity references to restore full system functionality

## 🔍 **Broken Entities Identified**

### Critical Missing Entities:
- ❌ `input_boolean.run_validation_test` → **ALREADY EXISTS**: `includes/input_booleans/validation_controls.yaml`
- ❌ `input_text.ai_context_note` → **MISSING** - needs creation
- ❌ `input_text.todo_task_1` → **MISSING** - needs creation  
- ❌ `input_boolean.ai_script_toggle_1` → **MISSING** - needs creation
- ❌ `input_boolean.ai_script_toggle_2` → **MISSING** - needs creation
- ❌ `notify.gmail_sender` → **MISSING** - needs notify config

### Dashboard Impact Assessment:
- 🔥 **AI Workspace Dashboard** - Multiple missing entities
- 🔥 **Admin Batch Dashboards** - test_mode, test_string missing
- 🔥 **Ops Dashboards** - Multiple navigation toggles missing
- ✅ **AI Navigation** - Working after our fixes!

## 📋 **Recovery Strategy**

### Phase 1: Create Missing Core Entities (15 min)
1. Create `ai_context_note` input_text
2. Create `todo_task_1` input_text  
3. Create AI script toggles
4. Create admin test entities

### Phase 2: Fix Notification Services (10 min)
1. Set up `notify.gmail_sender` 
2. Verify other notify services

### Phase 3: Dashboard Testing (15 min)
1. Test AI Workspace dashboard
2. Test Admin dashboards
3. Test Ops dashboards

## 🎯 **Expected Results**
- ✅ **AI Workspace Dashboard**: Fully functional
- ✅ **Admin Dashboards**: All 15 batches working
- ✅ **Ops Dashboards**: Navigation and controls working  
- ✅ **User Dashboards**: Error-free operation

## 📊 **Impact Measurement**
- **Before**: Multiple dashboards showing entity errors
- **After**: Complete dashboard functionality restored
- **Benefit**: Massive improvement in system usability

## 🚀 **Next Steps**
1. Start with Phase 1 entity creation
2. Test one dashboard at a time
3. Document successful fixes
4. Move to next phase

**Timeline**: ~40 minutes for complete recovery