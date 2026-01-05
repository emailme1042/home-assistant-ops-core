# ZIGBEE MESH SURGERY PROTOCOL - Socket Re-pairing
# Target: socket Z1, Z2, Z3 (moved to new rooms)
# Goal: Optimize mesh routing after relocation

## PHASE 1: Pre-Surgery Assessment
1. Check current LQI values in Z2M web UI
2. Note current locations of moved sockets
3. Verify coordinator position (should be central/elevated)

## PHASE 2: Strategic Re-pairing Sequence
# Re-pair in order of mesh importance:

### 1. Socket Z1 (0xa4c13801f84cffff)
- Location: [Room where moved]
- Purpose: Primary mesh router
- Re-pair first for best routing

### 2. Socket Z2 (0xa4c13801e95fffff)
- Location: [Room where moved]
- Purpose: Secondary mesh router
- Re-pair second

### 3. Socket Z3 (0xa4c13801d40cffff)
- Location: [Room where moved]
- Purpose: Tertiary mesh router
- Re-pair last

## PHASE 3: Re-pairing Process
For each socket:
1. Enable permit join for 60 seconds in Z2M
2. Press socket reset button 5x quickly
3. Wait for LED to flash rapidly (factory reset)
4. Socket should auto-pair within 60 seconds
5. Verify in Z2M dashboard with improved LQI

## PHASE 4: Post-Surgery Validation
1. Check LQI improvement (>50 preferred)
2. Test device responsiveness
3. Monitor mesh stability for 24 hours
4. Update HA entity references if needed

## SUCCESS METRICS
- LQI > 50 for all devices
- Faster device response times
- Reduced mesh congestion
- Improved battery life on end devices