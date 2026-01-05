# 🔊 Voice / Alexa Logic

## Overview
Alexa/OpenAI integration allows voice queries to be sent to OpenAI and responses spoken back via Alexa TTS.

## Files

### Automations
- **[TTS Response Automation](../includes/automations/tts_responses.yaml)** — Routes `speak_ai_response` events to Alexa TTS
  - Target: `notify.alexa_media_lounge_alexa`
  - Fallback: `media_player.play_media` if notify fails

### Scripts
- **[TTS Test Script](../scripts/tts_test_script.yaml)** — Manual TTS test trigger
- **[OpenAI Query Scripts](../includes/scripts/openai.yaml)** — `script.query_openai` and `script.query_openai_simple`

### Intent Handlers
- **[Intent Script](../includes/intent_script.yaml)** — Alexa intent handlers
  - `AskOpenAI` — "Alexa, ask Home Assistant to query OpenAI about {question}"
  - `SimpleOpenAIQuery` — Simple query without voice response

### Helper Entities
- **[GPT Input Texts](../includes/input_texts/gpt.yaml)** — `input_text.openai_query`, `input_text.openai_response`
- **[GPT Input Booleans](../includes/input_booleans/gpt.yaml)** — `input_boolean.openai_enabled`

## Flow Diagram

```
Jamie speaks to Alexa
  ↓
Alexa → HA intent_script.AskOpenAI
  ↓
script.query_openai → rest_command.ask_openai
  ↓
OpenAI API (GPT-4o)
  ↓
Response stored in input_text.openai_response
  ↓
notify.alexa_media_lounge_alexa (TTS)
  ↓ (fallback if notify fails)
media_player.play_media (lounge_alexa)
```

## Testing

### Dashboard
- [AI Navigation Dashboard](/lovelace-ai-navigation/0) — Includes TTS Test button

### Manual Test
1. Click "TTS Test" button in AI Navigation dashboard
2. Listen for test message on Lounge Alexa
3. Check `input_text.openai_response` for result

### Voice Test
1. Say: "Alexa, ask Home Assistant to query OpenAI about the weather"
2. Wait 3 seconds
3. Listen for response on Lounge Alexa

## Known Issues

### Alexa Media Player TTS (HA Core 2025.1–2025.2)
- **Issue**: Deprecated `notify.alexa_media_*` constants cause silent failures
- **Workaround**: Use `media_player.play_media` with TTS URI as fallback
- **Fix**: Restart HA after disabling/enabling Alexa Media Player integration

### Dual-Target TTS (Kitchen + Lounge)
- **Issue**: Parallel dispatch can cause silent failures
- **Workaround**: Use delay chaining (1–2s between targets)
- **Alternative**: Use Alexa "Everywhere" group (may include unwanted devices)

## Next Steps

1. **Restart Home Assistant** to load new automations and scripts
2. **Test TTS flow** using dashboard button
3. **Test voice flow** using Alexa utterance
4. **Add Kitchen Alexa** if dual-target TTS is desired (requires delay chaining)

## Tags
`#automation` `#alexa` `#openai` `#tts` `#voice` `#dashboard`
