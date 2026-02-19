# Offer / Rejection Email Automation
### Process Automation Opportunities Analysis — Staffing & Recruitment Field
**Data Science Internship Group Project | February 2026**

---

## 1. Module Overview

This module automates the Offer and Rejection email communication step in the
Staffing and Recruitment workflow. Instead of HR staff manually drafting and
sending individual emails to each candidate, this automation reads candidate
data from an Excel file, generates personalized emails based on each
candidate's status, attaches a professional PDF offer letter for selected
candidates, and updates the tracking sheet automatically.

This module is one of six automated tasks in the group project:
- Screen CVs
- Contact Candidates
- Schedule Interviews
- Update Candidate Status
- **Send Offer / Rejection Email  ← This Module**
- Generate Recruitment Reports

---

## 2. Objectives

- Eliminate manual effort in sending offer and rejection emails to candidates
- Ensure each candidate receives a personalized, professional email
- Auto-generate and attach a PDF offer letter for selected candidates
- Automatically update the Excel tracking sheet after each email is sent
- Generate a summary report of all emails processed

---

## 3. Project Folder Structure

offer_rejection_automation/
│
├── candidates.xlsx               # Input: Candidate data
├── main.py                       # Main controller script
├── email_sender.py               # Email sending logic
├── pdf_generator.py              # PDF offer letter generator
├── report_generator.py           # Summary report generator
└── templates/
├── offer_template.html       # HTML email template for offer
└── rejection_template.html   # HTML email template for rejection

---

## 4. Prerequisites

### 4.1 Python Version
Python 3.8 or above is required. Check your version:

python --version

### 4.2 Required Libraries
Install all required libraries by running:

pip install pandas openpyxl yagmail jinja2 fpdf2

| Library   | Purpose                                      |
|-----------|----------------------------------------------|
| pandas    | Read and update candidate data from Excel    |
| openpyxl  | Read/write .xlsx Excel files                 |
| yagmail   | Simplified Gmail email sending               |
| jinja2    | HTML email template rendering                |
| fpdf2     | PDF offer letter generation                  |

---

## 5. Input File — candidates.xlsx

The automation reads from candidates.xlsx placed in the project root folder.
The file must contain the following columns:

| Column Name  | Description                              | Example Value        |
|--------------|------------------------------------------|----------------------|
| Candidate_ID | Unique ID for each candidate             | 001                  |
| Name         | Full name of the candidate               | Amal Perera          |
| Email        | Candidate's email address                | amal.perera@gmail.com|
| Position     | Job role applied for                     | Data Analyst         |
| Status       | Must be exactly 'Offer' or 'Rejected'   | Offer                |
| Email_Sent   | Tracks if email was sent. Start as 'No' | No                   |

> Important: The Status column must contain exactly "Offer" or "Rejected"
> (capital first letter). Any other value will be skipped by the script.

---

## 6. File Descriptions

### 6.1 main.py — Main Controller
This is the entry point of the automation. It performs the following steps:
- Loads candidates.xlsx using pandas
- Filters candidates where Email_Sent is 'No'
- Loops through each pending candidate
- Calls send_offer_email() or send_rejection_email() based on status
- Updates Email_Sent to 'Yes' in the Excel file after each successful send
- Calls generate_report() to display and save the final summary

Before running, update these two lines in main.py:

SENDER_EMAIL    = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_char_app_password"

### 6.2 email_sender.py — Email Sending Logic
Contains two functions:
- send_offer_email()    — Renders offer HTML template, generates PDF offer
                          letter, and sends email with PDF attached
- send_rejection_email() — Renders rejection HTML template and sends email
                           without an attachment

Both functions use yagmail to send emails and Jinja2 to fill in the candidate
name and position inside the email templates.

### 6.3 pdf_generator.py — PDF Offer Letter
Automatically creates a professional PDF offer letter for each candidate who
receives an offer. The letter includes the company header, candidate name,
job title, position details, and a formal closing. The PDF is named
offer_letter_[CandidateName].pdf and is attached to the offer email, then
deleted after sending to keep the folder clean.

### 6.4 report_generator.py — Summary Report
After all emails are processed, this module prints a summary to the terminal
and saves a report as an Excel file. The report includes:
- Total candidates processed
- Number of offer emails sent
- Number of rejection emails sent
- Number of successfully sent emails
- Number of failed emails with reasons

### 6.5 Email Templates (templates/ folder)
Both are HTML files that use Jinja2 placeholder syntax:
- {{ name }}     — Replaced with the candidate's full name
- {{ position }} — Replaced with the job position they applied for

---

## 7. Gmail App Password Setup

Gmail blocks direct password logins from scripts. You must generate an
App Password. Follow these steps:

