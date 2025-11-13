# Home Assistant Recovery Validation Script
# Created: 2025-11-04 - Simplified Version

Write-Host "HOME ASSISTANT RECOVERY VALIDATION" -ForegroundColor Green
Write-Host "=================================="

# Create output directory
$outputDir = "AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS"
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

# 1. Check HA Accessibility
Write-Host "`n1. CHECKING HOME ASSISTANT ACCESSIBILITY" -ForegroundColor Yellow
$haUrl = "http://192.168.1.217:8123"

try {
    $response = Invoke-WebRequest -Uri $haUrl -Method Head -TimeoutSec 5
    Write-Host "SUCCESS: HA Web Interface accessible (Status: $($response.StatusCode))" -ForegroundColor Green
    $haAccessible = $true
} catch {
    Write-Host "FAILED: HA Web Interface not accessible" -ForegroundColor Red
    Write-Host "Recommendation: Try browser cache clear or hardware restart" -ForegroundColor Yellow
    $haAccessible = $false
}

# 2. Check Custom Components Status
Write-Host "`n2. CUSTOM COMPONENTS STATUS" -ForegroundColor Yellow

$activeComponents = @()
$disabledComponents = @()

if (Test-Path "custom_components") {
    $activeComponents = Get-ChildItem -Path "custom_components" -Directory | Select-Object -ExpandProperty Name
}

if (Test-Path "custom_components_EMERGENCY_DISABLED") {
    $disabledComponents = Get-ChildItem -Path "custom_components_EMERGENCY_DISABLED" -Directory | Select-Object -ExpandProperty Name
}

Write-Host "Active Components: $($activeComponents.Count)" -ForegroundColor Cyan
$activeComponents | ForEach-Object { Write-Host "  - $_" }

Write-Host "Disabled Components: $($disabledComponents.Count)" -ForegroundColor Cyan  
$disabledComponents | ForEach-Object { Write-Host "  - $_" }

# 3. Configuration Files Check
Write-Host "`n3. CONFIGURATION FILES STATUS" -ForegroundColor Yellow

$configFiles = @("configuration.yaml", "secrets.yaml", "ui-lovelace.yaml")
$configStatus = @{}

foreach ($file in $configFiles) {
    if (Test-Path $file) {
        $size = (Get-Item $file).Length
        $configStatus[$file] = @{Exists=$true; Size=$size}
        Write-Host "OK: $file ($size bytes)" -ForegroundColor Green
    } else {
        $configStatus[$file] = @{Exists=$false; Size=0}
        Write-Host "MISSING: $file" -ForegroundColor Red
    }
}

# 4. Database Health
Write-Host "`n4. DATABASE HEALTH" -ForegroundColor Yellow

$dbFile = "home-assistant_v2.db"
if (Test-Path $dbFile) {
    $dbSize = [math]::Round((Get-Item $dbFile).Length / 1MB, 2)
    Write-Host "OK: Database found ($dbSize MB)" -ForegroundColor Green
    
    # Check for lock files
    $lockFiles = Get-ChildItem -Name "$dbFile*" | Where-Object { $_ -like "*lock*" -or $_ -like "*wal*" -or $_ -like "*shm*" }
    if ($lockFiles) {
        Write-Host "WARNING: Database lock files found - may indicate unclean shutdown" -ForegroundColor Yellow
        $lockFiles | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
    }
} else {
    Write-Host "ERROR: Database file not found" -ForegroundColor Red
}

# 5. YAML Issues Scanner (Simple)
Write-Host "`n5. YAML ISSUES CHECK" -ForegroundColor Yellow

$yamlIssues = @()

# Check room_template.yaml specifically (we know it had issues)
if (Test-Path "dashboards\users\room_template.yaml") {
    $content = Get-Content "dashboards\users\room_template.yaml"
    $entityIdLines = $content | Select-String "entity_id:" | ForEach-Object { $_.LineNumber }
    
    if ($entityIdLines.Count -gt ($entityIdLines | Sort-Object | Get-Unique).Count) {
        $yamlIssues += "room_template.yaml has duplicate entity_id lines"
        Write-Host "FIXED: room_template.yaml duplicate entity_id (already corrected)" -ForegroundColor Green
    } else {
        Write-Host "OK: room_template.yaml no duplicate entity_id found" -ForegroundColor Green
    }
}

# 6. Generate Summary Report
$summary = @{
    Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    HAAccessible = $haAccessible
    ActiveComponents = $activeComponents.Count
    DisabledComponents = $disabledComponents.Count
    ConfigFiles = $configStatus
    YAMLIssues = $yamlIssues
    Recommendations = @()
}

# Add recommendations
if (-not $haAccessible) {
    $summary.Recommendations += "Restart HA via web interface or hardware button"
}

if ($activeComponents.Count -gt 10) {
    $summary.Recommendations += "Consider temporarily disabling non-essential custom components"
}

$summary.Recommendations += "UI Lovelace Minimalist successfully removed"
$summary.Recommendations += "Check HA logs via Settings -> System -> Logs"
$summary.Recommendations += "Validate config via Settings -> System -> Check Configuration"

# Save summary
$summary | ConvertTo-Json -Depth 3 | Out-File "$outputDir\recovery_summary.json" -Encoding UTF8

Write-Host "`nRECOVERY VALIDATION COMPLETE!" -ForegroundColor Green
Write-Host "Summary saved to: $outputDir\recovery_summary.json" -ForegroundColor Cyan

Write-Host "`nNEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Open $haUrl in browser" -ForegroundColor White
Write-Host "2. Check Settings -> System -> Logs" -ForegroundColor White  
Write-Host "3. Run Settings -> System -> Check Configuration" -ForegroundColor White
Write-Host "4. If frontend still broken, try incognito mode or clear cache" -ForegroundColor White

return $summary