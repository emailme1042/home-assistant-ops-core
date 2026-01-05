# 📦 HACS Installation Guide for TV Entertainment System

## Step 1: Install HACS
Run this command in Home Assistant terminal:
```bash
wget -O - https://get.hacs.xyz | bash -
```

## Step 2: Restart Home Assistant
- Go to Settings → System → Restart Home Assistant
- Wait 2-3 minutes for restart

## Step 3: Configure HACS
1. Go to Settings → Devices & Services
2. Click "+ Add Integration"
3. Search for "HACS"
4. Follow the setup wizard (you'll need a GitHub token)

## Step 4: Add Custom Repositories
**Add these repositories in HACS → Settings → Custom repositories:**

1. **Upcoming Media Card** (Frontend)
   - URL: `https://github.com/custom-cards/upcoming-media-card`
   - Category: Frontend

2. **TVMaze Integration** (Integration)
   - URL: `https://github.com/tcarlsen/ha-tvmaze`
   - Category: Integration

3. **BBC iPlayer Integration** (Integration)
   - URL: `https://github.com/allebb/ha-bbc-iplayer`
   - Category: Integration

4. **Watchlist Integration** (Integration)
   - URL: `https://github.com/thomasloven/hass-watchlist`
   - Category: Integration

## Step 5: Install Required Components
After adding repositories, install these components:

### A. Upcoming Media Card (REQUIRED for TV dashboard)
- In HACS → Frontend → Search "Upcoming Media Card"
- Click Install → Restart when prompted

### B. TVMaze Integration (for TV schedules)
- In HACS → Integrations → Search "TVMaze"
- Click Install → Restart when prompted

### C. BBC iPlayer Integration (UK TV)
- In HACS → Integrations → Search "BBC iPlayer"
- Click Install → Restart when prompted

### D. Watchlist Integration (personal watchlists)
- In HACS → Integrations → Search "Watchlist"
- Click Install → Restart when prompted

## Step 6: Final Restart
After installing all components, restart Home Assistant one final time.

## Expected Result
- TV Schedule dashboard will load properly
- No more white screen or "not found" errors
- Episode information will display in cards</content>
<parameter name="filePath">s:\AI_WORKSPACE\HACS_INSTALLATION_GUIDE.md