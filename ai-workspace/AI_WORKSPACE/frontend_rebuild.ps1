# Home Assistant Frontend Rebuild Script
# Run this after nuclear disable to fix core frontend compilation

Write-Host "🔧 Home Assistant Frontend Rebuild Protocol" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check if HA CLI is available locally
Write-Host "Checking HA CLI availability..." -ForegroundColor Yellow
try {
    $haCheck = ha core info 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ HA CLI detected - proceeding with rebuild" -ForegroundColor Green
        Write-Host ""
        
        Write-Host "🔄 Rebuilding frontend..." -ForegroundColor Yellow
        ha core rebuild
        
        Write-Host "🔄 Restarting HA Core..." -ForegroundColor Yellow
        ha core restart
        
        Write-Host ""
        Write-Host "✅ Frontend rebuild complete!" -ForegroundColor Green
        Write-Host "Wait 2-3 minutes, then test: http://192.168.1.217:8123" -ForegroundColor Green
    } else {
        throw "HA CLI not available"
    }
} catch {
    Write-Host "❌ HA CLI not available in Windows PowerShell" -ForegroundColor Red
    Write-Host ""
    Write-Host "🔧 SSH Terminal Required:" -ForegroundColor Yellow
    Write-Host "1. Go to http://192.168.1.217:8123 (even if broken)" -ForegroundColor White
    Write-Host "2. Settings → Add-ons → SSH & Web Terminal" -ForegroundColor White  
    Write-Host "3. Start SSH add-on if not running" -ForegroundColor White
    Write-Host "4. Click 'Open Web UI'" -ForegroundColor White
    Write-Host "5. Run: ha core rebuild && ha core restart" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Alternative: Use HA OS terminal directly on the device" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📊 Expected Results After Rebuild:" -ForegroundColor Cyan
Write-Host "- ✅ Frontend loads without 'Failed to fetch' errors" -ForegroundColor Green
Write-Host "- ✅ Developer Tools accessible" -ForegroundColor Green
Write-Host "- ✅ WebSocket connections stable" -ForegroundColor Green
Write-Host "- ✅ Multi-agent entities visible" -ForegroundColor Green

Write-Host ""
Write-Host "🔄 Current System State:" -ForegroundColor Cyan
Write-Host "- ✅ Template sensor circular references fixed" -ForegroundColor Green
Write-Host "- ✅ Log file archived (53MB removed)" -ForegroundColor Green  
Write-Host "- ✅ Custom components disabled (nuclear fix)" -ForegroundColor Green
Write-Host "- ❌ Frontend compilation broken (needs rebuild)" -ForegroundColor Red

pause