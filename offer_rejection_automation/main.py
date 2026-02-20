import pandas as pd
from email_sender import send_offer_email, send_rejection_email
from report_generator import generate_report

# ============================================================
# Update these before running
# ============================================================
SENDER_EMAIL = "your_email@gmail.com"       # Sender's Gmail address
SENDER_PASSWORD = "your_app_password_here"  # Gmail App Password 
EXCEL_FILE = "candidates.xlsx"
# ============================================================

def main():
    print("="*50)
    print("  OFFER / REJECTION EMAIL AUTOMATION")
    print("="*50)

    # Load candidate data from Excel
    df = pd.read_excel(EXCEL_FILE)
    print(f"\nLoaded {len(df)} candidates from {EXCEL_FILE}")

    # Filter only candidates where email hasn't been sent yet
    pending = df[df['Email_Sent'] == 'No']
    print(f"Pending emails to send: {len(pending)}\n")

    if len(pending) == 0:
        print("All emails have already been sent.")
        return

    results = []

    # Loop through each pending candidate
    for index, row in pending.iterrows():
        candidate = {
            'Name': row['Name'],
            'Email': row['Email'],
            'Position': row['Position'],
            'Status': row['Status']
        }

        print(f"Processing: {candidate['Name']} — {candidate['Status']}")

        try:
            if candidate['Status'] == 'Offer':
                send_offer_email(SENDER_EMAIL, SENDER_PASSWORD, candidate)

            elif candidate['Status'] == 'Rejected':
                send_rejection_email(SENDER_EMAIL, SENDER_PASSWORD, candidate)

            else:
                print(f"  Unknown status '{candidate['Status']}' — skipping.")
                continue

            # Update Excel — mark email as sent
            df.at[index, 'Email_Sent'] = 'Yes'

            results.append({
                'Name': candidate['Name'],
                'Position': candidate['Position'],
                'Status': candidate['Status'],
                'Email': candidate['Email'],
                'Email_Status': 'Sent'
            })

        except Exception as e:
            print(f"  ERROR sending to {candidate['Name']}: {e}")
            results.append({
                'Name': candidate['Name'],
                'Position': candidate['Position'],
                'Status': candidate['Status'],
                'Email': candidate['Email'],
                'Email_Status': 'Failed'
            })

    # Save updated Excel file
    df.to_excel(EXCEL_FILE, index=False)
    print(f"\nExcel file updated — {EXCEL_FILE}")

    # Generate and display report
    generate_report(results)
    print("\nAutomation Complete!")

if __name__ == "__main__":
    main()