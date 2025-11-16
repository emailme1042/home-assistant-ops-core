# 🧠 Automation & Script Map — November 2, 2025

**System Overview**: 107 Automations + 90 Scripts across 8 functional areas

---

## 🏠 **LIGHTING & ROOM CONTROL** (15 automations, 8 scripts)

### Automations:
- `automation.hall_light_on_when_others_off` - Hall light when all downstairs lights off at night
- `automation.loo_light_5_minute_auto_off` - Auto turn off loo light after 5 minutes
- `automation.office_light_on_motion_detected` - Office motion lighting
- `automation.office_light_off_after_no_motion` - Office motion timer
- `automation.bathroom_motion_switch_light_control` - Bathroom motion control
- `automation.aqara_cube_teddys_bedroom_colors` - Teddy's room color control via cube
- `automation.adaptive_lighting_ai` - AI adaptive lighting

### Scripts:
- `script.teddy_lights_on` - Turn on Teddy's lights
- `script.set_color_red` - Set Teddy's lights to red
- `script.office_shutdown` - Office shutdown sequence
- `script.office_focus_mode` - Office focus lighting

---

## 🚪 **DOORS & SECURITY** (8 automations, 4 scripts)

### Automations:
- `automation.garden_light_on_door_open_at_night` - Garden lights when front door opens after sunset
- `automation.garden_light_off_door_closed` - Garden lights off when door closes
- `automation.door_open_alexa_lounge_weather_advisory` - Weather alert when door opens
- `automation.front_door_lounge_light` - Front door trigger for lounge light

### Scripts:
- `script.build_weather_advisory` - Create weather advisory for door opening
- `script.activate_party_mode` - Party mode activation
- `script.entry_welcome_scene` - Welcome sequence

---

## 🔘 **BUTTON & DEVICE CONTROL** (12 automations, 6 scripts)

### Automations:
- `automation.sonoff_button_downstairs_shutdown` - Sonoff button safe downstairs shutdown
- `automation.zigbee_button_downstairs_off_hall_light` - Zigbee button downstairs control
- `automation.zigbee_button_smart_downstairs_off` - Smart Zigbee button control
- `automation.debug_sonoff_button_detection` - Sonoff button debugging
- `automation.test_sonoff_button_simple` - Test Sonoff button functionality
- `automation.button_card_debug` - Button card debug for tuple errors

### Scripts:
- `script.debug_office_motion` - Debug office motion system
- `script.test_office_light_on` - Test office light control
- `script.refresh_entity_watchdog` - Refresh entity monitoring

---

## 🤖 **AI & AUTOMATION SYSTEM** (18 automations, 15 scripts)

### Automations:
- `automation.ai_morning_routine` - AI morning automation
- `automation.ai_routine_lifecycle_handler` - AI routine management
- `automation.ai_scene_mood_selector` - AI scene selection
- `automation.ai_sleep_mode_automation` - AI sleep mode trigger
- `automation.ai_smart_sleep_trigger` - Smart sleep mode
- `automation.ai_workspace_auto_preview` - AI workspace file preview
- `automation.ai_dashboard_health_monitor` - AI dashboard monitoring
- `automation.dashboard_session_tracker` - Dashboard session tracking
- `automation.room_template_tag_tracker` - Room template management

### Scripts:
- `script.query_openai` - OpenAI query handler
- `script.query_openai_simple` - Simple OpenAI queries
- `script.gpt_send_prompt` - GPT prompt sending
- `script.gpt_create_backup` - GPT backup creation
- `script.gpt_flask_prompt` - GPT via Flask integration
- `script.clone_room_template` - Room template cloning
- `script.automation_health_audit` - Automation health checking
- `script.session_tag_automation` - Session tagging system

---

## 📡 **NETWORK & SYSTEM MONITORING** (16 automations, 12 scripts)

### Automations:
- `automation.network_speed_monitor` - SpeedTest monitoring
- `automation.ipv6_connectivity_monitor` - IPv6 connectivity checking
- `automation.mqtt_watchdog_hourly` - MQTT connection monitoring
- `automation.system_health_ga_notification` - System health notifications
- `automation.log_system_health_daily` - Daily system health logging
- `automation.entity_health_monitor` - Entity health tracking
- `automation.entity_unavailable_audit` - Unavailable entity auditing
- `automation.frontend_health_monitor` - Frontend health monitoring

