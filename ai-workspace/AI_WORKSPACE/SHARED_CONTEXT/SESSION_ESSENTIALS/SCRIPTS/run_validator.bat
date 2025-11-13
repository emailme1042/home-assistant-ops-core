@echo off
echo ===== Lovelace Config Validator =====
echo.
echo Running validator from: %CD%
echo.
python validate_lovelace_config.py
echo.
echo ===== Validation Complete =====
pause