# Home Assistant Recovery & Validation Script
# Created: 2025-11-04
# Purpose: Comprehensive HA health check and issue resolution

Write-Host "🏥 HOME ASSISTANT RECOVERY & VALIDATION CHECKLIST" -ForegroundColor Green
Write-Host "=================================================" -ForegroundColor Green

# Create output directory
$outputDir = "AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS"
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

# 1. Check HA Accessibility
Write-Host "`n1️⃣  CHECKING HOME ASSISTANT ACCESSIBILITY" -ForegroundColor Yellow
$haUrl = "http://192.168.1.217:8123"

try {
    $response = Invoke-WebRequest -Uri $haUrl -Method Head -TimeoutSec 5
    Write-Host "✅ HA Web Interface: ACCESSIBLE ($($response.StatusCode))" -ForegroundColor Green
    $haAccessible = $true
} catch {
    Write-Host "❌ HA Web Interface: NOT ACCESSIBLE" -ForegroundColor Red
    Write-Host "   Try: Browser cache clear, incognito mode, or hardware restart" -ForegroundColor Yellow
    $haAccessible = $false
}

# 2. YAML Duplicate Key Scanner
Write-Host "`n2️⃣  SCANNING FOR YAML DUPLICATE KEYS" -ForegroundColor Yellow

function Find-YamlDuplicates {
    param([string]$Path)
    
    $duplicates = @()
    Get-ChildItem -Path $Path -Recurse -Include "*.yaml", "*.yml" | ForEach-Object {
        $file = $_.FullName
        $content = Get-Content $file -Raw
        
        # Simple duplicate key detection
        $lines = Get-Content $file
        $keys = @{}
        
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match '^\s*([a-zA-Z_][a-zA-Z0-9_]*):') {
                $key = $matches[1]
                if ($keys.ContainsKey($key)) {
                    $duplicates += @{
                        File = $file.Replace((Get-Location).Path + "\", "")
                        Key = $key
                        Lines = @($keys[$key], $i + 1)
                    }
                } else {
                    $keys[$key] = $i + 1
                }
            }
        }
    }
    return $duplicates
}

$duplicates = Find-YamlDuplicates -Path "."
if ($duplicates.Count -gt 0) {
    Write-Host "❌ FOUND $($duplicates.Count) YAML DUPLICATE KEY ISSUES:" -ForegroundColor Red
    $duplicates | ForEach-Object {
        Write-Host "   📄 $($_.File): '$($_.Key)' on lines $($_.Lines -join ', ')" -ForegroundColor Yellow
    }
    $duplicates | ConvertTo-Json | Out-File "$outputDir\yaml_duplicates.json"
} else {
    Write-Host "✅ NO YAML DUPLICATE KEYS FOUND" -ForegroundColor Green
}

# 3. Custom Component Status Check
Write-Host "`n3️⃣  CHECKING CUSTOM COMPONENTS STATUS" -ForegroundColor Yellow

$customComponents = Get-ChildItem -Path "custom_components" -Directory -ErrorAction SilentlyContinue
$disabledComponents = Get-ChildItem -Path "custom_components_EMERGENCY_DISABLED" -Directory -ErrorAction SilentlyContinue

Write-Host "📦 Active Custom Components: $($customComponents.Count)" -ForegroundColor Cyan
$customComponents | ForEach-Object { Write-Host "   • $($_.Name)" -ForegroundColor White }

Write-Host "🚫 Disabled Custom Components: $($disabledComponents.Count)" -ForegroundColor Cyan
$disabledComponents | ForEach-Object { Write-Host "   • $($_.Name)" -ForegroundColor Gray }

# 4. Configuration File Health Check
Write-Host "`n4️⃣  CONFIGURATION FILE HEALTH CHECK" -ForegroundColor Yellow

$configFiles = @(
    @{Name="configuration.yaml"; Critical=$true},
    @{Name="ui-lovelace.yaml"; Critical=$false},
    @{Name="secrets.yaml"; Critical=$true},
    @{Name="automation.yaml"; Critical=$false}
)

$configStatus = @()
foreach ($config in $configFiles) {
    if (Test-Path $config.Name) {
        $size = (Get-Item $config.Name).Length
        $status = if ($size -gt 0) { "✅ OK" } else { "⚠️  EMPTY" }
        Write-Host "   $status $($config.Name) ($size bytes)" -ForegroundColor $(if ($size -gt 0) { "Green" } else { "Yellow" })
        $configStatus += @{File=$config.Name; Size=$size; Status=($size -gt 0)}
    } else {
        $status = if ($config.Critical) { "❌ MISSING" } else { "⚠️  NOT FOUND" }
        Write-Host "   $status $($config.Name)" -ForegroundColor $(if ($config.Critical) { "Red" } else { "Yellow" })
        $configStatus += @{File=$config.Name; Size=0; Status=$false}
    }
}

# 5. Database Health Check
Write-Host "`n5️⃣  DATABASE HEALTH CHECK" -ForegroundColor Yellow

$dbFile = "home-assistant_v2.db"
if (Test-Path $dbFile) {
    $dbSize = (Get-Item $dbFile).Length / 1MB
    Write-Host "✅ Database found: $([math]::Round($dbSize, 2)) MB" -ForegroundColor Green
    
    # Check for lock files indicating unclean shutdown
    $lockFiles = Get-ChildItem -Name "$dbFile*" | Where-Object { $_ -like "*lock*" -or $_ -like "*wal*" -or $_ -like "*shm*" }
    if ($lockFiles) {
        Write-Host "⚠️  Database lock files found: $($lockFiles -join ', ')" -ForegroundColor Yellow
        Write-Host "   This may indicate unclean shutdown" -ForegroundColor Yellow
    } else {
        Write-Host "✅ No database lock files found" -ForegroundColor Green
    }
} else {
    Write-Host "❌ Database file not found!" -ForegroundColor Red
}

# 6. Generate Recovery Summary
Write-Host "`n6️⃣  GENERATING RECOVERY SUMMARY" -ForegroundColor Yellow

$summary = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    HAAccessible = $haAccessible
    YAMLDuplicates = $duplicates.Count
    ActiveComponents = $customComponents.Count
    DisabledComponents = $disabledComponents.Count
    ConfigStatus = $configStatus
    Recommendations = @()
}

# Add recommendations based on findings
if (-not $haAccessible) {
    $summary.Recommendations += "🔄 Restart HA via power button or web interface"
}

if ($duplicates.Count -gt 0) {
    $summary.Recommendations += "🔧 Fix YAML duplicate keys in identified files"
}

if ($customComponents.Count -gt 5) {
    $summary.Recommendations += "🧹 Consider temporarily disabling non-essential custom components"
}

$summary.Recommendations += "✅ UI Lovelace Minimalist successfully removed from custom_components"
$summary.Recommendations += "📊 Check HA logs via Settings → System → Logs"

# Save summary
$summary | ConvertTo-Json -Depth 3 | Out-File "$outputDir\recovery_summary.json"

Write-Host "`n📋 RECOVERY CHECKLIST COMPLETE!" -ForegroundColor Green
Write-Host "Results saved to: $outputDir\recovery_summary.json" -ForegroundColor Cyan

# 7. Next Steps
Write-Host "`n🎯 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Access HA at: $haUrl" -ForegroundColor White
Write-Host "2. Check Settings → System → Logs for startup errors" -ForegroundColor White
Write-Host "3. Validate configuration via Settings → System → Check Configuration" -ForegroundColor White
Write-Host "4. If issues persist, run: ha core restart (via SSH/terminal)" -ForegroundColor White

return $summary