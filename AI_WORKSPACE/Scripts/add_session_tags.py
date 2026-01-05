#!/usr/bin/env python3
"""
Add session tags to copilot session notes
"""

import sys
import os
from datetime import datetime

def add_session_tag(tag):
    """Add a tag to the session notes"""
    session_file = "/config/AI_WORKSPACE/copilot_session_notes.md"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    tag_line = f"\n**{timestamp}** - Tag added: {tag}\n"

    try:
        with open(session_file, "a") as f:
            f.write(tag_line)
        print(f"Tag '{tag}' added to session notes")
    except Exception as e:
        print(f"Error adding tag: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        tag = sys.argv[1]
        add_session_tag(tag)
    else:
        print("Usage: python3 add_session_tags.py <tag>")