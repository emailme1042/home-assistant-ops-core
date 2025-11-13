@echo off
echo =============================================
echo    DISABLE CUSTOM COMPONENTS
echo =============================================
echo.
echo This script disables ALL custom components
echo by renaming the custom_components folder.
echo.
echo This is safe - no data is lost!
echo.
pause

cd /d "S:\"

echo Checking for custom_components folder...
if exist "custom_components" (
    echo Found custom_components folder
    echo Renaming to custom_components_DISABLED_%date:~-4,4%%date:~-10,2%%date:~-7,2%...
    ren "custom_components" "custom_components_DISABLED_%date:~-4,4%%date:~-10,2%%date:~-7,2%"
    echo.
    echo ✅ SUCCESS: Custom components disabled!
    echo All HACS integrations are now inactive.
    echo.
) else (
    echo ❌ No custom_components folder found
    echo Components may already be disabled.
    echo.
)

echo NEXT STEPS:
echo 1. Restart Home Assistant
echo 2. Try accessing http://192.168.1.217:8123
echo 3. If working, gradually restore components
echo.
pause