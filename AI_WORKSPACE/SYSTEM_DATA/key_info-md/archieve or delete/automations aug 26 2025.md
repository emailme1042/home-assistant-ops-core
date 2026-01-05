---

- alias: Add Task from Dashboard
  trigger:
    - platform: state
      entity_id: input_text.todo_task_1
      to: ""
      for: "00:00:01"
  action:
    - service: python_script.add_todo
      data:
        task: "{{ states('input_text.todo_task_1') }}"
        category: "{{ states('input_select.todo_category') }}"
    - service: input_text.set_value
      target:
        entity_id: input_text.todo_task_1
      data:
        value: ""

- alias: "ESP Offline Alert"
  id: esp_offline_alert
  trigger:
    - platform: state
      entity_id: binary_sensor.esp_device_status
      to: 'off'
      for: "00:05:00"
  condition: []
  action:
    - service: notify.mobile_app_jamies_phone
      data:
        title: "ESP Device Offline"
        message: "Your ESP device has been unreachable for over 5 minutes. Check WiFi, power, or mDNS."
  mode: single

- alias: "Log ESP Restart Reason"
  trigger:
    platform: homeassistant
    event: start
  action:
      - service: notify.persistent_notification
        data:
          message: "ESP restarted due to: {{ states('sensor.esp_restart_reason') }}"

- alias: "Send GPT Prompt from Direct Input"
  mode: single
  trigger:
    - platform: state
      entity_id: input_boolean.gpt_direct_send_trigger
      to: "on"
  action:
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_text_prompt
        value: "{{ states('input_text.gpt_direct_input') }}"
    - service: shell_command.run_chatgpt_user_reply
    - delay: "00:00:01"
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.gpt_direct_send_trigger


- alias: "Run YAML Validation & Log Result"
  trigger:
    - platform: time_pattern
      minutes: "/5"
    - platform: homeassistant
      event: start
  condition: []
  action:
    - service: python_script.fix_sheet_logger
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.force_yaml_check
  mode: single

- alias: "Add To-Do via Dashboard"
  trigger:
    - platform: state
      entity_id: input_text.new_todo_task
      to: ""
      for:
        seconds: 1
      from: ""
  action:
    - service: python_script.add_todo
      data:
        task: "{{ states('input_text.new_todo_task') }}"
        category: "{{ states('input_select.new_todo_category') }}"
    - service: input_text.set_value
      target:
        entity_id: input_text.new_todo_task
      data:
        value: ""

- alias: Save Latest Email Content to Files
  trigger:
    - platform: event
      event_type: email_received
  action:
    - service: shell_command.save_email_subject
      data:
        subject: "{{ trigger.event.data.subject | default('No subject') if trigger is defined else 'No trigger' }}"
    - service: shell_command.save_email_body
      data:
        body: "{{ trigger.event.data.text | default('No body') if trigger is defined else 'No trigger' }}"
    - service: shell_command.save_email_from
      data:
        from: "{{ trigger.event.data.from | default('Unknown sender') if trigger is defined else 'No trigger' }}"

- alias: Alert if WSL Restart Marker Missing
  description: Notify if /startup_marker is missing (sensor state is "Missing")
  trigger:
    - platform: state
      entity_id: sensor.wsl_startup_marker
      to: "Missing"
      for: "00:05:00"
  action:
    - service: persistent_notification.create
      data:
        title: "⚠️ WSL Startup Not Detected"
        message: "The Flask startup script may not have run. Please run run_flask_hardened.sh manually."
    - service: notify.mobile_app_yourdevice
      data:
        message: "WSL Flask marker not found — check Flask server."
        title: "🛑 JIT Plugin Not Auto-Launched"
  mode: single



- alias: Ensure GPT Status File Permissions
  description: >-
    Checks and repairs permissions on gpt_status.txt to prevent sync failures.
  trigger:
    - platform: time
      at: "03:00:00"
  condition: []
  action:
    - service: shell_command.fix_gpt_status_permissions
  mode: single

# -----------------------------
# Dashboard Toggles
# -----------------------------

- alias: Enable Entities Dashboard
  trigger:
    - platform: state
      entity_id: input_boolean.admin_dashboard_entities
      to: "on"
  action:
    - service: persistent_notification.create
      data:
        title: "Dashboard Enabled"
        message: "✅ Entities dashboard toggle turned ON."
  mode: single

- alias: Disable Entities Dashboard
  trigger:
    - platform: state
      entity_id: input_boolean.admin_dashboard_entities
      to: "off"
  action:
    - service: persistent_notification.create
      data:
        title: "Dashboard Disabled"
        message: "❌ Entities dashboard toggle turned OFF."
  mode: single

# -----------------------------
# AI & GPT
# -----------------------------

