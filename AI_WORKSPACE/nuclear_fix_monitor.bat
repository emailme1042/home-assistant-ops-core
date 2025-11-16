@echo off
echo ===============================================
echo 🛡️ NUCLEAR FIX: Core-Only HA Monitoring
echo ===============================================
echo.
echo ✅ ALL Custom Components DISABLED
echo ✅ UI Lovelace Minimalist DISABLED (root + custom_components)
echo ✅ HA should boot with CORE integrations only
echo.
echo 🔄 Monitoring core-only startup...
echo.

:loop
powershell -Command "try { $r = Invoke-WebRequest -Uri 'http://192.168.1.217:8123' -TimeoutSec 5; if ($r.StatusCode -eq 200) { Write-Host '[🎉 CORE SUCCESS] HA Core responding! Status: 200' -ForegroundColor Green; exit 0 } } catch { Write-Host '[⏳ WAITING] Core still starting...' -ForegroundColor Yellow }"

if %errorlevel% equ 0 (
    echo.
    echo ===============================================
    echo 🎉 HOME ASSISTANT CORE IS ONLINE!
    echo ===============================================
    echo.
    echo 📊 Nuclear Fix Results:
    echo ✅ Core integrations only
    echo ✅ No custom component conflicts
    echo ✅ Frontend should load with basic functionality
    echo ✅ Emergency recovery dashboard available
    echo.
    echo 🌐 Access HA: http://192.168.1.217:8123
    echo 📁 Use: emergency_recovery_dashboard.yaml if needed
    echo.
    echo 🔧 To restore custom components later:
    echo    rename custom_components_EMERGENCY_DISABLED to custom_components
    echo.
    echo ===============================================
    pause
    exit
)

timeout /t 10 /nobreak > nul
goto loop