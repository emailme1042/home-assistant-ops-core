@echo off
echo =============================================
echo    RESTORE CUSTOM COMPONENTS
echo =============================================
echo.
echo This script restores custom components
echo by finding and renaming disabled folders.
echo.
pause

cd /d "S:\"

echo Searching for disabled custom_components folders...
for /d %%i in (custom_components_DISABLED_*) do (
    echo Found: %%i
    echo Renaming back to custom_components...
    ren "%%i" "custom_components"
    echo.
    echo ✅ SUCCESS: Custom components restored!
    echo HACS integrations will load on next restart.
    echo.
    goto :restored
)

echo ❌ No disabled custom_components folders found
echo Components may already be restored or never disabled.
echo.

:restored
echo NEXT STEPS:
echo 1. Restart Home Assistant
echo 2. Wait for all integrations to load
echo 3. Check for any startup errors
echo.
pause