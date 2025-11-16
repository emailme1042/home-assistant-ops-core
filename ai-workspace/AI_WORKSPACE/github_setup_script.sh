# 🚀 GitHub HA Integration Setup Script
# Run this on your HA Green device to establish GitHub as central hub

#!/bin/bash

# Configuration - Update these with your details
GITHUB_USERNAME="YOUR_GITHUB_USERNAME"
REPO_NAME="home-assistant-ops-core"
GITHUB_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Starting GitHub HA Integration Setup${NC}"
echo "=========================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "${YELLOW}Checking prerequisites...${NC}"
if ! command_exists git; then
    echo -e "${RED}❌ Git is not installed. Installing...${NC}"
    apk add git
fi

if ! command_exists curl; then
    echo -e "${RED}❌ curl is not installed. Installing...${NC}"
    apk add curl
fi

echo -e "${GREEN}✅ Prerequisites OK${NC}"

# Configure Git
echo -e "${YELLOW}Configuring Git...${NC}"
git config --global user.name "$GITHUB_USERNAME"
git config --global user.email "$GITHUB_USERNAME@github.com"
git config --global init.defaultBranch main
echo -e "${GREEN}✅ Git configured${NC}"

# Create repository directory
REPO_DIR="/config/github_repo"
echo -e "${YELLOW}Creating repository directory: $REPO_DIR${NC}"
mkdir -p "$REPO_DIR"
cd "$REPO_DIR"

# Initialize Git repository
echo -e "${YELLOW}Initializing Git repository...${NC}"
git init
git remote add origin "https://$GITHUB_TOKEN@github.com/$GITHUB_USERNAME/$REPO_NAME.git"

# Create repository structure
echo -e "${YELLOW}Creating repository structure...${NC}"
mkdir -p config includes dashboards docs ai-workspace scripts backups automation_templates

# Copy HA configuration files
echo -e "${YELLOW}Copying HA configuration files...${NC}"
cp -r /config/*.yaml config/ 2>/dev/null || echo "No YAML files in /config root"
cp -r /config/includes/* includes/ 2>/dev/null || echo "No includes directory"
cp -r /config/dashboards/* dashboards/ 2>/dev/null || echo "No dashboards directory"

# Copy AI workspace
echo -e "${YELLOW}Copying AI workspace...${NC}"
cp -r /config/AI_WORKSPACE/* ai-workspace/ 2>/dev/null || echo "No AI_WORKSPACE directory"

# Create documentation structure
echo -e "${YELLOW}Creating documentation structure...${NC}"
cat > docs/README.md << 'EOF'
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
EOF

# Create GitHub Actions workflow
echo -e "${YELLOW}Creating GitHub Actions workflow...${NC}"
mkdir -p .github/workflows

cat > .github/workflows/validate-ha.yml << 'EOF'
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
          pip install PyYAML yamllint homeassistant

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
          " \;

      - name: Lint YAML files
        run: yamllint config/**/*.yaml includes/**/*.yaml dashboards/**/*.yaml || true

      - name: Check for secrets
        run: |
          if grep -r "password\|secret\|token\|key" config/ includes/ dashboards/; then
            echo "⚠️  Warning: Potential secrets found in configuration files"
            echo "Consider moving sensitive data to secrets.yaml"
          fi
EOF

# Create .gitignore
echo -e "${YELLOW}Creating .gitignore...${NC}"
cat > .gitignore << 'EOF'
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
EOF

# Initial commit
echo -e "${YELLOW}Creating initial commit...${NC}"
git add .
git commit -m "Initial commit: HA configuration and AI workspace migration

- Migrated Home Assistant configuration files
- Set up AI workspace structure
- Added GitHub Actions for validation
- Created documentation framework

AI Integration Ready:
- GitHub Copilot: Code generation and validation
- ChatGPT: Strategic planning and documentation
- M365 Copilot: Communication and task management
- OpenAI API: Advanced AI features"

# Push to GitHub
echo -e "${YELLOW}Pushing to GitHub...${NC}"
if git push -u origin main; then
    echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
else
    echo -e "${RED}❌ Failed to push to GitHub. Check your token and repository permissions.${NC}"
    echo -e "${YELLOW}Manual push command:${NC}"
    echo "git push -u origin main"
fi

# Create setup verification script
echo -e "${YELLOW}Creating verification script...${NC}"
cat > scripts/verify_setup.sh << 'EOF'
#!/bin/bash
echo "🔍 Verifying GitHub HA Integration Setup"
echo "========================================"

# Check Git status
echo "Git Status:"
git status --short

echo ""
echo "Remote Repository:"
git remote -v

echo ""
echo "Recent Commits:"
git log --oneline -5

echo ""
echo "Repository Structure:"
find . -type f -name "*.yaml" -o -name "*.md" | head -20

echo ""
echo "✅ Setup verification complete!"
echo "Next steps:"
echo "1. Check GitHub repository for uploaded files"
echo "2. Enable GitHub Actions in repository settings"
echo "3. Configure VS Code with GitHub Copilot"
echo "4. Connect ChatGPT to GitHub repository"
EOF

chmod +x scripts/verify_setup.sh

echo ""
echo -e "${GREEN}🎉 GitHub HA Integration Setup Complete!${NC}"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Update GITHUB_USERNAME and GITHUB_TOKEN in this script"
echo "2. Run: ./scripts/verify_setup.sh"
echo "3. Check your GitHub repository online"
echo "4. Configure VS Code GitHub integration"
echo "5. Connect ChatGPT and M365 Copilot to the repository"
echo ""
echo -e "${YELLOW}Repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME${NC}"