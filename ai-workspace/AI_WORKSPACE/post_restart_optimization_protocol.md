# 🚀 HA PERFORMANCE OPTIMIZATION - POST-RESTART PROTOCOL
# Execute immediately after HA restart to achieve <5s dashboard loads

## 📋 EXECUTION ORDER

### PHASE 1: IMMEDIATE (0-5 minutes after restart)
1. **Database Purge** - CRITICAL for >7GB → ~500MB reduction
   ```powershell
   # Run from PowerShell in AI_WORKSPACE folder
   .\purge_database.ps1
   ```
   Expected: Database size drops from >7GB to ~500MB-1GB

2. **Validate Configuration**
   - Settings → System → Check Configuration
   - Should show ✅ Valid (no errors)

### PHASE 2: MONITORING (5-15 minutes)
3. **Monitor Purge Progress**
   - Check HA logs for purge completion
   - Database size should reduce significantly
   - System may be slower during purge (normal)

4. **Dashboard Load Time Test**
   - Navigate to main dashboard
   - Time load from click to fully rendered
   - Target: <5 seconds (vs current 25s)

### PHASE 3: VERIFICATION (15-30 minutes)
5. **Entity Availability Check**
   - Developer Tools → States
   - Total entities: ~3,500
   - Available: Target >90% (vs current ~65%)

6. **Performance Metrics**
   - CPU/Memory usage should be normal
   - WebSocket connections stable
   - No excessive logging

## 🎯 EXPECTED RESULTS

### Immediate Improvements (Post-Purge):
- ✅ **Dashboard Load**: 25s → <5s
- ✅ **Database Size**: >7GB → ~500MB-1GB
- ✅ **Entity Availability**: 65% → >90%
- ✅ **System Responsiveness**: Significantly improved
- ✅ **Memory Usage**: Reduced pressure
- ✅ **WebSocket Stability**: No more disconnections

### Long-term Benefits:
- ✅ **Sustainable Performance**: 3-day retention prevents re-bloat
- ✅ **Optimized Storage**: MariaDB efficiency maintained
- ✅ **Clean History**: Only essential data retained
- ✅ **Fast Queries**: Database operations accelerated

## 🔧 TROUBLESHOOTING

### If Purge Fails:
1. Check HA logs for errors
2. Verify API token is valid
3. Use HA UI alternative: Developer Tools → Services → recorder.purge

### If Performance Not Improved:
1. Check database size reduction
2. Verify recorder exclusions applied
3. Monitor for new high-frequency sensors
4. Consider MariaDB optimization

### If Entity Availability Low:
1. Check MQTT broker status
2. Restart ESPHome containers
3. Verify Zigbee coordinator
4. Check device connectivity

## 📊 SUCCESS METRICS

**Before Optimization:**
- Dashboard load: 25+ seconds
- Database size: >7GB
- Entity availability: ~65%
- System responsiveness: Poor

**After Optimization (Target):**
- Dashboard load: <5 seconds ✅
- Database size: <1GB ✅
- Entity availability: >90% ✅
- System responsiveness: Excellent ✅

## 🚨 CRITICAL NOTES

- **Database purge may take 5-10 minutes** - be patient
- **System may be slower during purge** - this is normal
- **Restart HA after purge completes** for full effect
- **Monitor logs** for any errors during optimization
- **Backup created** - home-assistant_v2.db.backup exists

---
**EXECUTE THIS PROTOCOL IMMEDIATELY AFTER HA RESTART FOR MAXIMUM PERFORMANCE GAIN**