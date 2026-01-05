#!/usr/bin/env python3
"""
Browser-Specific Rendering Diagnostics
=====================================

Analyzes Home Assistant rendering failures across different browsers
and provides targeted troubleshooting for Chrome, Edge, and Firefox.

For Home Assistant Green - Network Drive S:\ Environment
"""

import os
import json
from datetime import datetime
from pathlib import Path

def create_browser_test_checklist():
    """Create comprehensive browser testing checklist"""
    
    checklist_content = """# 🌐 Browser-Specific HA Rendering Tests — Nov 3, 2025

## 🎯 Test Protocol

### **Phase 1: Chrome Diagnostics**
- [ ] **Access Method**: Local (192.168.1.217:8123)
  - [ ] Dashboard loads completely
  - [ ] All cards render properly  
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work
  
- [ ] **Access Method**: Nabu Casa (n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa)
  - [ ] Dashboard loads completely
  - [ ] All cards render properly
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work

- [ ] **Chrome Developer Tools** (F12)
  - [ ] Console tab: No red errors
  - [ ] Network tab: All resources load (no 404s)
  - [ ] WebSocket status: Connected and active
  - [ ] Performance: Load time < 3 seconds

### **Phase 2: Edge Diagnostics**  
- [ ] **Access Method**: Local (192.168.1.217:8123)
  - [ ] Dashboard loads completely
  - [ ] All cards render properly
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work
  
- [ ] **Access Method**: Nabu Casa
  - [ ] Dashboard loads completely
  - [ ] All cards render properly
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work

- [ ] **Edge Developer Tools** (F12)
  - [ ] Console tab: No red errors
  - [ ] Network tab: All resources load
  - [ ] Tracking prevention: Not blocking HA resources
  - [ ] SmartScreen: Not flagging HA content

### **Phase 3: Firefox Diagnostics**
- [ ] **Access Method**: Local (192.168.1.217:8123)
  - [ ] Dashboard loads completely
  - [ ] All cards render properly
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work
  
- [ ] **Access Method**: Nabu Casa
  - [ ] Dashboard loads completely
  - [ ] All cards render properly
  - [ ] Entity values update in real-time
  - [ ] Navigation buttons work

- [ ] **Firefox Developer Tools** (F12)
  - [ ] Console tab: No red errors
  - [ ] Network tab: All resources load
  - [ ] CORS policy: Not blocking cross-origin
  - [ ] Enhanced tracking protection: Disabled for HA

## 📊 Common Error Patterns

### **Chrome Issues**
```
CustomElementRegistry: "custom-element" already defined
Failed to load resource: net::ERR_BLOCKED_BY_CLIENT
WebSocket connection failed: Error in connection establishment
```

### **Edge Issues**
```
Mixed Content: The page was loaded over HTTPS but requested an insecure resource
CORS policy: No 'Access-Control-Allow-Origin' header
Certificate error: This site is not secure
```

### **Firefox Issues**
```
Cross-Origin Request Blocked: CORS policy
Content Security Policy: directive violated
Certificate transparency issues
```

## 🛠️ Browser-Specific Fixes

### **Chrome Fixes**
1. **Extensions**: Disable AdBlock, uBlock Origin for HA domain
2. **Cache**: Settings → Privacy → Clear browsing data → Cached images
3. **HTTPS**: Ensure using correct protocol (http vs https)
4. **DevTools**: Enable "Disable cache" during testing

### **Edge Fixes**  
1. **Tracking Prevention**: Settings → Privacy → Exceptions → Add HA domain
2. **SmartScreen**: Settings → Security → SmartScreen → Disable for HA
3. **Cache**: Settings → Privacy → Choose what to clear → Cached data
4. **Certificate**: Settings → Advanced → Manage certificates

### **Firefox Fixes**
1. **Enhanced Protection**: Settings → Privacy → Standard (not Strict)
2. **CORS**: Type `about:config` → security.tls.insecure_fallback_hosts
3. **Certificate**: Settings → Privacy → Certificates → View exceptions
4. **WebSocket**: network.websocket.enabled = true in about:config

## 🎯 Fallback Dashboard Test

**URL**: `http://192.168.1.217:8123/fallback-minimal/fallback-minimal`

### **Minimal Test Cards**:
- [ ] CPU/Memory usage entities load
- [ ] System uptime displays
- [ ] Router connectivity shows
- [ ] Speed test values present
- [ ] Navigation buttons work

**If fallback fails**: Core HA system issue (not browser-specific)
**If fallback works**: Main dashboard has card/entity problems

## 📝 Incident Log Template

```
Date: [YYYY-MM-DD HH:MM]
Browser: [Chrome/Edge/Firefox + Version]
Access: [Local/Nabu Casa]
Dashboard: [AI Main/System Overview/Users & Media/Fallback]
Issue: [Cards missing/Entity errors/Complete failure/Slow loading]
Console Errors: [Copy key errors from F12]
Network Issues: [404s, timeouts, WebSocket drops]
Fix Applied: [Cache clear/Extension disable/Settings change]
Result: [Resolved/Partial/No change]
```

---
**Last Updated**: November 3, 2025
**Status**: Ready for incident testing
**Next Action**: Use during next rendering failure
"""

    checklist_path = "S:/AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/browser_diagnostics_checklist.md"
    
    try:
        with open(checklist_path, 'w', encoding='utf-8') as f:
            f.write(checklist_content)
        return f"✅ Browser diagnostics checklist created: {checklist_path}"
    except Exception as e:
        return f"❌ Error creating checklist: {e}"

def add_rendering_task_to_vscode():
    """Add browser diagnostic task to VSCode tasks.json"""
    
    task_info = """
# 📋 VSCode Task Added: Browser Rendering Diagnostics

Add this task to your `.vscode/tasks.json`:

```json
{
  "label": "Browser Rendering Diagnostics",
  "type": "shell", 
  "command": "python",
  "args": [
    "S:/AI_WORKSPACE/Scripts/browser_rendering_diagnostics.py"
  ],
  "presentation": {
    "reveal": "always",
    "panel": "shared",
    "clear": true
  },
  "problemMatcher": [],
  "group": "test"
}
```

**Usage**: Ctrl+Shift+P → "Tasks: Run Task" → "Browser Rendering Diagnostics"
"""
    
    return task_info

def main():
    """Run browser diagnostics setup"""
    print("🌐 Setting up Browser-Specific Rendering Diagnostics...")
    
    # Create checklist
    checklist_result = create_browser_test_checklist()
    print(checklist_result)
    
    # Show task info
    task_info = add_rendering_task_to_vscode()
    print(task_info)
    
    print("\n🎯 Browser Diagnostics Setup Complete!")
    print("📋 Use checklist during next rendering failure")
    print("🛡️ Test fallback dashboard: /fallback-minimal/fallback-minimal")
    
    return True

if __name__ == "__main__":
    main()