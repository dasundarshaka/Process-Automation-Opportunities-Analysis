import os.path
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permissions required to manage your calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_interview_event(candidate_email, candidate_name, interview_date_str):
    # --- PATH LOGIC ---
    # This finds the 'credentials.json' file even if it's one folder up
    current_dir = Path(__file__).resolve().parent.parent
    creds_file = os.path.join(current_dir, 'credentials.json')
    token_file = os.path.join(current_dir, 'token.json')

    creds = None

    # Step A: Check if we are already logged in (look for token.json)
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # Step B: If not logged in, perform the 'Handshake' with Google
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Check if the credentials.json file actually exists where we expect it
            if not os.path.exists(creds_file):
                print(f"CRITICAL ERROR: 'credentials.json' not found at: {creds_file}")
                return False
            
            # This generates the link and opens the browser
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the login 'token' so the browser doesn't pop up next time
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    # Step C: Create the Calendar Event
    try:
        service = build('calendar', 'v3', credentials=creds)
        
        event_data = {
            'summary': f'Interview: {candidate_name}',
            'description': f'Technical Interview for {candidate_email}',
            'start': {'dateTime': '2026-03-01T10:00:00Z', 'timeZone': 'UTC'},
            'end': {'dateTime': '2026-03-01T11:00:00Z', 'timeZone': 'UTC'},
        }

        # Send to Google
        service.events().insert(calendarId='primary', body=event_data).execute()
        print(f"SUCCESS: Event created for {candidate_name}!")
        return True
    except Exception as e:
        print(f"GOOGLE API ERROR: {e}")
        return False