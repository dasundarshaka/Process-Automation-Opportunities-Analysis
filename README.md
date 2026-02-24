# Process Automation Opportunities Analysis
**Staffing & Recruitment Field**
**Data Science Internship Group Project | February 2026**

---

## Project Overview
This project identifies and implements automation opportunities within the staffing and recruitment lifecycle. Each team member owns one step of the pipeline and delivers a working automation script (and, where applicable, a web dashboard) to reduce manual effort, eliminate human errors, and speed up the overall recruitment process.

The six automation modules together form a complete end-to-end recruitment pipeline:

| # | Module | Description |
| :--- | :--- | :--- |
| 1 | **Screen CVs** | Automatically parse and rank incoming CVs against job requirements. |
| 2 | **Contact Candidates** | Send templated outreach emails to shortlisted candidates. |
| 3 | **Schedule Interviews** | Book interview slots and send calendar invites automatically. |
| 4 | **Update Candidate Status** | Process interview scores and set candidate status to Offer or Rejected. |
| 5 | **Send Offer / Rejection Email** | Dispatch outcome emails triggered by status changes. |
| 6 | **Generate Recruitment Reports** | Produce summary reports on pipeline metrics and time-to-hire. |

---

## Repository Structure
```
Process-Automation-Opportunities-Analysis/
│
└── candidate_status_automation/     # Module 4 — Update Candidate Status
    ├── candidates.xlsx              # Shared input/output data file
    ├── main.py                      # CLI automation script
    ├── app.py                       # Flask web dashboard server
    ├── generate_mock_data.py        # Test data generator
    ├── verify_data.py               # Data verification utility
    ├── README.md                    # Module documentation
    └── templates/
        └── index.html               # Web dashboard UI
```

---

## Tech Stack

| Tool / Library | Purpose |
| :--- | :--- |
| Python 3.8+ | Core scripting language |
| pandas | Data manipulation for Excel files |
| openpyxl | Excel file read/write engine |
| Flask | Web server for the dashboard |
| HTML / CSS / JS | Frontend dashboard interface |

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/dasundarshaka/Process-Automation-Opportunities-Analysis.git
cd Process-Automation-Opportunities-Analysis
```

### 2. Install Dependencies
```bash
pip install pandas openpyxl flask
```

### 3. Navigate to a Module
Each module has its own folder and `README.md` with detailed run instructions.

```bash
cd candidate_status_automation
```

Refer to the module-level `README.md` for step-by-step usage.

---

## Project Timeline
- **Month**: February 2026
- **Type**: Group Internship Project
- **Domain**: Staffing & Recruitment Process Automation
