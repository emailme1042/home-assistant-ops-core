# GitHub HA Integration Verification Script
# Run this after setup to verify everything is working correctly

param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "S:\github_repo"
)

# Colors for output
$Green = "Green"
$Yellow = "Yellow"
$Red = "Red"
$Blue = "Cyan"
$White = "White"

Write-Host "GitHub HA Integration Verification" -ForegroundColor $Blue
Write-Host "===================================" -ForegroundColor $Blue

$checksPassed = 0
$totalChecks = 0

function Test-Check {
    param($Description, $TestScript)
    $script:totalChecks++
    Write-Host "Testing: $Description... " -NoNewline -ForegroundColor $Yellow

    try {
        $result = & $TestScript
        if ($result) {
            Write-Host "PASSED" -ForegroundColor $Green
            $script:checksPassed++
        } else {
            Write-Host "FAILED" -ForegroundColor $Red
        }
    } catch {
        Write-Host "ERROR: $($_.Exception.Message)" -ForegroundColor $Red
    }
}

# Check if repository directory exists
Test-Check "Repository directory exists" {
    Test-Path $RepoPath
}

# Check if it's a git repository
Test-Check "Git repository initialized" {
    Push-Location $RepoPath
    try {
        $null = git status 2>$null
        $LASTEXITCODE -eq 0
    } finally {
        Pop-Location
    }
}

# Check remote origin
Test-Check "GitHub remote configured" {
    Push-Location $RepoPath
    try {
        $remote = git remote get-url origin 2>$null
        $remote -and $remote -match "github\.com"
    } finally {
        Pop-Location
    }
}

# Check if files were copied
Test-Check "HA configuration files copied" {
    Push-Location $RepoPath
    try {
        (Test-Path "config/configuration.yaml") -and (Test-Path "includes/")
    } finally {
        Pop-Location
    }
}

# Check GitHub Actions workflow
Test-Check "GitHub Actions workflow created" {
    Push-Location $RepoPath
    try {
        Test-Path ".github/workflows/validate-ha.yml"
    } finally {
        Pop-Location
    }
}

# Check .gitignore
Test-Check ".gitignore configured" {
    Push-Location $RepoPath
    try {
        Test-Path ".gitignore"
    } finally {
        Pop-Location
    }
}

# Check initial commit
Test-Check "Initial commit created" {
    Push-Location $RepoPath
    try {
        $commits = git log --oneline 2>$null | Measure-Object | Select-Object -ExpandProperty Count
        $commits -gt 0
    } finally {
        Pop-Location
    }
}

# Check repository structure
Test-Check "Repository structure complete" {
    Push-Location $RepoPath
    try {
        $requiredDirs = @("config", "includes", "dashboards", "docs", "ai-workspace", ".github/workflows")
        $allExist = $true
        foreach ($dir in $requiredDirs) {
            if (-not (Test-Path $dir)) {
                $allExist = $false
                break
            }
        }
        $allExist
    } finally {
        Pop-Location
    }
}

# Summary
Write-Host "" -ForegroundColor $White
Write-Host "Verification Summary" -ForegroundColor $Blue
Write-Host "===================" -ForegroundColor $Blue
Write-Host "Checks Passed: $checksPassed / $totalChecks" -ForegroundColor $(if ($checksPassed -eq $totalChecks) { $Green } else { $Yellow })

if ($checksPassed -eq $totalChecks) {
    Write-Host "" -ForegroundColor $Green
    Write-Host "SUCCESS! All checks passed!" -ForegroundColor $Green
    Write-Host "Your GitHub HA integration is ready!" -ForegroundColor $Green
    Write-Host "" -ForegroundColor $White
    Write-Host "Next Steps:" -ForegroundColor $Blue
    Write-Host "1. Visit your GitHub repository online" -ForegroundColor $White
    Write-Host "2. Enable GitHub Actions in repository settings" -ForegroundColor $White
    Write-Host "3. Configure VS Code with GitHub Copilot" -ForegroundColor $White
    Write-Host "4. Connect ChatGPT to the repository" -ForegroundColor $White
    Write-Host "5. Set up GitHub Backup add-on in HA" -ForegroundColor $White
} else {
    Write-Host "" -ForegroundColor $Yellow
    Write-Host "Some checks failed" -ForegroundColor $Yellow
    Write-Host "Review the failed checks above and re-run setup if needed." -ForegroundColor $Yellow
    Write-Host "" -ForegroundColor $White
    Write-Host "Common fixes:" -ForegroundColor $Blue
    Write-Host "- Re-run the setup script with correct credentials" -ForegroundColor $White
    Write-Host "- Check GitHub token permissions" -ForegroundColor $White
    Write-Host "- Verify repository name doesn't already exist" -ForegroundColor $White
}

# Show repository info
Write-Host "" -ForegroundColor $White
Write-Host "Repository Information" -ForegroundColor $Blue
Write-Host "======================" -ForegroundColor $Blue

Push-Location $RepoPath
try {
    Write-Host "Repository Path: $RepoPath" -ForegroundColor $White

    $remote = git remote get-url origin 2>$null
    if ($remote) {
        Write-Host "Remote URL: $remote" -ForegroundColor $White
    }

    $commits = git log --oneline 2>$null | Measure-Object | Select-Object -ExpandProperty Count
    Write-Host "Commits: $commits" -ForegroundColor $White

    Write-Host "" -ForegroundColor $White
    Write-Host "Repository Structure:" -ForegroundColor $Yellow
    Get-ChildItem -Directory | Where-Object { $_.Name -notmatch '^\.' } | ForEach-Object {
        $itemCount = (Get-ChildItem $_.FullName -Recurse -File 2>$null | Measure-Object).Count
        Write-Host "  $($_.Name)/ ($itemCount files)" -ForegroundColor $White
    }
} finally {
    Pop-Location
}

Write-Host "" -ForegroundColor $Blue
Write-Host "Useful Commands:" -ForegroundColor $Blue
Write-Host "cd $RepoPath" -ForegroundColor $White
Write-Host "git status" -ForegroundColor $White
Write-Host "git log --oneline" -ForegroundColor $White
Write-Host "git push origin main  # If initial push failed" -ForegroundColor $White