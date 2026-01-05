---

**🚨 PREFIX DELEGATION GREYED OUT — 2026-01-03**
**DATE:** 2026-01-03
**OPERATOR:** ⚙️ GitHub Copilot (VSCode)
**SESSION OWNER:** 👤 Jamie

#### 🎯 ISSUE IDENTIFIED
User reports: "prfix greyed out" - Prefix Delegation option is greyed out in Unifi Cloud Ultra IPv6 settings, preventing IPv6 enablement for Matter protocol.

#### 🔍 ROOT CAUSE ANALYSIS
**Prefix Delegation Greyed Out**: ✅ **ISP/IPV6 AVAILABILITY ISSUE**
- **Symptom**: Prefix Delegation option unavailable in Cloud Ultra interface
- **Root Cause**: ISP does not provide IPv6 prefix delegation, or WAN interface IPv6 not enabled
- **Impact**: Cannot enable IPv6 for LAN networks, blocking Tado Matter integration

#### 📋 TROUBLESHOOTING STEPS
**1. Check WAN IPv6 Status**:
- Navigate to Unifi Cloud Ultra → Settings → Networks → WAN
- Check if IPv6 is enabled on WAN interface
- Look for IPv6 address assignment from ISP

**2. Enable WAN IPv6**:
- In WAN settings, enable IPv6 if available
- Set IPv6 Connection Type to "DHCPv6" or "Auto"
- Save and wait for IPv6 address assignment

**3. Alternative: Static IPv6**:
- If Prefix Delegation unavailable, try "Static" IPv6
- You'll need IPv6 prefix from ISP (contact them)
- Configure static IPv6 range for LAN

**4. ISP IPv6 Support Check**:
- Contact your internet provider
- Ask if they support IPv6 and prefix delegation
- Request IPv6 enablement if available

**5. Test IPv6 Connectivity**:
- Use online IPv6 test tools
- Check if your WAN has IPv6 connectivity

#### 🎯 ALTERNATIVE SOLUTIONS
**If ISP Doesn't Support IPv6**:
- **6in4 Tunnel**: Use Hurricane Electric or similar service for IPv6 tunnel
- **DS-Lite**: Some ISPs use dual-stack lite (check with provider)
- **CGNAT Bypass**: May require ISP cooperation

**Matter Protocol Requirements**:
- IPv6 is mandatory for Matter device commissioning
- Without IPv6, Tado thermostat cannot join Matter fabric
- Aqara/Apple ecosystems require IPv6 for Matter integration

#### 📊 EXPECTED OUTCOMES
- **WAN IPv6 Enabled**: Prefix Delegation becomes available for LAN
- **Static IPv6 Works**: Alternative configuration if delegation unavailable
- **ISP Support Confirmed**: IPv6 enabled by provider
- **Matter Integration**: Tado thermostat can commission to Aqara/Apple

#### 🏆 ACHIEVEMENT LEVEL
**CRITICAL INFRASTRUCTURE BLOCKER IDENTIFIED**: Prefix Delegation greyed out indicates ISP IPv6 availability issue, requiring WAN IPv6 enablement or alternative configuration for Matter protocol support.

**✅ STATUS**: **ISP IPV6 VERIFICATION REQUIRED** - Check WAN IPv6 status and contact provider if needed!

**Tags:** `#prefix_delegation_greyed_out` `#ipv6_unavailable` `#isp_ipv6_support` `#wan_ipv6_enablement` `#matter_blocked` `#tado_integration_issue`