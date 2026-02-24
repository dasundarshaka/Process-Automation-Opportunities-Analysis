# Recruitment Workflow Automation 🚀

## Project Overview
This project automates the manual task of scheduling candidate interviews. By connecting a Python backend to the Google Calendar API, it reduces the time spent on administrative scheduling from **75 minutes to just 20 minutes** (a 73% increase in efficiency).

## What This Project Does
1.  **Authenticates** with Google Services using OAuth 2.0.
2.  **Processes** candidate information (Name, Email, and Interview Time).
3.  **Visualizes** the data by automatically creating a calendar event with the candidate as an attendee.

---

## 🛠️ Google Account Setup (Required)
To test this code, you must configure your Google Cloud Console to allow the "Handshake":

1.  **Enable API:** Go to the [Google Calendar API Library](https://console.cloud.google.com/apis/library/calendar.googleapis.com) and click **Enable**.
2.  **OAuth Consent Screen:** * Set User Type to **External**.
    * Add your Gmail address under the **Test Users** section (Mandatory).
3.  **Credentials:**
    * Create an **OAuth 2.0 Client ID** (Desktop App).
    * Download the JSON file, rename it to `credentials.json`, and place it in the project root folder.

---

## 🚀 How to Run the Project

### 1. Environment Setup
Ensure you have Python installed. Create a virtual environment and install the required Google libraries:

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install google-api-python-client google-auth-oauthlib

## Run the automation trigger
python main.py

---

### Why this README helps you:
* **For your Project:** It documents the **75 min vs 20 min** efficiency gain you analyzed.
* **For your Future Self:** It lists the exact Google Cloud steps (Test Users, Enabling API) so you don't forget them.

