import os

# Support both Linux (/config) and Windows (C:\config)
possible_bases = ['/config', 'C:\\config']
fix_candidates = [os.path.join(b, 'fix_sheet.yaml') for b in possible_bases]
out_candidate = None
for b in possible_bases:
    candidate = os.path.join(b, 'AI_WORKSPACE', 'validation_summary.txt')
    if os.path.isdir(os.path.join(b, 'AI_WORKSPACE')):
        out_candidate = candidate
        break

summary = 'No validation output found.'
for fix in fix_candidates:
    if os.path.isfile(fix):
        with open(fix, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.strip().splitlines()
        issues = sum(1 for l in lines if 'error' in l.lower() or 'warning' in l.lower())
        summary = f'Validation file present: {len(lines)} lines, approx {issues} issues.'
        break

if out_candidate:
    with open(out_candidate, 'w', encoding='utf-8') as f:
        f.write(summary)
else:
    # fallback: try to write to current dir
    with open('validation_summary.txt', 'w', encoding='utf-8') as f:
        f.write(summary)

