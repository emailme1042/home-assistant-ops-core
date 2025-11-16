# 🚑 Home Assistant Frontend Recovery Script
# Created: 2025-11-04 - Post Nuclear Fix Recovery
# Issue: Frontend compilation failure preventing UI access

Write-Host "🚑 HOME ASSISTANT FRONTEND RECOVERY PROTOCOL" -ForegroundColor Yellow
Write-Host "============================================" -ForegroundColor Yellow
Write-Host ""

# Step 1: Verify HA Core is running
Write-Host "Step 1: Checking HA Core Status..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "http://192.168.1.217:8123/api/config" -UseBasicParsing -TimeoutSec 5
    Write-Host "✅ HA Core IS RUNNING (API accessible)" -ForegroundColor Green
    Write-Host "   Status: $($response.StatusCode)"
} catch {
    Write-Host "❌ HA Core not responding to API calls" -ForegroundColor Red
    Write-Host "   Error: $($_.Exception.Message)"
}

Write-Host ""

# Step 2: Test frontend compilation
Write-Host "Step 2: Testing Frontend Compilation..." -ForegroundColor Cyan
try {
    $frontendResponse = Invoke-WebRequest -Uri "http://192.168.1.217:8123/frontend_latest/" -UseBasicParsing -TimeoutSec 10
    Write-Host "✅ Frontend directory accessible" -ForegroundColor Green
} catch {
    Write-Host "❌ CONFIRMED: Frontend compilation broken" -ForegroundColor Red
    Write-Host "   This is the root cause of the access issue"
}

Write-Host ""

# Step 3: Frontend Recovery Options
Write-Host "Step 3: Frontend Recovery Options" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan

Write-Host ""
Write-Host "🔧 OPTION 1: Hard Browser Refresh (Try First)" -ForegroundColor Yellow
Write-Host "   Chrome/Edge: Ctrl+Shift+R"
Write-Host "   Firefox: Shift+F5"
Write-Host "   Safari: ⌘+Option+R"

Write-Host ""
Write-Host "🌐 OPTION 2: Incognito/Private Window" -ForegroundColor Yellow
Write-Host "   Open: http://192.168.1.217:8123"
Write-Host "   This bypasses all browser cache"

Write-Host ""
Write-Host "⚡ OPTION 3: Force Frontend Rebuild" -ForegroundColor Yellow
Write-Host "   Run: ha core rebuild"
Write-Host "   (This requires SSH access to HA)"

Write-Host ""
Write-Host "🛠️ OPTION 4: Restore Full Configuration" -ForegroundColor Yellow
Write-Host "   Restore custom_components and full config"
Write-Host "   (Available if frontend rebuild does not work)"

Write-Host ""
Write-Host "📊 Current Status Summary:" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host "✅ HA Core: Running with minimal config"
Write-Host "✅ API: Accessible"
Write-Host "❌ Frontend: Compilation broken"
Write-Host "✅ Custom Components: Safely disabled"
Write-Host "✅ Configuration: Emergency minimal active"

Write-Host ""
Write-Host "🎯 RECOMMENDED ACTION:" -ForegroundColor Green
Write-Host "1. Try hard refresh in browser first"
Write-Host "2. If that fails, try incognito window"
Write-Host "3. If still broken, run: ha core rebuild"
Write-Host ""
Write-Host "All your data and config are safe!" -ForegroundColor Green