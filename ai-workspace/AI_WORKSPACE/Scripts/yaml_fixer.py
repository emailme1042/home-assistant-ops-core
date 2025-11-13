#!/usr/bin/env python3
"""
YAML Indentation Fixer for Home Assistant Config Files
Fixes common copy-paste indentation issues
"""

import sys
import os
import yaml
import re
from pathlib import Path

def fix_yaml_indentation(file_path):
    """Fix common YAML indentation issues in HA config files"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Processing: {file_path}")
        
        # First, try to parse as YAML to check current state
        try:
            yaml.safe_load(content)
            print("✅ YAML is already valid")
            return True
        except yaml.YAMLError as e:
            print(f"⚠️ YAML Error: {e}")
        
        # Common fixes for copy-paste issues
        lines = content.split('\n')
        fixed_lines = []
        
        for i, line in enumerate(lines):
            # Skip empty lines
            if not line.strip():
                fixed_lines.append(line)
                continue
            
            # Check for commands that should be at root level (0 indent)
            # In REST commands, script files, automation files
            if re.match(r'^  [a-zA-Z_][a-zA-Z0-9_]*:', line):
                # This looks like a root-level command with wrong indentation
                if any(keyword in str(file_path).lower() for keyword in ['rest_command', 'script', 'automation']):
                    # Check if this should be a root-level entry
                    command_name = line.strip().rstrip(':')
                    
                    # Known patterns that should be root level
                    root_patterns = [
                        'ask_openai', 'gpt_', 'jit_', 'dropbox_', 'openai_', 
                        'azure_', 'google_', 'notion_', 'external_', 'update_',
                        'query_openai', 'tts_test_script'
                    ]
                    
                    if any(pattern in command_name for pattern in root_patterns):
                        print(f"🔧 Line {i+1}: Moving '{command_name}' to root level")
                        fixed_lines.append(line[2:])  # Remove 2-space indent
                        continue
            
            fixed_lines.append(line)
        
        # Try to parse the fixed content
        fixed_content = '\n'.join(fixed_lines)
        
        try:
            yaml.safe_load(fixed_content)
            print("✅ Fixed YAML is valid!")
            
            # Write back the fixed content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            return True
            
        except yaml.YAMLError as e:
            print(f"❌ Fixed YAML still has errors: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Error processing file: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python yaml_fixer.py <file_or_directory>")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    
    if target.is_file():
        if target.suffix in ['.yaml', '.yml']:
            fix_yaml_indentation(target)
        else:
            print(f"Skipping non-YAML file: {target}")
    
    elif target.is_dir():
        yaml_files = list(target.glob('**/*.yaml')) + list(target.glob('**/*.yml'))
        print(f"Found {len(yaml_files)} YAML files to check...")
        
        for yaml_file in yaml_files:
            fix_yaml_indentation(yaml_file)
    
    else:
        print(f"Path not found: {target}")

if __name__ == "__main__":
    main()