# Import the function from the new folder structure
from schedule_interview.scheduler import create_interview_event

def run_automation():
    # This represents the data that would normally come from 
    # the "Selected Candidates" list or an Excel sheet.
    candidates = [
        {
            "name": "Hirushi", 
            "email": "hirushi@example.com", 
            "date": "2026-03-01 at 10:00 AM"
        }
    ]

    print("--- Starting Recruitment Workflow Automation ---")

    for person in candidates:
        print(f"Processing candidate: {person['name']}...")
        
        # 1. Trigger the "Schedule Interview" module (Your Part)
        # This will now attempt to 'visualize' the event on the Google Calendar
        success = create_interview_event(
            candidate_email=person['email'], 
            candidate_name=person['name'], 
            interview_date=person['date']
        )
        
        # 2. Handover to the next part of the process
        if success:
            print(f"✔ Calendar visualization complete for {person['name']}.")
            # This is where Ravindu's 'Update Status' function would be called next
        else:
            print(f"✘ Failed to schedule interview for {person['name']}.")

if __name__ == "__main__":
    run_automation()