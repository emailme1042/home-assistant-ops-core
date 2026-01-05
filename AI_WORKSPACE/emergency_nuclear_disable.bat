@echo off
echo ===============================================
echo 🚨 EMERGENCY: Full Custom Components Disable
echo ===============================================
echo.
echo This will disable ALL custom components as nuclear option
echo to get HA Core running with minimal dependencies
echo.
echo Press Ctrl+C to cancel, or
pause

cd /d "S:\"

if exist "custom_components" (
    echo [INFO] Disabling custom_components folder...
    
    if exist "custom_components_EMERGENCY_DISABLED" (
        echo [WARNING] Removing old emergency backup...
        rmdir /s /q "custom_components_EMERGENCY_DISABLED"
    )
    
    move "custom_components" "custom_components_EMERGENCY_DISABLED"
    
    if exist "custom_components_EMERGENCY_DISABLED" (
        echo [SUCCESS] ALL custom components disabled
        echo [INFO] HA should now boot with core-only
        echo.
        echo To restore: rename custom_components_EMERGENCY_DISABLED back
    ) else (
        echo [ERROR] Failed to disable custom components
    )
) else (
    echo [INFO] custom_components already disabled
)

echo.
echo [INFO] Also checking for other UI Minimalist folders...
if exist "ui_lovelace_minimalist_DISABLED_ROOT" (
    echo [INFO] Root UI Minimalist already disabled
) else (
    echo [WARNING] Root UI Minimalist folder may still be active
)

echo.
echo ===============================================
echo Nuclear option complete. Restart HA now.
echo ===============================================
pause