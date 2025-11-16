🧠 Manual Health Scan (ruamel) — 2025-08-11 01:20:42.417637

🔍 YAML Validation —
✅ Valid YAML: /resources.yaml
✅ Valid YAML: /generated_groups.yaml
✅ Valid YAML: /secrets.yaml
✅ Valid YAML: /configuration.yaml
❌ Invalid YAML: /automations.yaml — while constructing a mapping
in "/automations.yaml", line 97, column 3
found duplicate key "action" with value "[{'service': 'notify.alexa_media_your_device', 'data': {'message': "{{ states('input_text.gpt_result_core') }}", 'data': {'type': 'tts'}}}]" (original value: "[{'service': 'notify.mobile_app_plop', 'data': {'message': "A new automatic backup has been created at {{ now().strftime('%Y-%m-%d %H:%M:%S') }}."}}, {'platform': 'state', 'entity_id': 'input_text.gpt_result_core'}]")
in "/automations.yaml", line 120, column 3

To suppress this check see:
https://yaml.dev/doc/ruamel.yaml/api/#Duplicate_keys

✅ Valid YAML: /zigbee2mqtt/configuration_backup_v1.yaml
✅ Valid YAML: /zigbee2mqtt/configuration_backup_v2.yaml
✅ Valid YAML: /zigbee2mqtt/configuration_backup_v3.yaml
✅ Valid YAML: /zigbee2mqtt/configuration.yaml
✅ Valid YAML: /\_archived_backups fm inc/ai_fixes/master-admin-draft.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/recovery_dashboard.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/fire_tv.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin_maintenance.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-root.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/teddy_central.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-helpers.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/fire-merged.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-system.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-topology.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/teddys_pokemon_lab.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-nav.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin_automations.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/chatgpt-dashboard.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/garden_combined.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/04_admin-user-db-index.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/garden_flow.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/30_alexa-test.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/admin-entities.yaml
✅ Valid YAML: /\_archived_backups fm inc/final_auto_fixes/system_JD_overview_navigation.yaml
✅ Valid YAML: /.continue/prompts/new-prompt.yaml
❌ Invalid YAML: /www/generated_motion_group.yaml — while scanning a simple key
in "/www/generated_motion_group.yaml", line 17, column 1
could not find expected ':'
in "/www/generated_motion_group.yaml", line 17, column 19
✅ Valid YAML: /www/openapi_gpt_actions.yaml
❌ Invalid YAML: /www/context_snapshots/openapi_gpt_actions.yaml — mapping values are not allowed here
in "/www/context_snapshots/openapi_gpt_actions.yaml", line 10, column 52
❌ Invalid YAML: /www/includes/dashboard_suggestions/approved.yaml — while scanning a simple key
in "/www/includes/dashboard_suggestions/approved.yaml", line 5, column 1
could not find expected ':'
in "/www/includes/dashboard_suggestions/approved.yaml", line 6, column 13
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.68.rgb-wave/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.68.rgb-wave/package.yaml", line 15, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.65.cristal-lands/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/generator.1.svg-wave/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/generator.1.svg-wave/package.yaml", line 15, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.47.color-trails/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.47.color-trails/package.yaml", line 17, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/application.1.media-background/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.61.cube/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.69.bit-ocean/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.69.bit-ocean/package.yaml", line 11, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.67.fly-particle/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.24.trapped-gradient/package.yaml — while scanning a simple key
in "/www/community/lovelace-bg-animation/gallery/packages/animation.24.trapped-gradient/package.yaml", line 3, column 1
could not find expected ':'
in "/www/community/lovelace-bg-animation/gallery/packages/animation.24.trapped-gradient/package.yaml", line 6, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.80.particle-waves/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.90.aurora/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.56.azimuthal-viscosity/package.yaml — mapping values are not allowed here
in "/www/community/lovelace-bg-animation/gallery/packages/animation.56.azimuthal-viscosity/package.yaml", line 1, column 309
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.27.tron/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.82.storm/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.16.veil/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.16.veil/package.yaml", line 11, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.6.binary-spiral/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.88.fish-tank/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.21.noise-abstraction/package.yaml — while scanning a simple key
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.21.noise-abstraction/package.yaml", line 3, column 1
could not find expected ':'
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.21.noise-abstraction/package.yaml", line 5, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.3.spipa-circle/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.3.spipa-circle/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.75.hexagonal-truchet-10-print/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.75.hexagonal-truchet-10-print/package.yaml", line 15, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.10.css-dark-particles/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.10.css-dark-particles/package.yaml", line 3, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.77.hexanimation-2/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.19.trapped-particles/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.19.trapped-particles/package.yaml", line 23, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.18.particle-cube/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.74.dvd-screensaver/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.52.polyhedron-galaxy/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.52.polyhedron-galaxy/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.14.ribbons-two/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.14.ribbons-two/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.84.troisjs-starfield/package.yaml — mapping values are not allowed here
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.84.troisjs-starfield/package.yaml", line 5, column 65
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.50.sidelined/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.11.space/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.11.space/package.yaml", line 9, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.78.just-in-case/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/generator.79.more-columns/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.12.gradient-particles/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.12.gradient-particles/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/generator.86.silky-carpet/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/generator.86.silky-carpet/package.yaml", line 9, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.62.neural/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.62.neural/package.yaml", line 3, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.76.hexanimation/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.85.truchet-10-print-imitation/package.yaml — while parsing a block mapping
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.85.truchet-10-print-imitation/package.yaml", line 6, column 6
expected <block end>, but found '<scalar>'
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.85.truchet-10-print-imitation/package.yaml", line 6, column 89
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.9.rainbow-particles/package.yaml — mapping values are not allowed here
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.9.rainbow-particles/package.yaml", line 7, column 69
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.89.shamrocks/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.58.browniandrix-noise-l3/package.yaml — while scanning a simple key
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.58.browniandrix-noise-l3/package.yaml", line 3, column 1
could not find expected ':'
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.58.browniandrix-noise-l3/package.yaml", line 7, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.22.cloth-ribbons/package.yaml — mapping values are not allowed here
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.22.cloth-ribbons/package.yaml", line 7, column 127
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.35.canvas-light-explosion/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.49.curved-lines/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.28.black-sand-flow-field-v2/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.4.colored-swipe/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.4.colored-swipe/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.23.ribbons-four/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.23.ribbons-four/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.70.blur/package.yaml — mapping values are not allowed here
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.70.blur/package.yaml", line 5, column 107
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.33.canvas-bokeh/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.33.canvas-bokeh/package.yaml", line 3, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.73.alien-blackout-intro-scene-react-webgl/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/generator.2.knots/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.83.strange-tubes/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.83.strange-tubes/package.yaml", line 7, column 28
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.79.canvas-ribbons/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.79.canvas-ribbons/package.yaml", line 11, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.26.gpu-particles/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.64.howls-moving-castle/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.34.canvas-color-teams/package.yaml — mapping values are not allowed here
in "/www/community/lovelace-bg-animation/gallery/packages/animation.34.canvas-color-teams/package.yaml", line 5, column 95
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.20.manifold/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.20.manifold/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.5.neon-hexagon/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.5.neon-hexagon/package.yaml", line 3, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.71.interactive-gradient/package.yaml — mapping values are not allowed here
in "/www/community/lovelace-bg-animation/gallery/packages/animation.71.interactive-gradient/package.yaml", line 5, column 82
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.63.green-circuit/package.yaml — mapping values are not allowed here
in "/www/community/lovelace-bg-animation/gallery/packages/animation.63.green-circuit/package.yaml", line 5, column 65
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.57.browniandrix-noise/package.yaml — mapping values are not allowed here
in "/www/community/lovelace-bg-animation/gallery/packages/animation.57.browniandrix-noise/package.yaml", line 1, column 281
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.31.blooming-flower/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.13.cyber-lights/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.13.cyber-lights/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.81.remember-windows/package.yaml — while scanning a simple key
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.81.remember-windows/package.yaml", line 3, column 1
could not find expected ':'
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.81.remember-windows/package.yaml", line 6, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.46.codevember-05-simplex-vector-flow-field/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.32.canvas-blending-gradient-circles/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.17.ribbons/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.17.ribbons/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.48.colorful-wanderers/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.48.colorful-wanderers/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.59.dimension-two-and-a-half/package.yaml — mapping values are not allowed here
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.59.dimension-two-and-a-half/package.yaml", line 5, column 134
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.2.shooting-stars/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.2.shooting-stars/package.yaml", line 11, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.53.stars/package.yaml
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.36.starfield/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.60.digital-frontier/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.60.digital-frontier/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.66.fog-of-war/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.66.fog-of-war/package.yaml", line 5, column 29
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.15.sound/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.15.sound/package.yaml", line 15, column 1
✅ Valid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.87.point-sprites/package.yaml
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.5.plasma/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.5.plasma/package.yaml", line 11, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.25.galactic-swimmers/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.25.galactic-swimmers/package.yaml", line 15, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.7.rainbowness/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.7.rainbowness/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.54.stars-galaxy/package.yaml — while scanning for the next token
found character '`' that cannot start any token
  in "/www/community/lovelace-bg-animation/gallery/packages/animation.54.stars-galaxy/package.yaml", line 13, column 1
