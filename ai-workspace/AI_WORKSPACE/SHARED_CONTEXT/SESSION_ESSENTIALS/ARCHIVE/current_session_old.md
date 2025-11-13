# Current Session — 2025-11-10

## 🎯 Goal
Fix all 404 errors and JS load failures for custom Lovelace cards after HA restart.

## 📍 Current Status
✅ **Resources.yaml corrected** with exact filenames and case-sensitive paths.  
🚨 **JS files corrupted** - many contain webpack configs or empty files instead of browser JS.  
🔄 **Next: Reload resources + reinstall failing cards via HACS**

## ✅ Completed Steps
1. ✅ **Path Corrections**: Updated resources.yaml with exact JS filenames (e.g., swipe-navigation.js, HA-Firemote.js)
2. ✅ **Case Sensitivity**: All paths lowercase folders, exact file casing
3. ✅ **File Existence**: Verified all referenced JS files exist on disk
4. ✅ **YAML Cleanup**: Removed duplicates, fixed formatting

## � Next Steps
1. **Reload Lovelace Resources**: In HA UI → Developer Tools → YAML → "Reload Lovelace Resources"
2. **Reinstall Failing Cards via HACS**: For cards with JS errors (bubble-card, layout-card, etc.), go to HACS → Frontend → search and reinstall
3. **Hard Refresh Browser**: Ctrl+F5 to clear cache
4. **Test Dashboard Loading**: Verify no 404s or JS errors in console

## 🤔 Open Questions
- Why are some JS files webpack configs instead of built JS? (Need to download correct releases)
- Are there duplicate card registrations causing "name already used" errors?

## � Related Files
- `resources.yaml` - Corrected with exact paths
- `S:\www\community\*` - Some JS files need replacement (e.g., bubble-card.js is webpack config)
- HACS Frontend section - Use to reinstall corrupted cards

## 📊 Expected Results After Fixes
- ✅ No 404 errors for resource loading
- ✅ No "require is not defined" or "name already used" JS errors
- ✅ All custom cards render properly in dashboards
- ✅ Clean browser console

**Priority**: High - Cards not loading breaks dashboard functionality
