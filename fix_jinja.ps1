$content = Get-Content 's:\smartidashboards\smarti-dashboard-basic.yaml' -Raw
$content = $content -replace '(?ms)# # #                 \{\% if not is_state\(''alarm_control_panel\.alarmo'', ''unavailable''\)\s*# # #                 and states\(''alarm_control_panel\.alarmo''\) != ''unknown'' \%\}', '# # #                 {% if not is_state(''alarm_control_panel.alarmo'', ''unavailable'') %}'
$content = $content -replace '\{\% else \%\}', '# # #                 {% else %}'
$content = $content -replace '\{\% endif \%\}', '# # #                 {% endif %}'
$content | Set-Content 's:\smartidashboards\smarti-dashboard-basic.yaml'