# Home Assistant Operations Core

Centralized repository for Home Assistant configuration, AI integrations, and automation development.

## Structure
- config/ - Home Assistant configuration files
- includes/ - Modular configuration components
- dashboards/ - Lovelace dashboard definitions
- i-workspace/ - AI collaboration and context files
- scripts/ - Automation and utility scripts
- utomation_templates/ - Reusable automation patterns
- ackups/ - Automated configuration backups

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
3. Run validation: yamllint config/**/*.yaml
4. Deploy changes to HA
