@echo off
echo ============================================
echo Emergency UI Lovelace Minimalist Fix
echo ============================================
echo.
echo This script will temporarily disable UI Lovelace Minimalist
echo to resolve frontend card conflicts causing startup delays
echo.

cd /d "S:\custom_components"

if exist "ui_lovelace_minimalist" (
    echo [INFO] Found ui_lovelace_minimalist integration
    
    if exist "ui_lovelace_minimalist_DISABLED" (
        echo [WARNING] Backup already exists, removing old backup...
        rmdir /s /q "ui_lovelace_minimalist_DISABLED"
    )
    
    echo [ACTION] Disabling ui_lovelace_minimalist...
    move "ui_lovelace_minimalist" "ui_lovelace_minimalist_DISABLED"
    
    if exist "ui_lovelace_minimalist_DISABLED" (
        echo [SUCCESS] UI Lovelace Minimalist disabled
        echo [INFO] Frontend card conflicts should be resolved
        echo [INFO] To restore: rename ui_lovelace_minimalist_DISABLED back
    ) else (
        echo [ERROR] Failed to disable integration
    )
) else (
    echo [INFO] UI Lovelace Minimalist not found or already disabled
)

echo.
echo ============================================
echo Script complete. Restart HA to test fix.
echo ============================================
pause