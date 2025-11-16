#!/usr/bin/env python3
"""
Weekly AI Dashboard Audit Digest
Comprehensive weekly analysis with trend detection and optimization recommendations
Generates executive summary for system performance review
"""

import yaml
import os
import time
import json
from datetime import datetime, timedelta
from pathlib import Path

def calculate_dashboard_health_grade(score):
    """Convert complexity score to letter grade"""
    if score < 50:
        return "A+ (Excellent)"
    elif score < 100:
        return "A (Good)"
    elif score < 150:
        return "B (Fair)"
    elif score < 200:
        return "C (Needs Attention)"
    else:
        return "D (Critical)"

def analyze_dashboard_trends():
    """Analyze dashboard performance trends over the week"""
    try:
        # Read previous week's data if available
        trends_file = "/config/AI_WORKSPACE/dashboard_trends.json"
        current_data = {}
        
        # Analyze current dashboard complexity
        dashboard_paths = [
            "/config/dashboards/ai",
            "/config/dashboards/ops", 
            "/config/dashboards/admin", 
            "/config/dashboards/users",
            "/config/dashboards/SYSTEM_OVERVIEW"
        ]
        
        for dashboard_dir in dashboard_paths:
            if os.path.exists(dashboard_dir):
                for file in os.listdir(dashboard_dir):
                    if file.endswith('.yaml'):
                        file_path = os.path.join(dashboard_dir, file)
                        dashboard_name = Path(file).stem
                        
                        # Calculate complexity
                        with open(file_path, 'r') as f:
                            data = yaml.safe_load(f)
                        
                        score = 0
                        if data:
                            views = data.get('views', [])
                            score = len(views) * 5
                            
                            for view in views:
                                cards = view.get('cards', [])
                                score += len(cards) * 3
                                
                                for card in cards:
                                    if 'cards' in card:
                                        score += len(card['cards']) * 5
                                    
                                    card_type = card.get('type', '')
                                    if card_type.startswith('custom:'):
                                        score += 10
                                    elif card_type in ['entities', 'grid']:
                                        score += 5
                        
                        current_data[dashboard_name] = {
                            'complexity': min(score, 999),
                            'grade': calculate_dashboard_health_grade(score),
                            'timestamp': datetime.now().isoformat()
                        }
        
        # Load previous data for comparison
        previous_data = {}
        if os.path.exists(trends_file):
            try:
                with open(trends_file, 'r') as f:
                    previous_data = json.load(f)
            except:
                pass
        
        # Save current data
        with open(trends_file, 'w') as f:
            json.dump(current_data, f, indent=2)
        
        return current_data, previous_data
    
    except Exception as e:
        print(f"Error analyzing trends: {e}")
        return {}, {}

def generate_weekly_summary():
    """Generate comprehensive weekly audit summary"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = "/config/AI_WORKSPACE/dashboard_weekly_audit.log"
    
    # Get dashboard analysis
    current_data, previous_data = analyze_dashboard_trends()
    
    # Calculate metrics
    total_dashboards = len(current_data)
    total_complexity = sum(d['complexity'] for d in current_data.values())
    avg_complexity = total_complexity / total_dashboards if total_dashboards > 0 else 0
    
    # Count by grade
    grades = {}
    for dashboard_data in current_data.values():
        grade = dashboard_data['grade'].split()[0]  # Get letter grade only
        grades[grade] = grades.get(grade, 0) + 1
    
    # Get error count
    error_count = 0
    try:
        restore_file = "/config/.storage/core.restore_state"
        if os.path.exists(restore_file):
            with open(restore_file, 'r') as f:
                content = f.read()
                error_count = content.count('input_number.frontend_errors')
    except:
        pass
    
    # Generate trend analysis
    trend_analysis = []
    for name, current in current_data.items():
        if name in previous_data:
            prev_score = previous_data[name].get('complexity', 0)
            curr_score = current['complexity']
            change = curr_score - prev_score
            
            if abs(change) > 10:
                direction = "↗️" if change > 0 else "↘️"
                trend_analysis.append(f"{direction} {name}: {change:+d}")
    
    # Generate executive summary
    if avg_complexity < 50:
        summary_status = "🏆 EXCELLENT"
        summary_note = "System optimally configured with minimal complexity"
    elif avg_complexity < 100:
        summary_status = "✅ HEALTHY"
        summary_note = "System performing well within optimal parameters"
    elif avg_complexity < 150:
        summary_status = "⚠️ MODERATE"
        summary_note = "Some dashboards approaching complexity limits"
    else:
        summary_status = "🚨 ATTENTION"
        summary_note = "Multiple dashboards require optimization"
    
    # Generate actionable recommendations
    recommendations = []
    high_complexity = [name for name, data in current_data.items() if data['complexity'] > 150]
    
    if error_count > 5:
        recommendations.append(f"Address {error_count} frontend errors")
    
    if len(high_complexity) > 0:
        recommendations.append(f"Optimize high-complexity dashboards: {', '.join(high_complexity[:2])}")
    
    if avg_complexity > 100:
        recommendations.append("Consider splitting complex dashboards into focused views")
    
    if not recommendations:
        recommendations.append("Continue current optimization strategy")
    
    # Write comprehensive log
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"=== Weekly AI Dashboard Audit Digest ===\n")
        f.write(f"Generated: {timestamp}\n")
        f.write(f"Analysis Period: {datetime.now() - timedelta(days=7):%Y-%m-%d} to {datetime.now():%Y-%m-%d}\n\n")
        
        f.write("📊 EXECUTIVE SUMMARY\n")
        f.write(f"Status: {summary_status}\n")
        f.write(f"Total Dashboards: {total_dashboards}\n")
        f.write(f"Average Complexity: {avg_complexity:.1f}\n")
        f.write(f"Frontend Errors: {error_count}\n")
        f.write(f"Assessment: {summary_note}\n\n")
        
        f.write("📈 GRADE DISTRIBUTION\n")
        for grade in ['A+', 'A', 'B', 'C', 'D']:
            count = grades.get(grade, 0)
            f.write(f"{grade}: {count} dashboard{'s' if count != 1 else ''}\n")
        f.write("\n")
        
        if trend_analysis:
            f.write("📊 TREND ANALYSIS\n")
            for trend in trend_analysis:
                f.write(f"{trend}\n")
            f.write("\n")
        
        f.write("🎯 RECOMMENDATIONS\n")
        for i, rec in enumerate(recommendations, 1):
            f.write(f"{i}. {rec}\n")
        f.write("\n")
        
        f.write("📋 DETAILED DASHBOARD ANALYSIS\n")
        for name, data in sorted(current_data.items(), key=lambda x: x[1]['complexity'], reverse=True):
            complexity = data['complexity']
            grade = data['grade']
            status_emoji = "🔥" if complexity > 150 else "⚡" if complexity > 100 else "✅"
            f.write(f"{status_emoji} {name}: {complexity} points ({grade})\n")
        
        f.write("\n=== Audit Complete ===\n")
    
    # Generate summary for template sensor
    summary_text = f"{summary_status} | Avg: {avg_complexity:.0f} | Errors: {error_count}"
    if recommendations:
        summary_text += f" | Action: {recommendations[0]}"
    
    print(summary_text)
    return summary_text

if __name__ == "__main__":
    generate_weekly_summary()