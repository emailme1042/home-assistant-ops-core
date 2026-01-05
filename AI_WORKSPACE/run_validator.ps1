# Home Assistant Configuration Validator & Manager Script
# Enhanced version with full error handling and logging
# Created: 2025-11-04

param(
    [switch]$SwapConfig,
    [switch]$ValidateOnly,
    [switch]$EntitySnapshot,
    [switch]$FullCheck
)

# Set paths - using absolute paths to avoid issues
$workspaceRoot = "S:\"
$workspace = "S:\AI_WORKSPACE"
$contextPath = "$workspace\SHARED_CONTEXT"
$outPath = "$contextPath\SESSION_ESSENTIALS"
$tokenFile = "$contextPath\.ha_token"

Write-Host "🚀 HOME ASSISTANT VALIDATOR & MANAGER" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Green
Write-Host "Workspace: $workspaceRoot" -ForegroundColor Gray
Write-Host "Output: $outPath" -ForegroundColor Gray

# Ensure output folder exists
New-Item -ItemType Directory -Force -Path $outPath | Out-Null

# Load and validate token
Write-Host "`n🔐 CHECKING AUTHENTICATION..." -ForegroundColor Yellow
if (!(Test-Path $tokenFile)) {
    Write-Host "❌ Token file not found at: $tokenFile" -ForegroundColor Red
    Write-Host "Create token file with: New-Item -Path '$tokenFile' -Value 'your_token_here'" -ForegroundColor Yellow
    exit 1
}

$token = Get-Content $tokenFile -Raw
$token = $token.Trim()