### Scripts:
- `script.run_dashboard_analysis` - Dashboard performance analysis
- `script.audit_system_health` - System health auditing
- `script.run_verbose_validation` - Comprehensive YAML validation
- `script.system_overview_recover_adsb` - ADS-B feed recovery
- `script.system_overview_recover_health_monitor` - Health monitor recovery

---

## ✈️ **AIRCRAFT & ADS-B MONITORING** (8 automations, 4 scripts)

### Automations:
- `automation.aircraft_low_altitude_alert` - Low altitude aircraft alerts
- `automation.high_aircraft_activity_alert` - High activity alerts
- `automation.fallback_adsb_trigger` - ADS-B fallback trigger
- `automation.adsb_heartbeat` - ADS-B feed heartbeat
- `automation.log_adsb_emergency` - Emergency aircraft logging
- `automation.aircraft_noise_detection_lounge_vibration` - Vibration detection
- `automation.flash_lamp_low_aircraft` - Visual alert for low aircraft

### Scripts:
- `script.adsb_feed_recovery` - ADS-B feed recovery
- `script.aircraft_alert_system` - Aircraft alerting

---

## 📺 **MEDIA & ENTERTAINMENT** (12 automations, 8 scripts)

### Automations:
- `automation.sync_media_player_selector` - Media player selection sync
- `automation.start_party_music_party_mode` - Party music automation
- `automation.auto_bedtime_scene` - Bedroom bedtime automation
- `automation.remind_vpn_on_for_streaming` - VPN reminder for streaming

### Scripts:
- `script.chatgpt_kodi_command_handler` - Kodi AI commands
- `script.openai_quick_test` - OpenAI voice testing
- `script.combined_voice_test` - Combined voice workflow testing
- `script.mobile_alexa_announce` - Mobile Alexa announcements
- `script.announce_all_alexas` - Multi-Alexa announcements
- `script.tts_test_script` - TTS system testing

---

## 🔧 **SYSTEM MAINTENANCE** (18 automations, 33 scripts)

### Automations:
- `automation.reload_automations_after_startup` - Startup automation reload
- `automation.send_home_assistant_startup_report` - Startup reporting
- `automation.automated_backup_repair_trigger` - Backup repair automation
- `automation.update_notification_work_hours` - Update notifications
- `automation.notify_system_update_available` - System update alerts
- `automation.notify_backup_created` - Backup completion notifications
- `automation.validate_yaml_and_automations` - YAML validation automation
- `automation.ensure_gpt_status_file_permissions` - File permission management
- `automation.kitchen_blinds_open_morning_gradual` - Kitchen blind automation
- `automation.weekly_digest_trigger` - Weekly system digest
- `automation.save_latest_email_content` - Email content saving
- `automation.add_task_from_dashboard` - Task management
- `automation.generate_entity_validation_report` - Entity validation reporting

### Scripts:
- `script.test_rest_commands` - REST command testing
- `script.ask_chatgpt` - ChatGPT interaction
- `script.say_hello_to_teddy` - Teddy greeting
- `script.sexy_time` - Personal automation
- `script.send_test_email_gmail` - Email testing
- `script.test_voice_openai_workflow` - Voice workflow testing

---

## 📊 **SUMMARY BY AREA**

| Area | Automations | Scripts | Total |
|------|-------------|---------|-------|
| 🏠 Lighting & Room Control | 15 | 8 | 23 |
| 🚪 Doors & Security | 8 | 4 | 12 |
| 🔘 Button & Device Control | 12 | 6 | 18 |
| 🤖 AI & Automation System | 18 | 15 | 33 |
| 📡 Network & System Monitoring | 16 | 12 | 28 |
| ✈️ Aircraft & ADS-B Monitoring | 8 | 4 | 12 |
| 📺 Media & Entertainment | 12 | 8 | 20 |
| 🔧 System Maintenance | 18 | 33 | 51 |

**TOTAL: 107 Automations + 90 Scripts = 197 Total Entities**

---

## 🎯 **KEY INSIGHTS**

1. **Largest Categories**: System Maintenance (51) and AI System (33)
2. **Most Complex**: Network Monitoring and AI Automation systems
3. **Most Active**: Lighting, Button Control, and Media systems
4. **Critical Functions**: System health monitoring, entity validation, backup management
5. **AI Integration**: 33 AI-related automations/scripts across multiple domains

---

*Generated: November 2, 2025 | System Health: Active | Total Active Entities: 197*