❌ Invalid YAML: /www/community/lovelace-bg-animation/gallery/packages/animation.72.playstation-3-bg-style/package.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/www/community/lovelace-bg-animation/gallery/packages/animation.72.playstation-3-bg-style/package.yaml", line 9, column 1
✅ Valid YAML: /custom_components/ai_automation_suggester/services.yaml
✅ Valid YAML: /custom_components/ai_automation_suggester/automations/weekly-review-automation.yaml
✅ Valid YAML: /custom_components/ai_automation_suggester/automations/new-entity-automation.yaml
✅ Valid YAML: /custom_components/browser_mod/services.yaml
✅ Valid YAML: /custom_components/auto_backup/services.yaml
✅ Valid YAML: /custom_components/alexa_media/services.yaml
✅ Valid YAML: /custom_components/ble_monitor/services.yaml
✅ Valid YAML: /custom_components/meross_lan/services.yaml
✅ Valid YAML: /custom_components/dwains_dashboard/services.yaml
✅ Valid YAML: /custom_components/dwains_dashboard/lovelace/ui-lovelace.yaml
✅ Valid YAML: /custom_components/dwains_dashboard/lovelace/views/02.devices.yaml
✅ Valid YAML: /custom_components/dwains_dashboard/lovelace/views/05.more_pages.yaml
✅ Valid YAML: /custom_components/dwains_dashboard/lovelace/views/01.homepage.yaml
❌ Invalid YAML: /custom_components/dwains_dashboard/lovelace/views/04.more_page_view.yaml — while scanning for the next token
found character '%' that cannot start any token
in "/custom_components/dwains_dashboard/lovelace/views/04.more_page_view.yaml", line 4, column 2
✅ Valid YAML: /custom_components/tapo_control/services.yaml
✅ Valid YAML: /custom_components/ha_registry/services.yaml
✅ Valid YAML: /custom_components/scheduler/services.yaml
✅ Valid YAML: /esphome/atom-lite-btproxyv1.yaml
✅ Valid YAML: /esphome/secrets.yaml
✅ Valid YAML: /esphome/archive/atom-bt.yaml
✅ Valid YAML: /esphome/archive/home-wi-fi.yaml
✅ Valid YAML: /esphome/archive/atom-lite-btproxy.yaml
✅ Valid YAML: /esphome/archive/atom-bt-proxy.yaml
❌ Invalid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/masterX-adminX.yaml — while constructing a mapping
in "/\_archived_backups/pre_final_merge_2025-07-04_0121/masterX-adminX.yaml", line 67, column 5
found duplicate key "icon" with value "mdi:view-dashboard" (original value: "mdi:robot")
in "/\_archived_backups/pre_final_merge_2025-07-04_0121/masterX-adminX.yaml", line 256, column 5

