@echo off
echo ============================================
echo Emergency Custom Components Disable Script
echo ============================================
echo.
echo This script will temporarily rename custom_components
echo to custom_components_DISABLED for diagnosis
echo.
echo Press Ctrl+C to cancel, or
pause

cd /d "S:\"

if exist "custom_components" (
    echo [INFO] Found custom_components folder
    
    if exist "custom_components_DISABLED" (
        echo [WARNING] custom_components_DISABLED already exists
        echo [ACTION] Removing old disabled folder first...
        rmdir /s /q "custom_components_DISABLED"
    )
    
    echo [ACTION] Renaming custom_components to custom_components_DISABLED...
    move "custom_components" "custom_components_DISABLED"
    
    if exist "custom_components_DISABLED" (
        echo [SUCCESS] Custom components disabled successfully
        echo [INFO] HA should now boot with only core integrations
        echo.
        echo To re-enable: run emergency_custom_components_restore.bat
    ) else (
        echo [ERROR] Failed to disable custom components
    )
) else (
    echo [INFO] No custom_components folder found
)

echo.
echo ============================================
echo Script complete. HA Core should restart faster now.
echo ============================================
pause