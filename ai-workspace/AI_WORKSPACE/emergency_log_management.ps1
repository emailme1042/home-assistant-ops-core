# 🧼 Home Assistant Log Management & Recovery Script
# Automates log archiving, system health checks, and crash recovery
# Usage: .\emergency_log_management.ps1 [-ArchiveOnly] [-EmergencyMode] [-HealthCheck]

param(
    [switch]$ArchiveOnly,
    [switch]$EmergencyMode,
    [switch]$HealthCheck,
    [switch]$TestSelfHealing
)

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$baseUrl = "http://192.168.1.217:8123/api"

# Get HA token
try {
    $token = (Get-Content 'secrets.yaml' | Select-String 'ha_token:' | ForEach-Object { $_.ToString().Split(':')[1].Trim() })
    $headers = @{Authorization = "Bearer $token"}
} catch {
    Write-Host "⚠️ Could not read HA token from secrets.yaml" -ForegroundColor Yellow
    $headers = $null
}

function Test-HAConnectivity {
    if (-not $headers) { return $false }
    try {
        $response = Invoke-WebRequest -Uri $baseUrl -Headers $headers -TimeoutSec 5
        return $response.StatusCode -eq 200
    } catch {
        return $false
    }
}

function Get-LogSize {
    if (Test-Path 'home-assistant.log') {
        $size = (Get-Item 'home-assistant.log').Length / 1MB
        return [math]::Round($size, 2)
    }
    return 0
}

function Archive-HALog {
    param([string]$suffix = "archive")
    
    Write-Host "🧼 Archiving Home Assistant log..." -ForegroundColor Cyan
    
    if (Test-Path 'home-assistant.log') {
        $logSize = Get-LogSize
        $archiveName = "home-assistant.log.${suffix}_${timestamp}"
        
        try {
            Copy-Item 'home-assistant.log' $archiveName -ErrorAction Stop
            Write-Host "✅ Log archived as: $archiveName (${logSize} MB)" -ForegroundColor Green
            
            Remove-Item 'home-assistant.log' -Force -ErrorAction Stop
            Write-Host "✅ Current log cleared" -ForegroundColor Green
            
            return $true
        } catch {
            Write-Host "❌ Failed to archive log: $($_.Exception.Message)" -ForegroundColor Red
            return $false
        }
    } else {
        Write-Host "ℹ️ No current log file to archive" -ForegroundColor Yellow
        return $true
    }
}

function Backup-Configuration {
    Write-Host "💾 Backing up configuration..." -ForegroundColor Cyan
    
    if (Test-Path 'configuration.yaml') {
        try {
            $backupName = "configuration_backup_${timestamp}.yaml"
            Copy-Item 'configuration.yaml' $backupName -ErrorAction Stop
            Write-Host "✅ Configuration backed up as: $backupName" -ForegroundColor Green
            return $true
        } catch {
            Write-Host "❌ Failed to backup configuration: $($_.Exception.Message)" -ForegroundColor Red
            return $false
        }
    } else {
        Write-Host "⚠️ configuration.yaml not found!" -ForegroundColor Red
        return $false
    }
}

function Test-SystemHealth {
    Write-Host "📊 Running System Health Check..." -ForegroundColor Cyan
    Write-Host "Timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
    
    # Log size check
    $logSize = Get-LogSize
    if ($logSize -gt 50) {
        Write-Host "⚠️ Log Size: ${logSize} MB (LARGE - consider archiving)" -ForegroundColor Yellow
    } elseif ($logSize -gt 0) {
        Write-Host "✅ Log Size: ${logSize} MB (Normal)" -ForegroundColor Green
    } else {
        Write-Host "ℹ️ No current log file" -ForegroundColor Yellow
    }
    
    # Configuration check
    if (Test-Path 'configuration.yaml') {
        Write-Host "✅ configuration.yaml exists" -ForegroundColor Green
    } else {
        Write-Host "❌ configuration.yaml missing!" -ForegroundColor Red
    }
    
    # HA connectivity check
    if (Test-HAConnectivity) {
        Write-Host "✅ Home Assistant: Responding" -ForegroundColor Green
    } else {
        Write-Host "❌ Home Assistant: Not responding or token issue" -ForegroundColor Red
    }
    
    # Recent files
    Write-Host "`nRecent files:" -ForegroundColor Gray
    Get-ChildItem -Name '*.log*', '*.yaml' | Sort-Object LastWriteTime -Descending | Select-Object -First 10 | ForEach-Object {
        Write-Host "  $_" -ForegroundColor Gray
    }
}

