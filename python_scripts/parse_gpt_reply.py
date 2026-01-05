file_path = "/config/chatgpt_response.txt"

try:
    with open(file_path, "r") as f:
        content = f.read().strip()
    if not content:
        content = "🛑 No content returned"
except Exception as e:
    content = f"⚠️ Parse error: {e}"

# Set conversational reply entity
hass.states.set("input_text.gpt_text_reply", content)

# Build log with prompt (if available)
prompt = data.get("prompt", "")
old_log = hass.states.get("input_text.gpt_log").state
new_entry = f"Prompt: {prompt}\nReply: {content}\n\n---\n" + old_log

# Trim to 5000 chars max
hass.services.call("input_text", "set_value", {
    "entity_id": "input_text.gpt_log",
    "value": new_entry[:5000]
})
