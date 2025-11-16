# Integration Health Check Script
# Tests the problematic integrations identified in the system breakdown

Write-Host "=== INTEGRATION HEALTH CHECK ===" -ForegroundColor Cyan
Write-Host "Testing integrations that were reported as failing..."
Write-Host ""

$results = @{}

# Test DSM Backup (Synology)
Write-Host "1. Testing DSM Backup (Synology)..." -NoNewline
try {
    # Test basic connectivity to DSM
    $dsmResponse = Invoke-WebRequest -Uri "http://192.168.1.203:5001/api/test" -TimeoutSec 10 -ErrorAction Stop
    Write-Host " ✅ DSM API responding" -ForegroundColor Green
    $results["DSM"] = "PASS"
} catch {
    Write-Host " ❌ DSM connection failed: $($_.Exception.Message)" -ForegroundColor Red
    $results["DSM"] = "FAIL: $($_.Exception.Message)"
}

# Test Broadlink RM4 Pro
Write-Host "2. Testing Broadlink RM4 Pro..." -NoNewline
try {
    # Check if Broadlink entity exists and is available
    $haStates = Invoke-WebRequest -Uri "http://localhost:8123/api/states" -TimeoutSec 10 | ConvertFrom-Json
    $broadlinkEntities = $haStates | Where-Object { $_.entity_id -like "remote.broadlink*" -or $_.entity_id -like "switch.broadlink*" }

    if ($broadlinkEntities) {
        $availableCount = ($broadlinkEntities | Where-Object { $_.state -ne "unavailable" }).Count
        Write-Host " ✅ Found $($broadlinkEntities.Count) Broadlink entities ($availableCount available)" -ForegroundColor Green
        $results["Broadlink"] = "PASS: $($availableCount)/$($broadlinkEntities.Count) available"
    } else {
        Write-Host " ⚠️  No Broadlink entities found" -ForegroundColor Yellow
        $results["Broadlink"] = "NO_ENTITIES"
    }
} catch {
    Write-Host " ❌ Broadlink check failed: $($_.Exception.Message)" -ForegroundColor Red
    $results["Broadlink"] = "FAIL: $($_.Exception.Message)"
}

# Test Spotify Integration
Write-Host "3. Testing Spotify Integration..." -NoNewline
try {
    $spotifyEntities = Invoke-WebRequest -Uri "http://localhost:8123/api/states" -TimeoutSec 10 | ConvertFrom-Json | Where-Object { $_.entity_id -like "media_player.spotify*" }

    if ($spotifyEntities) {
        $availableCount = ($spotifyEntities | Where-Object { $_.state -ne "unavailable" }).Count
        Write-Host " ✅ Found $($spotifyEntities.Count) Spotify entities ($availableCount available)" -ForegroundColor Green
        $results["Spotify"] = "PASS: $($availableCount)/$($spotifyEntities.Count) available"
    } else {
        Write-Host " ⚠️  No Spotify entities found" -ForegroundColor Yellow
        $results["Spotify"] = "NO_ENTITIES"
    }
} catch {
    Write-Host " ❌ Spotify check failed: $($_.Exception.Message)" -ForegroundColor Red
    $results["Spotify"] = "FAIL: $($_.Exception.Message)"
}

# Test REST Sensors
Write-Host "4. Testing REST Sensors..." -NoNewline
try {
    $restEntities = Invoke-WebRequest -Uri "http://localhost:8123/api/states" -TimeoutSec 10 | ConvertFrom-Json | Where-Object { $_.entity_id -like "sensor.rest*" -or $_.attributes.platform -eq "rest" }

    if ($restEntities) {
        $availableCount = ($restEntities | Where-Object { $_.state -ne "unavailable" -and $_.state -ne "unknown" }).Count
        Write-Host " ✅ Found $($restEntities.Count) REST entities ($availableCount available)" -ForegroundColor Green
        $results["REST"] = "PASS: $($availableCount)/$($restEntities.Count) available"
    } else {
        Write-Host " ⚠️  No REST sensor entities found" -ForegroundColor Yellow
        $results["REST"] = "NO_ENTITIES"
    }
} catch {
    Write-Host " ❌ REST sensor check failed: $($_.Exception.Message)" -ForegroundColor Red
    $results["REST"] = "FAIL: $($_.Exception.Message)"
}

# Summary
Write-Host ""
Write-Host "=== INTEGRATION HEALTH SUMMARY ===" -ForegroundColor Yellow
foreach ($integration in $results.Keys) {
    $status = $results[$integration]
    if ($status -like "PASS*") {
        Write-Host "✅ $integration : $status" -ForegroundColor Green
    } elseif ($status -like "FAIL*") {
        Write-Host "❌ $integration : $status" -ForegroundColor Red
    } else {
        Write-Host "⚠️  $integration : $status" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "=== RECOMMENDATIONS ===" -ForegroundColor Cyan
Write-Host "• If DSM fails: Check Synology NAS connectivity and API endpoints"
Write-Host "• If Broadlink fails: Power cycle RM4 Pro and check network connectivity"
Write-Host "• If Spotify fails: Reauthorize Spotify integration in HA"
Write-Host "• If REST fails: Check REST sensor configurations for malformed URLs"