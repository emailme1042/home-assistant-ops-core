@echo off
echo ============================================
echo Emergency Custom Components Restore Script
echo ============================================
echo.

cd /d "S:\"

if exist "custom_components_DISABLED" (
    echo [INFO] Found disabled custom_components folder
    
    if exist "custom_components" (
        echo [WARNING] custom_components already exists
        echo [ACTION] Removing current custom_components folder...
        rmdir /s /q "custom_components"
    )
    
    echo [ACTION] Restoring custom_components_DISABLED to custom_components...
    move "custom_components_DISABLED" "custom_components"
    
    if exist "custom_components" (
        echo [SUCCESS] Custom components restored successfully
        echo [INFO] All HACS integrations should be available again
    ) else (
        echo [ERROR] Failed to restore custom components
    )
) else (
    echo [ERROR] No custom_components_DISABLED folder found
    echo [INFO] Nothing to restore
)

echo.
echo ============================================
echo Script complete. Restart HA to load all integrations.
echo ============================================
pause