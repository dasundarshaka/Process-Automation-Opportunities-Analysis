import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Access level for the calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_interview_event(candidate_email, candidate_name, interview_date_str):
    # Files are located in the same root folder
    creds_file = 'credentials.json'
    token_file = 'token.json'
    creds = None

    # Check for existing login session
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # If no login, start the browser handshake
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_file):
                print(f"❌ ERROR: {creds_file} not found in this folder!")
                return False
            
            flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        
        event = {
            'summary': f'Interview: {candidate_name}',
            'description': f'Technical Interview for {candidate_email}',
            'start': {'dateTime': '2026-03-01T10:00:00Z', 'timeZone': 'UTC'},
            'end': {'dateTime': '2026-03-01T11:00:00Z', 'timeZone': 'UTC'},
        }

        # Send data to Google
        result = service.events().insert(calendarId='primary', body=event).execute()
        print(f"✅ SUCCESS: Event created! Link: {result.get('htmlLink')}")
        return True
    except Exception as e:
        print(f"❌ API ERROR: {e}")
        return False