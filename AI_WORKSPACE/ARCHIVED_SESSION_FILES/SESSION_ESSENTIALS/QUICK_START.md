# 🚀 Quick Start Guide for Jamie

## 🎯 I Just Opened VSCode — What Now?

### Step 1: Remember What We Were Doing
1. Open the **AI Navigation Dashboard** in Home Assistant: `http://homeassistant.local:8123/lovelace-system-overview/ai-navigation`
2. OR open `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` in VSCode
3. Read the "Current Status" and "Next Steps" sections

### Step 2: Continue Working
- If working with **GitHub Copilot** (me): Open relevant files and ask questions in chat
- If working with **GPT** 🧠: Drag `current_session.md` to GPT chat window
- If working with **Edge Copilot** 💬: Drag `current_session.md` to Edge browser

---

## 📤 How to Share Context with Other AIs

### To GPT (Smart Home Ops Assistant) 🧠
1. In VSCode, open `AI_WORKSPACE/SHARED_CONTEXT/current_session.md` (or any other context file)
2. **Drag the file** from VSCode to your GPT chat window
3. GPT can now read it and help with logic validation, HA compatibility, etc.

### To Edge Copilot 💬
1. In VSCode or File Explorer, open `AI_WORKSPACE/SHARED_CONTEXT/current_session.md`
2. **Drag the file** to your Edge browser window (anywhere on the page)
3. Edge Copilot can now read it and search docs/forums/bugs

---

## 🤔 Which AI Should I Ask?

| I Need Help With... | Ask This AI |
|---------------------|-------------|
| **Editing files, running scripts** | ⚙️ **Me** (GitHub Copilot in VSCode) |
| **Is this HA-compatible? Does this logic make sense?** | 🧠 **GPT** (Smart Home Ops Assistant) |
| **Find docs, forum posts, GitHub issues** | 💬 **Edge Copilot** |
| **Dashboard design patterns** | 🧠 **GPT** |
| **SYSTEM_OVERVIEW tagging** | 🧠 **GPT** |
| **What changed in HA version X?** | 🧠 **GPT** + 💬 **Edge Copilot** |

---

## 🧭 Important Files to Know

### Always Keep Updated
- `SHARED_CONTEXT/current_session.md` — **Where we are right now**
- `SHARED_CONTEXT/active_issues.md` — **What needs to be done**
- `SHARED_CONTEXT/system_status.md` — **Is everything working?**

### Reference When Needed
- `AI_README.md` — Full protocol for all 3 AIs
- `.github/copilot-instructions.md` — Instructions for me (GitHub Copilot)
- `copilot_session_template.md` — How to structure session notes

---

## ✅ Common Tasks

### Start a New Session
1. Open `current_session.md`
2. Update the "Goal" and "Current Status"
3. Ask me (GitHub Copilot): "Let's continue from current_session.md"

### Share Work with GPT or Edge Copilot
1. Update `current_session.md` or `active_issues.md` with questions
2. Drag file to GPT chat or Edge browser
3. Ask them your questions

### Check System Health
1. Open `SHARED_CONTEXT/system_status.md`
2. Ask me: "Run validators and update system_status.md"
3. Review results

### End a Session
1. Update `current_session.md` with what we accomplished
2. Update `recent_changes.md` with new entries
3. Move completed items from `active_issues.md` to "Resolved"

---

## 🆘 I'm Confused or Forgot Something

**Just ask any AI:**
- "What were we working on?" (I'll check `current_session.md`)
- "What did we change recently?" (I'll check `recent_changes.md`)
- "What needs to be done?" (I'll check `active_issues.md`)

**Or open the dashboard:**
- Go to: `http://homeassistant.local:8123/lovelace-system-overview/ai-navigation`

---

## 💡 Tips for Working with AIs

1. **Don't worry about typos** — All AIs are told to ask for clarification if unclear
2. **Use the dashboard** — It's there to help you navigate back to work
3. **Drag files to share** — Easier than copy/paste
4. **Ask which AI to use** — Any AI can tell you who's best for your question
5. **It's okay to forget** — That's why we have `current_session.md` and the dashboard

---

**Last Updated**: 2025-10-24  
**Made by**: ⚙️ GitHub Copilot (for Jamie)
