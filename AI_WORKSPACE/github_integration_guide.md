# 🚀 GitHub HA Integration Setup Guide

## Overview
This guide establishes GitHub as the central hub for your Home Assistant development and AI collaboration, integrating GitHub Copilot, ChatGPT, M365 Copilot, and OpenAI API into a unified workflow.

## 📋 Prerequisites
- GitHub account with repository creation permissions
- GitHub Personal Access Token (classic) with `repo` scope
- Windows PowerShell access
- Home Assistant configuration files accessible

## 🛠️ Step 1: Generate GitHub Personal Access Token

1. Go to [GitHub.com](https://github.com) → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Set permissions:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
4. Copy the token immediately (you won't see it again!)

## 🚀 Step 2: Execute Setup Script

### Option A: Automated Setup (Recommended)
```powershell
# Navigate to your AI workspace
cd S:\AI_WORKSPACE

# Run the setup script with your credentials
.\github_setup_windows.ps1 -GitHubUsername "your-github-username" -GitHubToken "your-personal-access-token"
```

### Option B: Manual Setup
If the automated script fails, follow these manual steps:

1. **Configure Git**:
```powershell
git config --global user.name "your-github-username"
git config --global user.email "your-github-username@github.com"
git config --global init.defaultBranch main
```

2. **Create Repository Directory**:
```powershell
mkdir S:\github_repo
cd S:\github_repo
git init
```

3. **Add Remote and Copy Files**:
```powershell
git remote add origin https://your-token@github.com/your-username/home-assistant-ops-core.git
# Copy HA files manually...
```

## 🔍 Step 3: Verify Setup

Run the verification script:
```powershell
.\scripts\verify_setup.ps1
```

Expected output:
- ✅ Git status shows clean working directory
- ✅ Remote origin configured correctly
- ✅ Recent commits visible
- ✅ Repository structure matches expected layout

## ⚙️ Step 4: Configure GitHub Actions

1. Go to your repository on GitHub
2. Click "Settings" → "Pages"
3. Set source to "GitHub Actions"
4. The workflow will automatically validate your HA configuration on every push

## 🤖 Step 5: Connect AI Agents

### GitHub Copilot (VS Code)
1. Install GitHub Copilot extension in VS Code
2. Sign in with your GitHub account
3. Open the repository in VS Code
4. Copilot will automatically provide HA-specific suggestions

### ChatGPT Integration
1. Share repository URL with ChatGPT
2. Use prompts like: "Analyze this HA config: [paste config sections]"
3. Request strategic planning and documentation help

### M365 Copilot Integration
1. Use OneNote or Teams to link to repository issues
2. Create tasks and documentation that reference repository files
3. Use Copilot to generate meeting notes and action items

### OpenAI API Integration
1. Configure API keys in your HA secrets
2. Use repository as central documentation hub
3. Reference repository files in API prompts

## 🔄 Step 6: Set Up Automated Backups

### Option A: GitHub Backup Add-on (Recommended)
1. Install "GitHub Backup" add-on from HACS
2. Use the configuration from `github_backup_addon_config.yaml`
3. Update with your GitHub credentials
4. Configure backup schedule (default: daily at 2 AM)

### Option B: Manual Backup Script
Create a scheduled task to run the setup script periodically:
```powershell
# Windows Task Scheduler
schtasks /create /tn "HA GitHub Backup" /tr "powershell.exe -File S:\AI_WORKSPACE\github_setup_windows.ps1 -GitHubUsername your-username -GitHubToken your-token" /sc daily /st 02:00
```

## 📊 Step 7: Repository Structure

Your repository should look like this:
```
home-assistant-ops-core/
├── config/
│   ├── configuration.yaml
│   ├── secrets.yaml
│   └── ui-lovelace.yaml
├── includes/
│   ├── automations/
│   ├── sensors/
│   └── scripts/
├── dashboards/
├── ai-workspace/
│   ├── AI_README.md
│   ├── copilot_session_notes.md
│   └── SHARED_CONTEXT/
├── docs/
│   └── README.md
├── scripts/
│   └── verify_setup.ps1
├── .github/
│   └── workflows/
│       └── validate-ha.yml
└── .gitignore
```

## 🔧 Step 8: Development Workflow

### Making Changes
1. **Pull latest changes**: `git pull origin main`
2. **Make edits** in appropriate directories
3. **Test locally** with HA validation
4. **Commit changes**: `git add . && git commit -m "Your message"`
5. **Push to GitHub**: `git push origin main`
6. **GitHub Actions** will validate automatically

### AI Collaboration Protocol
1. **GitHub Copilot**: Code generation and validation
2. **ChatGPT**: Strategic planning and complex logic
3. **M365 Copilot**: Documentation and task management
4. **OpenAI API**: Advanced automation features

### Documentation Standards
- Use `ai-workspace/SHARED_CONTEXT/` for AI collaboration files
- Update `copilot_session_notes.md` for each session
- Reference repository files in all AI interactions

## 🚨 Troubleshooting

### Common Issues

**"Authentication failed"**
- Verify your GitHub token has `repo` scope
- Check token hasn't expired
- Ensure username is correct

**"Repository already exists"**
- Choose a different repository name
- Or delete the existing repository first

**"Permission denied"**
- Check GitHub token permissions
- Verify repository access

**GitHub Actions not running**
- Go to repository Settings → Actions → General
- Ensure "Allow all actions" is selected

### Getting Help
1. Check the verification script output
2. Review GitHub repository for error messages
3. Check HA logs for any configuration issues
4. Use the AI workspace documentation for guidance

## 🎯 Success Metrics

After setup, you should have:
- ✅ Centralized HA configuration in Git
- ✅ Automated validation on every change
- ✅ AI agents working from single source of truth
- ✅ Automated backups preventing data loss
- ✅ Collaborative development environment
- ✅ Version-controlled HA evolution

## 📞 Next Steps

1. **Test the integration** by making a small HA config change
2. **Connect your AI agents** to the repository
3. **Set up automated backups** for peace of mind
4. **Document your workflows** in the repository
5. **Scale your AI collaboration** across all tools

---

**🎉 Congratulations!** You've established GitHub as the central hub for your Home Assistant AI ecosystem. Your fragmented AI tools are now unified, your configurations are version-controlled, and your development workflow is future-proof.

**Repository URL**: `https://github.com/your-username/home-assistant-ops-core`