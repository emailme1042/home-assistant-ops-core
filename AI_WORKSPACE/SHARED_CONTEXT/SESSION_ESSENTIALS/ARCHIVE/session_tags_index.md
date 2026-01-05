# 🏷️ Session Tags Index — AI Collaboration Reference

## 🎯 Session Management Tags

### Session Lifecycle
- `#session_start` — Beginning of new AI session, includes timestamp
- `#session_end` — Completion of session work, includes summary
- `#context_refresh` — When helping Jamie remember previous work

### Work Status Tags  
- `🟦 confirmed` — Changes validated and approved by Jamie
- `🌸 pending` — Work in progress, awaiting review
- `🟥 deprecated` — Outdated or rejected changes

### Activity Types
- `#backup` — System backup operations
- `#automation` — Automation creation/modification
- `#dashboard` — Dashboard design and updates
- `#recovery` — System recovery and troubleshooting
- `#validation` — YAML and system validation
- `#refactor` — Code cleanup and reorganization

### Communication Tags
- `#jamie_question` — When Jamie needs clarification
- `#ai_handoff` — Passing work between AI agents
- `#multi_ai` — Multi-agent collaboration sessions

## 📋 Usage Rules

### When to Use Session Tags
- **Every session**: Start with `#session_start`, end with `#session_end`
- **Every change**: Tag with appropriate work type (`#automation`, `#dashboard`, etc.)
- **Every validation**: Include `#validation` with results
- **Every question**: Use `#jamie_question` when clarification needed

### Status Tag Guidelines
- **🟦 confirmed**: Only after Jamie explicitly approves
- **🌸 pending**: Default for new work awaiting review
- **🟥 deprecated**: For outdated code or rejected approaches

### Multi-AI Coordination
- **#ai_handoff**: When VSCode Copilot passes work to GPT or Edge Copilot
- **#multi_ai**: When multiple AI agents working simultaneously
- **#context_refresh**: When bringing agents up to speed

## 🔍 Tag Examples in Practice

### Session Start Example
```
#session_start 2025-10-26 14:30
Jamie wants to create new irrigation automation
Context: Working on garden automation, need weather integration
```

### Work Documentation
```
#automation #validation 🌸 pending
Created irrigation_weather_check.yaml
- Triggers on weather forecast change
- Includes rain delay logic
- Needs testing with actual weather data
```

### Status Updates
```
#validation 🟦 confirmed
YAML validation passed, all entities verified
Jamie approved automation logic
Ready for production deployment
```

### Multi-AI Handoff
```
#ai_handoff #dashboard
VSCode Copilot created dashboard YAML structure
Passing to GPT for entity validation and logic review
Files: dashboards/garden/irrigation_control.yaml
```

## 📁 Active Session Essentials (Limit: 10)
```
active_issues.md   # Open issues & pending tasks
current_session.md   # Session goal, status, next steps
CONSOLIDATED_SESSION_STATUS.md   # Full session summary & achievements
system_status.md   # Health checks, validation results
recent_changes.md   # Last changes made
AI_AGENT_REFERENCE.md   # Multi-AI protocol & agent roles
AI_RESTART_VALIDATION_CHECKLIST.md   # Restart-safe checklist
NEXT_STEPS_FOR_JAMIE.md   # Jamie’s next actions
entity_reference.md   # Entity catalog for dashboards
AI_SYNC_STATUS.yaml   # Workspace sync sensor for dashboards
# The above are the 10 most essential session files. All others are archived or for reference only.
```

## 📊 Tag Tracking Benefits

### For Jamie
- Quick session history scanning
- Clear status of pending work
- Easy identification of completed vs incomplete tasks

### For AI Agents
- Consistent communication protocol
- Clear handoff procedures between agents
- Audit trail for decision making

### For System Health
- Validation coverage tracking
- Error recovery documentation
- Performance impact assessment

## 🔄 Session Workflow Integration

### Standard Session Pattern
1. `#session_start` + timestamp + goals
2. Work documentation with appropriate activity tags
3. Status updates as work progresses
4. `#validation` before any changes go live
5. Status confirmation (🟦/🌸/🟥) from Jamie
6. `#session_end` + summary + handoff notes

### Emergency Recovery Pattern
1. `#recovery` + issue description
2. `#backup` if system restore needed
3. Step-by-step troubleshooting with tags
4. `#validation` after each fix attempt
5. Final status and lessons learned

---

**Tag Categories**: 3 main types (session, status, activity)  
**Usage**: Required for all AI session documentation  
**Integration**: Used in copilot_session_notes.md and ai_exec_log.md  
**Purpose**: Consistent communication and audit trail across all AI agents