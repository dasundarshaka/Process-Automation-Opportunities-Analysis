import pandas as pd
import smtplib
import os
import time
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader   

# LOAD ENVIRONMENT VARIABLES

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# LOAD EMAIL TEMPLATE (HTML)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("email_template.html")

# LOAD EXCEL FILE

FILE_NAME = "candidates.xlsx"

try:
    data = pd.read_excel(FILE_NAME)
except FileNotFoundError:
    print("Error: candidates.xlsx file not found.")
    exit()

# CREATE TRACKING COLUMNS IF NOT EXISTS

if "Contacted" not in data.columns:
    data["Contacted"] = "No"

if "Contact_Date" not in data.columns:
    data["Contact_Date"] = ""

data["Contact_Date"] = data["Contact_Date"].astype("object")

# FILTER ONLY SHORTLISTED + NOT CONTACTED

if "Status" not in data.columns:
    print("Error: 'Status' column missing in Excel.")
    exit()

filtered_data = data[
    (data["Status"] == "Shortlisted") &
    (data["Contacted"] == "No")
]

if filtered_data.empty:
    print("No new shortlisted candidates to contact.")
    exit()

# SETUP GMAIL SERVER

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
except Exception as e:
    print("Email login failed:", e)
    exit()

print("Starting Email Automation...\n")

# SEND EMAILS

for index in filtered_data.index:

    name = data.loc[index, "Name"]
    job_title = data.loc[index, "Position"]
    email = data.loc[index, "Email"]

    if pd.isna(email) or str(email).strip() == "":
        print(f"Skipping {name} — Invalid email.")
        continue

    msg = EmailMessage()
    msg["Subject"] = "Interview Invitation"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email

    # Render HTML template
    html_content = template.render(
        name=name,
        position=job_title
    )

    # Add both plain text + HTML
    msg.set_content("This email requires an HTML-supported email client.")
    msg.add_alternative(html_content, subtype="html")

    try:
        server.send_message(msg)
        print(f"Email sent to {name} ({email})")

        data.loc[index, "Contacted"] = "Yes"
        data.loc[index, "Contact_Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        time.sleep(2)

    except Exception as e:
        print(f"Failed to send email to {name}: {e}")

# CLOSE SERVER

server.quit()

# SAVE UPDATED EXCEL

try:
    data.to_excel(FILE_NAME, index=False)
    print("\nExcel file updated successfully.")
except Exception as e:
    print("Failed to save Excel file:", e)

print("\nContact Candidates Automation Completed!")
