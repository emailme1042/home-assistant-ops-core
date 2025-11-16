@echo off
REM 🧼 Quick Log Archive Script
REM Archives current HA log and prepares for restart

echo.
echo 🧼 Quick Log Archive - Home Assistant
echo =====================================
echo.

cd /d "S:\"

echo 📊 Checking current log size...
if exist "home-assistant.log" (
    for %%I in ("home-assistant.log") do (
        set size=%%~zI
        set /a sizeMB=!size!/1048576
        echo Current log size: !sizeMB! MB
    )
) else (
    echo No current log file found
)

echo.
echo 🧼 Archiving log...
powershell -ExecutionPolicy Bypass -Command "& {$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'; if (Test-Path 'home-assistant.log') { Copy-Item 'home-assistant.log' \"home-assistant.log.archive_$timestamp\" -ErrorAction SilentlyContinue; Remove-Item 'home-assistant.log' -Force -ErrorAction SilentlyContinue; Write-Host 'Log archived and cleared' } else { Write-Host 'No log to archive' }}"

echo.
echo ✅ Log management complete!
echo.
echo 🔄 Next steps:
echo 1. Open Home Assistant: http://192.168.1.217:8123
echo 2. Go to Settings → Add-ons → SSH ^& Web Terminal
echo 3. Click "Open Web UI"
echo 4. Run: ha core restart
echo.
pause