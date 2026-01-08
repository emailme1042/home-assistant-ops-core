$content = Get-Content 's:\smartidashboards\smarti-dashboard-basic.yaml' -Raw
$content = $content -replace '(?ms)            - type: markdown\s+content: >\s+# # #                 \{\% if not is_state\(''alarm_control_panel\.alarmo'', ''unavailable''\)\s+# # #                 and states\(''alarm_control_panel\.alarmo''\) != ''unknown'' \%\}\s+\s+                ✅ \*\*Alarmo is Installed and Available!\*\*\s+\s+# # #                 \{\% else \%\}\s+\s+                ⚠️ \*\*Important:\*\* Alarmo is NOT installed or not available!.*?\s+                👉 \[Click here to open the Alarmo GitHub\s+                page\]\(https://github\.com/nielsfaber/alarmo\)\s+\s+# # #                 \{\% endif \%\}', '            - type: markdown
              content: >
                ⚠️ **Important:** Alarmo is NOT installed or not available!

                Alarm-related features such as arming/disarming and alarm status
                indicators will not work until Alarmo is correctly installed.

                **To install Alarmo via HACS:**

                1. Go to **HACS → Integrations**

                2. Click the **"+" (Add Integration)** button in the bottom
                right

                3. Search for **"Alarmo"** and select it

                4. Click **Install**

                5. Restart Home Assistant after installation

                6. Go to **Settings → Devices & Services → Integrations**, click
                **"Add Integration"**, then search for **Alarmo** and complete
                setup

                👉 [Click here to open the Alarmo GitHub
                page](https://github.com/nielsfaber/alarmo)'
$content | Set-Content 's:\smartidashboards\smarti-dashboard-basic.yaml'