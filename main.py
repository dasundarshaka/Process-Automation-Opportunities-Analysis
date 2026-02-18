import os
from dotenv import load_dotenv
from scheduler import create_interview_event

# 1. Load environment variables from the .env file
load_dotenv()

def run_scheduling_automation():
    print("--- Starting Interview Scheduling Automation ---")
    
    # Security Check: Ensure API Key is loaded
    api_key = os.getenv("CALENDLY_API_KEY")
    if not api_key:
        print("CRITICAL ERROR: CALENDLY_API_KEY not found in .env file.")
        return

    # 2. Mock Data (This represents the candidates you need to process)
    # In a later step, we can pull this from an Excel sheet or ATS
    candidates = [
        {"name": "Hirushi", "email": "hirushi@example.com"},
        {"name": "Candidate B", "email": "b@example.com"}
    ]
    
    # 3. Process each candidate
    for candidate in candidates:
        print(f"\nProcessing: {candidate['name']}")
        
        # Trigger the logic from scheduler.py
        success = create_interview_event(candidate['email'], candidate['name'])
        
        if success:
            print(f"Status: Automation successful for {candidate['name']}.")
        else:
            print(f"Status: Failed to schedule for {candidate['name']}.")

    print("\n--- Automation Task Complete ---")

if __name__ == "__main__":
    run_scheduling_automation()