- alias: Re-Ask ChatGPT
  trigger:
    - platform: state
      entity_id: input_boolean.ask_ai_trigger
      to: "on"
  action:
    - service: shell_command.run_generate_yaml_ai
    - service: input_boolean.turn_off
      target:
        entity_id: input_boolean.ask_ai_trigger
  mode: single

- alias: Notify System Update Available
  trigger:
    - platform: state
      entity_id:
        - update.home_assistant_supervisor_update
        - update.home_assistant_core_update
        - update.matter_server_update
        - update.samba_share_update
        - update.advanced_ssh_web_terminal_update
        - update.mosquitto_broker_update
        - update.file_editor_update
        - update.govee_to_mqtt_bridge_update
        - update.home_assistant_operating_system_update
      to: "on"
  action:
    - service: notify.notify
      data:
        message: "A system update is available for Home Assistant."

- alias: Backup Success Reminder
  trigger:
    - platform: time_pattern
      # Checks daily at midnight
      hours: 0
      minutes: 0
      seconds: 0
  condition:
    - condition: template
      value_template: "{{ (now() - states('sensor.backup_last_successful_automatic_backup') | as_timestamp) > (7 * 86400) }}"
  action:
    - service: notify.notify
      data:
        message: "It has been more than 7 days since the last successful backup."

- alias: "Notify of Stale Updates"
  trigger:
    platform: time_pattern
    hours: "/1"
  condition:
    condition: or
    conditions:
      - condition: state
        entity_id: update.home_assistant_supervisor_update
        state: "off"
      - condition: state
        entity_id: update.home_assistant_core_update
        state: "off"
  action:
    - service: notify.mobile_app_plop
      data:
        message: "One or more updates have been inactive for a while. Please check!"

- alias: "Notify Backup Created"
  trigger:
    platform: event
    event_type: backup_automatic_backup
  action:
    - service: notify.mobile_app_plop
      data:
        message: "A new automatic backup has been created at {{ now().strftime('%Y-%m-%d %H:%M:%S') }}."

- alias: Run GPT when prompt changes
  trigger:
    - platform: state
      entity_id: input_text.chatgpt_prompt
  condition: []
  action:
    - service: script.chatgpt_user_query
  mode: single

- alias: Announce GPT reply
  trigger:
    - platform: state
      entity_id: input_text.gpt_result_core
  condition: []
  action:
    - service: notify.alexa_media_your_device
      data:
        message: "{{ states('input_text.gpt_result_core') }}"
        data:
          type: tts
  mode: single

- alias: Push GPT reply to mobile
  trigger:
    - platform: state
      entity_id: input_text.gpt_result_core
  condition: []
  action:
    - service: notify.mobile_app_plop
      data:
        message: "{{ states('input_text.gpt_result_core') }}"
  mode: single

- alias: Remind VPN on for streaming
  trigger:
    - platform: state
      entity_id: input_boolean.movie_night
      to: "on"
  action:
    - service: persistent_notification.create
      data:
        title: Check VPN
        message: Make sure Surfshark is connected before starting Movie Night!

- alias: Auto Bedtime Scene
  trigger:
    - platform: state
      entity_id: binary_sensor.bedroom_occupied
      to: "off"
      for: "00:15:00"
  action:
    - service: scene.turn_on
      target:
        entity_id: scene.bedroom_bedtime

- id: party_mode_auto_music
  alias: Start Party Music when Party Mode Scene Activated
  trigger:
    - platform: event
      event_type: call_service
      event_data:
        domain: scene
        service: turn_on
        service_data:
          entity_id: scene.bedroom_party_mode
  action:
    - service: media_player.play_media
      target:
        entity_id: media_player.bedroom
      data:
        media_content_id: "https://www.myinstants.com/media/sounds/party-time.mp3"
        media_content_type: music

- id: movie_night_voice_notify
  alias: Announce Movie Night
  trigger:
    - platform: state
      entity_id: input_boolean.movie_night
      to: "on"
  action:
    - service: notify.alexa_bedroom
  data:
    message: "Enjoy your movie night! Don't forget the popcorn."
    data:
      type: tts

- id: relax_mode_sound
  alias: Play Relaxing Sound when Relax Scene Activated
  trigger:
    - platform: event
      event_type: call_service
      event_data:
        domain: scene
        service: turn_on
        service_data:
          entity_id: scene.bedroom_relax
  action:
    - service: media_player.play_media
      target:
        entity_id: media_player.bedroom
      data:
        media_content_id: "https://www.myinstants.com/media/sounds/ocean-wave.mp3"
        media_content_type: music