To suppress this check see:
https://yaml.dev/doc/ruamel.yaml/api/#Duplicate_keys

✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/master-admin.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/admin-dashboard.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/main-dashboard.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin_maintenance.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-root.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/autopatch_preview.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/fun-test.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-helpers.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-system.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-topology.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-entities.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/admin-helpers-overview.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/ui-playground.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/recovery_dashboard.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/fire_tv.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/teddy_central.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/fire-merged.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/teddys_pokemon_lab.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/admin-nav.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/admin_automations.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/chatgpt-dashboard.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/garden_combined.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/04_admin-user-db-index.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/garden_flow.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/30_alexa-test.yaml
✅ Valid YAML: /\_archived_backups/pre_final_merge_2025-07-04_0121/aimagic/\_autopatch_preview/system_JD_overview_navigation.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/ask_ai_trigger.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/recovery_dashboard.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/confirmable_notification.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/fire_tv.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_maintenance.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-root.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/autopatch_preview.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/teddy_central.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/script.reask_chatgpt.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/latest_card_value.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/entity_watchdog_sensor.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/fun-test.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_topology_header.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-helpers.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/irrigation_override.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/fire-merged.yaml
❌ Invalid YAML: /\_archived_backups/final_auto_fixes/masterX-adminX.yaml — while constructing a mapping
in "/\_archived_backups/final_auto_fixes/masterX-adminX.yaml", line 66, column 5
found duplicate key "icon" with value "mdi:view-dashboard" (original value: "mdi:robot")
in "/\_archived_backups/final_auto_fixes/masterX-adminX.yaml", line 255, column 5