function Test-SelfHealingFeatures {
    if (-not (Test-HAConnectivity)) {
        Write-Host "❌ Cannot test self-healing features - HA not responding" -ForegroundColor Red
        return
    }
    
    Write-Host "🚀 Testing Self-Healing System Features..." -ForegroundColor Cyan
    
    # Test Restart Safety Score
    try {
        $safetyScore = Invoke-RestMethod -Uri "$baseUrl/states/sensor.restart_safety_score" -Headers $headers
        $score = $safetyScore.state
        $level = $safetyScore.attributes.safety_level
        
        if ($score -ge 90) {
            Write-Host "✅ Restart Safety Score: ${score}% ($level)" -ForegroundColor Green
        } elseif ($score -ge 70) {
            Write-Host "⚠️ Restart Safety Score: ${score}% ($level)" -ForegroundColor Yellow
        } else {
            Write-Host "🔴 Restart Safety Score: ${score}% ($level)" -ForegroundColor Red
        }
    } catch {
        Write-Host "⚠️ Restart Safety Score sensor not yet loaded" -ForegroundColor Yellow
    }
    
    # Test Self-Healing Automation
    try {
        $selfHealing = Invoke-RestMethod -Uri "$baseUrl/states/automation.self_healing_critical_automations_after_restart" -Headers $headers
        if ($selfHealing.state -eq "on") {
            Write-Host "✅ Self-Healing Automation: Active" -ForegroundColor Green
        } else {
            Write-Host "⚠️ Self-Healing Automation: Disabled" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "⚠️ Self-Healing automation not yet loaded" -ForegroundColor Yellow
    }
    
    # Test Modern Alexa TTS Wrapper
    try {
        $alexaScript = Invoke-RestMethod -Uri "$baseUrl/states/script.alexa_tts_announce" -Headers $headers
        Write-Host "✅ Modern Alexa TTS: Available" -ForegroundColor Green
    } catch {
        Write-Host "⚠️ Alexa TTS wrapper not yet loaded" -ForegroundColor Yellow
    }
    
    # Test Multi-Agent System
    try {
        $multiAgent = Invoke-RestMethod -Uri "$baseUrl/states/sensor.ai_messaging_status" -Headers $headers
        Write-Host "✅ Multi-Agent System: $($multiAgent.state)" -ForegroundColor Green
    } catch {
        Write-Host "⚠️ Multi-Agent system not yet loaded" -ForegroundColor Yellow
    }
}

function Show-SSHGuide {
    Write-Host "🔧 SSH Terminal Access Guide:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Open Home Assistant Web UI: http://192.168.1.217:8123" -ForegroundColor White
    Write-Host "2. Go to Settings → Add-ons → SSH & Web Terminal" -ForegroundColor White
    Write-Host "3. Click 'Open Web UI' button" -ForegroundColor White
    Write-Host ""
    Write-Host "Available HA CLI Commands:" -ForegroundColor Yellow
    Write-Host "  ha core restart    - Restart Home Assistant" -ForegroundColor Gray
    Write-Host "  ha core check      - Validate configuration" -ForegroundColor Gray
    Write-Host "  ha core logs       - View recent logs" -ForegroundColor Gray
    Write-Host "  ha core info       - System information" -ForegroundColor Gray
    Write-Host "  ha supervisor info - Supervisor details" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Log Management Commands:" -ForegroundColor Yellow
    Write-Host "  mv /config/home-assistant.log /config/home-assistant.log.old" -ForegroundColor Gray
    Write-Host "  ha core restart" -ForegroundColor Gray
}

# Main execution logic
if ($HealthCheck) {
    Test-SystemHealth
    if ($TestSelfHealing) {
        Write-Host ""
        Test-SelfHealingFeatures
    }
    Show-SSHGuide
} elseif ($EmergencyMode) {
    Write-Host "🏥 Emergency Recovery Mode Started..." -ForegroundColor Red
    
    $logArchived = Archive-HALog -suffix "crash"
    $configBacked = Backup-Configuration
    
    if ($logArchived -and $configBacked) {
        Write-Host ""
        Write-Host "✅ Emergency backup complete!" -ForegroundColor Green
        Write-Host "🔄 Ready for restart via SSH Terminal: ha core restart" -ForegroundColor Cyan
        Write-Host ""
        Show-SSHGuide
    } else {
        Write-Host "❌ Emergency backup had issues - check manually" -ForegroundColor Red
    }
} elseif ($ArchiveOnly) {
    Archive-HALog
    Write-Host "🔄 Use SSH Terminal to restart: ha core restart" -ForegroundColor Cyan
} elseif ($TestSelfHealing) {
    Test-SelfHealingFeatures
} else {
    # Default: Health check + archive
    Test-SystemHealth
    Write-Host ""
    
    $logSize = Get-LogSize
    if ($logSize -gt 10) {
        Write-Host "Log is getting large (${logSize} MB). Archive it? (y/n): " -NoNewline -ForegroundColor Yellow
        $response = Read-Host
        if ($response -eq 'y' -or $response -eq 'Y') {
            Archive-HALog
            Write-Host "🔄 Use SSH Terminal to restart: ha core restart" -ForegroundColor Cyan
        }
    }
    
    Write-Host ""
    Show-SSHGuide
}

Write-Host ""
Write-Host "📝 Log saved to: AI_WORKSPACE/SHARED_CONTEXT/SESSION_ESSENTIALS/" -ForegroundColor Gray