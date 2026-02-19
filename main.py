import os
# This connects the main file to your sub-folder logic
from schedule_interview.scheduler import create_interview_event

def run_automation():
    print("--- Starting Recruitment Workflow Automation ---")
    
    # This data simulates what you would get from a candidate list
    candidate_email = "test_candidate@example.com"
    candidate_name = "Hirushi"
    interview_date = "2026-03-01 at 10:00 AM"

    print(f"Step 1: Attempting to schedule interview for {candidate_name}...")
    
    # This calls the logic in your scheduler.py file
    success = create_interview_event(candidate_email, candidate_name, interview_date)
    
    if success:
        print("--- Automation Task Completed Successfully ---")
        print("Check your Google Calendar to see the visualization!")
    else:
        print("--- Automation Task Failed ---")
        print("Check the error messages above to troubleshoot.")

if __name__ == "__main__":
    run_automation()