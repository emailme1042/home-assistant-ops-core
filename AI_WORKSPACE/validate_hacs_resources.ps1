# ✅ HACS Resource Validation Script
# Purpose: Check all declared HACS resources for existence and conflicts
# Date: 2025-11-06

Write-Host "🔍 HACS RESOURCE VALIDATION STARTING..." -ForegroundColor Green
Write-Host ""

# Extract resources from configuration.yaml
$configPath = "S:\configuration.yaml"
$wwwPath = "S:\www\community"

Write-Host "📋 EXTRACTING RESOURCES FROM CONFIGURATION.YAML..." -ForegroundColor Cyan
$resources = @()
$inResourcesSection = $false

Get-Content $configPath | ForEach-Object {
    if ($_ -match "^\s*resources:") {
        $inResourcesSection = $true
    }
    elseif ($_ -match "^\s*dashboards:" -or $_ -match "^\w+:") {
        $inResourcesSection = $false
    }
    elseif ($inResourcesSection -and $_ -match "url:\s*/local/community/(.+)") {
        $resources += $Matches[1]
    }
}

Write-Host "✅ Found $($resources.Count) declared resources" -ForegroundColor Green
Write-Host ""

# Check file existence
Write-Host "🔍 CHECKING FILE EXISTENCE..." -ForegroundColor Cyan
$missing = @()
$existing = @()

foreach ($resource in $resources) {
    $fullPath = Join-Path $wwwPath $resource
    if (Test-Path $fullPath) {
        $existing += $resource
        Write-Host "✅ $resource" -ForegroundColor Green
    } else {
        $missing += $resource
        Write-Host "❌ $resource" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "📊 VALIDATION SUMMARY:" -ForegroundColor Yellow
Write-Host "✅ Existing files: $($existing.Count)" -ForegroundColor Green
Write-Host "❌ Missing files: $($missing.Count)" -ForegroundColor Red

if ($missing.Count -gt 0) {
    Write-Host ""
    Write-Host "🚨 MISSING FILES THAT NEED ATTENTION:" -ForegroundColor Red
    foreach ($missingFile in $missing) {
        Write-Host "   $missingFile" -ForegroundColor White
    }
}

Write-Host ""
Write-Host "💡 RECOMMENDED ACTIONS:" -ForegroundColor Yellow

if ($missing.Count -gt 0) {
    Write-Host "1. Install missing HACS components via HACS frontend" -ForegroundColor White
    Write-Host "2. Remove declarations for non-existent files" -ForegroundColor White
    Write-Host "3. Check component names in HACS for correct paths" -ForegroundColor White
} else {
    Write-Host "1. Clear browser cache (Ctrl+Shift+R)" -ForegroundColor White
    Write-Host "2. Try Incognito mode for clean testing" -ForegroundColor White
    Write-Host "3. Restart Home Assistant for fresh card registration" -ForegroundColor White
}

Write-Host ""
Write-Host "🔧 NEXT STEPS FOR DEVTOOLS ERRORS:" -ForegroundColor Magenta
Write-Host "1. Open DevTools Console" -ForegroundColor White
Write-Host "2. Filter by GET to see 404 file errors" -ForegroundColor White
Write-Host "3. Filter by custom to see card registration issues" -ForegroundColor White
Write-Host "4. Use Incognito mode to test without cache" -ForegroundColor White

Write-Host ""
Write-Host "✅ VALIDATION COMPLETE!" -ForegroundColor Green