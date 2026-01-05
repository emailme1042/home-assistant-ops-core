# 🔗 Custom HACS Repository Links for TV Entertainment System

## Required Custom Repositories to Add in HACS

### 1. **Upcoming Media Card** (Frontend Component)
- **Repository URL**: `https://github.com/custom-cards/upcoming-media-card`
- **Category**: Frontend
- **Status**: ✅ Verified - This URL is correct

### 2. **TVMaze Integration** (Integration)
- **Repository URL**: `https://github.com/tcarlsen/ha-tvmaze`
- **Category**: Integration
- **Status**: ✅ Corrected - Previous URL was wrong

### 3. **BBC iPlayer Integration** (Integration)
- **Repository URL**: `https://github.com/allebb/ha-bbc-iplayer`
- **Category**: Integration
- **Status**: ✅ Corrected - Previous URL was wrong

### 4. **Watchlist Integration** (Integration)
- **Repository URL**: `https://github.com/thomasloven/hass-watchlist`
- **Category**: Integration
- **Status**: ✅ Corrected - Previous URL was wrong

## How to Add Custom Repositories in HACS

1. **Install HACS first** (if not done):
   ```bash
   wget -O - https://get.hacs.xyz | bash -
   ```

2. **Restart Home Assistant**

3. **Configure HACS**:
   - Go to Settings → Devices & Services → Add Integration → HACS

4. **Add Custom Repositories**:
   - Open HACS (should appear in sidebar)
   - Go to HACS → Settings (gear icon)
   - Click "Custom repositories"
   - Add each repository URL above with correct category
   - Click "ADD"

5. **Install Components**:
   - Go to HACS → Frontend/Integrations tab
   - Search for each component name
   - Click Install → Restart when prompted

## Alternative: Use HACS Discovery
Some components might be discoverable in HACS without custom repos. Try searching first before adding custom repos.</content>
<parameter name="filePath">s:\AI_WORKSPACE\CUSTOM_HACS_REPOS.md