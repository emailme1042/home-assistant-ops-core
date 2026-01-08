"""
OpenAI HA Insight Script
Provides OpenAI with real-time HA system context for accurate troubleshooting and recommendations.
"""

import json
import logging
import requests

logger = logging.getLogger("openai_ha_insight")

def openai_ha_insight(hass, data):
    """Send HA system context to OpenAI for intelligent analysis."""

    # Get user prompt
    user_prompt = data.get('prompt', 'Analyze my Home Assistant system status')

    # Collect HA system context
    all_states = hass.states.all()
    total_entities = len(all_states)
    available_entities = len([s for s in all_states if s.state not in ['unavailable', 'unknown']])
    unavailable_entities = total_entities - available_entities

    # Get unavailable entities (first 20)
    unavailable_list = []
    for state in all_states:
        if state.state in ['unavailable', 'unknown']:
            unavailable_list.append(f"{state.entity_id}: {state.state}")
            if len(unavailable_list) >= 20:
                break

    # Get system health if available
    system_health = {}
    try:
        health_state = hass.states.get('sensor.home_assistant_system_health')
        if health_state:
            system_health = {
                'state': health_state.state,
                'attributes': dict(health_state.attributes)
            }
    except:
        pass

    # Get HA version
    ha_version = getattr(hass, 'version', 'unknown')

    # Build context summary
    context = f"""
Home Assistant System Status:
- Version: {ha_version}
- Total Entities: {total_entities}
- Available Entities: {available_entities}
- Unavailable Entities: {unavailable_entities}

Unavailable Entities Sample:
{chr(10).join(unavailable_list[:10])}

System Health: {json.dumps(system_health, indent=2)}

User Query: {user_prompt}

Please analyze this Home Assistant system and provide insights on what's working, what isn't, and what's required to fix issues.
"""

    # Get OpenAI API key from secrets
    try:
        api_key = hass.config['secrets']['openai_api_key']
    except:
        logger.error("OpenAI API key not found in secrets")
        return "Error: OpenAI API key not configured"

    # Call OpenAI API
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o",
                "messages": [
                    {"role": "user", "content": context}
                ],
                "temperature": 0.7,
                "max_tokens": 2000
            },
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            reply = result['choices'][0]['message']['content']
            
            # Set the response in an input_text for access
            hass.services.call(
                'input_text', 'set_value', {
                    'entity_id': 'input_text.openai_ha_insight_response',
                    'value': reply[:255]  # Limit to input_text max length
                }
            )
            
            return reply
        else:
            error_msg = f"OpenAI API error: {response.status_code} - {response.text}"
            hass.services.call(
                'input_text', 'set_value', {
                    'entity_id': 'input_text.openai_ha_insight_response',
                    'value': error_msg[:255]
                }
            )
            return error_msg

    except Exception as e:
        logger.error(f"Error calling OpenAI: {e}")
        error_msg = f"Error communicating with OpenAI: {str(e)}"
        hass.services.call(
            'input_text', 'set_value', {
                'entity_id': 'input_text.openai_ha_insight_response',
                'value': error_msg[:255]
            }
        )
        return error_msg