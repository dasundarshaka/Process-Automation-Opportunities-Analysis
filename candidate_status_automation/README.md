# Update Candidate Status Automation
**Process Automation Opportunities Analysis — Staffing & Recruitment Field**
**Data Science Internship Group Project | February 2026**

## 1. Module Overview
This module automates the decision-making process for candidate progression after the interview stage. Instead of recruiters manually reviewing scores and updating the tracking sheet, this automation reads the interview status, captures the interview score (interactively or via a web dashboard), determines the outcome (Offer vs. Rejection), and prepares the data for the next stage (Email Automation).

This module is one of six automated tasks in the group project:
1. Screen CVs
2. Contact Candidates
3. Schedule Interviews
4. **Update Candidate Status** ← This Module
5. Send Offer / Rejection Email
6. Generate Recruitment Reports

---

## 2. Objectives
- Eliminate manual data entry errors when updating candidate statuses.
- Standardize the decision threshold (Score ≥ 75 for Offer).
- Ensure the `Email_Sent` flag is correctly reset to trigger the downstream email automation.
- Provide a seamless bridge between the "Schedule Interviews" and "Send Offer/Rejection" modules.
- Offer both a **CLI script** (`main.py`) and a **web dashboard** (`app.py`) as interface options.

---

## 3. Project Folder Structure
```
candidate_status_automation/
│
├── candidates.xlsx            # Shared Input/Output file
├── main.py                    # CLI automation controller
├── app.py                     # Flask web API + dashboard server
├── generate_mock_data.py      # Utility to generate test data
├── verify_data.py             # Utility to verify updates
└── templates/
    └── index.html             # Web dashboard UI
```

---

## 4. Prerequisites

### 4.1 Python Version
Python 3.8 or above is required. Check your version:
```bash
python --version
```

### 4.2 Required Libraries
Install the required libraries:
```bash
pip install pandas openpyxl flask
```

| Library | Purpose |
| :--- | :--- |
| `pandas` | To read, filter, and modify the Excel dataset efficiently. |
| `openpyxl` | Engine used by pandas to interact with `.xlsx` files. |
| `flask` | Lightweight web framework that powers the dashboard server. |

---

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
| `Interview_Score` | Score used for decision logic | `85` |

**Important**: This module specifically processes candidates with `Status = 'Interview'`.

---

## 6. File Descriptions

### 6.1 main.py — CLI Automation Controller
The core command-line script. It performs the following steps:
1. **Loads** `candidates.xlsx`.
2. **Filters** for candidates currently in the `Interview` status.
3. **Iterates** through each candidate and prompts the user to enter an **Interview Score** (0–100).
4. **Applies Logic**:
   - Score ≥ 75 → Updates Status to **`Offer`**.
   - Score < 75 → Updates Status to **`Rejected`**.
5. **Resets** `Email_Sent` to `No` to trigger the next module.
6. **Saves** the updates back to `candidates.xlsx`.

### 6.2 app.py — Flask Web Dashboard Server
A Flask application that serves a modern web dashboard. It exposes two REST API endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Serves the `index.html` dashboard UI |
| `/api/candidates` | `GET` | Returns all candidate records as JSON |
| `/api/update` | `POST` | Accepts `{ candidate_id, score }` and updates status in Excel |

### 6.3 templates/index.html — Web Dashboard UI
A single-page dashboard with a dark, modern design built with vanilla HTML, CSS, and JavaScript. Features include:
- **Live statistics**: Total, Interview, Offer, and Rejected counts.
- **Candidate cards**: Display name, position, email, current status, and interview score.
- **Filter tabs**: View candidates by status (Interview / Offer / Rejected / All).
- **Score input**: Enter a score per candidate and submit to update status in real time.
- **Toast notifications**: Non-intrusive feedback on successful updates or errors.

### 6.4 generate_mock_data.py
A helper script to create a fresh `candidates.xlsx` file with dummy data for testing purposes.

### 6.5 verify_data.py
A helper script that prints the contents of the Excel file to the terminal to verify that updates were applied correctly.

---

## 7. How to Run the Automation

### Option A — CLI Script (main.py)

#### Step 1 — Open Terminal
Navigate to the project folder:
```bash
cd candidate_status_automation
```

#### Step 2 — Verify Input Data
Ensure `candidates.xlsx` exists. If not, generate it:
```bash
python generate_mock_data.py
```

#### Step 3 — Run the Script
```bash
python main.py
```

#### Step 4 — Interactive Execution
The script will prompt you for scores:
```
[2026-02-20 10:52:17] Starting Candidate Status Update Automation...
Found 3 candidates in 'Interview' status.
Enter Interview Score for Amal Perera (ID: 001): 88
Updated Amal Perera: Status -> Offer
...
Successfully updated 3 records in 'candidates.xlsx'.
```

---

### Option B — Web Dashboard (app.py)

#### Step 1 — Start the Flask Server
```bash
python app.py
```

#### Step 2 — Open Dashboard in Browser
Navigate to:
```
http://127.0.0.1:5000
```

#### Step 3 — Update Candidates via UI
- The dashboard loads all candidates automatically.
- Use the filter tabs to view candidates at the **Interview** stage.
- Enter a score in the input field on each candidate card and click **Update**.
- The status badge, score, and stats update instantly without a page refresh.

---

## 8. Automation Flow

| Step | Action | Output |
| :--- | :--- | :--- |
| 1 | Read `candidates.xlsx` | DataFrame with all records |
| 2 | Filter `Status = 'Interview'` | List of candidates pending review |
| 3 | Input Interview Score | User enters score (e.g., 88) |
| 4 | Apply Threshold Logic | Determine `Offer` or `Rejected` |
| 5 | Update Status & Reset Flag | `Status='Offer'`, `Email_Sent='No'` |
| 6 | Save to Excel | Updated `candidates.xlsx` |

---

## 9. Time Saving Analysis

| Task | Manual Time | Automated Time | Time Saved |
| :--- | :--- | :--- | :--- |
| Review Interview Score | 5 mins | < 10 seconds | ~4.5 mins |
| Update Excel Status | 2 mins | Instant | ~2 mins |
| Reset Email Trigger | 1 min | Instant | ~1 min |
| **Total per Candidate** | **~8 mins** | **~10 seconds** | **~7+ mins** |

---

## 10. Common Errors & Troubleshooting

| Error | Likely Cause | Solution |
| :--- | :--- | :--- |
| `FileNotFoundError` | `candidates.xlsx` missing | Run `generate_mock_data.py` first. |
| `ValueError` | Non-numeric input for score | Enter a number between 0–100. |
| `PermissionError` | Excel file is open | Close `candidates.xlsx` in Excel before running. |
| `ModuleNotFoundError: flask` | Flask not installed | Run `pip install flask`. |
| Port 5000 already in use | Another process on port 5000 | Kill the process or change the port in `app.py`. |

---

## 11. Deliverables
- `main.py`: Interactive CLI automation script.
- `app.py`: Flask web server with REST API.
- `templates/index.html`: Web dashboard UI.
- `candidates.xlsx`: Shared data file.
- `generate_mock_data.py`: Test data generator.
- `verify_data.py`: Data verification utility.
- `README.md`: Documentation.

---

## 12. Author Information

| Field | Details |
| :--- | :--- |
| **Module** | **Update Candidate Status Automation** |
| **Project** | Process Automation Opportunities Analysis |
| **Tools Used** | Python, pandas, openpyxl, Flask, HTML/CSS/JS |