if ($token.Length -lt 50) {
    Write-Host "❌ Token appears invalid (too short: $($token.Length) chars)" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Token loaded ($($token.Substring(0,10))...)" -ForegroundColor Green

# Configuration swap function
function Swap-Configuration {
    Write-Host "`n🔄 CONFIGURATION SWAP..." -ForegroundColor Yellow
    
    $currentConfig = "$workspaceRoot\configuration.yaml"
    $backupConfig = "$workspaceRoot\configuration_BROKEN_BACKUP_2025-11-04_01-24.yaml"
    $minimalSaved = "$workspaceRoot\configuration_minimal_SAVED.yaml"
    
    if (Test-Path $backupConfig) {
        Write-Host "📁 Moving current config to: configuration_minimal_SAVED.yaml" -ForegroundColor Cyan
        Move-Item $currentConfig $minimalSaved -Force
        
        Write-Host "📁 Restoring full config from: configuration_BROKEN_BACKUP_2025-11-04_01-24.yaml" -ForegroundColor Cyan
        Move-Item $backupConfig $currentConfig -Force
        
        Write-Host "✅ Configuration swap complete!" -ForegroundColor Green
        return $true
    } else {
        Write-Host "❌ Backup config not found at: $backupConfig" -ForegroundColor Red
        return $false
    }
}

# YAML validation function
function Test-HAConfiguration {
    Write-Host "`n🔍 VALIDATING CONFIGURATION..." -ForegroundColor Yellow
    
    try {
        $configResult = Invoke-RestMethod -Uri "http://192.168.1.217:8123/api/config" -Headers @{Authorization = "Bearer $token"} -TimeoutSec 10
        
        $validation = @{
            timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            version = $configResult.version
            status = "SUCCESS"
            components = $configResult.components.Count
            unit_system = $configResult.unit_system.temperature
        }
        
        $validation | ConvertTo-Json | Out-File "$outPath\validate_yaml.json"
        Write-Host "✅ Configuration valid! HA version: $($configResult.version)" -ForegroundColor Green
        Write-Host "📊 Components loaded: $($configResult.components.Count)" -ForegroundColor Cyan
        
        return $true
    } catch {
        Write-Host "❌ Configuration validation failed: $($_.Exception.Message)" -ForegroundColor Red
        @{
            timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            status = "FAILED"
            error = $_.Exception.Message
        } | ConvertTo-Json | Out-File "$outPath\validate_yaml_error.json"
        
        return $false
    }
}

# Entity snapshot function
function Get-EntitySnapshot {
    Write-Host "`n📊 CREATING ENTITY SNAPSHOT..." -ForegroundColor Yellow
    
    try {
        $entities = Invoke-RestMethod -Uri "http://192.168.1.217:8123/api/states" -Headers @{Authorization = "Bearer $token"} -TimeoutSec 15
        
        # Count by domain
        $domainCounts = $entities | Group-Object { $_.entity_id.Split('.')[0] } | Sort-Object Count -Descending
        
        $snapshot = @{
            timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            totalEntities = $entities.Count
            domains = @{}
        }
        
        $domainCounts | ForEach-Object {
            $snapshot.domains[$_.Name] = $_.Count
        }
        
        # Save full entities
        $entities | ConvertTo-Json -Depth 3 | Out-File "$outPath\entities.json"
        
        # Save summary
        $snapshot | ConvertTo-Json | Out-File "$outPath\entity_snapshot.json"
        
        Write-Host "✅ Entity snapshot complete! Total entities: $($entities.Count)" -ForegroundColor Green
        Write-Host "📁 Files saved: entities.json, entity_snapshot.json" -ForegroundColor Cyan
        
        # Display top domains
        Write-Host "`n🏷️  TOP ENTITY DOMAINS:" -ForegroundColor Yellow
        $domainCounts | Select-Object -First 10 | ForEach-Object {
            Write-Host "  $($_.Name): $($_.Count)" -ForegroundColor White
        }
        
        return $true
    } catch {
        Write-Host "❌ Entity snapshot failed: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Restart HA function
function Restart-HomeAssistant {
    Write-Host "`n🔄 RESTARTING HOME ASSISTANT..." -ForegroundColor Yellow
    
    try {
        Invoke-RestMethod -Uri "http://192.168.1.217:8123/api/services/homeassistant/restart" -Method POST -Headers @{Authorization = "Bearer $token"} -TimeoutSec 5
        Write-Host "✅ Restart command sent!" -ForegroundColor Green
        Write-Host "⏳ Wait 2-3 minutes for full startup..." -ForegroundColor Yellow
        return $true
    } catch {
        Write-Host "❌ Restart failed: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "💡 Try manual restart via web UI or power cycle" -ForegroundColor Yellow
        return $false
    }
}

# Main execution logic
Write-Host "`n🎯 EXECUTION MODE:" -ForegroundColor Yellow

if ($SwapConfig) {
    $swapSuccess = Swap-Configuration
    if ($swapSuccess) {
        Write-Host "🔄 Restarting HA to load new configuration..." -ForegroundColor Yellow
        Restart-HomeAssistant
    }
} elseif ($ValidateOnly) {
    Test-HAConfiguration
} elseif ($EntitySnapshot) {
    Get-EntitySnapshot
} elseif ($FullCheck) {
    Write-Host "🔍 Running full system check..." -ForegroundColor Cyan
    $validationSuccess = Test-HAConfiguration
    if ($validationSuccess) {
        Get-EntitySnapshot
    }
} else {
    # Default: run validation and entity snapshot
    Write-Host "🔍 Running default validation + entity snapshot..." -ForegroundColor Cyan
    $validationSuccess = Test-HAConfiguration
    if ($validationSuccess) {
        Get-EntitySnapshot
    }
}

Write-Host "`n🎉 VALIDATOR SCRIPT COMPLETE!" -ForegroundColor Green
Write-Host "📁 Results saved to: $outPath" -ForegroundColor Cyan
Write-Host "`n🎯 NEXT STEPS:" -ForegroundColor Yellow
Write-Host "1. Check http://192.168.1.217:8123 for web interface" -ForegroundColor White
Write-Host "2. Review validation results in SESSION_ESSENTIALS folder" -ForegroundColor White
Write-Host "3. If issues persist, try: .\run_validator.ps1 -SwapConfig" -ForegroundColor White