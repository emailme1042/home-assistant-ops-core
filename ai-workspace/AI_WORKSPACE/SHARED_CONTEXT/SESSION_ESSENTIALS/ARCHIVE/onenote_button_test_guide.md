# OneNote Sync Button Test Guide - Post-Restart

## 🎯 Testing Protocol

### Step 1: Wait for HA Restart
- Monitor http://192.168.1.217:8123 until HA is responsive
- Look for startup completion message

### Step 2: Navigate to Multi-Agent Dashboard
1. Go to HA sidebar
2. Click **🤖 AI Main**
3. Click **🧭 Multi-Agent Messaging Matrix** tab

### Step 3: Test OneNote Sync Button
1. Locate **OneNote Integration Panel**
2. Click **🔄 Sync OneNote File** button
3. **Expected Result**: 
   - Button should trigger immediate response
   - Should see notification: "OneNote manual sync triggered"
   - `input_boolean.trigger_onenote_sync` should briefly turn on then off

### Step 4: Verify New Entities
Check Developer Tools → States for:
- ✅ `input_boolean.trigger_onenote_sync` - Should exist
- ✅ `automation.onenote_manual_trigger` - Should exist

### Step 5: Validate Complete System
- **Multi-Agent Dashboard**: All 28 entities should load properly
- **Template Sensors**: No more "Entity not found" errors
- **SSH Terminal**: Should remain accessible via Settings → Add-ons

## 🚨 If Button Still Doesn't Work
1. Check Developer Tools → States for missing entities
2. Review Home Assistant logs for automation errors
3. Use SSH terminal for debugging if needed

## ✅ Success Criteria
- OneNote button responds immediately when pressed
- No "Entity not found" errors in dashboard
- All multi-agent coordination features functional
- SSH emergency access confirmed working

**Status**: Ready for testing after HA restart completes!