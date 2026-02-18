from scheduler import create_interview_event

def run_automation():
    # Example candidate data including specific Date/Time
    candidates = [
        {
            "name": "Hirushi", 
            "email": "hirushi@example.com", 
            "date": "2026-03-01 at 10:00 AM"
        }
    ]

    print("Starting Operational Workflow Automation...")

    for person in candidates:
        # Calling the function to update the calendar
        success = create_interview_event(person['email'], person['name'], person['date'])
        
        if success:
            print(f"Successfully automated scheduling for {person['name']}.")

if __name__ == "__main__":
    run_automation()