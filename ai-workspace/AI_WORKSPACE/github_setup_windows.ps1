# GitHub HA Integration Setup Script (PowerShell)
# Run this on your Windows machine to establish GitHub as central hub

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubUsername,

    [Parameter(Mandatory=$true)]
    [string]$GitHubToken,

    [Parameter(Mandatory=$false)]
    [string]$RepoName = "home-assistant-ops-core",

    [Parameter(Mandatory=$false)]
    [string]$HAConfigPath = "S:\",

    [Parameter(Mandatory=$false)]
    [string]$LocalRepoPath = "S:\github_repo"
)

# Colors for output
$Green = "Green"
$Yellow = "Yellow"
$Red = "Red"
$Blue = "Cyan"

Write-Host "🚀 Starting GitHub HA Integration Setup" -ForegroundColor $Blue
Write-Host "==========================================" -ForegroundColor $Blue

# Function to check if command exists
function Test-Command {
    param($Command)
    try {
        Get-Command $Command -ErrorAction Stop
        return $true
    } catch {
        return $false
    }
}

# Check prerequisites
Write-Host "Checking prerequisites..." -ForegroundColor $Yellow
if (-not (Test-Command "git")) {
    Write-Host "❌ Git is not installed. Please install Git first." -ForegroundColor $Red
    exit 1
}

Write-Host "✅ Prerequisites OK" -ForegroundColor $Green

# Configure Git
Write-Host "Configuring Git..." -ForegroundColor $Yellow
git config --global user.name $GitHubUsername
git config --global user.email "$GitHubUsername@github.com"
git config --global init.defaultBranch main
Write-Host "✅ Git configured" -ForegroundColor $Green

# Create repository directory
Write-Host "Creating repository directory: $LocalRepoPath" -ForegroundColor $Yellow
if (-not (Test-Path $LocalRepoPath)) {
    New-Item -ItemType Directory -Path $LocalRepoPath -Force
}
Set-Location $LocalRepoPath

# Initialize Git repository
Write-Host "Initializing Git repository..." -ForegroundColor $Yellow
git init
$repoUrl = "https://$GitHubToken@github.com/$GitHubUsername/$RepoName.git"
git remote add origin $repoUrl

# Create repository structure
Write-Host "Creating repository structure..." -ForegroundColor $Yellow
$directories = @(
    "config",
    "includes",
    "dashboards",
    "docs",
    "ai-workspace",
    "scripts",
    "backups",
    "automation_templates",
    ".github/workflows"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force
    }
}

# Copy HA configuration files
Write-Host "Copying HA configuration files..." -ForegroundColor $Yellow
$haFiles = @(
    "configuration.yaml",
    "secrets.yaml",
    "ui-lovelace.yaml"
)

foreach ($file in $haFiles) {
    $sourcePath = Join-Path $HAConfigPath $file
    if (Test-Path $sourcePath) {
        Copy-Item $sourcePath -Destination "config\" -Force
        Write-Host "  Copied $file" -ForegroundColor $Green
    } else {
        Write-Host "  $file not found, skipping" -ForegroundColor $Yellow
    }
}

# Copy includes directory
$includesPath = Join-Path $HAConfigPath "includes"
if (Test-Path $includesPath) {
    Copy-Item $includesPath -Destination "." -Recurse -Force
    Write-Host "  Copied includes directory" -ForegroundColor $Green
} else {
    Write-Host "  includes directory not found, skipping" -ForegroundColor $Yellow
}

# Copy dashboards directory
$dashboardsPath = Join-Path $HAConfigPath "dashboards"
if (Test-Path $dashboardsPath) {
    Copy-Item $dashboardsPath -Destination "." -Recurse -Force
    Write-Host "  Copied dashboards directory" -ForegroundColor $Green
} else {
    Write-Host "  dashboards directory not found, skipping" -ForegroundColor $Yellow
}

# Copy AI workspace
$aiPath = Join-Path $HAConfigPath "AI_WORKSPACE"
if (Test-Path $aiPath) {
    Copy-Item $aiPath -Destination "ai-workspace" -Recurse -Force
    Write-Host "  Copied AI workspace" -ForegroundColor $Green
} else {
    Write-Host "  AI_WORKSPACE directory not found, skipping" -ForegroundColor $Yellow
}

# Create documentation
Write-Host "Creating documentation..." -ForegroundColor $Yellow
$readmeContent = @"
# Home Assistant Operations Core

Centralized repository for Home Assistant configuration, AI integrations, and automation development.

## Structure
- `config/` - Home Assistant configuration files
- `includes/` - Modular configuration components
- `dashboards/` - Lovelace dashboard definitions
- `ai-workspace/` - AI collaboration and context files
- `scripts/` - Automation and utility scripts
- `automation_templates/` - Reusable automation patterns
- `backups/` - Automated configuration backups

## AI Integration
This repository serves as the central hub for:
- GitHub Copilot (code generation and validation)
- ChatGPT (strategic planning and documentation)
- M365 Copilot (communication and task management)
- OpenAI API (advanced AI features)

