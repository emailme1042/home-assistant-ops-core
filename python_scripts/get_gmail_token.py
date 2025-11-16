from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from urllib.parse import urlparse, parse_qs
import os, json

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CLIENT_SECRET_FILE = 'client_secret.json'
TOKEN_FILE = 'gmail_token.json'

REDIRECT_URIS = [
    'http://localhost:8080',
    'https://n1dwp10lkhgtxj0zfkunkpdvcu8kh6sb.ui.nabu.casa'
]

def get_credentials():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        print("🔄 Token refreshed.")
    elif not creds or not creds.valid:
        print("\n🌐 Choose redirect method:")
        print("1. Localhost (manual paste)")
        print("2. Nabu Casa (manual paste)")
        choice = input("Enter 1 or 2: ").strip()
        redirect_uri = REDIRECT_URIS[0] if choice == '1' else REDIRECT_URIS[1]

        flow = Flow.from_client_secrets_file(
            CLIENT_SECRET_FILE,
            scopes=SCOPES,
            redirect_uri=redirect_uri
        )

        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
        print("\n🔗 Go to this link in your browser:\n", auth_url)

        redirect_response = input("\n📥 Paste the FULL redirect URL here: ")
        code = parse_qs(urlparse(redirect_response).query)['code'][0]

        flow.fetch_token(code=code)
        creds = flow.credentials

        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
        print("✅ Token saved to", TOKEN_FILE)

    return creds

if __name__ == '__main__':
    creds = get_credentials()
    print("\n🔐 Access Token:", creds.token)
    print("🔁 Refresh Token:", creds.refresh_token)
