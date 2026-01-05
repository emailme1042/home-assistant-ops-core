rest_commands = {
    "gpt_chatgpt_query": {"prompt": "Test GPT"},
    "gpt_create_backup": {"label": "Test Backup"},
    "gpt_reload_automations": None,
    "gpt_reload_scripts": None,
    "gpt_set_input_text": {
        "entity_id": "input_text.test", 
        "value": "Test Value"
    },
    "gpt_get_entity_state": {
        "entity_id": "input_text.chatgpt_prompt"
    },
    "ask_openai": {"prompt": "Hello GPT"},
    "jit_plugin_call": {
        "endpoint": "ping",
        "payload": "{}"
    },
    "jit_get_file_contents": {"path": "python_scripts/jit_plugin.py"},
    "jit_list_folder": {"path": "python_scripts"},
    "run_nas_script": {"prompt": "Test NAS"},
    "": None,
    "jit_write_file": {
        "path": "test.txt",
        "content": "Hello World",
        "confirm": True
    },
    "jit_reload_ha": None,
    "jit_run_script": {
        "script_name": "test_helpers.yaml"
    }
}

for cmd, data in rest_commands.items():
    try:
        service_data = data if data else {}
        hass.services.call("rest_command", cmd, service_data, blocking=True)
        logger.info(f"✅ {cmd} worked.")
    except Exception as e:
        logger.error(f"❌ {cmd} failed: {e}")
