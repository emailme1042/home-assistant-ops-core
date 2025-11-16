# One-Click Boiler Stats Backup to Dropbox
# Run this script manually: .\backup_boiler_stats.ps1

param(
    [switch]$Weekly,
    [switch]$History
)

$timestamp = Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'

if ($Weekly) {
    $filename = "boiler_weekly_$(Get-Date -Format 'yyyy-MM-dd').json"
    Write-Host "📊 Creating weekly boiler summary..." -ForegroundColor Cyan

    # Create weekly summary (you can customize this data)
    $weeklyStats = @{
        week_of = (Get-Date).AddDays(-7).ToString('yyyy-MM-dd')
        summary = @{
            avg_daily_runtime = 4.1
            total_heating_hours = 19.2
            total_hot_water_hours = 8.4
            efficiency_rating = 'Good'
            recommendations = @('Monitor vibration patterns', 'Consider flow sensor upgrade')
        }
        daily_breakdown = @(
            @{date='2025-11-05'; heating=3.2; hot_water=1.1; total=4.3},
            @{date='2025-11-06'; heating=2.8; hot_water=1.4; total=4.2},
            @{date='2025-11-07'; heating=3.5; hot_water=0.9; total=4.4},
            @{date='2025-11-08'; heating=2.9; hot_water=1.6; total=4.5},
            @{date='2025-11-09'; heating=3.2; hot_water=1.3; total=4.5},
            @{date='2025-11-10'; heating=2.1; hot_water=1.8; total=3.9},
            @{date='2025-11-11'; heating=2.8; hot_water=1.4; total=4.2}
        )
    }

    $jsonData = $weeklyStats | ConvertTo-Json -Depth 10

} elseif ($History) {
    $filename = "boiler_history_$timestamp.csv"
    Write-Host "📈 Exporting boiler history..." -ForegroundColor Cyan

    # Create CSV history (customize with real data)
    $csvData = @"
Date,Total Runtime (h),Heating Runtime (h),Hot Water Runtime (h),Usage Type,Efficiency
2025-11-05,4.3,3.2,1.1,Heating,Good
2025-11-06,4.2,2.8,1.4,Mixed,Good
2025-11-07,4.4,3.5,0.9,Heating,Excellent
2025-11-08,4.5,2.9,1.6,Mixed,Good
2025-11-09,4.5,3.2,1.3,Heating,Good
2025-11-10,3.9,2.1,1.8,Mixed,Good
2025-11-11,4.2,2.8,1.4,Heating,Good
"@

    $jsonData = $csvData

} else {
    $filename = "boiler_stats_$timestamp.json"
    Write-Host "📊 Backing up current boiler stats..." -ForegroundColor Cyan

    # Get current boiler stats (this would need to be customized with real HA API calls)
    $boilerStats = @{
        timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
        entities = @{
            'sensor.boiler_runtime_today' = @{state = '4.2'; unit = 'h'}
            'sensor.boiler_heating_runtime_today' = @{state = '2.8'; unit = 'h'}
            'sensor.boiler_hot_water_runtime_today' = @{state = '1.4'; unit = 'h'}
            'sensor.boiler_usage_type' = @{state = 'Heating'}
            'binary_sensor.heating_demand_active' = @{state = 'on'}
            'sensor.aqara_vibration_sensor_occupancy' = @{state = 'off'}
        }
        system = @{
            ha_version = '2025.10.4'
            export_time = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
            backup_type = 'manual'
        }
    }

    $jsonData = $boilerStats | ConvertTo-Json -Depth 10
}

Write-Host "📁 Filename: $filename" -ForegroundColor Yellow

# Get Dropbox token from secrets
try {
    $secretsContent = Get-Content 'secrets.yaml' -Raw
    if ($secretsContent -match 'dropbox_token:\s*["'']?([^"'']+)["'']?') {
        $dropboxToken = $matches[1]
        Write-Host "✅ Found Dropbox token" -ForegroundColor Green
    } else {
        Write-Host "❌ Dropbox token not found in secrets.yaml" -ForegroundColor Red
        Write-Host "Add this to secrets.yaml:" -ForegroundColor Yellow
        Write-Host "dropbox_token: 'your_dropbox_token_here'" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "❌ Error reading secrets.yaml: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Upload to Dropbox
try {
    $headers = @{
        'Authorization' = "Bearer $dropboxToken"
        'Content-Type' = 'application/octet-stream'
        'Dropbox-API-Arg' = "{`"path`": `"/HA_Uploads/$filename`", `"mode`": `"add`", `"autorename`": true, `"mute`": false}"
    }

    Write-Host "☁️ Uploading to Dropbox..." -ForegroundColor Cyan
    $response = Invoke-RestMethod -Uri 'https://content.dropboxapi.com/2/files/upload' -Method Post -Headers $headers -Body $jsonData

    if ($response.name) {
        Write-Host "✅ SUCCESS! File uploaded as: $($response.name)" -ForegroundColor Green
        Write-Host "📂 Location: /HA_Uploads/$($response.name)" -ForegroundColor Green
    } else {
        Write-Host "✅ File uploaded successfully!" -ForegroundColor Green
    }

} catch {
    Write-Host "❌ Upload failed: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Check your Dropbox token and internet connection" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "🎉 Boiler stats backup complete!" -ForegroundColor Green
Write-Host "💡 Tip: Run with -Weekly or -History for different backup types" -ForegroundColor Cyan