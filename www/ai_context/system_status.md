# System Status

Last updated: 2025-10-24

## 🏥 Health Checks

### YAML Validation
**Status**: ⚠️ Not run recently  
**Last Run**: Unknown  
**Command**: `python3 /config/scripts/validate_yaml.py /config > /config/fix_sheet.yaml`  
**Result**: N/A

### Flask Services
**Status**: ⚠️ Not checked  
**Last Check**: Unknown  
**Command**: `curl -s -o $null -w "%{http_code}" http://localhost:5006/run_gpt`  
**Result**: N/A

### AI Preview
**Status**: ⚠️ Not run  
**Last Run**: Unknown  
**Command**: `python3 /config/python_scripts/ai_generate_suggestions.py`  
**Result**: N/A
