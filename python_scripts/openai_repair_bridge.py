#!/usr/bin/env python3
"""
OpenAI Repair Bridge for Home Assistant
Sends broken YAML files to OpenAI for automated repair suggestions
"""

import os
import sys
import json
import requests
from pathlib import Path

def get_openai_api_key():
    """Get OpenAI API key from environment or secrets.yaml"""
    # Try environment variable first
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key:
        return api_key
    
    # Try secrets.yaml
    try:
        with open('secrets.yaml', 'r') as f:
            for line in f:
                if line.strip().startswith('openai_api_key:'):
                    return line.split(':', 1)[1].strip()
    except FileNotFoundError:
        pass
    
    return None

def send_to_openai(file_content, file_path, error_description=""):
    """Send file content to OpenAI for repair suggestions"""
    api_key = get_openai_api_key()
    if not api_key:
        print("❌ ERROR: OpenAI API key not found")
        return None
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    prompt = f"""
You are a Home Assistant YAML configuration expert. Please analyze and fix the following YAML file:

File: {file_path}
Error Description: {error_description}

YAML Content:
```yaml
{file_content}
```

Please provide:
1. A corrected version of the YAML
2. A brief explanation of what was fixed
3. Any recommendations for preventing similar issues

Return the response in this format:
FIXED_YAML:
```yaml
[corrected yaml here]
```

EXPLANATION:
[explanation of fixes]

RECOMMENDATIONS:
[prevention recommendations]
"""
    
    data = {
        'model': 'gpt-4o',
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.1,
        'max_tokens': 2000
    }
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ ERROR calling OpenAI: {e}")
        return None

def repair_yaml_file(file_path, error_description=""):
    """Repair a YAML file using OpenAI"""
    file_path = Path(file_path)
    
    if not file_path.exists():
        print(f"❌ ERROR: File not found: {file_path}")
        return False
    
    print(f"🔍 Analyzing file: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ ERROR reading file: {e}")
        return False
    
    print("🧠 Sending to OpenAI for analysis...")
    response = send_to_openai(content, str(file_path), error_description)
    
    if not response:
        return False
    
    # Save the response
    output_file = file_path.parent / f"{file_path.stem}_FIXED{file_path.suffix}"
    response_file = file_path.parent / f"{file_path.stem}_REPAIR_RESPONSE.md"
    
    try:
        with open(response_file, 'w', encoding='utf-8') as f:
            f.write(response)
        
        # Extract fixed YAML if present
        if 'FIXED_YAML:' in response:
            yaml_start = response.find('```yaml', response.find('FIXED_YAML:'))
            if yaml_start != -1:
                yaml_start = response.find('\n', yaml_start) + 1
                yaml_end = response.find('```', yaml_start)
                if yaml_end != -1:
                    fixed_yaml = response[yaml_start:yaml_end].strip()
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(fixed_yaml)
                    print(f"✅ Fixed YAML saved to: {output_file}")
        
        print(f"✅ Full response saved to: {response_file}")
        return True
        
    except Exception as e:
        print(f"❌ ERROR saving response: {e}")
        return False

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python openai_repair_bridge.py <file_path> [error_description]")
        print("Example: python openai_repair_bridge.py configuration.yaml 'Duplicate key error'")
        return
    
    file_path = sys.argv[1]
    error_description = sys.argv[2] if len(sys.argv) > 2 else ""
    
    print("🤖 OpenAI YAML Repair Bridge")
    print(f"📁 Target file: {file_path}")
    if error_description:
        print(f"🐛 Error: {error_description}")
    
    success = repair_yaml_file(file_path, error_description)
    
    if success:
        print("🎉 Repair process completed successfully!")
    else:
        print("❌ Repair process failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()