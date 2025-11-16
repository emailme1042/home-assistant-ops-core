# 🤖 GPT → Home Assistant Access Troubleshooting Guide

**Date**: November 3, 2025  
**System**: Jamie's HA Green with Nabu Casa  
**Nabu Casa URL**: `https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa`  
**Local URL**: `http://192.168.1.217:8123`

---

## 🔍 DIAGNOSIS CHECKLIST

### ✅ **Quick Status Check**
- [ ] **Nabu Casa Active**: Settings → Home Assistant Cloud → Connected
- [ ] **Remote Control ON**: Settings → Home Assistant Cloud → Remote Control toggle
- [ ] **User Remote Access**: Settings → People → Your User → Allow remote login 
- [ ] **Internet Stable**: SpeedTest shows >1Mbps down/up
- [ ] **Router Responsive**: Ping to 192.168.1.1 working

---

## 🔧 COMMON FIXES BY SYMPTOM

### 🚫 **"GPT can't access HA at all"**
**Root Cause**: GPTs can't reach local network (`http://192.168.1.217:8123`)  
**Solution**: Always use Nabu Casa URL for external access
```
❌ Wrong: http://homeassistant.local:8123
❌ Wrong: http://192.168.1.217:8123  
✅ Correct: https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa
```

### ☁️ **"Nabu Casa URL returns errors"**
**Root Cause**: Remote access disabled or cloud connection issues  
**Fixes**:
1. Settings → Home Assistant Cloud → Log out → Log back in
2. Toggle "Remote Control" off and on
3. Restart Home Assistant
4. Check subscription status in Nabu Casa account

### 🌐 **"WebSocket connection failed in browser"**
**Root Cause**: Chrome 119+ has WebSocket issues with Nabu Casa URLs  
**Browser Solutions**:
- ✅ **Try Firefox**: Generally works best with Nabu Casa
- ✅ **Try Edge**: Good WebSocket support, stable connections
- ⚠️ **Chrome Issues**: Clear cache, disable extensions, or switch browsers
- ❓ **Safari**: Mixed results, try other browsers first

### 👤 **"Authentication failures from external networks"**
**Root Cause**: User restricted to local network only  
**Fix**: Settings → People → [Your User] → Uncheck "Can only log in from the local network"

### 🔄 **"Intermittent connection drops"**
**Root Cause**: Session timeout or cloud connection drift  
**Fixes**:
1. Increase session timeout: `auth_providers: trusted_networks: allow_bypass_login: true`
2. Restart Home Assistant to refresh cloud connection
3. Check network stability (SpeedTest integration)

---

## 🧪 BROWSER COMPATIBILITY MATRIX

| Browser | Nabu Casa | WebSocket | Stability | Recommendation |
|---------|-----------|-----------|-----------|----------------|
| **Firefox** | ✅ Excellent | ✅ Stable | ✅ High | **RECOMMENDED** |
| **Edge** | ✅ Good | ✅ Stable | ✅ High | **RECOMMENDED** |
| **Chrome 119+** | ⚠️ Issues | ❌ Unstable | ⚠️ Medium | Try others first |
| **Chrome <119** | ✅ Good | ✅ Stable | ✅ High | OK if older version |
| **Safari** | ⚠️ Mixed | ⚠️ Variable | ⚠️ Medium | Not recommended |
| **Mobile Safari** | ⚠️ Mixed | ⚠️ Variable | ⚠️ Medium | Use HA app instead |

---

## 📊 NETWORK REQUIREMENTS

### **Minimum Requirements for GPT Access**
- **Download Speed**: >1 Mbps (5+ Mbps recommended)
- **Upload Speed**: >0.5 Mbps (2+ Mbps recommended)  
- **Latency**: <100ms (50ms preferred)
- **Connection Stability**: <5% packet loss

### **Firewall/Router Settings**
- **Port 443**: HTTPS traffic to Nabu Casa (usually open)
- **WebSocket Support**: Router must not block WebSocket upgrades
- **DNS Resolution**: Must resolve `*.ui.nabu.casa` domains

---

## 🔍 DEBUG WORKFLOW

### **Step 1: Local Testing**
```bash
# From Jamie's network:
curl -I http://192.168.1.217:8123
# Should return: HTTP/1.1 200 OK
```

### **Step 2: Nabu Casa Testing**  
```bash
# From any internet connection:
curl -I https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa
# Should return: HTTP/1.1 200 OK or redirect to login
```

### **Step 3: WebSocket Testing**
1. Open Browser DevTools (F12)
2. Go to Network tab
3. Filter by "WS" (WebSocket)
4. Load HA dashboard
5. Look for WebSocket connections - should show "Connected"

### **Step 4: Authentication Testing**
1. Open incognito/private browser window
2. Navigate to Nabu Casa URL
3. Log in with HA credentials
4. Dashboard should load completely

---

## 🚨 EMERGENCY FIXES

### **"Nothing works, GPT completely blocked"**
1. **Local Access Recovery**:
   - Connect to Jamie's WiFi network
   - Use `http://192.168.1.217:8123` directly
   - This bypasses all cloud/external issues

2. **Cloud Reset Procedure**:
   ```
   Settings → Home Assistant Cloud → Sign Out
   Restart Home Assistant (wait 2 minutes)
   Settings → Home Assistant Cloud → Sign In
   Enable Remote Control toggle
   Test Nabu Casa URL in new browser tab
   ```

3. **Network Troubleshooting**:
   - Test from mobile hotspot (different ISP)
   - Try different browser/device
   - Check if other cloud services work (Google, etc.)

---

## 📋 MONITORING DASHBOARD

**Added to AI Main Hub**: GPT Access Monitor view
- **Live Status**: Cloud connection, remote UI, authentication
- **Health Score**: Composite score (0-100%) for GPT accessibility  
- **Quick Actions**: Restart HA, test Nabu Casa, cloud settings
- **Browser Guide**: Real-time compatibility recommendations

---

## 🔄 MAINTENANCE SCHEDULE

### **Weekly Checks**
- [ ] Verify Nabu Casa subscription active
- [ ] Test remote access from external network
- [ ] Check cloud connection stability logs
- [ ] Monitor WebSocket connection health

### **Monthly Actions**  
- [ ] Update browser if using Chrome (WebSocket fixes)
- [ ] Review authentication logs for failed attempts
- [ ] Test GPT access from different browsers/devices
- [ ] Document any new compatibility issues

---

## 📞 ESCALATION PATH

### **When to Contact Support**
1. **Nabu Casa Issues**: Subscription, billing, or persistent cloud connection failures
2. **Browser Issues**: WebSocket problems persist across multiple browsers
3. **Network Issues**: ISP blocking specific traffic or DNS resolution problems

### **Information to Gather**
- Browser name and version
- Error messages (exact text)
- Network location (home, mobile, etc.)
- Time when issue started
- Screenshot of any error pages

---

**Last Updated**: November 3, 2025  
**Monitoring**: AI Main Hub → GPT Access Monitor  
**Support**: Available via HA community forums or Nabu Casa support