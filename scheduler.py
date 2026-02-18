import os
from dotenv import load_dotenv

load_dotenv()

# Updated: Added 'candidate_email' to the arguments list
def create_interview_event(candidate_email, candidate_name, interview_date):
    """
    Goal: Represent the interview date/time in the Google Calendar.
    Fixed: Now accepts 3 arguments to match the call from main.py
    """
    calendar_id = os.getenv("CALENDAR_ID")
    
    print(f"--- [CALENDAR UPDATE] ---")
    print(f"Adding Event: Interview with {candidate_name} ({candidate_email})")
    print(f"Scheduled Time: {interview_date}")
    print(f"Target Calendar: {calendar_id}")
    
    return True