# POST-RESTORE VERIFICATION SCRIPT
# =====================================
# Comprehensive validation after configuration restoration

param(
    [switch]$ReloadServices,
    [switch]$CreateDashboard,
    [switch]$FullReport
)

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"

# Configuration
$OUTPUT_DIR = "AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS"
$TOKEN_FILE = "AI_WORKSPACE\SHARED_CONTEXT\.ha_token"
$HA_BASE = "http://192.168.1.217:8123"

Write-Host "POST-RESTORE VERIFICATION SCRIPT" -ForegroundColor Cyan
Write-Host "=================================" -ForegroundColor Cyan
Write-Host "Workspace: $(Get-Location)" -ForegroundColor Gray
Write-Host "Output: $OUTPUT_DIR" -ForegroundColor Gray
Write-Host ""

# Ensure output directory exists
if (-not (Test-Path $OUTPUT_DIR)) {
    New-Item -ItemType Directory -Force -Path $OUTPUT_DIR | Out-Null
}

# Load token
if (-not (Test-Path $TOKEN_FILE)) {
    Write-Host "ERROR: Token file not found at $TOKEN_FILE" -ForegroundColor Red
    exit 1
}

$token = Get-Content $TOKEN_FILE -Raw
$token = $token.Trim()
$headers = @{Authorization = "Bearer $token"}