1. Go to your Google Account at myaccount.google.com
2. Click on Security from the left panel
3. Enable 2-Step Verification if not already enabled
4. Search for "App Passwords" in the search bar
5. Select Mail as the app and your device, then click Generate
6. Copy the 16-character password and paste it into main.py as SENDER_PASSWORD

> Note: Never share your App Password or push it to GitHub. Keep it private.

---

## 8. How to Run the Automation

### Step 1 — Open Terminal
Navigate to your project folder:

cd offer_rejection_automation

### Step 2 — Verify Excel File
Make sure candidates.xlsx is in the folder and:
- Status column contains either "Offer" or "Rejected" for each candidate
- Email_Sent column is set to "No" for all pending candidates

### Step 3 — Run the Script

python main.py

### Step 4 — Expected Terminal Output

================================================
OFFER / REJECTION EMAIL AUTOMATION
Loaded 30 candidates from candidates.xlsx
Pending emails to send: 30
Processing: Amal Perera -- Offer
PDF generated: offer_letter_Amal_Perera.pdf
Offer email sent to Amal Perera (amal.perera@gmail.com)
Processing: Nimal Silva -- Rejected
Rejection email sent to Nimal Silva (nimal.silva@gmail.com)
...
Excel file updated -- candidates.xlsx
Report saved as: email_report_20260219_103000.xlsx

---

## 9. Automation Flow

| Step | Action                        | Output                              |
|------|-------------------------------|-------------------------------------|
| 1    | Read candidates.xlsx          | DataFrame with all candidate records|
| 2    | Filter Email_Sent = 'No'      | List of pending candidates only     |
| 3    | Check Status column           | 'Offer' or 'Rejected' per candidate |
| 4a   | If Offer → Generate PDF       | offer_letter_[Name].pdf created     |
| 4b   | Send offer email + PDF        | Email delivered with attachment     |
| 5a   | If Rejected → Send email      | Rejection email delivered           |
| 6    | Update Excel                  | Email_Sent changed to 'Yes'         |
| 7    | Generate Report               | Summary printed + saved as .xlsx    |

---

## 10. Time Saving Analysis

| Task                            | Manual Time      | Automated Time | Time Saved  |
|---------------------------------|------------------|----------------|-------------|
| Draft & send 1 offer email      | 10 minutes       | < 5 seconds    | ~10 minutes |
| Draft & send 1 rejection email  | 7 minutes        | < 5 seconds    | ~7 minutes  |
| Generate PDF offer letter       | 15 minutes       | < 3 seconds    | ~15 minutes |
| Update Excel tracking sheet     | 2 min per row    | Automatic      | ~2 minutes  |
| Process 30 candidates total     | ~7 to 8 hours    | < 2 minutes    | ~7+ hours   |

For a recruitment cycle with 30 candidates, this automation saves
approximately 7 to 8 hours of manual HR work.

---

## 11. Common Errors & Troubleshooting

| Error                          | Likely Cause                      | Solution                                      |
|--------------------------------|-----------------------------------|-----------------------------------------------|
| SMTPAuthenticationError        | Wrong email or password           | Use Gmail App Password, not normal password   |
| FileNotFoundError: candidates  | Excel file missing or wrong folder| Make sure candidates.xlsx is in same folder   |
| ModuleNotFoundError            | Library not installed             | Run: pip install pandas openpyxl yagmail ...  |
| TemplateNotFound               | templates/ folder missing         | Create templates/ folder with HTML files      |
| Status not recognized          | Typo in Status column             | Check values are exactly 'Offer' or 'Rejected'|

---

## 12. Deliverables for This Module

| File                     | Description                                    |
|--------------------------|------------------------------------------------|
| main.py                  | Main automation controller script              |
| email_sender.py          | Email sending logic for offer and rejection    |
| pdf_generator.py         | Automated PDF offer letter generator           |
| report_generator.py      | Post-run summary report generator              |
| offer_template.html      | HTML email template for offer emails           |
| rejection_template.html  | HTML email template for rejection emails       |
| candidates.xlsx          | Sample input file with 30 candidates           |
| README.md                | This documentation file                        |

---

## 13. Author Information

| Field       | Details                                                        |
|-------------|----------------------------------------------------------------|
| Module      | Send Offer / Rejection Email Automation                        |
| Project     | Process Automation Opportunities Analysis — Staffing & Recruitment |
| Field       | Data Science Internship Group Project                          |
| Duration    | 3 Weeks                                                        |
| Group Size  | 6 Members                                                      |
| Tools Used  | Python, pandas, yagmail, Jinja2, fpdf2, openpyxl               |

---

*This module is part of a 6-task recruitment automation pipeline developed
as a Data Science Internship project.*

