# Update Candidate Status Automation
**Process Automation Opportunities Analysis — Staffing & Recruitment Field**
**Data Science Internship Group Project | February 2026**

## 1. Module Overview
This module automates the decision-making process for candidate progression after the interview stage. Instead of recruiters manually reviewing scores and updating the tracking sheet, this automation reads the interview status, captures the interview score (interactively or from the system), determines the outcome (Offer vs. Rejection), and prepares the data for the next stage (Email Automation).

This module is one of six automated tasks in the group project:
1. Screen CVs
2. Contact Candidates
3. Schedule Interviews
4. **Update Candidate Status** ← This Module
5. Send Offer / Rejection Email
6. Generate Recruitment Reports

## 2. Objectives
-   Eliminate manual data entry errors when updating candidate statuses.
-   Standardize the decision threshold (e.g., Score >= 75 for Offer).
-   Ensure the `Email_Sent` flag is correctly reset to trigger the downstream email automation.
-   Provide a seamless bridge between the "Schedule Interviews" and "Send Offer/Rejection" modules.

## 3. Project Folder Structure
```
candidate_status_automation/
│
├── candidates.xlsx            # Shared Input/Output file
├── main.py                    # Main automation controller
├── generate_mock_data.py      # Utility to generate test data
└── verify_data.py             # Utility to verify updates
```

## 4. Prerequisites
### 4.1 Python Version
Python 3.8 or above is required. Check your version:
```bash
python --version
```

### 4.2 Required Libraries
Install the required libraries:
```bash
pip install pandas openpyxl
```

| Library | Purpose |
| :--- | :--- |
| `pandas` | To read, filter, and modify the Excel dataset efficiently. |
| `openpyxl` | Engine used by pandas to interact with `.xlsx` files. |

## 5. Input File — candidates.xlsx
The automation reads from `candidates.xlsx`. The file must contain the following columns:

| Column Name | Description | Example Value |
| :--- | :--- | :--- |
| `Candidate_ID` | Unique ID for each candidate | `001` |
| `Name` | Full name of the candidate | `Amal Perera` |
| `Email` | Candidate's email address | `amal@example.com` |
| `Position` | Job role applied for | `Data Analyst` |
| `Status` | Current state of the candidate | `Interview` |
| `Email_Sent` | Tracks if email was sent | `No` |
| `Interview_Score` | (Optional) Score used for logic | `85` |

**Important**: This module specifically looks for candidates with `Status = 'Interview'`.

## 6. File Descriptions

### 6.1 main.py — Main Controller
This is the core script. It performs the following steps:
1.  **Loads** `candidates.xlsx`.
2.  **Filters** for candidates currently in the 'Interview' status.
3.  **Iterates** through each candidate and prompts the user to enter an **Interview Score** (0-100).
4.  **Applies Logic**:
    -   Score >= 75 $\rightarrow$ Updates Status to **'Offer'**.
    -   Score < 75 $\rightarrow$ Updates Status to **'Rejected'**.
5.  **Resets** `Email_Sent` to 'No' to ensure the next module sends the notification.
6.  **Saves** the updates back to `candidates.xlsx`.

### 6.2 generate_mock_data.py
A helper script to create a fresh `candidates.xlsx` file with dummy data for testing purposes.

### 6.3 verify_data.py
A helper script that prints the contents of the Excel file to the terminal to verify that updates were applied correctly.

## 8. How to Run the Automation

### Step 1 — Open Terminal
Navigate to the project folder:
```bash
cd candidate_status_automation
```

### Step 2 — Verify Input Data
Ensure `candidates.xlsx` exists. If not, generate it:
```bash
python generate_mock_data.py
```

### Step 3 — Run the Script
```bash
python main.py
```

### Step 4 — Interactive Execution
The script will prompt you for scores:
```
[2026-02-20 10:52:17] Starting Candidate Status Update Automation...
Found 3 candidates in 'Interview' status.
Enter Interview Score for Amal Perera (ID: 001): 88
Updated Amal Perera: Status -> Offer
...
Successfully updated 3 records in 'candidates.xlsx'.
```

## 9. Automation Flow
| Step | Action | Output |
| :--- | :--- | :--- |
| 1 | Read `candidates.xlsx` | DataFrame with all records |
| 2 | Filter `Status = 'Interview'` | List of candidates pending review |
| 3 | Input Interview Score | User enters score (e.g., 88) |
| 4 | Apply Threshold Logic | Determine 'Offer' or 'Rejected' |
| 5 | Update Status & Reset Flag | `Status='Offer'`, `Email_Sent='No'` |
| 6 | Save to Excel | Updated `candidates.xlsx` |

## 10. Time Saving Analysis
| Task | Manual Time | Automated Time | Time Saved |
| :--- | :--- | :--- | :--- |
| Review Interview Score | 5 mins | < 10 seconds | ~4.5 mins |
| Update Excel Status | 2 mins | Instant | ~2 mins |
| Reset Email Trigger | 1 min | Instant | ~1 min |
| **Total per Candidate** | **~8 mins** | **~10 seconds** | **~7+ mins** |

## 11. Common Errors & Troubleshooting
| Error | Likely Cause | Solution |
| :--- | :--- | :--- |
| `FileNotFoundError` | `candidates.xlsx` missing | Run `generate_mock_data.py` first. |
| `ValueError` | Non-numeric input for score | Enter a number between 0-100. |
| `PermissionError` | Excel file is open | Close `candidates.xlsx` in Excel before running. |

## 12. Deliverables
-   `main.py`: Interactive automation script.
-   `candidates.xlsx`: Shared data file.
-   `README.md`: Documentation.
-   `generate_mock_data.py`: Test data generator.

## 13. Author Information
| Field | Details |
| :--- | :--- |
| **Module** | **Update Candidate Status Automation** |
| **Project** | Process Automation Opportunities Analysis |
| **Tools Used** | Python, pandas, openpyxl |
