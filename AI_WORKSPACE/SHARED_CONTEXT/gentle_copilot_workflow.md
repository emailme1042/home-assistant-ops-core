# Gentle Copilot Workflow for Jamie

## 🧠 How to Work with GitHub Copilot (Simple Steps)

### Before Starting
1. **Check Current Task**: Open `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` to see what we're working on
2. **Use Dashboard Navigation**: Go to "AI Navigation" dashboard → "AI Workspace Navigation" for context
3. **Ask if Unclear**: If anything is confusing, say "I need clarification" - it's okay!

### When Copilot Suggests Changes
1. **Read the Explanation**: Copilot will explain what it's doing
2. **Check if it Matches Patterns**: Does it look like other files in the project?
3. **Ask Questions**: "Is this safe?" or "Will this break anything?"
4. **Confirm Before Apply**: Say "yes" only if you're sure

### Safe Workflow
- **One File at a Time**: Don't change multiple files together
- **Small Changes**: Fix one thing, not everything
- **Test After**: Use the validation commands to check
- **Log Everything**: Changes go to `ai_exec_log.md` automatically

### If You Feel Overwhelmed
- **Take a Break**: Close VS Code and come back later
- **Use Dashboard**: Navigate back to work via the dashboard links
- **Ask for Help**: Say "Let's pause and check the dashboard" or "I need to review this"

### Quick Commands to Remember
- Validate YAML: `python3 /config/scripts/validate_yaml.py /config`
- Check includes: `python3 /config/scripts/validate_yaml.py /config/includes`
- View current session: Open `AI_WORKSPACE/SHARED_CONTEXT/current_session.md`

### Emergency Stop
If anything feels wrong:
1. Don't apply the change
2. Close the file
3. Go to dashboard navigation
4. Take a break

Remember: This is your system. Take it at your pace. Copilot is here to help, not stress you.