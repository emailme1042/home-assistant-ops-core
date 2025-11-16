# 🎯 What You Need to Do Next

## ⚠️ Step 1: Restart Home Assistant (REQUIRED)

**Why?** All the new automations, scripts, and intent handlers only load after a restart.

**How?**
1. In Home Assistant: **Settings** → **System** → **Restart**
2. Wait 1-2 minutes for HA to fully restart

---

## 🎙️ Step 2: Test TTS Flow (Dashboard Button)

**What?** Test that Alexa can speak messages triggered from the dashboard.

**How?**
1. Open: http://192.168.1.217:8123/lovelace-ai-navigation/0
2. Click the **"🎙️ TTS Test"** button
3. **Expected**: You should hear "This is a test of the AI voice system" on your Lounge Alexa

**If it doesn't work:**
- Check Developer Tools → States → `media_player.lounge_alexa` (make sure it's online)
- Check Developer Tools → States → `notify.alexa_media_lounge_alexa` (make sure it exists)
- If `notify.alexa_media_lounge_alexa` doesn't exist, the entity name might be different (e.g., `notify.alexa_media_echo_lounge`)

---

## 🗣️ Step 3: Test Voice Flow (Alexa Utterance)

**What?** Test that you can ask Alexa questions and get OpenAI responses.

**How?**
1. Say: **"Alexa, ask Home Assistant to query OpenAI about the weather"**
2. Wait 3-5 seconds
3. **Expected**: Alexa should speak back the OpenAI response

**If it doesn't work:**
- Check Developer Tools → States → `input_text.openai_query` (should contain your question)
- Check Developer Tools → States → `input_text.openai_response` (should contain the response or "Query sent")
- Check `rest_command.ask_openai` is configured correctly in `includes/rest_commands/rest.yaml`
- Check `!secret openai_bearer` is set in `secrets.yaml`

---

## 🔧 Step 4: Verify Dashboard Links (Optional)

**What?** Test that clicking links in the AI Navigation dashboard opens files in VSCode.

**How?**
1. Open: http://192.168.1.217:8123/lovelace-ai-navigation/0
2. Click any `vscode://file/...` link (e.g., "Current Session")
3. **Expected**: File should open in VSCode

**If it doesn't work:**
- Your browser may block `vscode://` links for security
- Alternative: Use the file paths shown and open manually in VSCode

---

## 🛠️ Settings You May Need to Change

### If `notify.alexa_media_lounge_alexa` doesn't exist:

1. Go to **Developer Tools** → **States**
2. Search for entities starting with `notify.alexa_media_`
3. Find your Lounge Alexa notify entity (e.g., `notify.alexa_media_echo_lounge`)
4. Edit `includes/intent_script.yaml` line 18:
   ```yaml
   - service: notify.alexa_media_lounge_alexa  # Change this to your actual entity
   ```
5. Restart HA again

### If `media_player.lounge_alexa` doesn't exist:

1. Go to **Developer Tools** → **States**
2. Search for entities starting with `media_player.`
3. Find your Lounge Alexa media player (e.g., `media_player.echo_lounge`)
4. Edit `includes/intent_script.yaml` line 28:
   ```yaml
   entity_id: media_player.lounge_alexa  # Change this to your actual entity
   ```
5. Restart HA again

### If OpenAI queries don't return responses:

**Problem**: Home Assistant's `rest_command` doesn't capture response data.

**Solution Options:**

1. **Install Extended OpenAI Conversation (Recommended)**:
   - Go to **HACS** → **Integrations** → Search "Extended OpenAI Conversation"
   - Install and configure with your OpenAI API key
   - This provides full OpenAI integration with response handling

2. **Create Python Script** (Advanced):
   - Ask me to create a Python script that calls OpenAI API and stores responses
   - This gives you full control over the integration

3. **Use Current Setup** (Limited):
   - Queries are sent to OpenAI, but responses aren't automatically captured
   - You'd see "Query sent" notifications only

---

## 📋 Quick Troubleshooting

### Problem: TTS doesn't work on Alexa
- **Check**: Alexa Media Player integration is installed and configured
- **Check**: Lounge Alexa device is online in HA
- **Try**: Restart HA after disabling/enabling Alexa Media Player integration
- **Fallback**: The intent_script includes automatic fallback to `media_player.play_media`

### Problem: Dashboard links don't open files
- **Browser blocks vscode:// links**: This is a security feature
- **Workaround**: Manually open files from the paths shown in the dashboard
- **Alternative**: Use file:/// links (but these may also be blocked)

### Problem: Alexa doesn't recognize the intent
- **Check**: Nabu Casa Cloud or Alexa Media Player is configured
- **Check**: `intent_script` is included in `configuration.yaml` (line 22)
- **Check**: Home Assistant is exposed to Alexa
- **Try**: Say "Alexa, discover devices" to refresh HA entities

---

## 📚 Reference Files

- **Setup Guide**: `S:\AI_WORKSPACE\SHARED_CONTEXT\openai_setup_guide.md`
- **Integration Overview**: `S:\SYSTEM_OVERVIEW\alexa_openai_integration.md`
- **Current Session**: `S:\AI_WORKSPACE\SHARED_CONTEXT\current_session.md`
- **AI Protocol**: `S:\AI_WORKSPACE\AI_README.md`

---

## 🆘 If You Get Stuck

1. **Check logs**: Configuration → Logs (look for errors related to intent_script, alexa, or openai)
2. **Ask GPT (Smart Home Ops Assistant)**: Share the error logs and ask for help
3. **Ask Edge Copilot**: Search for community solutions to similar issues
4. **Ask me (GitHub Copilot)**: Provide error details and I'll help debug

---

**Last Updated**: 2025-10-26  
**Status**: ✅ Ready for testing after restart
