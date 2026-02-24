# Contact Candidates Email Automation  
### Process Automation Opportunities Analysis — Staffing & Recruitment Field  
**Data Science Internship Group Project | February 2026**

---

## 1. Module Overview

This module automates the **Contact Candidates** step in the recruitment workflow.

Instead of HR staff manually drafting and sending interview invitation emails to shortlisted candidates, this automation system:

- Reads candidate data from an Excel file  
- Filters only shortlisted candidates  
- Sends personalized interview invitation emails  
- Updates tracking columns automatically  
- Saves the updated Excel file  

This module is part of the recruitment automation pipeline:

1. Screen CVs 
2. **Contact Candidates ← This Module** 
3. Schedule Interviews 
4. Update Candidate Status 
5. Send Offer / Rejection 
6. Generate Recruitment Reports  

---

## 2. Objectives

- Eliminate manual effort in contacting shortlisted candidates  
- Automatically send interview invitation emails  
- Prevent duplicate email sending  
- Maintain automated tracking (Contacted & Contact_Date)  
- Improve recruitment process efficiency  

---

## 3. Project Folder Structure

```
contact_candidates_automation/
│
├── contact_candidates.py      # Main automation script
├── email_template.html        # HTML interview email template
├── candidates.xlsx            # Input candidate file
├── requirements.txt           # Required Python libraries
├── .env                       # Email credentials (NOT pushed to GitHub)
├── .gitignore
└── README.md
```

---

## 4. Prerequisites

### 4.1 Python Version
Python 3.8 or above  

Check version:
```
python --version
```

### 4.2 Required Libraries

Install required libraries:
```
pip install pandas openpyxl python-dotenv jinja2
```

| Library | Purpose |
|----------|----------|
| pandas | Read and update Excel file |
| openpyxl | Excel file support (.xlsx) |
| python-dotenv | Load secure email credentials |
| jinja2 | Render HTML email template |

---

## 5. Input File — candidates.xlsx

The system reads data from `candidates.xlsx`.

### Required Columns

| Column Name | Description | Example Value |
|-------------|-------------|---------------|
| Name | Candidate full name | Nimal Perera |
| Email | Candidate email address | nimal@gmail.com |
| Position | Job role applied for | Software Engineer |
| Status | Must contain "Shortlisted" | Shortlisted |
| Contacted | Tracks if email sent ("No" initially) | No |
| Contact_Date | Stores date & time of contact | Initially blank |

Only candidates where:

Status = Shortlisted  
Contacted = No  

will receive emails.

---

## 6. Email Template

The file `email_template.html` contains the HTML structure for the interview email.

It uses Jinja2 placeholders:

```
{{ name }}  
{{ position }}  
```

These are dynamically replaced with candidate details when generating emails.

---

## 7. Environment Variables (.env Setup)

Create a `.env` file in the project root:

```
EMAIL_ADDRESS=your_email@gmail.com  
EMAIL_PASSWORD=your_16_character_app_password  
```

⚠ Use a Gmail App Password (not your real Gmail password).

The `.gitignore` file excludes:

```
.env  
__pycache__/  
*.pyc  
```

So credentials are never uploaded to GitHub.

---

## 8. How to Run the Automation

### Step 1 — Navigate to Project Folder
```
cd contact_candidates_automation
```

### Step 2 — Verify Excel File

Make sure:
- candidates.xlsx is in the project root  
- Status column contains "Shortlisted"  
- Contacted column contains "No" for pending candidates  

### Step 3 — Run the Script
```
python contact_candidates.py
```

---

### Step 4 — Expected Terminal Output Example

```
Starting Email Automation...  
Email sent to Nimal Perera (nimal@gmail.com)  
Email sent to Saman Jayasinghe (saman@gmail.com)  
Email sent to Dilshan Kumara (dilshan@gmail.com)  
Excel file updated successfully.  
Contact Candidates Automation Completed!  
```

If there are no new shortlisted candidates:
```
No new shortlisted candidates to contact.  
```

If login fails:
```
Email login failed: SMTPAuthenticationError  
```

---

## 9. Automation Flow

| Step | Action | Output |
|------|--------|--------|
| 1 | Read candidates.xlsx | DataFrame loaded |
| 2 | Filter shortlisted candidates | Pending list created |
| 3 | Render HTML template | Personalized email generated |
| 4 | Send email via SMTP | Email delivered |
| 5 | Update Contacted column | Marked as "Yes" |
| 6 | Update Contact_Date | Timestamp added |
| 7 | Save Excel file | Tracking updated |

---

## 10. Time Saving Analysis

| Task | Manual Time | Automated Time | Time Saved |
|------|------------|---------------|------------|
| Contact 1 candidate | 5–10 minutes | ~3 seconds | ~5–10 minutes |
| Contact 10 candidates | ~1 hour | < 30 seconds | ~55 minutes |
| Update tracking sheet | 1–2 min per row | Automatic | Full time saved |

For 10 shortlisted candidates:

Manual Process: ~60 minutes  
Automated Process: < 30 seconds  

This significantly reduces HR workload.

---

## 11. Deliverables

| File | Description |
|------|------------|
| contact_candidates.py | Main automation script |
| email_template.html | Interview email template |
| candidates.xlsx | Sample candidate data |
| requirements.txt | Required libraries |
| README.md | Documentation |
| .gitignore | Protects sensitive files |

---

## 12. Author Information

| Field | Details |
|-------|----------|
| Module | Contact Candidates Email Automation |
| Project | Process Automation Opportunities Analysis — Staffing & Recruitment |
| Type | Data Science Internship Group Project |
| Tools Used | Python, pandas, Jinja2, SMTP, openpyxl |
