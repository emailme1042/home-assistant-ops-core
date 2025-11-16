# Emergency HA Diagnostic Script
# Quick checks before restart

Write-Host "🔍 Emergency HA Diagnostic - $(Get-Date)" -ForegroundColor Yellow
Write-Host ""

# Check if HA is responding
Write-Host "1. Testing HA Web Interface..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "http://192.168.1.217:8123" -TimeoutSec 3
    Write-Host "✅ HA Web: HTTP $($response.StatusCode)" -ForegroundColor Green
} catch {
    Write-Host "❌ HA Web: Not responding ($($_.Exception.Message))" -ForegroundColor Red
}

# Check log file size
Write-Host "2. Checking Log File..." -ForegroundColor Cyan
if (Test-Path "home-assistant.log") {
    $logSize = (Get-Item "home-assistant.log").Length / 1MB
    Write-Host "📄 Log Size: $([math]::Round($logSize, 1)) MB" -ForegroundColor $(if ($logSize -gt 50) { "Red" } else { "Green" })
    
    if ($logSize -gt 50) {
        Write-Host "⚠️  Large log detected - likely causing performance issues" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ No log file found" -ForegroundColor Red
}

# Check recent critical errors
Write-Host "3. Recent Critical Errors..." -ForegroundColor Cyan
try {
    $errors = Get-Content "home-assistant.log" -Tail 100 | Select-String -Pattern "CRITICAL|FATAL" | Select-Object -Last 5
    if ($errors) {
        Write-Host "❌ Found critical errors:" -ForegroundColor Red
        $errors | ForEach-Object { Write-Host "   $($_.Line)" -ForegroundColor Red }
    } else {
        Write-Host "✅ No recent critical errors" -ForegroundColor Green
    }
} catch {
    Write-Host "❌ Could not read log errors" -ForegroundColor Red
}

# Check our template sensor files
Write-Host "4. Template Sensor Files..." -ForegroundColor Cyan
$files = @(
    "includes/sensors/multi_agent_messaging.yaml",
    "includes/input_texts/multi_agent_messaging.yaml",
    "includes/input_numbers/multi_agent_messaging.yaml"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✅ $file exists" -ForegroundColor Green
    } else {
        Write-Host "❌ $file missing" -ForegroundColor Red
    }
}

# Simple restart recommendation
Write-Host ""
Write-Host "🚀 RECOMMENDATION:" -ForegroundColor Yellow
if ($logSize -gt 50) {
    Write-Host "1. Archive large log file first" -ForegroundColor Yellow
    Write-Host "2. Then restart Home Assistant" -ForegroundColor Yellow
} else {
    Write-Host "1. Restart Home Assistant (simple restart should work)" -ForegroundColor Yellow
}

Write-Host "2. Monitor dashboard after restart" -ForegroundColor Yellow
Write-Host ""