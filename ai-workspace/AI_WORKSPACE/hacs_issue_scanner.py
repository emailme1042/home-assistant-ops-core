#!/usr/bin/env python3
"""
HACS GitHub Issue Scanner
Scans installed HACS components for known issues and compatibility problems.
"""

import json
import requests
import os
import sys
from pathlib import Path
from datetime import datetime

class HACSIssueScanner:
    def __init__(self, ha_path="S:/"):
        self.ha_path = Path(ha_path)
        self.custom_components_path = self.ha_path / "custom_components"
        self.hacs_repos_file = self.ha_path / "hacs_repos.json"
        self.session = requests.Session()
        
    def get_installed_components(self):
        """Get list of installed custom components"""
        if not self.custom_components_path.exists():
            return []
            
        components = []
        for item in self.custom_components_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                components.append(item.name)
        return components
        
    def load_hacs_repos(self):
        """Load HACS repository information"""
        if not self.hacs_repos_file.exists():
            return {}
            
        try:
            with open(self.hacs_repos_file, 'r') as f:
                return json.load(f)
        except:
            return {}
            
    def check_github_issues(self, repo_url, component_name):
        """Check GitHub repository for open issues"""
        if not repo_url.startswith('https://github.com/'):
            return []
            
        # Extract owner/repo from URL
        parts = repo_url.replace('https://github.com/', '').split('/')
        if len(parts) < 2:
            return []
            
        owner, repo = parts[0], parts[1]
        
        # Search for relevant issues
        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {
            'state': 'open',
            'per_page': 10,
            'sort': 'updated'
        }
        
        try:
            response = self.session.get(api_url, params=params, timeout=10)
            if response.status_code == 200:
                issues = response.json()
                relevant_issues = []
                
                keywords = ['home assistant', 'ha', 'error', 'conflict', 'duplicate', 'card', 'frontend']
                
                for issue in issues:
                    title = issue.get('title', '').lower()
                    body = issue.get('body', '').lower()
                    
                    if any(keyword in title or keyword in body for keyword in keywords):
                        relevant_issues.append({
                            'title': issue.get('title'),
                            'url': issue.get('html_url'),
                            'created': issue.get('created_at'),
                            'updated': issue.get('updated_at'),
                            'labels': [label.get('name') for label in issue.get('labels', [])]
                        })
                        
                return relevant_issues[:5]  # Limit to 5 most relevant
        except:
            pass
            
        return []
        
    def scan_components(self):
        """Scan all installed components for issues"""
        components = self.get_installed_components()
        hacs_repos = self.load_hacs_repos()
        
        results = {
            'scan_date': str(datetime.now()),
            'total_components': len(components),
            'components': {}
        }
        
        print(f"🔍 Scanning {len(components)} custom components...")
        
        for component in components:
            print(f"  Checking {component}...")
            
            component_info = {
                'name': component,
                'status': 'unknown',
                'issues': [],
                'repo_url': None
            }
            
            # Check if disabled
            if '_DISABLED' in component:
                component_info['status'] = 'disabled'
                component_info['note'] = 'Component disabled (folder renamed)'
            else:
                component_info['status'] = 'active'
                
            # Find repository URL in HACS data
            for repo_data in hacs_repos.values():
                if isinstance(repo_data, dict) and repo_data.get('domain') == component:
                    component_info['repo_url'] = repo_data.get('repository_url')
                    break
                    
            # Scan for GitHub issues if we have a repo URL
            if component_info['repo_url']:
                issues = self.check_github_issues(component_info['repo_url'], component)
                component_info['issues'] = issues
                
            results['components'][component] = component_info
            
        return results
        
    def generate_report(self, results):
        """Generate a formatted report"""
        report_lines = [
            "# 🔍 HACS Component Issue Scan Report",
            f"**Scan Date:** {results['scan_date']}",
            f"**Total Components:** {results['total_components']}",
            "",
            "## 📊 Component Status Overview",
            ""
        ]
        
        active_count = sum(1 for comp in results['components'].values() if comp['status'] == 'active')
        disabled_count = sum(1 for comp in results['components'].values() if comp['status'] == 'disabled')
        
        report_lines.extend([
            f"- ✅ **Active:** {active_count} components",
            f"- ⚠️ **Disabled:** {disabled_count} components",
            "",
            "## 🚨 Components with Known Issues",
            ""
        ])
        
        components_with_issues = {k: v for k, v in results['components'].items() if v['issues']}
        
        if components_with_issues:
            for comp_name, comp_data in components_with_issues.items():
                report_lines.extend([
                    f"### {comp_name}",
                    f"**Status:** {comp_data['status']}",
                    f"**Repository:** {comp_data['repo_url']}",
                    ""
                ])
                
                for issue in comp_data['issues']:
                    report_lines.extend([
                        f"- **[{issue['title']}]({issue['url']})**",
                        f"  - Updated: {issue['updated']}",
                        f"  - Labels: {', '.join(issue['labels'])}",
                        ""
                    ])
        else:
            report_lines.append("✅ No components with known GitHub issues found!")
            
        report_lines.extend([
            "",
            "## 📋 All Components",
            ""
        ])
        
        for comp_name, comp_data in sorted(results['components'].items()):
            status_icon = "⚠️" if comp_data['status'] == 'disabled' else "✅"
            issues_count = len(comp_data['issues'])
            issues_text = f" ({issues_count} issues)" if issues_count > 0 else ""
            
            report_lines.append(f"- {status_icon} **{comp_name}** - {comp_data['status']}{issues_text}")
            
        return "\n".join(report_lines)

def main():
    scanner = HACSIssueScanner()
    
    print("🔍 HACS GitHub Issue Scanner")
    print("=" * 40)
    
    results = scanner.scan_components()
    report = scanner.generate_report(results)
    
    # Save report
    report_file = Path("S:/AI_WORKSPACE/hacs_issue_scan_report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
        
    print(f"\n📄 Report saved to: {report_file}")
    print("\n" + "=" * 40)
    print("Scan complete!")

if __name__ == "__main__":
    main()