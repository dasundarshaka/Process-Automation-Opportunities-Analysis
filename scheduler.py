import os
from dotenv import load_dotenv
import requests

# 1. Load the variables from the .env file
load_dotenv()

# 2. Retrieve credentials from environment variables
# These are the variables we set up in your .env file
API_KEY = os.getenv("CALENDLY_API_KEY")
SENDER_EMAIL = os.getenv("EMAIL_USER")

def create_interview_event(candidate_email, candidate_name):
    """
    This function handles the automation logic for scheduling.
    It is called by main.py to process each candidate.
    """
    
    # Simple validation to ensure we have an API key before trying to work
    if not API_KEY:
        print(f"Error: API Key is missing. Check your .env file.")
        return False

    # This represents the automation logic that replaces the manual 75-minute task
    # In a real-world scenario, this would send a POST request to a Scheduling API
    try:
        # For your project simulation, we print the automated action
        print(f"--- Automation Logic Triggered ---")
        print(f"Action: Sending personalized invite to {candidate_name}")
        print(f"Recipient: {candidate_email}")
        print(f"Using API Key: {API_KEY[:4]}**** (Securely masked)")
        
        # Return True to tell main.py that this task was successful
        return True
        
    except Exception as e:
        print(f"An error occurred during automation: {e}")
        return False