- alias: Update Dashboard List
  mode: single
  trigger:
    - platform: time_pattern
      minutes: "/5"
  action:
    - service: input_text.set_value
      target:
        entity_id: input_text.dashboard_urls
      data:
        value: >
          {{ state_attr('sensor.lovelace_dashboards', 'dashboards') | join(', ') if state_attr('sensor.lovelace_dashboards', 'dashboards') else 'No dashboards found' }}


# 🍽️💡 Kitchen Automations — Final with Correct Entities

- alias: Kitchen Light On With Motion
  mode: restart
  trigger:
    - platform: state
      entity_id: binary_sensor.tapo_motion_sensor_motion
      to: "on"
  condition:
    - condition: sun
      after: sunset
    - condition: state
      entity_id: switch.kitchen_light_switch
      state: "off"
  action:
    - service: switch.turn_on
      target:
        entity_id: switch.kitchen_light_switch

- alias: Kitchen Light Off After No Motion
  mode: restart
  trigger:
    - platform: state
      entity_id: binary_sensor.tapo_motion_sensor_motion
      to: "off"
      for: "00:03:00"
  condition:
    - condition: state
      entity_id: switch.kitchen_light_switch
      state: "on"
  action:
    - service: switch.turn_off
      target:
        entity_id: switch.kitchen_light_switch

- alias: Kitchen Fan On If Hot And Motion
  mode: restart
  trigger:
    - platform: state
      entity_id: binary_sensor.tapo_motion_sensor_motion
      to: "on"
  condition:
    - condition: numeric_state
      entity_id: sensor.temperature_and_humidity_sensor_egg_temperature
      above: 26
    - condition: state
      entity_id: switch.kitchen_fan
      state: "off"
  action:
    - service: switch.turn_on
      target:
        entity_id: switch.kitchen_fan

- alias: Kitchen Fan Off After No Motion Or Cool
  mode: restart
  trigger:
    - platform: state
      entity_id: binary_sensor.tapo_motion_sensor_motion
      to: "off"
      for: "00:03:00"
    - platform: numeric_state
      entity_id: sensor.temperature_and_humidity_sensor_egg_temperature
      below: 26
  condition:
    - condition: state
      entity_id: switch.kitchen_fan
      state: "on"
  action:
    - service: switch.turn_off
      target:
        entity_id: switch.kitchen_fan

- alias: Kitchen Blinds Open Morning (Gradual)
  mode: single
  trigger:
    - platform: sun
      event: sunrise
  action:
    - service: cover.set_cover_position
      target:
        entity_id: cover.kitchen_blinds
      data:
        position: 50
    - delay: "00:10:00"
    - service: cover.open_cover
      target:
        entity_id: cover.kitchen_blinds

- alias: Kitchen Blinds Close Evening (Gradual)
  mode: single
  trigger:
    - platform: sun
      event: sunset
  action:
    - service: cover.set_cover_position
      target:
        entity_id: cover.kitchen_blinds
      data:
        position: 50
    - delay: "00:10:00"
    - service: cover.close_cover
      target:
        entity_id: cover.kitchen_blinds

- alias: Kitchen Window Open Alert
  mode: single
  trigger:
    - platform: state
      entity_id: binary_sensor.kitchen_window_door
      to: "on"
  condition:
    - condition: state
      entity_id: light.downstairs
      state: "off"
  action:
    - service: notify.alexa_media
      data:
        target: media_player.kitchen_echo
        message: "⚠️ Alert! The kitchen window is open while all downstairs lights are off."
        data:
          type: announce

- alias: Alexa Kitchen Afternoon Greeting
  mode: single
  trigger:
    - platform: time
      at: "16:00:00"
  action:
    - service: notify.alexa_media
      data:
        target: media_player.kitchen
        message: >
          Good afternoon! Do you need to add anything to the shopping list? It's {{ states('sensor.temperature_and_humidity_sensor_egg_temperature') }} degrees in the kitchen.
        data:
          type: announce

- alias: "GPT Conversational Text Trigger (Shell)"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.gpt_text_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 5 }}"
  action:
    - service: script.chatgpt_convo_query
      data:
        prompt: "{{ states('input_text.gpt_text_prompt') }}"

- alias: "Run NAS Script from ChatGPT Prompt"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.chatgpt_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 1 }}"
  action:
    - service: rest_command.run_nas_script
      data:
        prompt: "{{ states('input_text.chatgpt_prompt') }}"

- alias: "Mark GPT as Sent"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.chatgpt_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 1 }}"
  action:
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_status_flag
      data:
        value: "Sent to GPT"
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_last_sent_prompt
      data:
        value: "{{ states('input_text.chatgpt_prompt') }}"
    - service: rest_command.run_nas_script
      data:
        prompt: "{{ states('input_text.chatgpt_prompt') }}"

