filename = data.get('filename') if data.get('filename') else None
base = '/config'
allowed_prefixes = ['AI_WORKSPACE', '.github']

def safe_join(base, path):
    import os
    full = os.path.normpath(os.path.join(base, path))
    if not full.startswith(os.path.normpath(base)):
        return None
    return full

if filename:
    # Allow only whitelisted prefixes
    if any(filename.startswith(p) for p in allowed_prefixes) or filename.startswith('/'): 
        full = safe_join(base, filename)
        if full and os.path.isfile(full):
            with open(full, 'r', encoding='utf-8') as f:
                content = f.read(9999)
            hass.states.set('input_text.ai_file_preview', content)
        else:
            hass.bus.fire('ai_preview_error', {'msg': 'file not found or invalid path', 'file': filename})
    else:
        hass.bus.fire('ai_preview_error', {'msg': 'not allowed path', 'file': filename})
else:
    hass.bus.fire('ai_preview_error', {'msg': 'no filename provided'})
