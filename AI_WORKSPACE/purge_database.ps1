# Database Purge Script for HA Performance Optimization
# Run this after HA restart to reduce >7GB database size

Write-Host "Starting HA Database Purge..." -ForegroundColor Green

# HA API endpoint for recorder purge
$url = "http://localhost:8123/api/services/recorder/purge"
$headers = @{
    "Authorization" = "Bearer YOUR_LONG_LIVED_ACCESS_TOKEN"
    "Content-Type" = "application/json"
}

# Purge configuration: keep 2 days, repack database, apply filters
$body = @{
    "keep_days" = 2
    "repack" = $true
    "apply_filter" = $true
} | ConvertTo-Json

try {
    Write-Host "Sending purge request..." -ForegroundColor Yellow
    $response = Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Body $body

    Write-Host "Database purge initiated successfully!" -ForegroundColor Green
    Write-Host "Expected results:" -ForegroundColor Cyan
    Write-Host "- Database size reduction from >7GB to ~500MB-1GB"
    Write-Host "- Dashboard load times: 25s → <5s"
    Write-Host "- Entity availability: 65% → >90%"
    Write-Host "- System performance: Significantly improved"

} catch {
    Write-Host "Error executing database purge:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "Alternative: Use HA UI - Developer Tools → Services → recorder.purge" -ForegroundColor Yellow
    Write-Host "Parameters: keep_days: 2, repack: true, apply_filter: true" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Monitor progress in HA logs or wait 5-10 minutes for completion." -ForegroundColor Cyan