- alias: "Admin GPT Mark as Sent"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.chatgpt_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 1 }}"
  action:
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_status_flag
      data:
        value: "Sent to Admin GPT"
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_last_sent_prompt
      data:
        value: "{{ states('input_text.chatgpt_prompt') }}"
    - service: rest_command.run_nas_script
      data:
        prompt: "{{ states('input_text.chatgpt_prompt') }}"

- alias: "Admin GPT Reply Complete"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.gpt_result_core
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 5 }}"
  action:
    - service: input_text.set_value
      target:
        entity_id: input_text.gpt_status_flag
      data:
        value: "Reply Ready"

- alias: "GPT Conversational Text Trigger"
  mode: single
  trigger:
    - platform: state
      entity_id: input_text.gpt_text_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.to_state.state | length > 5 }}"
  action:
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_status_flag
        value: "Submitting..."
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_last_sent_prompt
        value: "{{ states('input_text.gpt_text_prompt') }}"
    - service: script.chatgpt_query
    - delay: "00:00:02"
    - service: input_text.set_value
      data:
        entity_id: input_text.gpt_status_flag
        value: "Done"

- id: run_kodi_ai_on_prompt
  alias: "Run Kodi AI when Prompt is Updated"
  trigger:
    - platform: state
      entity_id: input_text.kodi_command_prompt
  condition:
    - condition: template
      value_template: "{{ trigger.from_state.state != trigger.to_state.state }}"
  action:
    - service: script.chatgpt_kodi_command_handler

- alias: "Alert if JIT Plugin goes offline"
  trigger:
    - platform: state
      entity_id: binary_sensor.jit_plugin_flask_online
      to: "off"
      for: "00:01:00"
  action:
    - service: notify.mobile_app_plop
      data:
        title: "🚨 JIT Plugin Offline"
        message: "Flask server is unreachable at port 5001."

- alias: Alert if WSL Restart Marker Missing
  description: Notify if /startup_marker is missing (sensor state is "Missing")
  trigger:
    - platform: state
      entity_id: sensor.wsl_startup_marker
      to: "Missing"
      for: "00:05:00"
  condition: []
  action:
    - service: persistent_notification.create
      data:
        title: "⚠️ WSL Startup Not Detected"
        message: "The Flask startup script may not have run. Please run run_flask.sh manually."
    - service: notify.mobile_app_yourdevice #  Optional
      data:
        message: "WSL Flask marker not found — check Flask server."
        title: "🛑 JIT Plugin Not Auto-Launched"
  mode: single



- alias: Notify Oversized Input Text
  trigger:
    - platform: time_pattern
      minutes: "/30"
  action:
    - service: notify.gmail_smtp
      data:
        title: "Oversized Input Text Entries"
        message: "Please review the file: input_text_oversized.yaml"
  mode: single

- alias: "Send Home Assistant Startup Report"
  trigger:
    - platform: homeassistant
      event: start
  action:
    - service: notify.gmail_smtp
      data:
        title: "✅ Home Assistant Started"
        message: >
          Home Assistant has restarted successfully at {{ now().strftime('%Y-%m-%d %H:%M:%S') }}.

          **Entities Loaded:** {{ states | count }}
          **Automations Enabled:** {{ states.automation | selectattr('state','eq','on') | list | count }}
          **Scripts Loaded:** {{ states.script | count }}

          IP Address: {{ states('sensor.local_ip') if states('sensor.local_ip') else 'Unknown' }}
          Uptime Sensor: {{ states('sensor.uptime') if states('sensor.uptime') else 'Not available' }}

          Have a great day!

# - alias: Save Latest Email Content to Files
#   id: save_latest_email_content_to_files
#   trigger:
#     - platform: event
#       event_type: imap_content

#   action:
#     - service: notify.notify
#       data:
#         message: "📬 New email received — updating local files"

#     - service: shell_command.write_email_subject
#     - service: shell_command.write_email_body
#     - service: shell_command.write_email_from

#   mode: queued

- alias: React to GPT Context Change
  trigger:
    - platform: state
      entity_id: input_text.gpt_context_file
  condition: []
  action:
    - service: notify.persistent_notification
      data:
        message: "Context file updated to {{ states('input_text.gpt_context_file') }}"

- alias: Reload Automations After Startup
  trigger:
    - platform: homeassistant
      event: start
  action:
    - service: automation.reload

- alias: Log GPT Context Change
  trigger:
    - platform: state
      entity_id: input_text.gpt_context_file
  condition:
    - condition: template
      value_template: "{{ states('input_text.gpt_context_file') != 'unknown' }}"
  action:
    - service: persistent_notification.create
      data:
        title: "GPT Context Updated"
        message: "New context file: {{ states('input_text.gpt_context_file') }}"
