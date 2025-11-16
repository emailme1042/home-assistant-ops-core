# Session Update  2025-11-15 23:37
## Network Status
-  IPv6 enabled and working (2a01::/64)
-  IPv4 stable, DNS functional for normal domains
-  nabu.casa / ui.nabu.casa unresolved globally (provider-side DNS outage)

## Verified Results
- nslookup google.com  OK
- nslookup nabu.casa  No answer (all resolvers)
- ping -6 google.com  OK
- Home Assistant: local OK, Cloud pending DNS restore

## Next Steps
1. Keep HA running normally (local automations safe)
2. Re-check DNS hourly:
   
slookup ui.nabu.casa 1.1.1.1
3. Once IP resolves, reconnect HA Cloud
