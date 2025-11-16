# 🤖 OpenAI Integration Guide — Alexa + Home Assistant

## ✅ What's Now Configured

### 1. Helper Entities Created
**Input Text** (`includes/input_texts/gpt.yaml`):
- `input_text.openai_query` — Your question for OpenAI
- `input_text.openai_response` — OpenAI's response (placeholder for now)
- Plus all GPT-related entities (gpt_text_prompt, chatgpt_prompt, etc.)

**Input Boolean** (`includes/input_booleans/gpt.yaml`):
- `input_boolean.openai_enabled` — Toggle OpenAI integration on/off
- Plus GPT workflow toggles

### 2. Scripts Created
**`script.query_openai`** (`includes/scripts/openai.yaml`):
- Calls `rest_command.ask_openai`
- Stores query in `input_text.openai_query`
- Creates notification when sent

**`script.query_openai_simple`**:
- Minimal version without parameters

### 3. Alexa Intent Handlers
**`intent_script`** (`includes/intent_script.yaml`):
- `AskOpenAI` intent — "Alexa, ask Home Assistant to query OpenAI about {question}"
- Sends to OpenAI and reads back response via Alexa TTS

### 4. REST Command (Already Exists)
**`rest_command.ask_openai`** (`includes/rest_commands/rest.yaml`):
- Configured to call OpenAI API
- Uses `!secret openai_bearer` for authentication

---

## ⚠️ Important Limitation

**Problem**: Home Assistant's `rest_command` doesn't return response data directly. It just sends the HTTP request.

**What This Means**: 
- The script will SEND your query to OpenAI ✅
- But it can't automatically capture the response ❌
- You'd see "Query sent" notifications, but no actual GPT answer

---

## 🔧 Two Solutions

### Option A: Use Python Script (Recommended)
Create a Python script that:
1. Calls OpenAI API
2. Parses JSON response
3. Stores result in `input_text.openai_response`

I can create this for you if you want.

### Option B: Use Extended OpenAI Conversation (HACS)
Install the HACS integration `extended-openai-conversation`:
- Full OpenAI integration with response handling
- Works with Assist pipeline
- Supports Alexa via conversation integration

**Recommendation**: Install `extended-openai-conversation` from HACS

---

## 📋 How to Test What's Working Now

### Test 1: Verify Helpers Exist
1. Restart Home Assistant
2. Go to Settings → Devices & Services → Helpers
3. Search for "openai" — should see `openai_query` and `openai_response`

### Test 2: Test the Script
1. In Developer Tools → Services
2. Call `script.query_openai`
3. Data: `{ "query": "What is 2+2?" }`
4. Check notifications — should see "Query sent"

### Test 3: Test REST Command Directly
1. Developer Tools → Services
2. Call `rest_command.ask_openai`
3. Data: `{ "prompt": "Hello GPT" }`
4. Check Home Assistant logs for HTTP 200 response

---

## 🎙️ Alexa Integration Steps

### Step 1: Enable Alexa Integration
1. Install Nabu Casa Cloud (if not already)
2. Or use Alexa Media Player custom component

### Step 2: Create Custom Intent (Nabu Casa Method)
1. In Alexa app → Skills → Your Skills → Dev Skills
2. Create new skill: "Home Query"
3. Add intent: `AskOpenAI`
4. Slot: `{question}` (AMAZON.SearchQuery type)
5. Sample utterances:
   - "ask home assistant to query openai about {question}"
   - "ask openai {question}"

### Step 3: Link to Home Assistant
1. In HA: Configuration → Cloud → Alexa
2. Expose `script.query_openai` to Alexa
3. Test: "Alexa, ask Home Query to ask OpenAI about the weather"

---

## 🚀 Next Steps — Choose Your Path

### Path 1: Full Working Solution (Recommended)
1. Install `extended-openai-conversation` from HACS
2. Configure with your OpenAI API key
3. Enable in Assist pipeline
4. Link Alexa to Assist
5. Say: "Alexa, ask Home Assistant: What's the weather like?"

### Path 2: Custom Python Script
1. I create a Python script to handle OpenAI API calls with response parsing
2. You get full control over prompts and formatting
3. More complex but more flexible

### Path 3: Keep Current Setup (Limited)
1. Use existing scripts to send queries
2. Check OpenAI directly for responses
3. No automatic Alexa readback

---

## 💡 Which Path Do You Want?

Reply with:
- **"Install extended OpenAI"** — I'll guide you through HACS install
- **"Create Python script"** — I'll build a working script with response handling
- **"Test current setup first"** — I'll help you verify what works now

---

**Files Modified This Session**:
- ✅ `includes/input_texts/gpt.yaml` (created)
- ✅ `includes/input_booleans/gpt.yaml` (created)
- ✅ `includes/scripts/openai.yaml` (created)
- ✅ `includes/intent_script.yaml` (created)
- ✅ `configuration.yaml` (added intent_script include)
- ✅ `includes/automations/dashboard.yaml` (fixed duplicate ID)

**Ready to test after Home Assistant restart!**
