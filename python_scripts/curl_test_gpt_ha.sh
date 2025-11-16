#!/bin/bash
echo "🔁 Testing /api/chatgpt_query"
curl -X POST http://192.168.1.203:5001/api/chatgpt_query \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Turn off hallway light"}'
echo -e "\n"

echo "🔁 Testing /api/backup"
curl -X POST http://192.168.1.203:5001/api/backup \
     -H "Content-Type: application/json" \
     -d '{"label": "Test backup"}'
echo -e "\n"

echo "🔁 Testing /api/reload_automations"
curl -X POST http://192.168.1.203:5001/api/reload_automations
echo -e "\n"

echo "🔁 Testing /api/reload_scripts"
curl -X POST http://192.168.1.203:5001/api/reload_scripts
echo -e "\n"

echo "🔁 Testing /api/input_text"
curl -X POST http://192.168.1.203:5001/api/input_text \
     -H "Content-Type: application/json" \
     -d '{"entity_id": "input_text.test", "value": "Test value"}'
echo -e "\n"

echo "🔁 Testing /api/entity_state"
curl -G http://192.168.1.203:5001/api/entity_state --data-urlencode "entity_id=input_text.chatgpt_prompt"
echo -e "\n"