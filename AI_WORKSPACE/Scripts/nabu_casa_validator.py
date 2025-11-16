# Nabu Casa Access Validation Script
# Purpose: Test and validate Nabu Casa connectivity, generate proper HA tokens
# Usage: Run to diagnose GPT access issues and token problems

import requests
import json
from datetime import datetime

def test_nabu_casa_access():
    """Test Nabu Casa URL accessibility"""
    nabu_url = "https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa"

    print("🧪 Testing Nabu Casa Access")
    print("="*50)

    try:
        # Test basic connectivity
        print(f"🔗 Testing URL: {nabu_url}")
        response = requests.get(nabu_url, timeout=10, allow_redirects=False)

        print(f"✅ Status Code: {response.status_code}")
        print(f"✅ Response Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("✅ Nabu Casa URL is accessible")
        elif response.status_code in [301, 302, 307, 308]:
            print(f"🔄 Redirect to: {response.headers.get('Location', 'Unknown')}")
        else:
            print(f"⚠️ Unexpected status: {response.status_code}")

    except requests.exceptions.ConnectTimeout:
        print("❌ Connection timeout - check internet connectivity")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - DNS or network issue")
    except Exception as e:
        print(f"❌ Error: {e}")

def validate_ha_token_format(token):
    """Validate if token looks like a proper HA Long-Lived Access Token"""
    print("\n🔑 Token Validation")
    print("="*50)

    if not token:
        print("❌ No token provided")
        return False

    if token.startswith("sk-proj-") or token.startswith("sk-"):
        print("❌ PROBLEM DETECTED: This is an OpenAI API key, not a Home Assistant token!")
        print("   OpenAI keys start with 'sk-' or 'sk-proj-'")
        print("   HA tokens are usually longer alphanumeric strings")
        return False

    if len(token) < 100:
        print("⚠️ Token seems short for HA Long-Lived Access Token")
        print("   HA tokens are typically 150+ characters")
        return False

    print("✅ Token format looks like a valid HA Long-Lived Access Token")
    return True

def test_ha_api_access(nabu_url, token):
    """Test HA API access with token"""
    print("\n🏠 Testing Home Assistant API")
    print("="*50)

    if not validate_ha_token_format(token):
        print("❌ Skipping API test - invalid token format")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        # Test API root
        api_url = f"{nabu_url}/api/"
        print(f"🔗 Testing API: {api_url}")

        response = requests.get(api_url, headers=headers, timeout=10)
        print(f"📊 API Status: {response.status_code}")

        if response.status_code == 200:
            print("✅ API accessible with token")
            data = response.json()
            print(f"📋 API Response: {data}")
        elif response.status_code == 401:
            print("❌ Authentication failed - check token validity")
        elif response.status_code == 404:
            print("❌ API not found - check URL or remote access settings")
        else:
            print(f"⚠️ Unexpected API response: {response.status_code}")

    except Exception as e:
        print(f"❌ API Error: {e}")

def generate_token_instructions():
    """Generate instructions for creating proper HA token"""
    print("\n📝 How to Generate HA Long-Lived Access Token")
    print("="*50)
    print("""
1. 🏠 Open Home Assistant in browser:
   https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa

2. 👤 Go to your profile (click your name in bottom left)

3. 🔑 Scroll down to "Long-Lived Access Tokens" section

4. ➕ Click "Create Token"

5. 📝 Enter token name: "VSCode HA Extension"

6. 💾 Copy the generated token (starts with long alphanumeric string)

7. ⚙️ Update VSCode settings.json:
   "vscode-home-assistant.longLivedAccessToken": "YOUR_NEW_TOKEN_HERE"

⚠️  IMPORTANT: Remove the OpenAI key that's currently there!
""")

if __name__ == "__main__":
    print(f"🤖 Nabu Casa Access Validator - {datetime.now()}")
    print("="*60)

    # Test basic connectivity
    test_nabu_casa_access()

    # Simulate checking the problematic token from VSCode settings
    problematic_token = "PLACEHOLDER_OPENAI_KEY_FOR_DEMONSTRATION"

    validate_ha_token_format(problematic_token)

    # Show instructions
    generate_token_instructions()

    print("\n🎯 Summary")
    print("="*50)
    print("❌ PROBLEM: OpenAI API key used instead of HA token")
    print("✅ SOLUTION: Generate proper HA Long-Lived Access Token")
    print("🔧 ACTION: Update VSCode settings with correct token")
    print("📊 MONITOR: Use AI Hub → GPT Access Monitor after fix")