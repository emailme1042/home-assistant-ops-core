# Returns minutes since last audit log update
import os
import time
import sys

def get_audit_freshness():
    """Return minutes since last audit log update"""
    log_path = "/config/AI_WORKSPACE/dashboard_health_audit.log"
    
    try:
        if os.path.exists(log_path):
            # Get file modification time
            mtime = os.path.getmtime(log_path)
            current_time = time.time()
            
            # Calculate age in minutes
            age_seconds = current_time - mtime
            age_minutes = age_seconds / 60
            
            return int(age_minutes)
        else:
            # File doesn't exist - return large number to indicate stale
            return 9999
            
    except Exception as e:
        # On error, assume stale
        print(f"Error checking audit freshness: {e}", file=sys.stderr)
        return 9999

def main():
    """Main execution"""
    freshness = get_audit_freshness()
    print(freshness)

if __name__ == "__main__":
    main()