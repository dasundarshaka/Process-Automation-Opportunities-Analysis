# Simple import because scheduler.py is in the same folder
from scheduler import create_interview_event

def run_automation():
    print("--- Starting Recruitment Workflow Automation ---")
    
    # Sample data for testing
    candidate_email = "test_candidate@example.com"
    candidate_name = "Hirushi"
    interview_date = "2026-03-01 at 10:00 AM"

    print(f"Step 1: Attempting to schedule interview for {candidate_name}...")
    
    # Trigger the calendar magic
    success = create_interview_event(candidate_email, candidate_name, interview_date)
    
    if success:
        print("--- Automation Task Completed Successfully ---")
        print("Magic complete! Check your Google Calendar.")
    else:
        print("--- Automation Task Failed ---")

if __name__ == "__main__":
    run_automation()