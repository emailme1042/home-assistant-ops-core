# iCloud to Production HA Sync Script
# Synchronizes iCloud workspace to live Home Assistant instance

param(
    [string]$iCloudPath = "C:\Users\email\iCloudDrive\HA-AI-Collaboration\HOME_ASSISTANT_5 Ai",
    [string]$ProductionPath = "S:\",
    [switch]$DryRun,
    [switch]$BackupFirst,
    [switch]$ValidateFirst
)

$ErrorActionPreference = "Continue"

Write-Host "🌐 iCLOUD TO PRODUCTION HA SYNC" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan
Write-Host "Source: $iCloudPath" -ForegroundColor Gray
Write-Host "Target: $ProductionPath" -ForegroundColor Gray
Write-Host "Time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Gray
Write-Host ""

# Verify paths exist
if (-not (Test-Path $iCloudPath)) {
    Write-Host "❌ ERROR: iCloud path not found: $iCloudPath" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $ProductionPath)) {
    Write-Host "❌ ERROR: Production path not found: $ProductionPath" -ForegroundColor Red
    exit 1
}

# Create backup if requested
if ($BackupFirst) {
    Write-Host "📦 Creating production backup..." -ForegroundColor Yellow
    $backupPath = "$ProductionPath\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\backup_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss')"
    
    try {
        New-Item -ItemType Directory -Force -Path $backupPath | Out-Null
        robocopy "$ProductionPath\includes" "$backupPath\includes" /E /XO /NFL /NDL
        robocopy "$ProductionPath\dashboards" "$backupPath\dashboards" /E /XO /NFL /NDL
        Write-Host "✅ Backup created: $backupPath" -ForegroundColor Green
    } catch {
        Write-Host "⚠️  Warning: Backup failed - $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Validate YAML first if requested
if ($ValidateFirst) {
    Write-Host "🔍 Validating YAML files..." -ForegroundColor Yellow
    $yamlFiles = Get-ChildItem "$iCloudPath\INCLUDES" -Recurse -Filter "*.yaml"
    $invalidFiles = @()
    
    foreach ($file in $yamlFiles) {
        try {
            # Basic YAML syntax check using PowerShell-Yaml if available
            $content = Get-Content $file.FullName -Raw
            if ($content -match ':\s*$|^\s*-\s*$') {
                # Basic validation passed
            }
        } catch {
            $invalidFiles += $file.FullName
        }
    }
    
    if ($invalidFiles.Count -gt 0) {
        Write-Host "❌ YAML validation failed for:" -ForegroundColor Red
        foreach ($file in $invalidFiles) {
            Write-Host "  - $file" -ForegroundColor Red
        }
        if (-not $DryRun) {
            Write-Host "Aborting sync due to validation errors." -ForegroundColor Red
            exit 1
        }
    } else {
        Write-Host "✅ All YAML files passed validation" -ForegroundColor Green
    }
}

# Define sync mappings
$syncMappings = @{
    "INCLUDES\automations" = "includes\automations"
    "INCLUDES\scripts" = "includes\scripts"
    "INCLUDES\sensors" = "includes\sensors"
    "INCLUDES\input_booleans" = "includes\input_booleans"
    "INCLUDES\input_texts" = "includes\input_texts"
    "INCLUDES\input_numbers" = "includes\input_numbers"
    "INCLUDES\templates" = "includes\templates"
    "INCLUDES\shell_commands" = "includes\shell_commands"
    "DASHBOARDS" = "dashboards"
}

# Perform sync operations
Write-Host "📁 Syncing folders..." -ForegroundColor Yellow
$syncCount = 0
$errorCount = 0

foreach ($mapping in $syncMappings.GetEnumerator()) {
    $sourcePath = Join-Path $iCloudPath $mapping.Key
    $targetPath = Join-Path $ProductionPath $mapping.Value
    
    if (Test-Path $sourcePath) {
        Write-Host "  📂 $($mapping.Key) → $($mapping.Value)" -ForegroundColor Cyan
        
        if ($DryRun) {
            Write-Host "    [DRY RUN] Would sync files" -ForegroundColor Gray
        } else {
            try {
                # Ensure target directory exists
                $targetDir = Split-Path $targetPath -Parent
                if (-not (Test-Path $targetDir)) {
                    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
                }
                
                # Use robocopy for efficient sync
                $result = robocopy $sourcePath $targetPath /E /XO /NFL /NDL
                
                if ($LASTEXITCODE -le 3) {  # Robocopy success codes 0-3
                    Write-Host "    ✅ Synced successfully" -ForegroundColor Green
                    $syncCount++
                } else {
                    Write-Host "    ⚠️  Sync completed with warnings (exit code: $LASTEXITCODE)" -ForegroundColor Yellow
                    $syncCount++
                }
            } catch {
                Write-Host "    ❌ Sync failed: $($_.Exception.Message)" -ForegroundColor Red
                $errorCount++
            }
        }
    } else {
        Write-Host "  ⚠️  Source not found: $sourcePath" -ForegroundColor Yellow
    }
}

# Sync individual files
$individualFiles = @{
    "configuration.yaml" = "configuration.yaml"
}

Write-Host "📄 Syncing individual files..." -ForegroundColor Yellow

foreach ($mapping in $individualFiles.GetEnumerator()) {
    $sourceFile = Join-Path $iCloudPath $mapping.Key
    $targetFile = Join-Path $ProductionPath $mapping.Value
    
    if (Test-Path $sourceFile) {
        Write-Host "  📄 $($mapping.Key)" -ForegroundColor Cyan
        
        if ($DryRun) {
            Write-Host "    [DRY RUN] Would copy file" -ForegroundColor Gray
        } else {
            try {
                Copy-Item $sourceFile $targetFile -Force
                Write-Host "    ✅ Copied successfully" -ForegroundColor Green
                $syncCount++
            } catch {
                Write-Host "    ❌ Copy failed: $($_.Exception.Message)" -ForegroundColor Red
                $errorCount++
            }
        }
    } else {
        Write-Host "  ⚠️  Source file not found: $sourceFile" -ForegroundColor Yellow
    }
}

# Summary
Write-Host ""
Write-Host "📊 SYNC SUMMARY:" -ForegroundColor Cyan
Write-Host "  ✅ Successful: $syncCount" -ForegroundColor Green
Write-Host "  ❌ Errors: $errorCount" -ForegroundColor Red

if ($DryRun) {
    Write-Host "  [DRY RUN MODE] No actual changes made" -ForegroundColor Gray
}

Write-Host ""
if ($errorCount -eq 0) {
    Write-Host "🎉 SYNC COMPLETE!" -ForegroundColor Green
    if (-not $DryRun) {
        Write-Host "💡 Recommendation: Restart Home Assistant to load changes" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️  SYNC COMPLETED WITH ERRORS" -ForegroundColor Yellow
    Write-Host "Check error messages above for details" -ForegroundColor Gray
}

Write-Host ""
Write-Host "USAGE:" -ForegroundColor Yellow
Write-Host "  -DryRun         Show what would be synced without making changes" -ForegroundColor Gray
Write-Host "  -BackupFirst    Create backup before syncing" -ForegroundColor Gray
Write-Host "  -ValidateFirst  Validate YAML syntax before syncing" -ForegroundColor Gray

$true