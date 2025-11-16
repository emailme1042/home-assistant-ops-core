@echo off
echo =============================================
echo    HA FRONTEND REBUILD SCRIPT
echo =============================================
echo.
echo This script rebuilds the Home Assistant frontend
echo to fix compilation errors and restore UI access.
echo.
echo WARNING: This requires SSH access to HA
echo.
pause

echo Starting frontend rebuild...
ha core rebuild

echo.
echo Frontend rebuild initiated!
echo.
echo NEXT STEPS:
echo 1. Wait 5-10 minutes for rebuild to complete
echo 2. Try accessing http://192.168.1.217:8123
echo 3. If still broken, run disable_custom_components.bat
echo.
pause