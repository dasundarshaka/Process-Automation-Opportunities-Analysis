import pandas as pd
import os
from datetime import datetime

# Configuration
FILE_PATH = 'candidates.xlsx'
PASSING_SCORE = 75

def update_candidate_status():
    print(f"[{datetime.now()}] Starting Candidate Status Update Automation...")
    
    if not os.path.exists(FILE_PATH):
        print(f"Error: '{FILE_PATH}' not found.")
        return

    try:
        # Load the Excel file
        df = pd.read_excel(FILE_PATH, dtype={'Candidate_ID': str})
        print(f"Loaded {len(df)} records from {FILE_PATH}")

        # Filter candidates in 'Interview' status
        # We also check if they have a score to process
        mask_interview = df['Status'] == 'Interview'
        candidates_to_process = df[mask_interview].copy()
        
        if candidates_to_process.empty:
            print("No candidates found in 'Interview' status.")
            return

        print(f"Found {len(candidates_to_process)} candidates in 'Interview' status.")
        
        updated_count = 0
        
        for index, row in candidates_to_process.iterrows():
            # Interactive Input
            while True:
                try:
                    score_input = input(f"Enter Interview Score for {row['Name']} (ID: {row['Candidate_ID']}): ")
                    score = float(score_input)
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Logic to update status
            new_status = ""
            if score >= PASSING_SCORE:
                new_status = "Offer"
            else:
                new_status = "Rejected"
            
            # Update the main DataFrame
            # Note: We update the original df using the index
            df.at[index, 'Status'] = new_status
            df.at[index, 'Email_Sent'] = "No"  # Reset for the next agent
            
            # Optional: Save the score if the column exists, or create it
            if 'Interview_Score' in df.columns:
                 df.at[index, 'Interview_Score'] = score
            
            print(f"Updated {row['Name']}: Status -> {new_status}")
            updated_count += 1

        if updated_count > 0:
            # Save the changes
            df.to_excel(FILE_PATH, index=False)
            print(f"Successfully updated {updated_count} records in '{FILE_PATH}'.")
        else:
            print("No updates made.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_candidate_status()
