# Home Assistant Entity Analysis Summary

**Generated:** $(Get-Date)  
**Total Entities:** 2,684  
**Unavailable Entities:** 678 (25.3%)  

## Top Unavailable Entity Domains

1. **sensor** - 306 unavailable (45.1% of unavailable)
2. **binary_sensor** - 99 unavailable (14.6% of unavailable)  
3. **automation** - 75 unavailable (11.1% of unavailable)
4. **switch** - 57 unavailable (8.4% of unavailable)
5. **media_player** - 38 unavailable (5.6% of unavailable)
6. **light** - 36 unavailable (5.3% of unavailable)

## Files Created for GPT Analysis

1. **entities.csv** - Complete list of all 2,684 entities with states
2. **unavailable_entities.csv** - Filtered list of 678 unavailable entities  
3. **unavailable_by_domain.txt** - Summary count by entity domain
4. **config.json** - Home Assistant configuration data
5. **entities.json** - Raw entity state data from HA REST API

## Key Findings

- 25% of entities are currently unavailable 
- Most unavailable entities are sensors (306), likely from integrations that need restart or reconfiguration
- 75 automations are unavailable, suggesting some automation issues
- Media players and lights show significant unavailability

## Next Steps for GPT Analysis

Drag the **unavailable_entities.csv** and **unavailable_by_domain.txt** files to GPT to:
1. Identify patterns in unavailable entities
2. Suggest which integrations might need attention
3. Determine if unavailable entities are critical or can be cleaned up
4. Recommend specific fixes for each domain type

## File Locations

All files located in: `S:\AI_WORKSPACE\SHARED_CONTEXT\SESSION_ESSENTIALS\`