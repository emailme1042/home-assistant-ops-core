#!/usr/bin/env python3
"""
AI-Powered Dashboard Complexity Audit Script
Analyzes dashboard complexity, performance trends, and generates optimization recommendations
Part of the intelligent Home Assistant monitoring system
"""

import yaml
import os
import time
import json
from datetime import datetime, timedelta
from pathlib import Path

def calculate_complexity_score(file_path):
    """Calculate complexity score for a single dashboard file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not data:
            return 0
            
        score = 0
        views = data.get('views', [])
        
        # Base complexity from views
        score += len(views) * 5
        
        for view in views:
            cards = view.get('cards', [])
            # Each card adds complexity
            score += len(cards) * 3
            
            for card in cards:
                # Nested cards increase complexity significantly
                if 'cards' in card:
                    score += len(card['cards']) * 5
                    
                # Complex card types
                card_type = card.get('type', '')
                if card_type.startswith('custom:'):
                    score += 10
                elif card_type in ['entities', 'grid', 'horizontal-stack', 'vertical-stack']:
                    score += 5
                elif card_type in ['conditional', 'markdown']:
                    score += 3
                    
                # Entity count multiplier
                entities = card.get('entities', [])
                if len(entities) > 10:
                    score += len(entities) // 2
        
        return min(score, 999)  # Cap at 999
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def get_frontend_error_count():
    """Get current frontend error count from restore state"""
    try:
        restore_file = "/config/.storage/core.restore_state"
        if os.path.exists(restore_file):
            with open(restore_file, 'r') as f:
                content = f.read()
                return content.count('input_number.frontend_errors')
        return 0
    except:
        return 0

def generate_optimization_recommendation(dashboard_scores, error_count):
    """Generate AI-powered optimization recommendations"""
    high_complexity = [name for name, score in dashboard_scores.items() if score > 150]
    moderate_complexity = [name for name, score in dashboard_scores.items() if 100 < score <= 150]
    
    recommendations = []
    
    if error_count > 10:
        recommendations.append("🚨 HIGH ERROR RATE: Consider reducing dashboard complexity")
    elif error_count > 5:
        recommendations.append("⚠️ MODERATE ERRORS: Monitor dashboard performance")
    
    if len(high_complexity) > 2:
        recommendations.append(f"🔥 OVERLOADED DASHBOARDS: {', '.join(high_complexity[:2])}")
    elif len(high_complexity) > 0:
        recommendations.append(f"⚡ HIGH COMPLEXITY: {high_complexity[0]} needs optimization")
    
    if len(moderate_complexity) > 5:
        recommendations.append("📊 CONSIDER SPLITTING: Multiple dashboards need review")
    
    if not recommendations:
        total_score = sum(dashboard_scores.values())
        avg_score = total_score / len(dashboard_scores) if dashboard_scores else 0
        if avg_score < 50:
            recommendations.append("✅ EXCELLENT: System optimally configured")
        else:
            recommendations.append("👍 HEALTHY: System performing well")
    
    return " | ".join(recommendations)

def run_dashboard_audit():
    """Main audit function"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = "/config/AI_WORKSPACE/dashboard_health_audit.log"
    
    # Dashboard paths to analyze
    dashboard_paths = [
        "/config/dashboards/ai",
        "/config/dashboards/ops", 
        "/config/dashboards/admin",
        "/config/dashboards/users",
        "/config/dashboards/SYSTEM_OVERVIEW"
    ]
    
    dashboard_scores = {}
    total_complexity = 0
    dashboard_count = 0
    
    # Analyze all dashboards
    for dashboard_dir in dashboard_paths:
        if os.path.exists(dashboard_dir):
            for file in os.listdir(dashboard_dir):
                if file.endswith('.yaml'):
                    file_path = os.path.join(dashboard_dir, file)
                    dashboard_name = Path(file).stem
                    score = calculate_complexity_score(file_path)
                    
                    dashboard_scores[dashboard_name] = score
                    total_complexity += score
                    dashboard_count += 1
    
    # Get error count
    error_count = get_frontend_error_count()
    
    # Generate recommendations
    recommendation = generate_optimization_recommendation(dashboard_scores, error_count)
    
    # Calculate averages
    avg_complexity = total_complexity / dashboard_count if dashboard_count > 0 else 0
    
    # Write audit log
    with open(log_file, 'w') as f:
        f.write(f"=== AI Dashboard Audit {timestamp} ===\n")
        f.write(f"Total Dashboards: {dashboard_count}\n")
        f.write(f"Average Complexity: {avg_complexity:.1f}\n")
        f.write(f"Frontend Errors: {error_count}\n")
        f.write(f"Recommendation: {recommendation}\n")
        f.write("--- Individual Dashboard Scores ---\n")
        
        for name, score in sorted(dashboard_scores.items(), key=lambda x: x[1], reverse=True):
            status = "🔥" if score > 150 else "⚡" if score > 100 else "✅"
            f.write(f"{status} {name}: {score}\n")
        
        f.write("--- Audit Complete ---\n")
    
    # Output summary for sensor
    print(f"Audit completed: {dashboard_count} dashboards, avg complexity {avg_complexity:.1f}")
    print(f"Recommendation: {recommendation}")
    
    return {
        'dashboard_count': dashboard_count,
        'avg_complexity': avg_complexity,
        'error_count': error_count,
        'recommendation': recommendation,
        'high_complexity_count': len([s for s in dashboard_scores.values() if s > 150])
    }

if __name__ == "__main__":
    run_dashboard_audit()