To suppress this check see:
https://yaml.dev/doc/ruamel.yaml/api/#Duplicate_keys

✅ Valid YAML: /\_archived_backups/final_auto_fixes/package.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/last_chatgpt_prompt.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/master-admin.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/input_datetimes.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/gpt_result_core.yaml
❌ Invalid YAML: /\_archived_backups/final_auto_fixes/motion_light.yaml — while parsing a block mapping
in "/\_archived_backups/final_auto_fixes/motion_light.yaml", line 2, column 3
expected <block end>, but found '<block mapping start>'
in "/\_archived_backups/final_auto_fixes/motion_light.yaml", line 15, column 5
✅ Valid YAML: /\_archived_backups/final_auto_fixes/inverted_binary_sensor.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/latest_card_features.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/irrigation.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-system.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-dashboard.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-topology.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/teddys_pokemon_lab.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/chatgpt_prompt.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-nav.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/new_dashboard_slug.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/teddy_input_text.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_automations.yaml
❌ Invalid YAML: /\_archived_backups/final_auto_fixes/notify_leaving_zone.yaml — while parsing a block mapping
in "/\_archived_backups/final_auto_fixes/notify_leaving_zone.yaml", line 2, column 3
expected <block end>, but found '<block mapping start>'
in "/\_archived_backups/final_auto_fixes/notify_leaving_zone.yaml", line 16, column 5
✅ Valid YAML: /\_archived_backups/final_auto_fixes/latest_card_name.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/entity_audit_refresh.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/chatgpt-dashboard.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/new_dashboard_keyword.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/entity_audit_note.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/helper_watchdog_card.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/chatgpt_enchanted.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/garden_combined.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_system_header.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_entities_header.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/entity_status_overview.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/show_entity_search.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/theme_mode.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/set_value.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/decluttering_templates.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/04_admin-user-db-index.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/script.chatgpt_query.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/turn_off.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/garden_flow.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/topology_mapping_note.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/latest_card_rarity.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/30_alexa-test.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/main-dashboard.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/system_tracker_helpers.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-entities.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin_helpers_header.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/scan_pokemon_card.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/teddy_input_select.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/admin-helpers-overview.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/all_input_booleans_combined.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/turn_on.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/ui-playground.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/dashboard_builder_helpers.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/new_dashboard_title.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/system_JD_overview_navigation.yaml
✅ Valid YAML: /\_archived_backups/final_auto_fixes/input_numbers.yaml
✅ Valid YAML: /lovelace/resources.yaml
✅ Valid YAML: /config/test.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/fun-test.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/test_user_db.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/chatgpt.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/homev2.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/entity-manager.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/chatgpt-dashboard.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/user_dashboards/ui-playground.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin_maintenance.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-root.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/autopatch_preview.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-helpers.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-system.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-topology.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-entities.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/admin-helpers-overview.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/recovery_dashboard.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/admin-nav.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/admin_automations.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/04_admin-user-db-index.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/30_alexa-test.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/- TO DO SORT ETC -NOT IN STORAGE AI GPT SYSTEM YET/aimagic/\_autopatch_preview/system_JD_overview_navigation.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/system_overview_navigation.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/user_root.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/admin_tools.yaml
❌ Invalid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/ops_dashboard.yaml — while scanning a simple key
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/ops_dashboard.yaml", line 5, column 1
could not find expected ':'
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/ops_dashboard.yaml", line 9, column 12
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/JD COPY 6.7.25 ADMIN COCKPIT AI GPT YAML.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/admin_control_and \_health.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/likely_for_bin/user db.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/admin_dashboards/JD in use ADMIN COCKPIT AI GPT YAML.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/admin_dashboards/all 13.07.25.yaml
❌ Invalid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/ops_dashboard.yaml — while scanning a simple key
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/ops_dashboard.yaml", line 4, column 1
could not find expected ':'
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/ops_dashboard.yaml", line 7, column 9
❌ Invalid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/masterX-adminX.yaml — while constructing a mapping
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/masterX-adminX.yaml", line 67, column 5
found duplicate key "icon" with value "mdi:view-dashboard" (original value: "mdi:robot")
in "/secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/masterX-adminX.yaml", line 256, column 5

