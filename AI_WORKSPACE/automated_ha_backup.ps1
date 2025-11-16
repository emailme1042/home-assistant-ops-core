# Automated HA Backup to GitHub
# Run this script to backup HA configuration to GitHub repository

param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "S:\github_repo",
    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "S:\config",  # Default to live config
    [Parameter(Mandatory=$false)]
    [string]$NasBackupPath = ""  # If provided, use NAS backup instead
)

# Use NAS backup if specified, otherwise use live config
$sourcePath = if ($NasBackupPath -and (Test-Path $NasBackupPath)) {
    Write-Host "Using NAS backup location: $NasBackupPath" -ForegroundColor Cyan
    $NasBackupPath
} else {
    Write-Host "Using live config location: $ConfigPath" -ForegroundColor Cyan
    $ConfigPath
}

Write-Host "Starting HA Configuration Backup to GitHub" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

try {
    # Check if source directory exists
    if (-not (Test-Path $sourcePath)) {
        throw "Source directory not found: $sourcePath"
    }

    # Check if repo directory exists
    if (-not (Test-Path $RepoPath)) {
        throw "Repository directory not found: $RepoPath"
    }

    # Change to repo directory
    Push-Location $RepoPath

    Write-Host "Copying latest configuration files..." -ForegroundColor Yellow

    # Copy configuration files (excluding sensitive ones)
    $excludePatterns = @(
        "*.db", "*.db-*", "*.db-wal", "*.db-shm",
        "storage", "deps", "__pycache__", "*.log",
        "backups", "snapshots", "secrets.yaml",
        "github_repo"
    )

    # Copy config directory contents
    $configItems = Get-ChildItem $sourcePath -Exclude $excludePatterns
    foreach ($item in $configItems) {
        $destPath = Join-Path $RepoPath $item.Name
        if ($item.PSIsContainer) {
            # Copy directory
            if (Test-Path $destPath) {
                Remove-Item $destPath -Recurse -Force
            }
            Copy-Item $item.FullName $destPath -Recurse
        } else {
            # Copy file
            Copy-Item $item.FullName $destPath -Force
        }
    }

    Write-Host "Files copied successfully" -ForegroundColor Green

    # Check git status
    Write-Host "Checking git status..." -ForegroundColor Yellow
    $status = git status --porcelain
    if ($status) {
        Write-Host "Changes detected, committing..." -ForegroundColor Yellow

        # Add all changes
        git add .

        # Create commit message with timestamp
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $commitMessage = "Automated backup: $timestamp"

        # Commit
        git commit -m $commitMessage

        # Push to GitHub
        Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
        git push origin main

        Write-Host "Backup completed successfully!" -ForegroundColor Green
        Write-Host "Commit: $commitMessage" -ForegroundColor White

    } else {
        Write-Host "No changes detected, skipping commit" -ForegroundColor Yellow
    }

} catch {
    Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Backup failed!" -ForegroundColor Red
} finally {
    Pop-Location
}

Write-Host "Backup process completed" -ForegroundColor Cyan