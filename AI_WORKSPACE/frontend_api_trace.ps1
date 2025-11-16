# Frontend API Failure Diagnostics Script
# Run this to identify which API endpoints are failing

Write-Host "=== FRONTEND API FAILURE DIAGNOSTICS ===" -ForegroundColor Cyan
Write-Host "Testing HA API endpoints that frontend relies on..."
Write-Host ""

# Test core API endpoints that frontend uses
$endpoints = @(
    @{url="http://localhost:8123/api/"; name="Core API"},
    @{url="http://localhost:8123/api/states"; name="States API"},
    @{url="http://localhost:8123/api/config"; name="Config API"},
    @{url="http://localhost:8123/api/logbook"; name="Logbook API"},
    @{url="http://localhost:8123/api/history/period"; name="History API"},
    @{url="http://localhost:8123/api/events"; name="Events API"},
    @{url="http://localhost:8123/api/services"; name="Services API"}
)

$failedEndpoints = @()

foreach ($endpoint in $endpoints) {
    Write-Host "Testing $($endpoint.name) ($($endpoint.url))..." -NoNewline
    try {
        $response = Invoke-WebRequest -Uri $endpoint.url -TimeoutSec 15 -ErrorAction Stop
        Write-Host " ✅ Status: $($response.StatusCode)" -ForegroundColor Green
    } catch {
        Write-Host " ❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
        $failedEndpoints += $endpoint
    }
}

Write-Host ""
Write-Host "=== DIAGNOSTIC RESULTS ===" -ForegroundColor Yellow

if ($failedEndpoints.Count -eq 0) {
    Write-Host "✅ All API endpoints responding correctly" -ForegroundColor Green
    Write-Host "Issue may be frontend-side (JavaScript, cache, or rendering)"
} else {
    Write-Host "❌ $($failedEndpoints.Count) API endpoints failing:" -ForegroundColor Red
    foreach ($endpoint in $failedEndpoints) {
        Write-Host "  - $($endpoint.name): $($endpoint.url)" -ForegroundColor Red
    }
    Write-Host ""
    Write-Host "RECOMMENDATION: Backend API issues detected" -ForegroundColor Yellow
    Write-Host "Check HA logs for API-related errors"
}

Write-Host ""
Write-Host "=== NEXT STEPS ===" -ForegroundColor Cyan
Write-Host "1. If APIs are working: Focus on frontend JavaScript/cache issues"
Write-Host "2. If APIs are failing: Check HA core logs for backend problems"
Write-Host "3. Run in incognito mode to rule out cache issues"
Write-Host "4. Check DevTools Network tab for specific failing requests"