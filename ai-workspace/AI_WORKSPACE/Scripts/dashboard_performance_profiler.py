#!/usr/bin/env python3
"""
Dashboard Performance Profiler for Home Assistant
Analyzes dashboard performance, resource usage, and identifies optimization opportunities
Integrates with the existing dashboard watchdog system

Usage: python3 dashboard_performance_profiler.py [config_path]
"""

import yaml
import json
import os
import time
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

class DashboardPerformanceProfiler:
    def __init__(self, config_path="/config"):
        self.config_path = Path(config_path)
        self.results = {
            'analysis_time': datetime.now().isoformat(),
            'dashboard_metrics': {},
            'resource_analysis': {},
            'performance_recommendations': [],
            'audit_integration': {}
        }
        
    def analyze_dashboard_complexity(self):
        """Analyze each dashboard for complexity metrics"""
        print("🔍 Analyzing Dashboard Complexity...")
        
        config_file = self.config_path / "configuration.yaml"
        if not config_file.exists():
            print("❌ configuration.yaml not found")
            return
            
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
            
        dashboards = config.get('lovelace', {}).get('dashboards', {})
        
        for dash_key, dash_config in dashboards.items():
            filename = dash_config.get('filename', '')
            dashboard_path = self.config_path / filename
            
            metrics = {
                'file_size': 0,
                'estimated_load_time': 'Unknown',
                'complexity_score': 0,
                'resource_dependencies': [],
                'optimization_potential': 'Low'
            }
            
            if dashboard_path.exists():
                # File size analysis
                metrics['file_size'] = dashboard_path.stat().st_size
                
                # Load and analyze dashboard content
                try:
                    with open(dashboard_path, 'r') as f:
                        dashboard_yaml = yaml.safe_load(f)
                    
                    # Calculate complexity score
                    complexity = self._calculate_complexity_score(dashboard_yaml)
                    metrics['complexity_score'] = complexity
                    
                    # Estimate load time based on complexity and file size
                    load_time = self._estimate_load_time(metrics['file_size'], complexity)
                    metrics['estimated_load_time'] = f"{load_time:.1f}s"
                    
                    # Identify resource dependencies
                    metrics['resource_dependencies'] = self._find_resource_dependencies(dashboard_yaml)
                    
                    # Determine optimization potential
                    if complexity > 100 or metrics['file_size'] > 50000:
                        metrics['optimization_potential'] = 'High'
                    elif complexity > 50 or metrics['file_size'] > 25000:
                        metrics['optimization_potential'] = 'Medium'
                    
                except Exception as e:
                    print(f"⚠️ Error analyzing {filename}: {e}")
                    metrics['error'] = str(e)
            else:
                metrics['error'] = 'File not found'
                
            self.results['dashboard_metrics'][dash_key] = metrics
            print(f"  📊 {dash_key}: {metrics['complexity_score']} complexity, {metrics['estimated_load_time']} load time")
            
    def _calculate_complexity_score(self, dashboard_yaml):
        """Calculate complexity score based on dashboard structure"""
        if not dashboard_yaml:
            return 0
            
        score = 0
        
        # Count views
        views = dashboard_yaml.get('views', [])
        score += len(views) * 5
        
        # Count cards in each view
        for view in views:
            cards = view.get('cards', [])
            score += len(cards) * 2
            
            # Additional complexity for specific card types
            for card in cards:
                card_type = card.get('type', '')
                if card_type in ['entities', 'glance']:
                    entities = card.get('entities', [])
                    score += len(entities)
                elif card_type in ['custom:button-card', 'custom:mushroom-template-card']:
                    score += 3  # Custom cards add complexity
                elif card_type == 'conditional':
                    score += 5  # Conditional logic adds complexity
                elif card_type == 'vertical-stack':
                    nested_cards = card.get('cards', [])
                    score += len(nested_cards) * 1.5
                    
        return int(score)
        
    def _estimate_load_time(self, file_size_bytes, complexity_score):
        """Estimate dashboard load time based on size and complexity"""
        # Base load time from file size (assuming ~1KB per 0.01s on HA Green)
        size_factor = file_size_bytes / 1000 * 0.01
        
        # Complexity factor (each complexity point adds ~0.005s)
        complexity_factor = complexity_score * 0.005
        
        # Network factor (add 0.5s base for HA Green)
        network_factor = 0.5
        
        return size_factor + complexity_factor + network_factor
        
    def _find_resource_dependencies(self, dashboard_yaml):
        """Find custom card dependencies in dashboard"""
        dependencies = set()
        
        def scan_for_custom_cards(obj):
            if isinstance(obj, dict):
                card_type = obj.get('type', '')
                if card_type.startswith('custom:'):
                    dependencies.add(card_type)
                for value in obj.values():
                    scan_for_custom_cards(value)
            elif isinstance(obj, list):
                for item in obj:
                    scan_for_custom_cards(item)
                    
        scan_for_custom_cards(dashboard_yaml)
        return list(dependencies)
        
    def analyze_resource_performance(self):
        """Analyze resources.yaml for performance impact"""
        print("🔍 Analyzing Resource Performance...")
        
        resources_file = self.config_path / "resources.yaml"
        if not resources_file.exists():
            print("❌ resources.yaml not found")
            return
            
        with open(resources_file, 'r') as f:
            resources = yaml.safe_load(f)
            
        resource_metrics = {
            'total_resources': len(resources),
            'load_impact': 'Unknown',
            'large_resources': [],
            'optimization_suggestions': []
        }
        
        # Analyze each resource
        large_resource_threshold = 100000  # 100KB
        total_size = 0
        
        for resource in resources:
            url = resource.get('url', '')
            if url.startswith('/hacsfiles/'):
                file_path = self.config_path / "www" / "community" / url.replace('/hacsfiles/', '')
                if file_path.exists():
                    size = file_path.stat().st_size
                    total_size += size
                    
                    if size > large_resource_threshold:
                        resource_metrics['large_resources'].append({
                            'url': url,
                            'size_kb': round(size / 1024, 1)
                        })
        
        # Calculate load impact
        if total_size > 2000000:  # 2MB total
            resource_metrics['load_impact'] = 'High'
            resource_metrics['optimization_suggestions'].append("Consider removing unused resources")
        elif total_size > 1000000:  # 1MB total
            resource_metrics['load_impact'] = 'Medium'
            resource_metrics['optimization_suggestions'].append("Monitor resource usage")
        else:
            resource_metrics['load_impact'] = 'Low'
            
        self.results['resource_analysis'] = resource_metrics
        print(f"  📦 {resource_metrics['total_resources']} resources, {resource_metrics['load_impact']} impact")
        
    def generate_recommendations(self):
        """Generate performance optimization recommendations"""
        print("🚀 Generating Performance Recommendations...")
        
        recommendations = []
        
        # Dashboard-specific recommendations
        for dash_key, metrics in self.results['dashboard_metrics'].items():
            complexity = metrics.get('complexity_score', 0)
            load_time = float(metrics.get('estimated_load_time', '0s').replace('s', ''))
            
            if complexity > 100:
                recommendations.append({
                    'priority': 'High',
                    'dashboard': dash_key,
                    'issue': f'High complexity score ({complexity})',
                    'suggestion': 'Consider splitting into multiple views or using conditional cards'
                })
                
            if load_time > 3.0:
                recommendations.append({
                    'priority': 'Medium',
                    'dashboard': dash_key,
                    'issue': f'Slow estimated load time ({load_time:.1f}s)',
                    'suggestion': 'Reduce entities per card or optimize custom cards'
                })
                
        # Resource recommendations
        resource_analysis = self.results.get('resource_analysis', {})
        if resource_analysis.get('load_impact') == 'High':
            recommendations.append({
                'priority': 'High',
                'dashboard': 'Global',
                'issue': 'High resource load impact',
                'suggestion': 'Audit and remove unused HACS components'
            })
            
        # Performance recommendations
        if len(self.results['dashboard_metrics']) > 15:
            recommendations.append({
                'priority': 'Medium',
                'dashboard': 'Global',
                'issue': f"Many dashboards ({len(self.results['dashboard_metrics'])})",
                'suggestion': 'Consider consolidating similar dashboards or hiding unused ones'
            })
            
        self.results['performance_recommendations'] = recommendations
        
        print(f"  💡 Generated {len(recommendations)} recommendations")
        
    def integrate_with_audit_workflow(self):
        """Integrate results with existing audit workflow"""
        print("🔗 Integrating with Audit Workflow...")
        
        # Create audit integration data
        audit_data = {
            'timestamp': datetime.now().isoformat(),
            'total_dashboards': len(self.results['dashboard_metrics']),
            'high_priority_issues': len([r for r in self.results['performance_recommendations'] if r['priority'] == 'High']),
            'average_complexity': sum(m.get('complexity_score', 0) for m in self.results['dashboard_metrics'].values()) / max(len(self.results['dashboard_metrics']), 1),
            'resource_load_impact': self.results.get('resource_analysis', {}).get('load_impact', 'Unknown'),
            'ready_for_production': len([r for r in self.results['performance_recommendations'] if r['priority'] == 'High']) == 0
        }
        
        self.results['audit_integration'] = audit_data
        
        # Create copilot session note entry
        session_note = f"""
## Dashboard Performance Audit - {datetime.now().strftime('%Y-%m-%d %H:%M')}

### 📊 System Metrics
- **Total Dashboards**: {audit_data['total_dashboards']}
- **Average Complexity**: {audit_data['average_complexity']:.1f}
- **Resource Impact**: {audit_data['resource_load_impact']}
- **Production Ready**: {'✅ Yes' if audit_data['ready_for_production'] else '⚠️ Needs attention'}

### 🚨 High Priority Issues
{len([r for r in self.results['performance_recommendations'] if r['priority'] == 'High'])} issues requiring attention

### 🎯 Next Actions
{', '.join([r['suggestion'] for r in self.results['performance_recommendations'][:3]])}
"""
        
        return session_note
        
    def save_results(self, output_path=None):
        """Save analysis results to file"""
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = self.config_path / "AI_WORKSPACE" / f"dashboard_performance_analysis_{timestamp}.json"
            
        try:
            with open(output_path, 'w') as f:
                json.dump(self.results, f, indent=2, default=str)
            print(f"📄 Results saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error saving results: {e}")
            
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "="*60)
        print("📊 DASHBOARD PERFORMANCE ANALYSIS SUMMARY")
        print("="*60)
        
        dashboard_count = len(self.results['dashboard_metrics'])
        recommendations_count = len(self.results['performance_recommendations'])
        high_priority = len([r for r in self.results['performance_recommendations'] if r['priority'] == 'High'])
        
        print(f"🏠 Dashboards Analyzed: {dashboard_count}")
        print(f"💡 Recommendations: {recommendations_count}")
        print(f"🚨 High Priority Issues: {high_priority}")
        
        resource_analysis = self.results.get('resource_analysis', {})
        print(f"📦 Resource Impact: {resource_analysis.get('load_impact', 'Unknown')}")
        
        audit_data = self.results.get('audit_integration', {})
        if audit_data.get('ready_for_production'):
            print("✅ Production Status: READY")
        else:
            print("⚠️  Production Status: NEEDS ATTENTION")
            
        if self.results['performance_recommendations']:
            print("\n🎯 TOP RECOMMENDATIONS:")
            for i, rec in enumerate(self.results['performance_recommendations'][:3], 1):
                print(f"  {i}. [{rec['priority']}] {rec['suggestion']}")

def main():
    import sys
    config_path = sys.argv[1] if len(sys.argv) > 1 else "/config"
    
    profiler = DashboardPerformanceProfiler(config_path)
    
    # Run analysis
    profiler.analyze_dashboard_complexity()
    profiler.analyze_resource_performance()
    profiler.generate_recommendations()
    
    # Generate audit integration
    session_note = profiler.integrate_with_audit_workflow()
    
    # Save and display results
    profiler.save_results()
    profiler.print_summary()
    
    # Output session note for copilot integration
    print("\n" + "="*60)
    print("📝 COPILOT SESSION NOTE (Ready for AI_WORKSPACE)")
    print("="*60)
    print(session_note)

if __name__ == "__main__":
    main()