Write-Host "CHECKING AUTHENTICATION..." -ForegroundColor Yellow
try {
    $config = Invoke-RestMethod -Uri "$HA_BASE/api/config" -Headers $headers
    Write-Host "SUCCESS: Token authenticated" -ForegroundColor Green
    Write-Host "HA Version: $($config.version)" -ForegroundColor Gray
    Write-Host "Components: $($config.components.Count)" -ForegroundColor Gray
} catch {
    Write-Host "ERROR: Authentication failed - $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# 1. FRESH ENTITY SNAPSHOT
Write-Host ""
Write-Host "1. CREATING FRESH ENTITY SNAPSHOT..." -ForegroundColor Yellow
try {
    $entities = Invoke-RestMethod -Uri "$HA_BASE/api/states" -Headers $headers
    
    # Save full entities JSON
    $entities | ConvertTo-Json -Depth 10 | Out-File "$OUTPUT_DIR\entities_fresh.json" -Encoding UTF8
    
    # Create entity analysis
    $entityAnalysis = @{
        total_entities = $entities.Count
        timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        by_domain = @{}
        critical_counts = @{}
    }
    
    # Group by domain
    $domainGroups = $entities | Group-Object { $_.entity_id.Split('.')[0] }
    foreach ($group in $domainGroups) {
        $entityAnalysis.by_domain[$group.Name] = $group.Count
    }
    
    # Critical component counts
    $entityAnalysis.critical_counts = @{
        automations = ($entities | Where-Object { $_.entity_id -like "automation.*" }).Count
        scripts = ($entities | Where-Object { $_.entity_id -like "script.*" }).Count
        input_booleans = ($entities | Where-Object { $_.entity_id -like "input_boolean.*" }).Count
        input_numbers = ($entities | Where-Object { $_.entity_id -like "input_number.*" }).Count
        input_selects = ($entities | Where-Object { $_.entity_id -like "input_select.*" }).Count
        input_texts = ($entities | Where-Object { $_.entity_id -like "input_text.*" }).Count
        sensors = ($entities | Where-Object { $_.entity_id -like "sensor.*" }).Count
        binary_sensors = ($entities | Where-Object { $_.entity_id -like "binary_sensor.*" }).Count
        switches = ($entities | Where-Object { $_.entity_id -like "switch.*" }).Count
        lights = ($entities | Where-Object { $_.entity_id -like "light.*" }).Count
    }
    
    $entityAnalysis | ConvertTo-Json -Depth 5 | Out-File "$OUTPUT_DIR\entity_analysis.json" -Encoding UTF8
    
    Write-Host "SUCCESS: Entity snapshot complete! Total entities: $($entities.Count)" -ForegroundColor Green
    Write-Host "Critical counts:" -ForegroundColor Gray
    foreach ($key in $entityAnalysis.critical_counts.Keys) {
        Write-Host "  $key`: $($entityAnalysis.critical_counts[$key])" -ForegroundColor Gray
    }
    
} catch {
    Write-Host "ERROR: Entity snapshot failed - $($_.Exception.Message)" -ForegroundColor Red
}

# 2. CONFIGURATION INCLUDE VERIFICATION
Write-Host ""
Write-Host "2. VERIFYING CONFIGURATION INCLUDES..." -ForegroundColor Yellow

$configChecks = @{
    "automation: !include_dir_merge_list includes/automations/" = $false
    "script: !include_dir_merge_named includes/scripts/" = $false
    "input_boolean: !include_dir_merge_named includes/input_booleans/" = $false
    "template: !include_dir_merge_list includes/templates/" = $false
    "sensor: !include_dir_merge_list includes/sensors/" = $false
}

if (Test-Path "configuration.yaml") {
    $configContent = Get-Content "configuration.yaml" -Raw
    foreach ($check in $configChecks.Keys) {
        if ($configContent -match [regex]::Escape($check)) {
            $configChecks[$check] = $true
            Write-Host "  FOUND: $check" -ForegroundColor Green
        } else {
            Write-Host "  MISSING: $check" -ForegroundColor Red
        }
    }
} else {
    Write-Host "ERROR: configuration.yaml not found" -ForegroundColor Red
}

# 3. INCLUDE DIRECTORY VERIFICATION
Write-Host ""
Write-Host "3. CHECKING INCLUDE DIRECTORIES..." -ForegroundColor Yellow

$includeDirs = @(
    "includes/automations",
    "includes/scripts", 
    "includes/input_booleans",
    "includes/templates",
    "includes/sensors",
    "dashboards"
)

foreach ($dir in $includeDirs) {
    if (Test-Path $dir) {
        $fileCount = (Get-ChildItem $dir -File -Recurse).Count
        Write-Host "  $dir`: $fileCount files" -ForegroundColor Green
    } else {
        Write-Host "  $dir`: MISSING" -ForegroundColor Red
    }
}

# 4. RELOAD SERVICES (if requested)
if ($ReloadServices) {
    Write-Host ""
    Write-Host "4. RELOADING HA SERVICES..." -ForegroundColor Yellow
    
    $reloadEndpoints = @(
        "automations",
        "scripts", 
        "template",
        "input_boolean",
        "lovelace"
    )
    
    foreach ($endpoint in $reloadEndpoints) {
        try {
            $response = Invoke-RestMethod -Uri "$HA_BASE/api/services/homeassistant/reload_config_entry" -Method POST -Headers $headers -Body (@{entry_id = $endpoint} | ConvertTo-Json) -ContentType "application/json"
            Write-Host "  Reloaded: $endpoint" -ForegroundColor Green
        } catch {
            Write-Host "  Failed to reload: $endpoint - $($_.Exception.Message)" -ForegroundColor Yellow
        }
    }
}

# 5. CREATE POST-RESTORE DASHBOARD (if requested)
if ($CreateDashboard) {
    Write-Host ""
    Write-Host "5. CREATING POST-RESTORE DASHBOARD..." -ForegroundColor Yellow
    
    $dashboardYaml = @"
title: "Post-Restore System Status"
path: post-restore-status
icon: mdi:check-circle
cards:
  - type: markdown
    content: |
      # System Restoration Status
      **Timestamp**: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
      **Total Entities**: $($entities.Count)
      
      ## Critical Components
      - **Automations**: $($entityAnalysis.critical_counts.automations)
      - **Scripts**: $($entityAnalysis.critical_counts.scripts)
      - **Input Helpers**: $($entityAnalysis.critical_counts.input_booleans + $entityAnalysis.critical_counts.input_numbers + $entityAnalysis.critical_counts.input_selects + $entityAnalysis.critical_counts.input_texts)
      - **Sensors**: $($entityAnalysis.critical_counts.sensors)
      - **Switches**: $($entityAnalysis.critical_counts.switches)
      - **Lights**: $($entityAnalysis.critical_counts.lights)

  - type: entities
    title: "System Health Indicators"
    entities:
      - entity: sensor.home_assistant_core_cpu_percent
        name: "CPU Usage"
      - entity: sensor.home_assistant_core_memory_percent  
        name: "Memory Usage"
      - entity: sensor.uptime
        name: "System Uptime"
        
  - type: horizontal-stack
    cards:
      - type: button
        entity: script.reload_automations
        name: "Reload Automations"
        icon: mdi:refresh
      - type: button
        entity: script.reload_scripts
        name: "Reload Scripts" 
        icon: mdi:script-text
      - type: button
        entity: script.check_config
        name: "Check Config"
        icon: mdi:check-circle
"@
    
    $dashboardYaml | Out-File "dashboards/post_restore_status.yaml" -Encoding UTF8
    Write-Host "SUCCESS: Dashboard created at dashboards/post_restore_status.yaml" -ForegroundColor Green
}

# 6. GENERATE FULL REPORT (if requested)
if ($FullReport) {
    Write-Host ""
    Write-Host "6. GENERATING FULL REPORT..." -ForegroundColor Yellow
    
    $report = @"
# POST-RESTORE VERIFICATION REPORT
Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

## System Status
- HA Version: $($config.version)
- Total Components: $($config.components.Count) 
- Total Entities: $($entities.Count)

## Entity Breakdown
"@
    
    foreach ($domain in ($entityAnalysis.by_domain.Keys | Sort-Object)) {
        $report += "`n- $domain`: $($entityAnalysis.by_domain[$domain])"
    }
    
    $report += @"

## Configuration Includes Status
"@
    
    foreach ($check in $configChecks.Keys) {
        $status = if ($configChecks[$check]) { "✅ FOUND" } else { "❌ MISSING" }
        $report += "`n- $status`: $check"
    }
    
    $report += @"

## Include Directory Status
"@
    
    foreach ($dir in $includeDirs) {
        if (Test-Path $dir) {
            $fileCount = (Get-ChildItem $dir -File -Recurse).Count
            $report += "`n- ✅ $dir`: $fileCount files"
        } else {
            $report += "`n- ❌ $dir`: MISSING"
        }
    }
    
    $report | Out-File "$OUTPUT_DIR\post_restore_report.md" -Encoding UTF8
    Write-Host "SUCCESS: Full report saved to $OUTPUT_DIR\post_restore_report.md" -ForegroundColor Green
}

Write-Host ""
Write-Host "POST-RESTORE VERIFICATION COMPLETE!" -ForegroundColor Cyan
Write-Host "Results saved to: $OUTPUT_DIR" -ForegroundColor Gray
Write-Host ""
Write-Host "NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Check http://192.168.1.217:8123 for web interface" -ForegroundColor Gray
Write-Host "2. Review entity analysis in SESSION_ESSENTIALS folder" -ForegroundColor Gray  
Write-Host "3. If issues found, run with -ReloadServices flag" -ForegroundColor Gray
Write-Host "4. Use -CreateDashboard to generate system status dashboard" -ForegroundColor Gray
Write-Host "5. Use -FullReport for comprehensive analysis" -ForegroundColor Gray

# Return success
$true