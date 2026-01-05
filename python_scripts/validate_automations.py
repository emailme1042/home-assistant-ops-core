import yaml
import os
from datetime import datetime

# Dynamic paths for cross-platform compatibility
AUTOMATIONS_PATH = os.getenv("AUTOMATIONS_PATH", "automations.yaml")
LOG_PATH = os.getenv("LOG_PATH", "validation_logs/automation_validation.md")
COMMENT_OUT = True  # Set to False to skip commenting broken blocks

def validate_block(block):
    issues = []
    alias = block.get('alias', 'Unnamed')
    line_hint = f"Alias: {alias}"

    # Check for nested 'data' blocks
    if isinstance(block.get('action'), list):
        for step in block['action']:
            if 'data' in step and isinstance(step['data'], dict):
                if 'data' in step['data']:
                    issues.append(f"{line_hint} → Nested 'data' block")

    # Deprecated delay syntax
    for step in block.get('action', []):
        if 'delay' in step and isinstance(step['delay'], str):
            issues.append(f"{line_hint} → Deprecated delay string")

    # Missing ID
    if 'id' not in block:
        issues.append(f"{line_hint} → Missing 'id' field")

    return issues

def comment_block(block):
    lines = yaml.dump([block], default_flow_style=False).splitlines()
    return ['# ' + line for line in lines]

def main():
    if not os.path.exists(AUTOMATIONS_PATH):
        print(f"❌ File not found: {AUTOMATIONS_PATH}")
        return

    with open(AUTOMATIONS_PATH, 'r', encoding='utf-8') as f:
        automations = yaml.safe_load(f)

    valid = []
    broken = []
    output_lines = []

    for block in automations:
        issues = validate_block(block)
        if issues:
            broken.append((block, issues))
            output_lines.extend(issues)
            if COMMENT_OUT:
                output_lines.extend(comment_block(block))
        else:
            valid.append(block)
            output_lines.extend(yaml.dump([block], default_flow_style=False).splitlines())

    # Write log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, 'w', encoding='utf-8') as log:
        log.write(f"## 🧪 Automation Validation Report\n")
        log.write(f"- ✅ Valid: {len(valid)}\n")
        log.write(f"- ⚠️ Broken: {len(broken)}\n")
        log.write(f"- 🕒 Timestamp: {timestamp}\n\n")
        for line in output_lines:
            log.write(line + '\n')

if __name__ == "__main__":
    main()
