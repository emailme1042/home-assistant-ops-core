#!/usr/bin/env python3
"""
Dashboard Complexity Scoring Engine
Analyzes individual dashboard complexity for heatmap visualization
Outputs per-dashboard scores for command_line sensors
"""

import yaml
import os
import sys
from pathlib import Path

def score_dashboard_complexity(file_path):
    """Calculate complexity score for a single dashboard file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not data:
            return 0
            
        score = 0
        views = data.get('views', [])
        
        # Base score from number of views
        score += len(views) * 5
        
        for view in views:
            cards = view.get('cards', [])
            # Each card adds to complexity
            score += len(cards) * 3
            
            for card in cards:
                # Nested cards (like grid, vertical-stack) increase complexity
                if 'cards' in card:
                    score += len(card['cards']) * 5
                    
                # Complex card types add more weight
                card_type = card.get('type', '')
                if card_type in ['custom:', 'picture-elements', 'map']:
                    score += 10
                elif card_type in ['entities', 'grid', 'horizontal-stack', 'vertical-stack']:
                    score += 5
                elif card_type in ['conditional', 'markdown']:
                    score += 3
                    
                # Entity count in entities cards
                if card_type == 'entities' and 'entities' in card:
                    score += len(card['entities']) * 2
        
        return min(score, 999)  # Cap at 999 for display purposes
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return 0

def get_dashboard_name_from_path(file_path):
    """Extract clean dashboard name from file path"""
    filename = Path(file_path).stem
    
    # Clean up common dashboard name patterns
    name_map = {
        'ai_workspace_overview': 'ai_workspace',
        'recovery_dashboard': 'recovery', 
        'SYSTEM_OVERVIEW': 'system_overview',
        'user_dashboard': 'user_dashboard',
        'network_diagnostics': 'network_diagnostics',
        'entity_reference': 'entity_reference',
        'main_admin': 'main_admin',
        'automation_audit': 'automation_audit',
        'main': 'ops_main',
        'ai-workspace': 'ai_workspace'
    }
    
    return name_map.get(filename, filename.lower())

def main():
    """Main function - can be called with specific dashboard name or scan all"""
    base_path = "S:" if os.name == 'nt' else "/config"
    dashboard_paths = [
        f"{base_path}/dashboards/ai",
        f"{base_path}/dashboards/ops", 
        f"{base_path}/dashboards/admin",
        f"{base_path}/dashboards/users",
        f"{base_path}/dashboards/SYSTEM_OVERVIEW"
    ]
    
    # If specific dashboard requested via command line argument
    if len(sys.argv) > 1:
        requested_dashboard = sys.argv[1].lower()
        
        # Search for matching dashboard file
        for dashboard_dir in dashboard_paths:
            if os.path.exists(dashboard_dir):
                for file in os.listdir(dashboard_dir):
                    if file.endswith('.yaml'):
                        file_path = os.path.join(dashboard_dir, file)
                        dashboard_name = get_dashboard_name_from_path(file_path)
                        
                        if dashboard_name == requested_dashboard:
                            score = score_dashboard_complexity(file_path)
                            print(score)  # Output just the score for command_line sensor
                            return
        
        # If not found, return 0
        print(0)
        return
    
    # Otherwise, output all dashboard scores (for debugging)
    print("Dashboard Complexity Analysis:")
    print("=" * 40)
    
    total_score = 0
    dashboard_count = 0
    
    for dashboard_dir in dashboard_paths:
        if os.path.exists(dashboard_dir):
            for file in os.listdir(dashboard_dir):
                if file.endswith('.yaml'):
                    file_path = os.path.join(dashboard_dir, file)
                    dashboard_name = get_dashboard_name_from_path(file_path)
                    score = score_dashboard_complexity(file_path)
                    
                    print(f"{dashboard_name}: {score}")
                    total_score += score
                    dashboard_count += 1
    
    if dashboard_count > 0:
        avg_score = total_score / dashboard_count
        print(f"\nAverage Complexity: {avg_score:.1f}")
        print(f"Total Dashboards: {dashboard_count}")

if __name__ == "__main__":
    main()