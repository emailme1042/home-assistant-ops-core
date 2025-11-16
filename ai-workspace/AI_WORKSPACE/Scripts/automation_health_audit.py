#!/usr/bin/env python3
"""
Automation Health Audit Script
Implements CP's suggested automation health scanning
"""

import os
import yaml
import json
import sys
from pathlib import Path

def scan_automation_files(automation_dir):
    """Scan automation files for orphaned triggers, unused IDs, legacy patterns"""
    results = {
        "orphaned_triggers": [],
        "unused_ids": [],
        "legacy_conditions": [],
        "missing_entities": [],
        "session_tags": []
    }
    
    automation_files = list(Path(automation_dir).rglob("*.yaml"))
    
    for file_path in automation_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = yaml.safe_load(f)
                
            if not content:
                continue
                
            # Handle both single automation and list of automations
            automations = content if isinstance(content, list) else [content]
            
            for automation in automations:
                if not isinstance(automation, dict):
                    continue
                    
                # Check for orphaned triggers
                if 'trigger' in automation and 'condition' not in automation:
                    results["orphaned_triggers"].append({
                        "file": str(file_path),
                        "automation": automation.get('alias', 'unnamed'),
                        "id": automation.get('id', 'no_id')
                    })
                
                # Check for unused IDs (basic check)
                if 'id' not in automation and 'alias' in automation:
                    results["unused_ids"].append({
                        "file": str(file_path),
                        "automation": automation.get('alias', 'unnamed'),
                        "issue": "missing_id"
                    })
                
                # Check for legacy condition patterns
                if 'condition' in automation:
                    conditions = automation['condition']
                    if isinstance(conditions, dict) and 'platform' in conditions:
                        results["legacy_conditions"].append({
                            "file": str(file_path),
                            "automation": automation.get('alias', 'unnamed'),
                            "pattern": "old_platform_syntax"
                        })
                
                # Check for session tags
                if 'session_tag' in automation:
                    results["session_tags"].append({
                        "file": str(file_path),
                        "automation": automation.get('alias', 'unnamed'),
                        "tag": automation['session_tag']
                    })
                        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    return results

def generate_audit_report(results, output_file):
    """Generate markdown audit report"""
    report = f"""# 🤖 Automation Health Audit Report
Generated: {os.popen('date').read().strip()}

## 📊 Summary
- **Orphaned Triggers**: {len(results['orphaned_triggers'])}
- **Missing IDs**: {len(results['unused_ids'])}
- **Legacy Patterns**: {len(results['legacy_conditions'])}
- **Session Tagged**: {len(results['session_tags'])}

## 🔍 Detailed Results

### Orphaned Triggers (Triggers without Conditions)
"""
    
    if results['orphaned_triggers']:
        for item in results['orphaned_triggers']:
            report += f"- **{item['automation']}** in `{item['file']}`\n"
    else:
        report += "✅ No orphaned triggers found.\n"
    
    report += "\n### Missing Automation IDs\n"
    if results['unused_ids']:
        for item in results['unused_ids']:
            report += f"- **{item['automation']}** in `{item['file']}`\n"
    else:
        report += "✅ All automations have IDs.\n"
    
    report += "\n### Legacy Condition Patterns\n"
    if results['legacy_conditions']:
        for item in results['legacy_conditions']:
            report += f"- **{item['automation']}** in `{item['file']}` - {item['pattern']}\n"
    else:
        report += "✅ No legacy patterns detected.\n"
        
    report += "\n### Session Tags Applied\n"
    if results['session_tags']:
        for item in results['session_tags']:
            report += f"- **{item['automation']}** - Tag: `{item['tag']}`\n"
    else:
        report += "⚠️ No session tags found - consider adding for traceability.\n"
    
    report += f"""
## 🎯 Recommendations

### Immediate Actions
1. **Add Session Tags**: Tag automations with `session_tag: audit_2025_10_27`
2. **Fix Orphaned Triggers**: Add conditions or remove unused triggers
3. **Add Missing IDs**: Ensure all automations have unique IDs

### CP's Suggested Focus Areas
- ✅ Orphaned trigger blocks: {len(results['orphaned_triggers'])} found
- ✅ Unused automation IDs: {len(results['unused_ids'])} found  
- ✅ Legacy condition logic: {len(results['legacy_conditions'])} found
- ⚙️ Session tagging: {len(results['session_tags'])} automations tagged

### Multi-Agent Coordination
- **GitHub Copilot**: Apply session tags and fix structural issues
- **ChatGPT**: Review logic patterns and suggest improvements
- **Edge Copilot**: Research latest HA automation best practices
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Audit report generated: {output_file}")

if __name__ == "__main__":
    automation_dir = "includes/automations"
    output_file = "AI_WORKSPACE/automation_audit_report.md"
    
    print("🤖 Running Automation Health Audit...")
    print(f"Scanning directory: {automation_dir}")
    
    if not os.path.exists(automation_dir):
        print(f"❌ Directory not found: {automation_dir}")
        sys.exit(1)
    
    results = scan_automation_files(automation_dir)
    print(f"📊 Scan results: {results}")
    
    generate_audit_report(results, output_file)
    
    print(f"✅ Audit complete! Found:")
    print(f"   - {len(results['orphaned_triggers'])} orphaned triggers")
    print(f"   - {len(results['unused_ids'])} missing IDs") 
    print(f"   - {len(results['legacy_conditions'])} legacy patterns")
    print(f"   - {len(results['session_tags'])} session tags")