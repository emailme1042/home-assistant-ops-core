#!/usr/bin/env python3
"""
HACS Resource Validation
Checks if declared resources actually exist in www/community/ or www/hacsfiles/
"""

import re
from pathlib import Path

def validate_hacs_resources():
    """Validate HACS resource declarations against actual files"""
    
    print("🔍 HACS Resource Validation")
    print("=" * 40)
    
    # Read configuration.yaml to find resource declarations
    config_path = Path("s:/configuration.yaml")
    resources = []
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find resource URLs
            url_pattern = r'- url: ([^\n]+)'
            urls = re.findall(url_pattern, content)
            
            for url in urls:
                url = url.strip()
                if '/hacsfiles/' in url or '/local/community/' in url:
                    resources.append(url)
                    
    except Exception as e:
        print(f"❌ Error reading configuration.yaml: {e}")
        return
    
    print(f"📦 Found {len(resources)} HACS resource declarations")
    print()
    
    # Check if files exist
    www_root = Path("s:/www")
    missing_resources = []
    existing_resources = []
    
    for resource_url in resources:
        # Convert URL to file path
        if '/hacsfiles/' in resource_url:
            # /hacsfiles/component-name/file.js -> www/community/component-name/file.js
            file_path = resource_url.replace('/hacsfiles/', '/local/community/')
        
        if '/local/community/' in resource_url:
            # /local/community/component-name/file.js -> www/community/component-name/file.js
            relative_path = resource_url.replace('/local/community/', '')
            file_path = www_root / "community" / relative_path
        else:
            continue
            
        if file_path.exists():
            existing_resources.append(resource_url)
            print(f"✅ {resource_url}")
        else:
            missing_resources.append({
                'url': resource_url,
                'path': str(file_path)
            })
            print(f"❌ {resource_url}")
            print(f"   Expected at: {file_path}")
    
    print()
    print("📊 Summary:")
    print(f"   ✅ Existing: {len(existing_resources)}")
    print(f"   ❌ Missing: {len(missing_resources)}")
    
    # Generate report
    if missing_resources:
        print("\n🔧 HACS Resource Fix Plan:")
        print("```yaml")
        print("# Remove these broken resource declarations:")
        for resource in missing_resources:
            print(f"# - url: {resource['url']}")
        print("```")
        
        # Save detailed report
        report_lines = [
            "# 🧩 HACS Resource Validation Report",
            "",
            f"**Analysis Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total Resources Declared**: {len(resources)}",
            f"**Missing Resources**: {len(missing_resources)}",
            f"**Success Rate**: {(len(existing_resources) / len(resources) * 100):.1f}%",
            "",
            "## 🚨 Missing Resources",
            ""
        ]
        
        for resource in missing_resources:
            report_lines.extend([
                f"### ❌ `{resource['url']}`",
                f"**Expected Path**: `{resource['path']}`",
                f"**Action**: Remove from configuration.yaml or install via HACS",
                ""
            ])
        
        report_lines.extend([
            "## ✅ Existing Resources",
            ""
        ])
        
        for resource in existing_resources:
            report_lines.append(f"- ✅ `{resource}`")
        
        # Write report
        report_path = Path("s:/AI_WORKSPACE/hacs_resource_fix_plan.md")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        print(f"\n📋 Detailed report saved to: {report_path}")
    else:
        print("\n🎉 All HACS resources are properly installed!")

if __name__ == "__main__":
    validate_hacs_resources()