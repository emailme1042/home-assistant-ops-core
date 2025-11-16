@echo off
REM AI Configuration Auto-Patch Script for Windows
REM One-click YAML repair and validation

echo 🤖 AI Configuration Auto-Patch Script
echo ========================================

echo.
echo 📋 Checking system status...

REM Check if we're in the right directory
if not exist "configuration.yaml" (
    echo ❌ ERROR: configuration.yaml not found
    echo Please run this script from your Home Assistant config directory
    pause
    exit /b 1
)

echo ✅ Found configuration.yaml

REM Check Python availability
python --version >nul 2>&1
if errorlevel 1 (
    echo ⚠️ WARNING: Python not found in PATH
    echo Some repair functions may not work
) else (
    echo ✅ Python available
)

echo.
echo 🔍 Running YAML validation...

REM Try HA CLI validation first
ha core check >validate_output.txt 2>&1
if errorlevel 1 (
    echo ⚠️ HA CLI validation failed or not available
    echo Trying alternative validation...
    
    REM Try Python YAML validation
    python -c "import yaml; yaml.safe_load(open('configuration.yaml'))" 2>yaml_errors.txt
    if errorlevel 1 (
        echo ❌ YAML syntax errors detected
        echo Errors saved to yaml_errors.txt
        goto :repair
    ) else (
        echo ✅ YAML syntax is valid
    )
) else (
    echo ✅ HA CLI validation passed
    goto :success
)

:repair
echo.
echo 🔧 Starting repair process...

REM Check if OpenAI bridge is available
if exist "python_scripts\openai_repair_bridge.py" (
    echo 🧠 OpenAI repair bridge found
    echo.
    set /p use_openai="Use OpenAI for automated repair? (y/n): "
    if /i "%use_openai%"=="y" (
        echo 🚀 Calling OpenAI for repair suggestions...
        python python_scripts\openai_repair_bridge.py configuration.yaml "YAML validation failed"
        if errorlevel 1 (
            echo ❌ OpenAI repair failed
        ) else (
            echo ✅ OpenAI repair completed
            echo Check configuration_FIXED.yaml for suggested fixes
        )
    )
)

REM Create backup
echo.
echo 💾 Creating backup...
copy configuration.yaml configuration_backup_%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%.yaml
echo ✅ Backup created

REM Common fix attempts
echo.
echo 🔧 Applying common fixes...

REM Fix duplicate key issues (common issue)
powershell -Command "(Get-Content configuration.yaml) | Select-Object -Unique | Set-Content configuration_temp.yaml"
if exist configuration_temp.yaml (
    move configuration_temp.yaml configuration.yaml
    echo ✅ Duplicate line removal attempted
)

REM Validate again
echo.
echo 🔍 Re-validating after fixes...
python -c "import yaml; yaml.safe_load(open('configuration.yaml'))" 2>yaml_errors_after.txt
if errorlevel 1 (
    echo ❌ Issues still remain
    echo Check yaml_errors_after.txt for details
) else (
    echo ✅ YAML validation now passes!
    goto :success
)

goto :end

:success
echo.
echo 🎉 Configuration validation successful!
echo ✅ Your Home Assistant configuration is ready
echo.
echo 📋 Next steps:
echo 1. Restart Home Assistant
echo 2. Check for any startup errors
echo 3. Verify dashboards load correctly

:end
echo.
echo 📁 Log files created:
if exist validate_output.txt echo - validate_output.txt (HA CLI output)
if exist yaml_errors.txt echo - yaml_errors.txt (YAML syntax errors)
if exist yaml_errors_after.txt echo - yaml_errors_after.txt (Post-fix validation)
if exist configuration_FIXED.yaml echo - configuration_FIXED.yaml (OpenAI suggestions)

echo.
echo 📞 For additional help, check the AI workspace documentation
pause