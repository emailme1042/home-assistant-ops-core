2025-08-16 23:57:26.883 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration browser_mod which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.884 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration alexa_media which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.886 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration scheduler which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.887 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration ha_registry which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.891 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration dwains_dashboard which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.893 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration meross_lan which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.895 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration notion_todo which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.896 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration hacs which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.897 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration govee_ble_hci which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.899 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration auto_backup which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.903 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration tapo_control which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.907 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration simpleicons which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.921 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration ai_automation_suggester which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.938 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration meross_cloud which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:26.943 WARNING (SyncWorker_0) [homeassistant.loader] We found a custom integration ble_monitor which has not been tested by Home Assistant. This component might cause stability problems, be sure to disable it if you experience issues with Home Assistant
2025-08-16 23:57:34.978 ERROR (MainThread) [homeassistant.components.sensor] The file platform for the sensor integration does not support platform setup. Please remove it from your config.
2025-08-16 23:57:34.980 ERROR (MainThread) [homeassistant.components.sensor] The file platform for the sensor integration does not support platform setup. Please remove it from your config.
2025-08-16 23:57:35.314 ERROR (MainThread) [homeassistant.components.script] Script with object id 'service' could not be validated and has been disabled: expected a dictionary. Got 'shell_command.run_gpt_via_flask'
2025-08-16 23:57:35.318 ERROR (MainThread) [homeassistant.components.script] Script with object id 'data' could not be validated and has been disabled: extra keys not allowed @ data['prompt']. Got "Summarize today's automation changes"
required key not provided @ data['sequence']. Got None
2025-08-16 23:57:38.994 WARNING (ImportExecutor_0) [py.warnings] /usr/local/lib/python3.13/site-packages/google/**init**.py:2: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
**import**('pkg_resources').declare_namespace(**name**)

2025-08-16 23:57:58.359 ERROR (MainThread) [homeassistant.components.google_cloud.tts] Error from calling list_voices: 403 Cloud Text-to-Speech API has not been used in project 241591379082 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview?project=241591379082 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry. [reason: "SERVICE_DISABLED"
domain: "googleapis.com"
metadata {
key: "service"
value: "texttospeech.googleapis.com"
}
metadata {
key: "serviceTitle"
value: "Cloud Text-to-Speech API"
}
metadata {
key: "containerInfo"
value: "241591379082"
}
metadata {
key: "consumer"
value: "projects/241591379082"
}
metadata {
key: "activationUrl"
value: "https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview?project=241591379082"
}
, locale: "en-US"
message: "Cloud Text-to-Speech API has not been used in project 241591379082 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview?project=241591379082 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry."
, links {
description: "Google developers console API activation"
url: "https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview?project=241591379082"
}
]
2025-08-16 23:57:58.838 ERROR (MainThread) [homeassistant.components.automation] Automation with alias 'Sync AI Exec Log Snapshot' failed to setup triggers and has been disabled: must be a value between 0 and 59 for dictionary value @ data['minutes']. Got None
2025-08-16 23:57:58.843 ERROR (MainThread) [homeassistant.components.automation] Automation with alias 'Log GPT Session with Fallback' could not be validated and has been disabled: extra keys not allowed @ data['actions'][3]['choose'][1]['default']. Got [{'service': 'shell_command.log_gpt_session_fallback'}]
required key not provided @ data['actions'][3]['choose'][1]['conditions']. Got None
required key not provided @ data['actions'][3]['choose'][1]['sequence']. Got None
2025-08-16 23:58:00.370 ERROR (MainThread) [homeassistant.components.automation] Platform automation does not generate unique IDs. ID git_sync_failure_alert already exists - ignoring automation.git_sync_failure_alert
2025-08-16 23:58:11.461 ERROR (MainThread) [homeassistant.helpers.event] Error while processing template: Template<template=({% set path = '/SYSTEM_OVERVIEW/ai_exec_log.md' %} {% set last_mod = as_timestamp(states('sensor.file_last_modified')) %} {% set now = as_timestamp(now()) %} {% if (now - last_mod) > 86400 %}
stale
{% else %}
fresh
{% endif %}) renders=2>
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 2209, in forgiving_as_timestamp
return dt_util.as_timestamp(value)
~~~~~~~~~~~~~~~~~~~~^^^^^^^
File "/usr/src/homeassistant/homeassistant/util/dt.py", line 155, in as_timestamp
raise ValueError("not a valid date/time.")
ValueError: not a valid date/time.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 641, in async_render
render_result = \_render_with_context(self.template, compiled, **kwargs)
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 2977, in \_render_with_context
return template.render(**kwargs)
~~~~~~~~~~~~~~~^^^^^^^^^^
File "/usr/local/lib/python3.13/site-packages/jinja2/environment.py", line 1295, in render
self.environment.handle_exception()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
File "/usr/local/lib/python3.13/site-packages/jinja2/environment.py", line 942, in handle_exception
raise rewrite_traceback_stack(source=source)
File "<template>", line 1, in top-level template code
File "/usr/local/lib/python3.13/site-packages/jinja2/sandbox.py", line 401, in call
return **context.call(**obj, \*args, \*\*kwargs)
~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 2212, in forgiving_as_timestamp
raise_no_default("as_timestamp", value)
~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 1975, in raise_no_default
raise ValueError(
...<2 lines>...
)
ValueError: Template error: as_timestamp got invalid input 'unknown' when rendering template '{% set path = '/SYSTEM_OVERVIEW/ai_exec_log.md' %} {% set last_mod = as_timestamp(states('sensor.file_last_modified')) %} {% set now = as_timestamp(now()) %} {% if (now - last_mod) > 86400 %}
stale
{% else %}
fresh
{% endif %}' but no default was specified

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 758, in async_render_to_info
render_info.\_result = self.async_render( # noqa: SLF001
~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
variables, strict=strict, log_fn=log_fn, \*\*kwargs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
)
^
File "/usr/src/homeassistant/homeassistant/helpers/template.py", line 643, in async_render
raise TemplateError(err) from err
homeassistant.exceptions.TemplateError: ValueError: Template error: as_timestamp got invalid input 'unknown' when rendering template '{% set path = '/SYSTEM_OVERVIEW/ai_exec_log.md' %} {% set last_mod = as_timestamp(states('sensor.file_last_modified')) %} {% set now = as_timestamp(now()) %} {% if (now - last_mod) > 86400 %}
stale
{% else %}
fresh
{% endif %}' but no default was specified
2025-08-16 23:58:11.481 ERROR (MainThread) [homeassistant.components.template.template_entity] TemplateError('ValueError: Template error: as_timestamp got invalid input 'unknown' when rendering template '{% set path = '/SYSTEM_OVERVIEW/ai_exec_log.md' %} {% set last_mod = as_timestamp(states('sensor.file_last_modified')) %} {% set now = as_timestamp(now()) %} {% if (now - last_mod) > 86400 %}
stale
{% else %}
fresh
{% endif %}' but no default was specified') while processing template 'Template<template=({% set path = '/SYSTEM_OVERVIEW/ai_exec_log.md' %} {% set last_mod = as_timestamp(states('sensor.file_last_modified')) %} {% set now = as_timestamp(now()) %} {% if (now - last_mod) > 86400 %}
stale
{% else %}
fresh
{% endif %}) renders=4>' for attribute '\_attr_native_value' in entity 'sensor.copilot_log_stale'
2025-08-16 23:58:23.511 INFO (MainThread) [homeassistant.components.automation.ai_workspace_access_toggle] Initialized trigger AI Workspace Access Toggle
2025-08-16 23:58:23.511 INFO (MainThread) [homeassistant.components.automation.add_task_from_dashboard] Initialized trigger Add Task from Dashboard
2025-08-16 23:58:23.511 INFO (MainThread) [homeassistant.components.automation.esp_offline_alert] Initialized trigger ESP Offline Alert
2025-08-16 23:58:23.512 INFO (MainThread) [homeassistant.components.automation.log_esp_restart_reason] Log ESP Restart Reason: Running automation actions
2025-08-16 23:58:23.512 INFO (MainThread) [homeassistant.components.automation.log_esp_restart_reason] Log ESP Restart Reason: Executing step call service
2025-08-16 23:58:23.512 INFO (MainThread) [homeassistant.components.automation.log_esp_restart_reason] Initialized trigger Log ESP Restart Reason
2025-08-16 23:58:23.512 INFO (MainThread) [homeassistant.components.automation.send_gpt_prompt_from_direct_input] Initialized trigger Send GPT Prompt from Direct Input
2025-08-16 23:58:23.512 INFO (MainThread) [homeassistant.components.automation.email_long_gpt_reply] Initialized trigger Email Long GPT Reply
2025-08-16 23:58:23.513 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-16 23:58:23.513 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-16 23:58:23.513 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Initialized trigger Run YAML Validation & Log Result
2025-08-16 23:58:23.513 INFO (MainThread) [homeassistant.components.automation.add_to_do_via_dashboard] Initialized trigger Add To-Do via Dashboard
2025-08-16 23:58:23.513 INFO (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge_2] Initialized trigger Start Lounge HomeKit Bridge
2025-08-16 23:58:23.514 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files_2] Initialized trigger Save Latest Email Content to Files
2025-08-16 23:58:23.514 INFO (MainThread) [homeassistant.components.automation.alert_if_wsl_restart_marker_missing] Initialized trigger Alert if WSL Restart Marker Missing
2025-08-16 23:58:23.514 INFO (MainThread) [homeassistant.components.automation.git_sync_missed] Initialized trigger ⚠️ Git Sync Missed
2025-08-16 23:58:23.515 INFO (MainThread) [homeassistant.components.automation.notify_if_git_sync_stale_2] Initialized trigger Notify if Git Sync Stale
2025-08-16 23:58:23.515 INFO (MainThread) [homeassistant.components.automation.git_sync_failure_alert] Initialized trigger 🚨 Git Sync Failure Alert
2025-08-16 23:58:23.515 INFO (MainThread) [homeassistant.components.automation.ensure_gpt_status_file_permissions] Initialized trigger Ensure GPT Status File Permissions
2025-08-16 23:58:23.519 WARNING (SyncWorker_7) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-16 23:58:23.555 INFO (MainThread) [homeassistant.components.automation.enable_entities_dashboard] Initialized trigger Enable Entities Dashboard
2025-08-16 23:58:23.555 INFO (MainThread) [homeassistant.components.automation.disable_entities_dashboard] Initialized trigger Disable Entities Dashboard
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.re_ask_chatgpt] Initialized trigger Re-Ask ChatGPT
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.notify_system_update_available] Initialized trigger Notify System Update Available
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.backup_success_reminder] Initialized trigger Backup Success Reminder
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.notify_of_stale_updates] Initialized trigger Notify of Stale Updates
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.notify_backup_created] Initialized trigger Notify Backup Created
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.run_gpt_when_prompt_changes] Initialized trigger Run GPT when prompt changes
2025-08-16 23:58:23.556 INFO (MainThread) [homeassistant.components.automation.announce_gpt_reply] Initialized trigger Announce GPT reply
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.push_gpt_reply_to_mobile] Initialized trigger Push GPT reply to mobile
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.remind_vpn_on_for_streaming] Initialized trigger Remind VPN on for streaming
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.auto_bedtime_scene] Initialized trigger Auto Bedtime Scene
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.start_party_music_when_party_mode_scene_activated] Initialized trigger Start Party Music when Party Mode Scene Activated
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.announce_movie_night] Initialized trigger Announce Movie Night
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.play_relaxing_sound_when_relax_scene_activated] Initialized trigger Play Relaxing Sound when Relax Scene Activated
2025-08-16 23:58:23.557 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Initialized trigger Update Dashboard List
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.github_auto_pull_on_commit_change] Initialized trigger GitHub Auto Pull on Commit Change
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_light_on_with_motion] Initialized trigger Kitchen Light On With Motion
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_light_off_after_no_motion] Initialized trigger Kitchen Light Off After No Motion
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_fan_on_if_hot_and_motion] Initialized trigger Kitchen Fan On If Hot And Motion
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_fan_off_after_no_motion_or_cool] Initialized trigger Kitchen Fan Off After No Motion Or Cool
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_blinds_open_morning_gradual] Initialized trigger Kitchen Blinds Open Morning (Gradual)
2025-08-16 23:58:23.558 INFO (MainThread) [homeassistant.components.automation.kitchen_blinds_close_evening_gradual] Initialized trigger Kitchen Blinds Close Evening (Gradual)
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.kitchen_window_open_alert] Initialized trigger Kitchen Window Open Alert
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.alexa_kitchen_afternoon_greeting] Initialized trigger Alexa Kitchen Afternoon Greeting
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger_shell] Initialized trigger GPT Conversational Text Trigger (Shell)
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.run_nas_script_from_chatgpt_prompt] Initialized trigger Run NAS Script from ChatGPT Prompt
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.mark_gpt_as_sent] Initialized trigger Mark GPT as Sent
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.admin_gpt_mark_as_sent] Initialized trigger Admin GPT Mark as Sent
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.admin_gpt_reply_complete] Initialized trigger Admin GPT Reply Complete
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] Initialized trigger GPT Conversational Text Trigger
2025-08-16 23:58:23.559 INFO (MainThread) [homeassistant.components.automation.notify_on_git_sync_trigger] Initialized trigger Notify on Git Sync Trigger
2025-08-16 23:58:23.560 INFO (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge] Start Lounge HomeKit Bridge: Running automation actions
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge] Start Lounge HomeKit Bridge: Executing step delay 0:00:30
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge] Initialized trigger Start Lounge HomeKit Bridge
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.run_kodi_ai_when_prompt_is_updated] Initialized trigger Run Kodi AI when Prompt is Updated
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.alert_if_jit_plugin_goes_offline] Initialized trigger Alert if JIT Plugin goes offline
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] Initialized trigger 🔁 Auto-reload sensors and templates on file change
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.alert_if_wsl_restart_marker_missing_2] Initialized trigger Alert if WSL Restart Marker Missing
2025-08-16 23:58:23.561 INFO (MainThread) [homeassistant.components.automation.sync_git_to_ha_on_startup] Sync Git to HA on startup: Running automation actions
2025-08-16 23:58:23.562 INFO (MainThread) [homeassistant.components.automation.sync_git_to_ha_on_startup] Sync Git to HA on startup: Executing step call service
2025-08-16 23:58:23.519 ERROR (SyncWorker_7) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-16 23:58:23.573 INFO (MainThread) [homeassistant.components.automation.sync_git_to_ha_on_startup] Initialized trigger Sync Git to HA on startup
2025-08-16 23:58:23.574 INFO (MainThread) [homeassistant.components.automation.git_sync_missed_2] Initialized trigger ⚠️ Git Sync Missed
2025-08-16 23:58:23.574 INFO (MainThread) [homeassistant.components.automation.notify_if_git_sync_stale] Initialized trigger Notify if Git Sync Stale
2025-08-16 23:58:23.574 INFO (MainThread) [homeassistant.components.automation.auto_git_sync_every_6_hours] Initialized trigger 🔁 Auto Git Sync Every 6 Hours
2025-08-16 23:58:23.574 INFO (MainThread) [homeassistant.components.automation.notify_oversized_input_text] Initialized trigger Notify Oversized Input Text
2025-08-16 23:58:23.574 INFO (MainThread) [homeassistant.components.automation.send_home_assistant_startup_report] Send Home Assistant Startup Report: Running automation actions
2025-08-16 23:58:23.575 INFO (MainThread) [homeassistant.components.automation.send_home_assistant_startup_report] Send Home Assistant Startup Report: Executing step call service
2025-08-16 23:58:23.576 INFO (MainThread) [homeassistant.components.automation.send_home_assistant_startup_report] Initialized trigger Send Home Assistant Startup Report
2025-08-16 23:58:23.576 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Initialized trigger Save Latest Email Content to Files
2025-08-16 23:58:23.576 INFO (MainThread) [homeassistant.components.automation.react_to_gpt_context_change] Initialized trigger React to GPT Context Change
2025-08-16 23:58:23.577 INFO (MainThread) [homeassistant.components.automation.reload_automations_after_startup] Reload Automations After Startup: Running automation actions
2025-08-16 23:58:23.577 INFO (MainThread) [homeassistant.components.automation.reload_automations_after_startup] Reload Automations After Startup: Executing step call service
2025-08-16 23:58:23.577 INFO (MainThread) [homeassistant.components.automation.reload_automations_after_startup] Initialized trigger Reload Automations After Startup
2025-08-16 23:58:23.577 INFO (MainThread) [homeassistant.components.automation.log_gpt_context_change] Initialized trigger Log GPT Context Change
2025-08-16 23:58:23.673 WARNING (MainThread) [homeassistant.components.kodi.media_player] Unable to connect to Kodi via websocket
2025-08-16 23:58:23.681 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-16 23:58:23.746 ERROR (MainThread) [homeassistant.components.homekit] HomeKit Front Door Live view cannot startup: entity not available: {'exclude_domains': [], 'exclude_entities': [], 'include_domains': [], 'include_entities': ['camera.front_door_live_view'], 'include_entity_globs': [], 'exclude_entity_globs': []}
2025-08-16 23:58:23.873 ERROR (MainThread) [homeassistant.components.automation] Automation with alias 'Sync AI Exec Log Snapshot' failed to setup triggers and has been disabled: must be a value between 0 and 59 for dictionary value @ data['minutes']. Got None
2025-08-16 23:58:23.875 ERROR (MainThread) [homeassistant.components.automation] Automation with alias 'Log GPT Session with Fallback' could not be validated and has been disabled: extra keys not allowed @ data['actions'][3]['choose'][1]['default']. Got [{'service': 'shell_command.log_gpt_session_fallback'}]
required key not provided @ data['actions'][3]['choose'][1]['conditions']. Got None
required key not provided @ data['actions'][3]['choose'][1]['sequence']. Got None
2025-08-16 23:58:24.037 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.auto_bedtime_scene as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.037 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.start_party_music_when_party_mode_scene_activated as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.announce_movie_night as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.play_relaxing_sound_when_relax_scene_activated as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.update_dashboard_list as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.github_auto_pull_on_commit_change as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_light_on_with_motion as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_light_off_after_no_motion as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_fan_on_if_hot_and_motion as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_fan_off_after_no_motion_or_cool as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_blinds_open_morning_gradual as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_blinds_close_evening_gradual as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.kitchen_window_open_alert as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.alexa_kitchen_afternoon_greeting as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.gpt_conversational_text_trigger_shell as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.run_nas_script_from_chatgpt_prompt as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.mark_gpt_as_sent as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.admin_gpt_mark_as_sent as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.admin_gpt_reply_complete as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.gpt_conversational_text_trigger as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.notify_on_git_sync_trigger as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.start_lounge_homekit_bridge as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.run_kodi_ai_when_prompt_is_updated as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.alert_if_jit_plugin_goes_offline as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.auto_reload_sensors_and_templates_on_file_change as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.alert_if_wsl_restart_marker_missing_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.sync_git_to_ha_on_startup as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.git_sync_missed_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.notify_if_git_sync_stale as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.auto_git_sync_every_6_hours as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.notify_oversized_input_text as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.send_home_assistant_startup_report as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.save_latest_email_content_to_files as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.react_to_gpt_context_change as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.reload_automations_after_startup as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.log_gpt_context_change as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_ddf0 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_ddf0_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_ddf0_light as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.blind_tilt_94a1_light_level as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bot_181f as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_e2bb as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_e2bb_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.contact_sensor_e2bb_light as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.038 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.gvh5105_6172_estimated_distance as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bot_253f as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5075_d927_temperature as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5075_d927_humidity as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5075_d927_battery as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5075_d927_signal_strength as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_7058_temperature as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_7058_humidity as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_7058_battery as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_7058_signal_strength as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_6172_temperature as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_6172_humidity as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_6172_battery as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.h5105_6172_signal_strength as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ai_automation_suggestions_openai as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.bangbangbangoo7 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.swapped3843 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.cryingful as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.dacfamportal_security_status as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_cpu_utilisation_user as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_cpu_utilisation_total as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_cpu_load_average_5_min as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_cpu_load_average_15_min as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_memory_usage_real as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_memory_available_swap as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_memory_available_real as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_memory_total_swap as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_memory_total_real as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_upload_throughput as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_download_throughput as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_volume_1_status as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_volume_1_used_space as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.dacfamportal_volume_1_volume_used as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.dacfamportal_surveillance_station_home_mode as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.kitchen_window_contact_sensor_door as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.kitchen_fan_energy as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.kitchen_fan_energy_difference as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.kitchen_fan_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.sonoff_swv_volume_flow_rate as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.sonoff_swv as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.dashboard_builder as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.dashboard_tweaker as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.entity_fixer as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.ask_ai as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.admin_ai_tools as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.039 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.govee_to_mqtt_purge_caches as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add scene.govee_to_mqtt_one_click_default_copytest_tap_to_run as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add scene.govee_to_mqtt_one_click_default_test_tap_to_run as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add humidifier.humidifier as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.humidifier_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.humidifier_activate_mode_auto as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.humidifier_activate_mode_custom as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.humidifier_nightlight_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bedroom_fan_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bedroom_fan_oscillation_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.bedroom_fan_activate_mode_auto as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.bedroom_fan_activate_mode_custom as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bedroom_strip_lights_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.bedroom_strip_lights_gradient_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.basic_group_control_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.scenic_dreamview3_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.lounge_tv_strip_lights_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.lounge_tv_strip_lights_gradient_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.lounge_tv_strip_lights_dream_view_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.lounge_fan_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.lounge_fan_oscillation_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.lounge_fan_activate_mode_auto as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add button.lounge_fan_activate_mode_custom as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.teddys_strip_light_power_switch as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.teddys_strip_light_gradient_toggle as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add switch.basic_group_control_power_switch_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.revoke_user_access as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.enable_all_dashboards as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.script as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add script.fields as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.tv_lounge_tv_ad07_estimated_distance as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_fbe2a9be_141b192a as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_f762ea30_8842e63e as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_b09bc7f5_072f879b as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.gvh5075_d927_estimated_distance as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.universal_remote_rf_temperature as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.universal_remote_rf_humidity as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.gvh5105_7058_estimated_distance as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_804093b6_c8d4067c as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_f54cb36d_a95625c4 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_0580196b_0694cb94 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_8e389cd9_c559fcc5 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.entity_watchdog_last_run as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.040 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.gpt_summary_preview as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.aqara_vibration_sensor_occupancy as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.aqara_door_and_window_sensor_door as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.aqara_door_and_window_sensor_door_2 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.aqara_door_and_window_sensor_door_3 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.aqara_water_leak_sensor_water_leak as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.041 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_d026456c_82f6c2b9 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_ae6fe47c_b6d8c971 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_e9b0daf9_f8bbcd51 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_471c0d04_7fce5c65 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_f7cde70a_af8ad977 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_75cef63e_4919f2c0 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_950aad24_bbdcc40b as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add automation.run_yaml_validation_log_result as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_b212cd6e_5ae06ca0 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.cast as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_25811f86_457c9e11 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_dbae1aa6_8a17f6dd as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add binary_sensor.browser_mod_fccf5905_2309fe23 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.s8f98a7e80f726accc_2708_estimated_distance as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_temperature_d33038367058 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.065 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_humidity_d33038367058 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.066 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_temperature_c83038366172 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.066 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_humidity_c83038366172 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.066 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_temperature_a4c138dad927 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.066 WARNING (MainThread) [homeassistant.components.homekit] Cannot add sensor.ble_humidity_a4c138dad927 as this would exceed the 150 device limit. Consider using the filter option
2025-08-16 23:58:24.213 INFO (MainThread) [homeassistant.components.automation.git_sync_failure_alert] Initialized trigger 🚨 Git Sync Failure Alert
2025-08-16 23:58:24.214 ERROR (MainThread) [homeassistant.components.automation] Platform automation does not generate unique IDs. ID git_sync_failure_alert already exists - ignoring automation.git_sync_failure_alert
2025-08-16 23:58:24.374 ERROR (MainThread) [homeassistant.components.homekit.util] media_player.tv_lounge_tv does not support any media_player features
2025-08-16 23:58:24.374 ERROR (MainThread) [homeassistant.components.homekit.util] media_player.tv_bedroom_tv does not support any media_player features
2025-08-16 23:58:24.512 ERROR (MainThread) [homeassistant.components.shell_command] Error running command: `bash /config/scripts/git_auto_sync.sh from-git`, return code: 127
NoneType: None
2025-08-16 23:58:24.749 WARNING (Recorder) [homeassistant.components.recorder.db_schema] State attributes for sensor.fire_tab_active_notification_count exceed maximum size of 16384 bytes. This can cause database performance issues; Attributes will not be stored
2025-08-16 23:58:24.776 WARNING (Recorder) [homeassistant.components.recorder.db_schema] State attributes for sensor.ai_automation_suggestions_openai exceed maximum size of 16384 bytes. This can cause database performance issues; Attributes will not be stored
2025-08-16 23:58:25.178 WARNING (MainThread) [homeassistant.components.kodi.media_player] Unable to connect to Kodi via websocket
2025-08-16 23:58:27.200 WARNING (MainThread) [homeassistant.components.kodi.media_player] Unable to connect to Kodi via websocket
2025-08-16 23:58:28.343 WARNING (Recorder) [homeassistant.components.recorder.db_schema] State attributes for sensor.fire_tab_active_notification_count exceed maximum size of 16384 bytes. This can cause database performance issues; Attributes will not be stored
2025-08-16 23:58:29.094 WARNING (Recorder) [homeassistant.components.recorder.db_schema] State attributes for sensor.ai_automation_suggestions_openai exceed maximum size of 16384 bytes. This can cause database performance issues; Attributes will not be stored
2025-08-16 23:58:44.895 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Running automation actions
2025-08-16 23:58:44.895 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Executing step call service
2025-08-16 23:58:45.502 ERROR (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Error executing script. Error for call_service at pos 1: Device not connected to local push notifications
2025-08-16 23:58:45.508 ERROR (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Error while executing automation automation.save_latest_email_content_to_files: Device not connected to local push notifications
2025-08-16 23:58:53.565 INFO (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge] Start Lounge HomeKit Bridge: Executing step call service
2025-08-16 23:58:53.567 ERROR (MainThread) [homeassistant.components.automation.start_lounge_homekit_bridge] Start Lounge HomeKit Bridge: Error executing script. Service not found for call_service at pos 2: Action homekit.start not found
2025-08-17 00:00:00.188 WARNING (MainThread) [homeassistant.components.automation] Error evaluating condition in '⚠️ Git Sync Missed':
In 'condition':
In 'template' condition: TemplateRuntimeError: No filter named 'file_exists' found.
2025-08-17 00:00:00.198 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Running automation actions
2025-08-17 00:00:00.199 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Executing step call service
2025-08-17 00:00:00.217 WARNING (MainThread) [homeassistant.components.automation] Error evaluating condition in '⚠️ Git Sync Missed':
In 'condition':
In 'template' condition: ValueError: Template error: as_timestamp got invalid input 'unknown' when rendering template '{% set mod = (as_timestamp(now()) - as_timestamp(states('sensor.git_sync_last'))) %} {{ mod > 1900 }}' but no default was specified
2025-08-17 00:00:00.244 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-17 00:00:00.244 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:00:00.254 WARNING (SyncWorker_6) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-17 00:00:00.257 ERROR (SyncWorker_6) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-17 00:00:00.263 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:00:00.387 INFO (MainThread) [homeassistant.components.automation.auto_git_sync_every_6_hours] 🔁 Auto Git Sync Every 6 Hours: Running automation actions
2025-08-17 00:00:00.388 INFO (MainThread) [homeassistant.components.automation.auto_git_sync_every_6_hours] 🔁 Auto Git Sync Every 6 Hours: Executing step call service
2025-08-17 00:00:00.421 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Running automation actions
2025-08-17 00:00:00.421 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:00:00.424 INFO (MainThread) [homeassistant.components.automation.notify_oversized_input_text] Notify Oversized Input Text: Running automation actions
2025-08-17 00:00:00.424 INFO (MainThread) [homeassistant.components.automation.notify_oversized_input_text] Notify Oversized Input Text: Executing step call service
2025-08-17 00:00:00.425 ERROR (MainThread) [homeassistant.components.automation.notify_oversized_input_text] Notify Oversized Input Text: Error executing script. Service not found for call_service at pos 1: Action notify.your_gmail_address not found
2025-08-17 00:00:00.503 INFO (MainThread) [homeassistant.components.automation.notify_of_stale_updates] Notify of Stale Updates: Running automation actions
2025-08-17 00:00:00.503 INFO (MainThread) [homeassistant.components.automation.notify_of_stale_updates] Notify of Stale Updates: Executing step call service
2025-08-17 00:00:00.519 WARNING (MainThread) [homeassistant.components.automation] Error evaluating condition in 'Backup Success Reminder':
In 'condition':
In 'template' condition: TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'float'
2025-08-17 00:00:00.605 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:00:00.605 ERROR (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Error executing script. Service not found for call_service at pos 2: Action homeassistant.reload_template_entities not found
2025-08-17 00:00:10.457 WARNING (Recorder) [homeassistant.components.sensor.recorder] The unit of sensor.fire_tab_active_notification_count (None) cannot be converted to the unit of previously compiled statistics (notifications). Generation of long term statistics will be suppressed unless the unit changes back to notifications or a compatible unit. Go to https://my.home-assistant.io/redirect/developer_statistics to fix this
2025-08-17 00:05:00.199 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Running automation actions
2025-08-17 00:05:00.199 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Executing step call service
2025-08-17 00:05:00.254 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-17 00:05:00.255 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:05:00.260 WARNING (SyncWorker_5) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-17 00:05:00.260 ERROR (SyncWorker_5) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-17 00:05:00.269 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:05:00.410 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Running automation actions
2025-08-17 00:05:00.410 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:05:00.463 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:05:00.463 ERROR (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Error executing script. Service not found for call_service at pos 2: Action homeassistant.reload_template_entities not found
2025-08-17 00:10:00.198 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Running automation actions
2025-08-17 00:10:00.198 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Executing step call service
2025-08-17 00:10:00.253 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-17 00:10:00.253 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:10:00.259 WARNING (SyncWorker_9) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-17 00:10:00.259 ERROR (SyncWorker_9) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-17 00:10:00.269 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:10:00.403 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Running automation actions
2025-08-17 00:10:00.404 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:10:00.470 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:10:00.470 ERROR (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Error executing script. Service not found for call_service at pos 2: Action homeassistant.reload_template_entities not found
2025-08-17 00:15:00.217 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Running automation actions
2025-08-17 00:15:00.218 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Executing step call service
2025-08-17 00:15:00.247 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-17 00:15:00.247 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:15:00.251 WARNING (SyncWorker_1) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-17 00:15:00.251 ERROR (SyncWorker_1) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-17 00:15:00.258 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:15:00.403 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Running automation actions
2025-08-17 00:15:00.403 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:15:01.618 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:15:01.618 ERROR (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Error executing script. Service not found for call_service at pos 2: Action homeassistant.reload_template_entities not found
2025-08-17 00:17:15.766 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Running automation actions
2025-08-17 00:17:15.767 INFO (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Executing step call service
2025-08-17 00:17:16.132 ERROR (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Save Latest Email Content to Files: Error executing script. Error for call_service at pos 1: Device not connected to local push notifications
2025-08-17 00:17:16.135 ERROR (MainThread) [homeassistant.components.automation.save_latest_email_content_to_files] Error while executing automation automation.save_latest_email_content_to_files: Device not connected to local push notifications
2025-08-17 00:17:55.914 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger_shell] GPT Conversational Text Trigger (Shell): Running automation actions
2025-08-17 00:17:55.915 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger_shell] GPT Conversational Text Trigger (Shell): Executing step call service
2025-08-17 00:17:55.916 INFO (MainThread) [homeassistant.components.script.chatgpt_convo_query] Send Conversational Prompt to GPT (Shell Command): Running script sequence
2025-08-17 00:17:55.917 INFO (MainThread) [homeassistant.components.script.chatgpt_convo_query] Send Conversational Prompt to GPT (Shell Command): Executing step call service
2025-08-17 00:17:55.920 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Running automation actions
2025-08-17 00:17:55.920 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Executing step call service
2025-08-17 00:17:55.920 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Executing step call service
2025-08-17 00:17:55.925 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Executing step call service
2025-08-17 00:17:55.925 INFO (MainThread) [homeassistant.components.script.chatgpt_query] Send GPT Prompt (Admin): Running script sequence
2025-08-17 00:17:55.926 INFO (MainThread) [homeassistant.components.script.chatgpt_query] Send GPT Prompt (Admin): Executing step call service
2025-08-17 00:17:55.926 INFO (MainThread) [homeassistant.components.script.chatgpt_query] Send GPT Prompt (Admin): Executing step call service
2025-08-17 00:17:55.945 INFO (MainThread) [homeassistant.components.script.chatgpt_convo_query] Send Conversational Prompt to GPT (Shell Command): Executing step delay 0:00:03
2025-08-17 00:17:56.173 WARNING (MainThread) [homeassistant.components.rest_command] Error. Url: https://api.openai.com/v1/chat/completions. Status code 401. Payload: b'{\n "model": "gpt-4o",\n "messages": [\n {\n "role": "user",\n "content": "why does my google Ai dashboard not work"\n }\n ],\n "temperature": 0.7\n}'
2025-08-17 00:17:56.174 INFO (MainThread) [homeassistant.components.script.chatgpt_query] Send GPT Prompt (Admin): Executing step call service
2025-08-17 00:17:56.175 INFO (MainThread) [homeassistant.components.script.chatgpt_query] Send GPT Prompt (Admin): Executing step call service
2025-08-17 00:17:56.176 INFO (MainThread) [homeassistant.components.automation.announce_gpt_reply] Announce GPT reply: Running automation actions
2025-08-17 00:17:56.176 INFO (MainThread) [homeassistant.components.automation.announce_gpt_reply] Announce GPT reply: Executing step call service
2025-08-17 00:17:56.177 ERROR (MainThread) [homeassistant.components.automation.announce_gpt_reply] Announce GPT reply: Error executing script. Service not found for call_service at pos 1: Action notify.alexa_media_your_device not found
2025-08-17 00:17:56.177 INFO (MainThread) [homeassistant.components.automation.push_gpt_reply_to_mobile] Push GPT reply to mobile: Running automation actions
2025-08-17 00:17:56.177 INFO (MainThread) [homeassistant.components.automation.push_gpt_reply_to_mobile] Push GPT reply to mobile: Executing step call service
2025-08-17 00:17:56.180 INFO (MainThread) [homeassistant.components.automation.admin_gpt_reply_complete] Admin GPT Reply Complete: Running automation actions
2025-08-17 00:17:56.181 INFO (MainThread) [homeassistant.components.automation.admin_gpt_reply_complete] Admin GPT Reply Complete: Executing step call service
2025-08-17 00:17:56.198 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Executing step delay 0:00:02
2025-08-17 00:17:58.199 INFO (MainThread) [homeassistant.components.automation.gpt_conversational_text_trigger] GPT Conversational Text Trigger: Executing step call service
2025-08-17 00:17:58.946 INFO (MainThread) [homeassistant.components.script.chatgpt_convo_query] Send Conversational Prompt to GPT (Shell Command): Executing step call service
2025-08-17 00:17:58.948 INFO (MainThread) [homeassistant.components.script.chatgpt_convo_query] Send Conversational Prompt to GPT (Shell Command): Executing step call service
2025-08-17 00:20:00.201 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Running automation actions
2025-08-17 00:20:00.201 INFO (MainThread) [homeassistant.components.automation.update_dashboard_list] Update Dashboard List: Executing step call service
2025-08-17 00:20:00.243 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Running automation actions
2025-08-17 00:20:00.243 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:20:00.252 WARNING (SyncWorker_1) [homeassistant.components.python_script] Warning loading script fix_sheet_logger.py: Line None: Prints, but never reads 'printed' variable.
2025-08-17 00:20:00.252 ERROR (SyncWorker_1) [homeassistant.components.python_script.fix_sheet_logger.py] Error executing script
Traceback (most recent call last):
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 290, in execute
exec(compiled.code, restricted_globals) # noqa: S102
~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "fix_sheet_logger.py", line 1, in <module>
File "/usr/src/homeassistant/homeassistant/components/python_script/**init**.py", line 182, in guarded_import
raise ImportError(f"Not allowed to import {name}")
ImportError: Not allowed to import os
2025-08-17 00:20:00.268 INFO (MainThread) [homeassistant.components.automation.run_yaml_validation_log_result_2] Run YAML Validation & Log Result: Executing step call service
2025-08-17 00:20:00.402 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Running automation actions
2025-08-17 00:20:00.402 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:20:00.451 INFO (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Executing step call service
2025-08-17 00:20:00.452 ERROR (MainThread) [homeassistant.components.automation.auto_reload_sensors_and_templates_on_file_change] 🔁 Auto-reload sensors and templates on file change: Error executing script. Service not found for call_service at pos 2: Action homeassistant.reload_template_entities not found
