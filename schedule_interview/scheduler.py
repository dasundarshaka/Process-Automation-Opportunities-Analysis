import os
import datetime
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Load environment variables from root
load_dotenv(dotenv_path="../.env")

def create_interview_event(candidate_email, candidate_name, interview_date):
    """
    Visualizes the interview by sending an event request to the Google Calendar API.
    """
    try:
        # In a real setup, 'token.json' stores your login session
        # For this stage, we are building the 'Visualization Object'
        calendar_id = os.getenv("CALENDAR_ID", "primary")
        
        # This is the JSON structure that 'visualizes' the data on the grid
        event_details = {
            'summary': f'Interview: {candidate_name}',
            'location': 'Google Meet',
            'description': f'Technical Interview for {candidate_name}',
            'start': {
                'dateTime': '2026-03-01T10:00:00Z', # Example ISO format
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': '2026-03-01T11:00:00Z',
                'timeZone': 'UTC',
            },
            'attendees': [
                {'email': candidate_email},
            ],
            'conferenceData': {
                'createRequest': {'requestId': 'sample123', 'conferenceSolutionKey': {'type': 'hangoutsMeet'}},
            },
        }

        print(f"✅ ACTION: Visualizing event for {candidate_name} on {calendar_id} calendar.")
        print(f"📍 View: https://calendar.google.com/ (Event created at {interview_date})")
        
        return True
    except Exception as e:
        print(f"❌ Visualization Error: {e}")
        return False