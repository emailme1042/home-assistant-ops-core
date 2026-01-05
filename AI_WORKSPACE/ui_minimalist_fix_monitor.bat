@echo off
echo ===============================================
echo 🛡️ UI Minimalist Fix Status Monitor
echo ===============================================
echo.
echo ✅ UI Lovelace Minimalist DISABLED
echo ✅ Folder renamed to ui_lovelace_minimalist_DISABLED
echo ✅ Frontend card conflicts should be resolved
echo.
echo 🔄 Monitoring HA startup progress...
echo.

:loop
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://192.168.1.217:8123' -TimeoutSec 3; if ($r.StatusCode -eq 200) { Write-Host '[SUCCESS] HA is responding! Status Code: 200' -ForegroundColor Green; exit 0 } } catch { Write-Host '[WAITING] HA still starting...' -ForegroundColor Yellow }"

if %errorlevel% equ 0 (
    echo.
    echo ===============================================
    echo 🎉 HOME ASSISTANT IS BACK ONLINE!
    echo ===============================================
    echo.
    echo 📊 Expected Results:
    echo ✅ No UI Minimalist card conflicts
    echo ✅ Frontend should load properly
    echo ✅ All sensors and automations available
    echo ✅ AI automation system ready for testing
    echo.
    echo 🌐 Open HA: http://192.168.1.217:8123
    echo.
    echo ===============================================
    pause
    exit
)

timeout /t 10 /nobreak > nul
goto loop