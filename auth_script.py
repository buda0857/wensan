import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

# The scopes required by the GA4 MCP
SCOPES = [
    'https://www.googleapis.com/auth/analytics.readonly',
    'https://www.googleapis.com/auth/cloud-platform'
]

def authenticate():
    print("Starting authentication flow...")
    # This will open a browser window for the user to log in
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
    
    # Run the local server flow
    creds = flow.run_local_server(port=0)
    
    # Prepare the credentials in the format expected by Application Default Credentials (ADC)
    adc_data = {
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "refresh_token": creds.refresh_token,
        "type": "authorized_user"
    }
    
    # Save to the local workspace
    output_path = os.path.join(os.getcwd(), 'user_credentials.json')
    with open(output_path, 'w') as f:
        json.dump(adc_data, f, indent=2)
        
    print(f"\nSuccess! Your credentials have been saved to {output_path}")
    print("Please tell the AI that authentication is complete!")

if __name__ == '__main__':
    authenticate()
