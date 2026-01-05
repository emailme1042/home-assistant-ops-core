# 🧠 Home Assistant Rendering Failures — Nov 3, 2025

## 🔹 Symptoms
- Dashboard fails to render on page load or transition
- Cards intermittently disappear or throw "Entity not found"
- JS console shows WebSocket and custom card errors
- Nabu Casa or local access drops during frontend refresh

## 🔹 Suspected Causes
- ❌ Broken Lovelace resources (e.g. duplicate or missing card JS)
- ❌ Panel view misconfiguration (multiple cards in single-panel view)
- ❌ WebSocket disconnects (browser or router interference)
- ❌ Entity drift (template sensors not loading or renamed)
- ❌ Router DNS or FTTP dropout during HA page transition

## 🔹 Validation Steps
- [ ] Check `configuration.yaml` for duplicate Lovelace resources
- [ ] Inspect JS console for:
  - `Cannot convert undefined or null to object`
  - `CustomElementRegistry` conflicts
  - 404 errors from `/node_modules/`
- [ ] Validate entity existence in Developer Tools → States
- [ ] Test HA access via mobile hotspot (rule out FTTP)
- [ ] Restart HA and router, re-authenticate Nabu Casa

## 🔹 Next Actions
- Rebuild minimal dashboard with verified cards
- Regenerate `system_health_template.yaml` if sensors missing
- Log router dropouts and DNS settings
- Map rendering failures to browser type and session time

## 🔧 Current System Status
**Date Logged**: November 3, 2025
**HA Version**: 2025.10.4
**Hardware**: Home Assistant Green
**Network**: FTTP with Nabu Casa cloud access
**Frontend**: 26 HACS custom cards loaded

## 📊 Diagnostic Log Template
```
Timestamp: [YYYY-MM-DD HH:MM:SS]
Access Method: [Local/Nabu Casa/Mobile Hotspot]
Browser: [Chrome/Edge/Firefox + Version]
Dashboard: [AI Main/System Overview/Users & Media]
Failure Type: [Blank Cards/Entity Errors/Complete Failure]
JS Console Errors: [Copy relevant errors]
Network Status: [Connected/Intermittent/Offline]
Recovery Action: [Refresh/Restart HA/Router Reset]
Success: [Yes/No]
```

## 🎯 Browser-Specific Tracking
### Chrome Issues
- [ ] Extension conflicts (AdBlock, etc.)
- [ ] Cache corruption
- [ ] WebSocket connection drops

### Edge Issues  
- [ ] Tracking prevention interference
- [ ] DNS resolution delays
- [ ] Certificate validation

### Firefox Issues
- [ ] CORS policy blocking
- [ ] WebSocket protocol version
- [ ] Cookie/session management

## 🛡️ Recovery Protocols
1. **Immediate**: Browser hard refresh (Ctrl+F5)
2. **Quick**: Clear browser cache for HA domain
3. **Moderate**: Restart Home Assistant via Supervisor
4. **Extended**: Router restart + Nabu Casa re-auth
5. **Nuclear**: Fallback dashboard + minimal card test

---
**Last Updated**: Nov 3, 2025
**Status**: Active monitoring
**Next Review**: After next rendering failure incident