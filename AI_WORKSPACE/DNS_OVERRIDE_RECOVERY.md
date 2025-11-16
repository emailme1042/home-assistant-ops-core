# DNS Override Recovery Protocol — HA OS Bug #4005

## 🐛 Bug Summary

Home Assistant OS has a confirmed bug where DNS fallback is permanently locked to `true`, ignoring manual overrides despite accepting them. This causes CoreDNS to stall and fail external resolution for domains like `nabu.casa`.

**GitHub Issue**: [#4005](https://github.com/home-assistant/operating-system/issues/4005)

## ✅ Recovery Steps

### 1. Force Fallback Off (Correct Syntax)

```bash
ha dns options --fallback=false
ha dns restart
```

**Important**: Use `--fallback=false` (not `--no-fallback`). The value must be passed explicitly.

**If restart fails with "Can't restart CoreDNS plugin"**:

### 2. Supervisor Restart (Required for Bug #4005)

```bash
ha supervisor restart
```

This forces all supervisor services including DNS to reload, applying the fallback=false change.

**If supervisor restart fails with "system is not running - startup"**:

### 2a. Wait for Startup Completion
Wait 5 minutes for HA to fully initialize, then retry supervisor restart.

### 2b. Force DNS Container Rebuild
```bash
ha dns update --version 2025.11.0
ha dns restart
```

### 2c. Full Supervisor Reset (Last Resort)
```bash
ha supervisor stop
sleep 30
ha supervisor start
```

### 3. Disable IPv6 (If Not Done)

```bash
ha network update end0 --ipv6-method disabled
ha host reboot
```

This prevents CoreDNS from attempting IPv6 resolution first, which fails silently.

### 3. Validation Commands

```bash
# Check DNS config
ha dns info

# Test resolution
nslookup nabu.casa
ping nabu.casa

# Check cloud logs
ha core logs | grep cloud
```

**Expected Results**:

- `fallback: false`
- `nslookup` returns IP address
- `ping` succeeds
- Cloud logs show successful connections (no timeouts)

### 4. If Still Failing

```bash
ha supervisor logs | grep dns
```

Look for:

- `CoreDNS plugin error`
- `bind: address already in use`
- `failed to start container`

## 📊 Success Metrics

- Nabu Casa cloud connectivity restored
- Alexa sync completes without timeouts
- External API calls (feelfit, etc.) succeed
- No DNS-related errors in supervisor logs

## 🛡️ Prevention

Use the `DNS_WATCHDOG.yaml` automation to monitor and auto-correct fallback drift.

## 📝 Log Entry

Executed: [Date/Time]  
Result: [Success/Failure]  
Notes: [Any issues encountered]

---
**Status**: Ready for execution  
**Priority**: Critical (blocks cloud access)  
**Estimated Time**: 5-10 minutes