To suppress this check see:
https://yaml.dev/doc/ruamel.yaml/api/#Duplicate_keys

✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/master-admin.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/admin-dashboard.yaml
✅ Valid YAML: /secret_not_syncing/D-ASHBOARDS - NOT USED YET/unused_dashboards/main-dashboard.yaml
✅ Valid YAML: /dashboards/ops/admin_ops_fix.yaml
✅ Valid YAML: /dashboards/ops/daily-ops.yaml
✅ Valid YAML: /dashboards/ops/network_diagnostics.yaml
✅ Valid YAML: /dashboards/ops/ops_future_6.yaml
✅ Valid YAML: /dashboards/ops/ops_integration_test_3.yaml
✅ Valid YAML: /dashboards/ops/gpt-session.yaml
✅ Valid YAML: /dashboards/ops/todo-dashboard.yaml
✅ Valid YAML: /dashboards/ops/ops_hacs_test_2.yaml
✅ Valid YAML: /dashboards/ops/ops_future_5.yaml
✅ Valid YAML: /dashboards/ops/main.yaml
✅ Valid YAML: /dashboards/ops/openapi_gpt_actions.yaml
✅ Valid YAML: /dashboards/ops/ops_hacs_test_1.yaml
✅ Valid YAML: /dashboards/ops/ops_admin_overview.yaml
✅ Valid YAML: /dashboards/ops/ops_api_test_4.yaml
✅ Valid YAML: /dashboards/admin/people.yaml
✅ Valid YAML: /dashboards/admin/zones.yaml
✅ Valid YAML: /dashboards/admin/maintenance.yaml
✅ Valid YAML: /dashboards/admin/location_custom.yaml
✅ Valid YAML: /dashboards/admin/gpt_tools.yaml
✅ Valid YAML: /dashboards/admin/helpers.yaml
✅ Valid YAML: /dashboards/admin/conversation.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch1.yaml
✅ Valid YAML: /dashboards/admin/mqtt.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch12.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch4.yaml
✅ Valid YAML: /dashboards/admin/index.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch6.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch15.yaml
✅ Valid YAML: /dashboards/admin/admin_root.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch10.yaml
✅ Valid YAML: /dashboards/admin/schedule.yaml
✅ Valid YAML: /dashboards/admin/homekit.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch7.yaml
✅ Valid YAML: /dashboards/admin/timers.yaml
✅ Valid YAML: /dashboards/admin/topology.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch9.yaml
✅ Valid YAML: /dashboards/admin/main.yaml
✅ Valid YAML: /dashboards/admin/system_issues.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch3.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch14.yaml
✅ Valid YAML: /dashboards/admin/scenes.yaml
✅ Valid YAML: /dashboards/admin/admin_batch_index.yaml
✅ Valid YAML: /dashboards/admin/scripts.yaml
✅ Valid YAML: /dashboards/admin/templates.yaml
✅ Valid YAML: /dashboards/admin/admin_sidebar.yaml
✅ Valid YAML: /dashboards/admin/ai_control.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch11.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch8.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch5.yaml
✅ Valid YAML: /dashboards/admin/automations.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch2.yaml
✅ Valid YAML: /dashboards/admin/admin_partials_batch13.yaml
✅ Valid YAML: /dashboards/admin/system.yaml
✅ Valid YAML: /dashboards/admin/input_helpers.yaml
✅ Valid YAML: /dashboards/users/fire_tv.yaml
✅ Valid YAML: /dashboards/users/fire_tv_bedroom.yaml
✅ Valid YAML: /dashboards/users/gpt_user.yaml
✅ Valid YAML: /dashboards/users/teddy_central.yaml
✅ Valid YAML: /dashboards/users/user_dashboard.yaml
✅ Valid YAML: /dashboards/users/kodi_remote.yaml
✅ Valid YAML: /dashboards/users/teddys_pokemon_lab.yaml
✅ Valid YAML: /dashboards/users/main.yaml
✅ Valid YAML: /dashboards/users/kodi_ai_control.yaml
✅ Valid YAML: /dashboards/users/garden_combined.yaml
✅ Valid YAML: /dashboards/users/home.yaml
✅ Valid YAML: /blueprints/script/homeassistant/confirmable_notification.yaml
✅ Valid YAML: /blueprints/template/homeassistant/inverted_binary_sensor.yaml
✅ Valid YAML: /blueprints/automation/homeassistant/motion_light.yaml
✅ Valid YAML: /blueprints/automation/homeassistant/notify_leaving_zone.yaml
✅ Valid YAML: /includes/rest_commands/gpt_rest.yaml
✅ Valid YAML: /includes/input_datetimes/input_datetimes.yaml
✅ Valid YAML: /includes/input_datetimes/irrigation.yaml
❌ Invalid YAML: /includes/dashboard_suggestions/approved.yaml — while scanning for the next token
found character '`' that cannot start any token
in "/includes/dashboard_suggestions/approved.yaml", line 8, column 6
✅ Valid YAML: /includes/input_texts/input_textdata.yaml
✅ Valid YAML: /includes/scenes/scenes.yaml
✅ Valid YAML: /includes/ops/todo.yaml
✅ Valid YAML: /includes/helpers/teddy_pokemon_lab_stubs.yaml
✅ Valid YAML: /includes/input_booleans/ask_ai_trigger.yaml
✅ Valid YAML: /includes/input_booleans/irrigation_override.yaml
✅ Valid YAML: /includes/input_booleans/kodi_helpers.yaml
✅ Valid YAML: /includes/input_booleans/irrigation.yaml
✅ Valid YAML: /includes/input_booleans/show_entity_search.yaml
✅ Valid YAML: /includes/input_booleans/turn_off.yaml
✅ Valid YAML: /includes/input_booleans/scan_pokemon_card.yaml
✅ Valid YAML: /includes/input_booleans/all_input_booleans_combined.yaml
✅ Valid YAML: /includes/input_booleans/turn_on.yaml
✅ Valid YAML: /includes/input_booleans/gpt_session.yaml
✅ Valid YAML: /includes/input_selects/tts_target.yaml
✅ Valid YAML: /includes/input_selects/theme_mode.yaml
✅ Valid YAML: /includes/input_selects/teddy_input_select.yaml
✅ Valid YAML: /includes/input_selects/input_selects.yaml
✅ Valid YAML: /includes/input_selects/input_select.mood.yaml
✅ Valid YAML: /includes/notify/email_notify.yaml
✅ Valid YAML: /includes/scripts/test_rest_commands.yaml
✅ Valid YAML: /includes/scripts/gpt_flask_prompt.yaml
✅ Valid YAML: /includes/scripts/gpt_action_scripts.yaml
✅ Valid YAML: /includes/scripts/kodi.yaml
✅ Valid YAML: /includes/scripts/scripts.yaml
✅ Valid YAML: /includes/cards/entity_audit_note.yaml
✅ Valid YAML: /includes/cards/helper_watchdog_card.yaml
✅ Valid YAML: /includes/cards/entity_status_overview.yaml
✅ Valid YAML: /includes/cards/topology_mapping_note.yaml
✅ Valid YAML: /includes/input_numbers/irrigation.yaml
✅ Valid YAML: /includes/input_numbers/input_numbers.yaml
✅ Valid YAML: /includes/includes/input_datetimes/input_datetimes.yaml
✅ Valid YAML: /includes/includes/input_datetimes/irrigation.yaml
❌ Invalid YAML: /includes/includes/dashboard_suggestions/approved.yaml — while scanning a simple key
in "/includes/includes/dashboard_suggestions/approved.yaml", line 5, column 1
could not find expected ':'
in "/includes/includes/dashboard_suggestions/approved.yaml", line 6, column 13
✅ Valid YAML: /includes/includes/input_texts/input_textdata.yaml
✅ Valid YAML: /includes/includes/scenes/scenes.yaml
✅ Valid YAML: /includes/includes/ops/todo.yaml
✅ Valid YAML: /includes/includes/input_booleans/ask_ai_trigger.yaml
✅ Valid YAML: /includes/includes/input_booleans/irrigation_override.yaml
✅ Valid YAML: /includes/includes/input_booleans/kodi_helpers.yaml
✅ Valid YAML: /includes/includes/input_booleans/irrigation.yaml
✅ Valid YAML: /includes/includes/input_booleans/show_entity_search.yaml
✅ Valid YAML: /includes/includes/input_booleans/turn_off.yaml
✅ Valid YAML: /includes/includes/input_booleans/scan_pokemon_card.yaml
✅ Valid YAML: /includes/includes/input_booleans/all_input_booleans_combined.yaml
✅ Valid YAML: /includes/includes/input_booleans/turn_on.yaml
✅ Valid YAML: /includes/includes/input_booleans/gpt_session.yaml
✅ Valid YAML: /includes/includes/input_selects/tts_target.yaml
✅ Valid YAML: /includes/includes/input_selects/theme_mode.yaml
✅ Valid YAML: /includes/includes/input_selects/teddy_input_select.yaml
✅ Valid YAML: /includes/includes/input_selects/input_selects.yaml
✅ Valid YAML: /includes/includes/input_selects/input_select.mood.yaml
✅ Valid YAML: /includes/includes/scripts/gpt_flask_prompt.yaml
✅ Valid YAML: /includes/includes/scripts/kodi.yaml
✅ Valid YAML: /includes/includes/scripts/scripts.yaml
✅ Valid YAML: /includes/includes/cards/entity_audit_note.yaml
✅ Valid YAML: /includes/includes/cards/helper_watchdog_card.yaml
✅ Valid YAML: /includes/includes/cards/entity_status_overview.yaml
✅ Valid YAML: /includes/includes/cards/topology_mapping_note.yaml
✅ Valid YAML: /includes/includes/input_numbers/irrigation.yaml
✅ Valid YAML: /includes/includes/input_numbers/input_numbers.yaml
✅ Valid YAML: /includes/includes/chips/admin_topology_header.yaml
✅ Valid YAML: /includes/includes/chips/admin_system_header.yaml
✅ Valid YAML: /includes/includes/chips/admin_entities_header.yaml
✅ Valid YAML: /includes/includes/chips/admin_helpers_header.yaml
✅ Valid YAML: /includes/includes/sensors/command_sensors.yaml
✅ Valid YAML: /includes/includes/templates/template_sensors.yaml
✅ Valid YAML: /includes/includes/templates/jit_plugin_sensor.yaml
✅ Valid YAML: /includes/chips/admin_topology_header.yaml
✅ Valid YAML: /includes/chips/admin_system_header.yaml
✅ Valid YAML: /includes/chips/admin_entities_header.yaml
✅ Valid YAML: /includes/chips/admin_helpers_header.yaml
✅ Valid YAML: /includes/gpt_prompts/openapi_gpt_actions.yaml
✅ Valid YAML: /includes/sensors/command_sensors.yaml
✅ Valid YAML: /includes/templates/template_sensors.yaml
✅ Valid YAML: /includes/templates/jit_plugin_sensor.yaml
✅ Valid YAML: /ai_suggestions/ai made/home_messenger.yaml
>>>>>>> 4b9559e (Post-backup sync — 2025-08-18):media/AI_Zone/context_snapshots/manual_health_report.md

✅ Scan complete. See full report at:
/home/emailadmin/HA_Samba-Repo/www/context_snapshots/manual_health_report.txt
