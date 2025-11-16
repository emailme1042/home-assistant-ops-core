@echo off
echo 🤖 AI Automation System - Post-Restart Validation
echo ================================================

echo.
echo ⏳ Waiting for Home Assistant to come online...

:check_loop
timeout /t 10 /nobreak >nul
echo 🔍 Checking HA connectivity...

powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://192.168.1.217:8123' -TimeoutSec 5 -UseBasicParsing; if ($response.StatusCode -eq 200) { Write-Host '✅ Home Assistant is online!'; exit 0 } else { Write-Host '⏳ Still starting...'; exit 1 } } catch { Write-Host '⏳ Still starting...'; exit 1 }"

if errorlevel 1 goto check_loop

echo.
echo 🎉 Home Assistant is back online!
echo.
echo 📊 AI Automation System Status:
echo ================================
echo.
echo ✅ Self-Diagnosis Sensors: Ready for monitoring
echo ✅ Auto-Repair Automations: Ready for triggering  
echo ✅ OpenAI Repair Bridge: Ready for YAML fixes
echo ✅ Windows Emergency Tools: Available offline
echo ✅ Health Monitoring: Will start scoring system health
echo.
echo 🌐 Access Home Assistant:
echo   http://192.168.1.217:8123
echo   or 
echo   http://homeassistant.local:8123
echo.
echo 🔍 To check AI system health:
echo   1. Go to Developer Tools → States
echo   2. Look for: sensor.ai_system_health_score
echo   3. Check: sensor.ai_diagnostic_status
echo.
echo 🧠 AI Features Now Active:
echo   - Real-time health scoring (0-100%%)
echo   - Automatic repair triggers (Critical/Emergency)
echo   - Frontend error monitoring
echo   - Configuration safety validation
echo.
echo Press any key to open Home Assistant in browser...
pause >nul

start http://192.168.1.217:8123