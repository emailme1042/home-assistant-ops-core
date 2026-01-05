# Home Assistant Post-Restore Validation Script
# Checks if full configuration loaded properly

$token = Get-Content 'AI_WORKSPACE\SHARED_CONTEXT\.ha_token' -Raw
$token = $token.Trim()

Write-Host "🔍 POST-RESTORE VALIDATION CHECK" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green

try {
    # Test API connectivity
    $config = Invoke-RestMethod -Uri 'http://192.168.1.217:8123/api/config' -Headers @{Authorization = "Bearer $token"}
    Write-Host "✅ API: Connected to HA version $($config.version)" -ForegroundColor Green
    
    # Get all entities  
    $entities = Invoke-RestMethod -Uri 'http://192.168.1.217:8123/api/states' -Headers @{Authorization = "Bearer $token"}
    $totalEntities = $entities.Count
    
    # Count by domain
    $automations = ($entities | Where-Object { $_.entity_id -like 'automation.*' }).Count
    $inputBooleans = ($entities | Where-Object { $_.entity_id -like 'input_boolean.*' }).Count
    $sensors = ($entities | Where-Object { $_.entity_id -like 'sensor.*' }).Count
    $scripts = ($entities | Where-Object { $_.entity_id -like 'script.*' }).Count
    $inputNumbers = ($entities | Where-Object { $_.entity_id -like 'input_number.*' }).Count
    
    Write-Host "`n📊 ENTITY COUNTS:" -ForegroundColor Yellow
    Write-Host "  Total Entities: $totalEntities" -ForegroundColor Cyan
    Write-Host "  Automations: $automations" -ForegroundColor White
    Write-Host "  Input Booleans: $inputBooleans" -ForegroundColor White
    Write-Host "  Sensors: $sensors" -ForegroundColor White
    Write-Host "  Scripts: $scripts" -ForegroundColor White
    Write-Host "  Input Numbers: $inputNumbers" -ForegroundColor White
    
    # Check for key AI entities
    $aiEntities = $entities | Where-Object { $_.entity_id -like '*gpt*' -or $_.entity_id -like '*ai*' -or $_.entity_id -like '*copilot*' }
    Write-Host "`n🤖 AI ENTITIES: $($aiEntities.Count)" -ForegroundColor Yellow
    $aiEntities | ForEach-Object { Write-Host "  - $($_.entity_id)" -ForegroundColor Gray }
    
    # Save results
    $results = @{
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        version = $config.version
        totalEntities = $totalEntities
        automations = $automations
        inputBooleans = $inputBooleans
        sensors = $sensors
        scripts = $scripts
        inputNumbers = $inputNumbers
        aiEntities = $aiEntities.Count
        status = "SUCCESS"
    }
    
    $results | ConvertTo-Json | Out-File 'AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\post_restore_validation.json'
    
    Write-Host "`n🎉 VALIDATION RESULT: " -NoNewline -ForegroundColor Green
    if ($automations -gt 0 -and $inputBooleans -gt 0 -and $sensors -gt 0) {
        Write-Host "FULL CONFIGURATION LOADED!" -ForegroundColor Green
        Write-Host "✅ Automations, helpers, and sensors are all present" -ForegroundColor Green
    } else {
        Write-Host "PARTIAL CONFIGURATION LOADED" -ForegroundColor Yellow
        Write-Host "⚠️  Some includes may not have loaded properly" -ForegroundColor Yellow
    }
    
} catch {
    Write-Host "❌ VALIDATION FAILED: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Check token and HA accessibility" -ForegroundColor Yellow
}

Write-Host "`n🎯 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Open http://192.168.1.217:8123 in browser" -ForegroundColor White
Write-Host "2. Check Settings → Automations (should show automations)" -ForegroundColor White
Write-Host "3. Check Settings → Helpers (should show input_boolean entities)" -ForegroundColor White
Write-Host "4. Verify dashboards are loading properly" -ForegroundColor White