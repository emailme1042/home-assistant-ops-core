# HISTORICAL STATS TRACKER
# ========================
# Tracks last 5 snapshots with trends and component health

param(
    [switch]$ShowHistory,
    [switch]$CreateDashboard,
    [int]$KeepSnapshots = 5
)

$ErrorActionPreference = "Continue"
$OUTPUT_DIR = "AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS"
$HISTORY_DIR = "$OUTPUT_DIR\HISTORY"
$TOKEN_FILE = "AI_WORKSPACE\SHARED_CONTEXT\.ha_token"
$HA_BASE = "http://192.168.1.217:8123"

Write-Host "HISTORICAL STATS TRACKER" -ForegroundColor Cyan
Write-Host "========================" -ForegroundColor Cyan
Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""

# Ensure directories exist
@($OUTPUT_DIR, $HISTORY_DIR) | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Force -Path $_ | Out-Null
    }
}

# Load token and authenticate
if (-not (Test-Path $TOKEN_FILE)) {
    Write-Host "ERROR: Token file not found" -ForegroundColor Red
    exit 1
}

$token = Get-Content $TOKEN_FILE -Raw
$token = $token.Trim()
$headers = @{Authorization = "Bearer $token"}

try {
    $config = Invoke-RestMethod -Uri "$HA_BASE/api/config" -Headers $headers
    $entities = Invoke-RestMethod -Uri "$HA_BASE/api/states" -Headers $headers
    Write-Host "SUCCESS: Connected to HA $($config.version)" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Cannot connect to HA - $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Create current snapshot
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$snapshot = @{
    timestamp = $timestamp
    datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    ha_version = $config.version
    total_components = $config.components.Count
    total_entities = $entities.Count
    domains = @{}
    critical_health = @{}
    include_files = @{}
    entity_health = @{}
}

# Group entities by domain
$domainGroups = $entities | Group-Object { $_.entity_id.Split('.')[0] }
foreach ($group in $domainGroups) {
    $snapshot.domains[$group.Name] = $group.Count
}

# Critical component health
$snapshot.critical_health = @{
    automations_total = ($entities | Where-Object { $_.entity_id -like "automation.*" }).Count
    automations_unavailable = ($entities | Where-Object { $_.entity_id -like "automation.*" -and $_.state -eq "unavailable" }).Count
    scripts_total = ($entities | Where-Object { $_.entity_id -like "script.*" }).Count
    scripts_unavailable = ($entities | Where-Object { $_.entity_id -like "script.*" -and $_.state -eq "unavailable" }).Count
    sensors_total = ($entities | Where-Object { $_.entity_id -like "sensor.*" }).Count
    sensors_unavailable = ($entities | Where-Object { $_.entity_id -like "sensor.*" -and $_.state -eq "unavailable" }).Count
    lights_total = ($entities | Where-Object { $_.entity_id -like "light.*" }).Count
    lights_unavailable = ($entities | Where-Object { $_.entity_id -like "light.*" -and $_.state -eq "unavailable" }).Count
    switches_total = ($entities | Where-Object { $_.entity_id -like "switch.*" }).Count
    switches_unavailable = ($entities | Where-Object { $_.entity_id -like "switch.*" -and $_.state -eq "unavailable" }).Count
}

# Include files count
$includeDirs = @(
    "includes/automations",
    "includes/scripts", 
    "includes/input_booleans",
    "includes/templates",
    "includes/sensors",
    "dashboards"
)

foreach ($dir in $includeDirs) {
    $dirName = Split-Path $dir -Leaf
    if (Test-Path $dir) {
        $snapshot.include_files[$dirName] = (Get-ChildItem $dir -File -Recurse).Count
    } else {
        $snapshot.include_files[$dirName] = 0
    }
}

# Overall entity health percentage
$totalEntities = $entities.Count
$unavailableEntities = ($entities | Where-Object { $_.state -eq "unavailable" }).Count
$snapshot.entity_health = @{
    total = $totalEntities
    unavailable = $unavailableEntities
    available = $totalEntities - $unavailableEntities
    health_percentage = if ($totalEntities -gt 0) { [math]::Round((($totalEntities - $unavailableEntities) / $totalEntities) * 100, 1) } else { 0 }
}

# Save current snapshot
$snapshotFile = "$HISTORY_DIR\snapshot_$timestamp.json"
$snapshot | ConvertTo-Json -Depth 10 | Out-File $snapshotFile -Encoding UTF8

Write-Host "CURRENT SNAPSHOT SAVED: $snapshotFile" -ForegroundColor Green

# Clean up old snapshots (keep only last N)
$allSnapshots = Get-ChildItem "$HISTORY_DIR\snapshot_*.json" | Sort-Object Name -Descending
if ($allSnapshots.Count -gt $KeepSnapshots) {
    $toDelete = $allSnapshots | Select-Object -Skip $KeepSnapshots
    foreach ($file in $toDelete) {
        Remove-Item $file.FullName -Force
        Write-Host "Removed old snapshot: $($file.Name)" -ForegroundColor Yellow
    }
}

# Show history if requested
if ($ShowHistory) {
    Write-Host ""
    Write-Host "HISTORICAL ANALYSIS (Last 5 Snapshots)" -ForegroundColor Cyan
    Write-Host "=======================================" -ForegroundColor Cyan
    
    $recentSnapshots = Get-ChildItem "$HISTORY_DIR\snapshot_*.json" | Sort-Object Name -Descending | Select-Object -First 5
    $historyData = @()
    
    foreach ($file in $recentSnapshots) {
        try {
            $data = Get-Content $file.FullName -Raw | ConvertFrom-Json
            $historyData += $data
        } catch {
            Write-Host "Warning: Could not parse $($file.Name)" -ForegroundColor Yellow
        }
    }
    
    if ($historyData.Count -gt 0) {
        # Create comparison table
        Write-Host ""
        Write-Host "ENTITY TRENDS (Most Recent First):" -ForegroundColor White
        Write-Host "Timestamp               | Total | Auto | Script | Sensor | Switch | Light | Health%" -ForegroundColor Gray
        Write-Host "------------------------|-------|------|--------|--------|--------|-------|--------" -ForegroundColor Gray
        
        foreach ($snap in $historyData) {
            $line = "{0,-23} | {1,5} | {2,4} | {3,6} | {4,6} | {5,6} | {6,5} | {7,6}%" -f `
                $snap.datetime,
                $snap.total_entities,
                $snap.critical_health.automations_total,
                $snap.critical_health.scripts_total,
                $snap.critical_health.sensors_total,
                $snap.critical_health.switches_total,
                $snap.critical_health.lights_total,
                $snap.entity_health.health_percentage
            Write-Host $line -ForegroundColor White
        }
        
        Write-Host ""
        Write-Host "INCLUDE FILE TRENDS:" -ForegroundColor White
        Write-Host "Timestamp               | Auto | Script | Sensor | Template | Dashboard" -ForegroundColor Gray
        Write-Host "------------------------|------|--------|--------|----------|----------" -ForegroundColor Gray
        
        foreach ($snap in $historyData) {
            $line = "{0,-23} | {1,4} | {2,6} | {3,6} | {4,8} | {5,9}" -f `
                $snap.datetime,
                $snap.include_files.automations,
                $snap.include_files.scripts,
                $snap.include_files.sensors,
                $snap.include_files.templates,
                $snap.include_files.dashboards
            Write-Host $line -ForegroundColor White
        }
        
        # Calculate trends
        if ($historyData.Count -ge 2) {
            $latest = $historyData[0]
            $previous = $historyData[1]
            
            Write-Host ""
            Write-Host "TREND ANALYSIS (Latest vs Previous):" -ForegroundColor Yellow
            
            $trends = @{
                "Total Entities" = $latest.total_entities - $previous.total_entities
                "Automations" = $latest.critical_health.automations_total - $previous.critical_health.automations_total
                "Scripts" = $latest.critical_health.scripts_total - $previous.critical_health.scripts_total
                "Sensors" = $latest.critical_health.sensors_total - $previous.critical_health.sensors_total
                "Health %" = $latest.entity_health.health_percentage - $previous.entity_health.health_percentage
            }
            
            foreach ($trend in $trends.GetEnumerator()) {
                $arrow = if ($trend.Value -gt 0) { "↗️ +" } elseif ($trend.Value -lt 0) { "↘️ " } else { "➡️  " }
                $color = if ($trend.Value -gt 0) { "Green" } elseif ($trend.Value -lt 0) { "Red" } else { "Gray" }
                Write-Host "$($trend.Key): $arrow$($trend.Value)" -ForegroundColor $color
            }
        }
    }
}

# Create dashboard if requested
if ($CreateDashboard) {
    Write-Host ""
    Write-Host "CREATING HISTORICAL STATS DASHBOARD..." -ForegroundColor Yellow
    
    $dashboardYaml = @"
title: "📊 Historical System Stats"
path: historical-system-stats
icon: mdi:chart-timeline-variant
cards:
  - type: markdown
    content: |
      # 📊 Historical System Statistics
      **Last Updated**: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
      **Snapshots Tracked**: Last 5 system states
      
  - type: entities
    title: "Current System Health"
    entities:
      - entity: sensor.ha_system_entities_total
        name: "Total Entities"
      - entity: sensor.ha_system_health_percentage
        name: "System Health %"
      - entity: sensor.ha_system_automations_working
        name: "Working Automations"
      - entity: sensor.ha_system_scripts_working
        name: "Working Scripts"
      - entity: sensor.ha_system_unavailable_entities
        name: "Unavailable Entities"
        
  - type: history-graph
    title: "Entity Count Trends (24h)"
    entities:
      - sensor.ha_system_entities_total
      - sensor.ha_system_automations_working
      - sensor.ha_system_scripts_working
    hours_to_show: 24
    refresh_interval: 300
    
  - type: entities
    title: "Include File Counts"
    entities:
      - entity: sensor.ha_include_automations_count
        name: "Automation Files"
      - entity: sensor.ha_include_scripts_count
        name: "Script Files"
      - entity: sensor.ha_include_sensors_count
        name: "Sensor Files"
      - entity: sensor.ha_include_templates_count
        name: "Template Files"
      - entity: sensor.ha_include_dashboards_count
        name: "Dashboard Files"
        
  - type: horizontal-stack
    cards:
      - type: button
        name: "Refresh Stats"
        icon: mdi:refresh
        tap_action:
          action: call-service
          service: shell_command.update_historical_stats
      - type: button
        name: "Health Check"
        icon: mdi:heart-pulse
        tap_action:
          action: call-service
          service: script.system_health_check
      - type: button
        name: "Export Report"
        icon: mdi:file-export
        tap_action:
          action: call-service
          service: shell_command.export_system_report
"@
    
    $dashboardYaml | Out-File "dashboards/historical_system_stats.yaml" -Encoding UTF8
    Write-Host "SUCCESS: Dashboard created at dashboards/historical_system_stats.yaml" -ForegroundColor Green
}

Write-Host ""
Write-Host "HISTORICAL STATS TRACKER COMPLETE!" -ForegroundColor Cyan
Write-Host "Files saved to: $HISTORY_DIR" -ForegroundColor Gray
Write-Host ""
Write-Host "USAGE:" -ForegroundColor Yellow
Write-Host "  -ShowHistory     Show last 5 snapshots with trends" -ForegroundColor Gray
Write-Host "  -CreateDashboard Create HA dashboard for stats" -ForegroundColor Gray
Write-Host "  -KeepSnapshots N Keep N historical snapshots (default: 5)" -ForegroundColor Gray

$true