## Development Workflow
1. Make changes in appropriate directories
2. Test configurations locally
3. Commit and push changes
4. GitHub Actions validate YAML syntax
5. Deploy to production HA instance

## Quick Start
1. Clone this repository
2. Copy config files to your HA instance
3. Run validation: `yamllint config/**/*.yaml`
4. Deploy changes to HA
"@

$readmeContent | Out-File -FilePath "docs/README.md" -Encoding UTF8

# Create GitHub Actions workflow
Write-Host "Creating GitHub Actions workflow..." -ForegroundColor $Yellow
$workflowContent = @'
name: Validate Home Assistant Configuration
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install PyYAML yamllint

      - name: Validate YAML syntax
        run: |
          find config includes dashboards -name "*.yaml" -exec python -c "
          import yaml, sys
          try:
              with open('{}', 'r') as f:
                  yaml.safe_load(f)
          except Exception as e:
              print('ERROR in {}: {}'.format('{}', e))
              sys.exit(1)
          " \; 2>/dev/null || true

      - name: Lint YAML files
        run: |
          yamllint config/**/*.yaml includes/**/*.yaml dashboards/**/*.yaml 2>/dev/null || true

      - name: Check for potential secrets
        run: |
          if grep -r "password\|secret\|token\|key" config/ includes/ dashboards/ 2>/dev/null; then
            echo "⚠️  Warning: Potential secrets found in configuration files"
            echo "Consider moving sensitive data to secrets.yaml"
          else
            echo "✅ No obvious secrets found in configuration"
          fi
'@

$workflowContent | Out-File -FilePath ".github/workflows/validate-ha.yml" -Encoding UTF8

# Create .gitignore
Write-Host "Creating .gitignore..." -ForegroundColor $Yellow
$gitignoreContent = @"
# Home Assistant
secrets.yaml
*.db
*.db-shm
*.db-wal
storage/
deps/
custom_components/__pycache__/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp

# Local development
.vscode/
.idea/
"@
$gitignoreContent | Out-File -FilePath ".gitignore" -Encoding UTF8

# Initial commit
Write-Host "Creating initial commit..." -ForegroundColor $Yellow
git add .
git commit -m @"
Initial commit: HA configuration and AI workspace migration

- Migrated Home Assistant configuration files
- Set up AI workspace structure
- Added GitHub Actions for validation
- Created documentation framework

AI Integration Ready:
- GitHub Copilot: Code generation and validation
- ChatHub Copilot: Strategic planning and documentation
- M365 Copilot: Communication and task management
- OpenAI API: Advanced AI features

Repository: $RepoName
Maintainer: $GitHubUsername
"@

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor $Yellow
try {
    git push -u origin main
    Write-Host "✅ Successfully pushed to GitHub!" -ForegroundColor $Green
} catch {
    Write-Host "❌ Failed to push to GitHub. Check your token and repository permissions." -ForegroundColor $Red
    Write-Host "Manual push command:" -ForegroundColor $Yellow
    Write-Host "git push -u origin main"
}

# Create verification script
Write-Host "Creating verification script..." -ForegroundColor $Yellow
$verifyScript = @'
Write-Host "🔍 Verifying GitHub HA Integration Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

Write-Host "Git Status:" -ForegroundColor Yellow
git status --short

Write-Host "Remote Repository:" -ForegroundColor Yellow
git remote -v

Write-Host "Recent Commits:" -ForegroundColor Yellow
git log --oneline -5

Write-Host "Repository Structure:" -ForegroundColor Yellow
Get-ChildItem -Recurse -File | Where-Object { $_.Extension -in @('.yaml','.md') } | Select-Object FullName | Format-Table -AutoSize

Write-Host "✅ Setup verification complete!" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Check GitHub repository for uploaded files" -ForegroundColor White
Write-Host "2. Enable GitHub Actions in repository settings" -ForegroundColor White
Write-Host "3. Configure VS Code with GitHub Copilot" -ForegroundColor White
Write-Host "4. Connect ChatGPT to GitHub repository" -ForegroundColor White
Write-Host "5. Set up GitHub Backup add-on in HA" -ForegroundColor White
'@

$verifyScript | Out-File -FilePath "scripts/verify_setup.ps1" -Encoding UTF8

Write-Host "" -ForegroundColor $Green
Write-Host "🎉 GitHub HA Integration Setup Complete!" -ForegroundColor $Green
Write-Host "" -ForegroundColor $Green
Write-Host "Next Steps:" -ForegroundColor $Blue
Write-Host "1. Run: .\scripts\verify_setup.ps1" -ForegroundColor $White
Write-Host "2. Check your GitHub repository online" -ForegroundColor $White
Write-Host "3. Configure VS Code GitHub integration" -ForegroundColor $White
Write-Host "4. Connect ChatGPT and M365 Copilot to the repository" -ForegroundColor $White
Write-Host "5. Set up GitHub Backup add-on in HA" -ForegroundColor $White
Write-Host "" -ForegroundColor $Blue
Write-Host "Repository URL: https://github.com/$GitHubUsername/$RepoName" -ForegroundColor $Yellow