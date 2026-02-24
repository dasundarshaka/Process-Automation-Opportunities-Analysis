Complete Project README

This document consolidates all automation module README files into a
single workflow-based documentation. Each section follows the execution
order of automation parts in the overall project workflow.



Candidate Recommendation System 🎯

AI-Powered Talent Matching Using TF-IDF Vectorization & Cosine
Similarity

A complete full-stack web application that automatically matches
candidates to job roles based on skills, experience, education, and CV
content similarity.

------------------------------------------------------------------------

🌟 Features

Core Functionality

-   Vector-Based Matching: Converts CVs and job descriptions into TF-IDF
    vectors for semantic comparison
-   Cosine Similarity Scoring: Ranks candidates from best to least match
    (0-100% match score)
-   Multiple Input Methods:
    -   📝 Manual text entry for quick testing
    -   📁 CSV file uploads for batch processing
    -   📊 JSON batch processing for API integration
-   Real-Time Processing: Instant recommendations using pre-trained
    models
-   Export Results: Download recommendations as CSV

Technical Features

-   Pre-trained TF-IDF vectorizer for consistent text representation
-   NLTK-based text preprocessing (stopword removal, lemmatization)
-   RESTful API for easy integration
-   Modern, responsive web interface
-   Comprehensive error handling and validation

------------------------------------------------------------------------

📁 Project Structure

    Candidate-Recommendation-System/
    │
    ├── app.py                          # Flask backend server
    ├── requirements.txt                 # Python dependencies
    ├── README.md                        # This file
    │
    ├── data/                           # Original datasets
    │   ├── cvs_100.csv                 # Sample candidate CVs
    │   └── jobs_10.csv                 # Sample job descriptions
    │
    ├── models/                         # Trained models (pickle files)
    │   ├── vectorizer.pkl              # TF-IDF vectorizer
    │   ├── cv_vectors.pkl              # Pre-computed CV vectors
    │   └── job_vectors.pkl             # Pre-computed job vectors
    │
    ├── src/                            # Source code modules
    │   ├── preprocessing.py            # Text cleaning & preprocessing
    │   ├── vectorization.py            # TF-IDF vectorization
    │   ├── similarity.py               # Similarity computation
    │   └── recommendation_pipeline.py  # Main pipeline for real-time recommendations
    │
    ├── results/                        # Output files
    │   ├── cvs_cleaned.csv            # Preprocessed CVs
    │   ├── jobs_cleaned.csv           # Preprocessed jobs
    │   └── top_candidates.csv         # Recommendation results
    │
    ├── templates/                      # Frontend HTML
    │   └── index.html                 # Main web interface
    │
    ├── static/                         # Frontend assets
    │   ├── script.js                  # JavaScript functionality
    │   └── style.css                  # CSS styling
    │
    └── uploads/                        # Temporary file uploads

------------------------------------------------------------------------

🚀 Installation & Setup

Prerequisites

-   Python 3.7+
-   pip (Python package manager)

Step 1: Install Dependencies

    pip install flask pandas scikit-learn nltk scipy

Step 2: Download NLTK Data

    python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet'); nltk.download('omw-1.4')"

Step 3: Train Models (First-Time Setup)

If you don’t have pre-trained models in the models/ folder:

    # 1. Run preprocessing
    cd src
    python preprocessing.py

    # 2. Train vectorizer and create vectors
    python vectorization.py

    # 3. (Optional) Test recommendations with sample data
    python similarity.py

This will create: - models/vectorizer.pkl - TF-IDF vectorizer -
models/cv_vectors.pkl - CV vectors - models/job_vectors.pkl - Job
vectors

Step 4: Start the Server

    python app.py

The server will start at: http://localhost:5000

------------------------------------------------------------------------

🎯 How to Use

Method 1: Manual Input (Quick Testing)

1.  Navigate to Manual Input tab
2.  Fill in the job description:
    -   Required Skills
    -   Experience Required
    -   Education Required
    -   Full Job Description
3.  Add candidates using the “Add Candidate” button
4.  Fill in candidate details (skills, experience, education, CV text)
5.  Set the number of top candidates to recommend
6.  Click “Get Recommendations”

Method 2: File Upload (Batch Processing)

1.  Navigate to File Upload tab
2.  Prepare two CSV files:

Candidates CSV (columns): - candidate_id (required) - skills -
experience - education - cv_text

Jobs CSV (columns): - job_id (required) - required_skills -
experience_required - education_required - job_description

3.  Upload both files
4.  Set top N candidates per job
5.  Click “Upload & Process”

Method 3: Batch JSON (API Integration)

1.  Navigate to Batch Process tab
2.  Enter jobs in JSON array format:

    [
      {
        "job_id": "J001",
        "required_skills": "Python, Machine Learning",
        "experience_required": "3+ years",
        "education_required": "BS Computer Science",
        "job_description": "Looking for a Data Scientist..."
      }
    ]

3.  Enter candidates in JSON array format:

    [
      {
        "candidate_id": "C001",
        "skills": "Python, TensorFlow, Keras",
        "experience": "4 years as ML Engineer",
        "education": "MS Computer Science",
        "cv_text": "Experienced in building ML models..."
      }
    ]

4.  Click “Process Batch”

------------------------------------------------------------------------

🔧 API Endpoints

Health Check

    GET /api/health

Returns system status

Single Job Recommendation

    POST /api/recommend
    Content-Type: application/json

    {
      "job": {
        "required_skills": "...",
        "experience_required": "...",
        "education_required": "...",
        "job_description": "..."
      },
      "candidates": [
        {
          "candidate_id": "C001",
          "skills": "...",
          "experience": "...",
          "education": "...",
          "cv_text": "..."
        }
      ],
      "top_n": 5
    }

File Upload Recommendation

    POST /api/recommend/file
    Content-Type: multipart/form-data

    Form Data:
    - cvs_file: CSV file
    - jobs_file: CSV file
    - top_n: integer (optional)

Batch Recommendation

    POST /api/batch/recommend
    Content-Type: application/json

    {
      "jobs": [...],
      "candidates": [...],
      "top_n": 5
    }

Process Single CV

    POST /api/process/cv
    Content-Type: application/json

    {
      "skills": "...",
      "experience": "...",
      "education": "...",
      "cv_text": "..."
    }

Process Single Job

    POST /api/process/job
    Content-Type: application/json

    {
      "required_skills": "...",
      "experience_required": "...",
      "education_required": "...",
      "job_description": "..."
    }

------------------------------------------------------------------------

🧠 How It Works

1. Text Preprocessing

    # Steps performed on all text:
    1. Convert to lowercase
    2. Remove punctuation and numbers
    3. Tokenize into words
    4. Remove stopwords (common words like "the", "is", "and")
    5. Lemmatize (convert words to base form: "running" → "run")

2. Vectorization (TF-IDF)

    TF-IDF (Term Frequency-Inverse Document Frequency):
    - Converts text to numerical vectors
    - Weighs words by importance (rare words get higher scores)
    - Max 5000 features for efficiency
    - Same vectorizer used for both CVs and jobs (consistency)

3. Similarity Computation

    Cosine Similarity:
    - Measures angle between two vectors
    - Range: 0 (no match) to 1 (perfect match)
    - Formula: cos(θ) = (A · B) / (||A|| × ||B||)

4. Ranking & Recommendation

    1. Compute similarity scores for all CV-Job pairs
    2. Sort candidates by similarity score (descending)
    3. Select top N candidates
    4. Return with rank, score, and match percentage

------------------------------------------------------------------------

📊 Sample Output

    {
      "success": true,
      "total_candidates": 10,
      "recommendations": [
        {
          "candidate_id": "C003",
          "similarity_score": 0.8756,
          "rank": 1,
          "match_percentage": 87.56
        },
        {
          "candidate_id": "C007",
          "similarity_score": 0.7823,
          "rank": 2,
          "match_percentage": 78.23
        },
        ...
      ]
    }

------------------------------------------------------------------------

📈 Results & Evaluation

Metrics

-   Cosine Similarity Score: 0-1 (higher = better match)
-   Match Percentage: 0-100% (normalized score)
-   Rank: 1, 2, 3… (1 = best match)

Visual Features

-   🥇 Gold badge for #1 rank
-   🥈 Silver badge for #2 rank
-   🥉 Bronze badge for #3 rank
-   Color-coded progress bars:
    -   🟢 Green (70%+): Excellent match
    -   🟡 Yellow (50-70%): Good match
    -   🔴 Red (<50%): Weak match

------------------------------------------------------------------------

🎨 Frontend Features

-   Modern UI: Gradient backgrounds, smooth animations
-   Tabbed Navigation: Switch between input methods easily
-   Real-Time Feedback: Loading spinners, error messages
-   Responsive Design: Works on desktop, tablet, mobile
-   Export Functionality: Download results as CSV
-   Statistics Dashboard: Total jobs, candidates, matches

------------------------------------------------------------------------

🔒 Security & Best Practices

-   File size limit: 16MB
-   Input validation on all endpoints
-   Error handling with descriptive messages
-   CORS-ready for API integration
-   No sensitive data stored (stateless)

------------------------------------------------------------------------

🚧 Known Limitations

1.  Model Version Warning: If you see scikit-learn version warnings,
    consider retraining the vectorizer with your current scikit-learn
    version
2.  Memory Usage: Processing large CSV files (1000+ rows) may require
    additional memory
3.  Development Server: Current setup uses Flask’s development server.
    For production, use Gunicorn or uWSGI

------------------------------------------------------------------------

🔄 Retraining the Model

If you update dependencies or want to retrain:

    cd src

    # Step 1: Preprocess new data
    python preprocessing.py

    # Step 2: Retrain vectorizer
    python vectorization.py

    # Step 3: Test
    python similarity.py

    # Step 4: Restart server
    cd ..
    python app.py

------------------------------------------------------------------------

🛠️ Troubleshooting

Issue: “Vectorizer not found”

Solution: Run training scripts in src/ folder first

Issue: NLTK data errors

Solution:

    python -c "import nltk; nltk.download('all')"

Issue: Version warnings

Solution: Retrain models or ignore (usually harmless)

Issue: Port 5000 already in use

Solution: Change port in app.py:

    app.run(debug=True, port=5001)

------------------------------------------------------------------------

📝 Project Requirements Met

✅ Vector Representations: TF-IDF vectorization for CVs and jobs
✅ Preprocessing: Cleaning, tokenization, stopword removal,
lemmatization
✅ Similarity Computation: Cosine similarity implementation
✅ Top N Recommendations: Ranked candidate list for each job
✅ Evaluation: Similarity scores, match percentages, visual ranking
✅ Full-Stack Application: Backend API + Frontend UI
✅ Documentation: Complete README with usage instructions
✅ Code Organization: Modular structure with separate folders

------------------------------------------------------------------------

👥 Contributors

Group Project - AI/ML Course

------------------------------------------------------------------------

📄 License

This project is for educational purposes.

------------------------------------------------------------------------

🎓 Academic Context

This system was developed as part of a group project to build a
Candidate Recommendation Engine. The implementation covers:

-   Machine Learning: TF-IDF vectorization, cosine similarity
-   Natural Language Processing: Text preprocessing, lemmatization
-   Software Engineering: Modular design, API development
-   Full-Stack Development: Flask backend, responsive frontend
-   Data Science: CSV processing, batch analysis, evaluation metrics

------------------------------------------------------------------------

🚀 Future Enhancements

-   ☐ Add BERT/Transformer-based embeddings
-   ☐ Implement user authentication
-   ☐ Add database support (PostgreSQL/MongoDB)
-   ☐ Create admin dashboard
-   ☐ Add email notifications
-   ☐ Implement caching for faster responses
-   ☐ Add more similarity metrics (Euclidean, Jaccard)
-   ☐ Create Docker container for easy deployment
-   ☐ Add unit tests and integration tests

------------------------------------------------------------------------

📞 Support

For issues or questions, please check: 1. This README 2. Code comments
in source files 3. Error messages in the browser console or terminal

------------------------------------------------------------------------

🎉 Happy Recruiting! 🎉



Contact Candidates Email Automation

Process Automation Opportunities Analysis — Staffing & Recruitment Field

Data Science Internship Group Project | February 2026

------------------------------------------------------------------------

1. Module Overview

This module automates the Contact Candidates step in the recruitment
workflow.

Instead of HR staff manually drafting and sending interview invitation
emails to shortlisted candidates, this automation system:

-   Reads candidate data from an Excel file
-   Filters only shortlisted candidates
-   Sends personalized interview invitation emails
-   Updates tracking columns automatically
-   Saves the updated Excel file

This module is part of the recruitment automation pipeline:

1.  Screen CVs
2.  Contact Candidates ← This Module
3.  Schedule Interviews
4.  Update Candidate Status
5.  Send Offer / Rejection
6.  Generate Recruitment Reports

------------------------------------------------------------------------

2. Objectives

-   Eliminate manual effort in contacting shortlisted candidates
-   Automatically send interview invitation emails
-   Prevent duplicate email sending
-   Maintain automated tracking (Contacted & Contact_Date)
-   Improve recruitment process efficiency

------------------------------------------------------------------------

3. Project Folder Structure

    contact_candidates_automation/
    │
    ├── contact_candidates.py      # Main automation script
    ├── email_template.html        # HTML interview email template
    ├── candidates.xlsx            # Input candidate file
    ├── requirements.txt           # Required Python libraries
    ├── .env                       # Email credentials (NOT pushed to GitHub)
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

4. Prerequisites

4.1 Python Version

Python 3.8 or above

Check version:

    python --version

4.2 Required Libraries

Install required libraries:

    pip install pandas openpyxl python-dotenv jinja2

  Library         Purpose
  --------------- -------------------------------
  pandas          Read and update Excel file
  openpyxl        Excel file support (.xlsx)
  python-dotenv   Load secure email credentials
  jinja2          Render HTML email template

------------------------------------------------------------------------

5. Input File — candidates.xlsx

The system reads data from candidates.xlsx.

Required Columns

  Column Name    Description                             Example Value
  -------------- --------------------------------------- -------------------
  Name           Candidate full name                     Nimal Perera
  Email          Candidate email address                 nimal@gmail.com
  Position       Job role applied for                    Software Engineer
  Status         Must contain “Shortlisted”              Shortlisted
  Contacted      Tracks if email sent (“No” initially)   No
  Contact_Date   Stores date & time of contact           Initially blank

Only candidates where:

Status = Shortlisted
Contacted = No

will receive emails.

------------------------------------------------------------------------

6. Email Template

The file email_template.html contains the HTML structure for the
interview email.

It uses Jinja2 placeholders:

    {{ name }}  
    {{ position }}  

These are dynamically replaced with candidate details when generating
emails.

------------------------------------------------------------------------

7. Environment Variables (.env Setup)

Create a .env file in the project root:

    EMAIL_ADDRESS=your_email@gmail.com  
    EMAIL_PASSWORD=your_16_character_app_password  

⚠ Use a Gmail App Password (not your real Gmail password).

The .gitignore file excludes:

    .env  
    __pycache__/  
    *.pyc  

So credentials are never uploaded to GitHub.

------------------------------------------------------------------------

8. How to Run the Automation

Step 1 — Navigate to Project Folder

    cd contact_candidates_automation

Step 2 — Verify Excel File

Make sure: - candidates.xlsx is in the project root
- Status column contains “Shortlisted”
- Contacted column contains “No” for pending candidates

Step 3 — Run the Script

    python contact_candidates.py

------------------------------------------------------------------------

Step 4 — Expected Terminal Output Example

    Starting Email Automation...  
    Email sent to Nimal Perera (nimal@gmail.com)  
    Email sent to Saman Jayasinghe (saman@gmail.com)  
    Email sent to Dilshan Kumara (dilshan@gmail.com)  
    Excel file updated successfully.  
    Contact Candidates Automation Completed!  

If there are no new shortlisted candidates:

    No new shortlisted candidates to contact.  

If login fails:

    Email login failed: SMTPAuthenticationError  

------------------------------------------------------------------------

9. Automation Flow

  Step   Action                          Output
  ------ ------------------------------- ------------------------------
  1      Read candidates.xlsx            DataFrame loaded
  2      Filter shortlisted candidates   Pending list created
  3      Render HTML template            Personalized email generated
  4      Send email via SMTP             Email delivered
  5      Update Contacted column         Marked as “Yes”
  6      Update Contact_Date             Timestamp added
  7      Save Excel file                 Tracking updated

------------------------------------------------------------------------

10. Time Saving Analysis

  --------------------------------------------------------------------------
  Task         Manual Time        Automated Time          Time Saved
  ------------ ------------------ ----------------------- ------------------
  Contact 1    5–10 minutes       ~3 seconds              ~5–10 minutes
  candidate                                               

  Contact 10   ~1 hour            < 30 seconds            ~55 minutes
  candidates                                              

  Update       1–2 min per row    Automatic               Full time saved
  tracking                                                
  sheet                                                   
  --------------------------------------------------------------------------

For 10 shortlisted candidates:

Manual Process: ~60 minutes
Automated Process: < 30 seconds

This significantly reduces HR workload.

------------------------------------------------------------------------

11. Deliverables

  File                    Description
  ----------------------- --------------------------
  contact_candidates.py   Main automation script
  email_template.html     Interview email template
  candidates.xlsx         Sample candidate data
  requirements.txt        Required libraries
  README.md               Documentation
  .gitignore              Protects sensitive files

------------------------------------------------------------------------

12. Author Information

  -----------------------------------------------------------------------
  Field                         Details
  ----------------------------- -----------------------------------------
  Module                        Contact Candidates Email Automation

  Project                       Process Automation Opportunities Analysis
                                — Staffing & Recruitment

  Type                          Data Science Internship Group Project

  Tools Used                    Python, pandas, Jinja2, SMTP, openpyxl
  -----------------------------------------------------------------------



Recruitment Workflow Automation 🚀

Project Overview

This project automates the manual task of scheduling candidate
interviews. By connecting a Python backend to the Google Calendar API,
it reduces the time spent on administrative scheduling from 75 minutes
to just 20 minutes (a 73% increase in efficiency).

What This Project Does

1.  Authenticates with Google Services using OAuth 2.0.
2.  Processes candidate information (Name, Email, and Interview Time).
3.  Visualizes the data by automatically creating a calendar event with
    the candidate as an attendee.

------------------------------------------------------------------------

🛠️ Google Account Setup (Required)

To test this code, you must configure your Google Cloud Console to allow
the “Handshake”:

1.  Enable API: Go to the Google Calendar API Library and click Enable.
2.  OAuth Consent Screen: * Set User Type to External.
    -   Add your Gmail address under the Test Users section (Mandatory).
3.  Credentials:
    -   Create an OAuth 2.0 Client ID (Desktop App).
    -   Download the JSON file, rename it to credentials.json, and place
        it in the project root folder.

------------------------------------------------------------------------

🚀 How to Run the Project

1. Environment Setup

Ensure you have Python installed. Create a virtual environment and
install the required Google libraries:

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

candidate_status_automation/ │ ├── candidates.xlsx # Shared Input/Output
file ├── main.py # CLI automation controller ├── app.py # Flask web
API + dashboard server ├── generate_mock_data.py # Utility to generate
test data ├── verify_data.py # Utility to verify updates └── templates/
└── index.html # Web dashboard UI


    ---

    ## 4. Prerequisites

    ### 4.1 Python Version
    Python 3.8 or above is required. Check your version:
    ```bash
    python --version

4.2 Required Libraries

Install the required libraries:

    pip install pandas openpyxl flask

  -----------------------------------------------------------------------
  Library                             Purpose
  ----------------------------------- -----------------------------------
  pandas                              To read, filter, and modify the
                                      Excel dataset efficiently.

  openpyxl                            Engine used by pandas to interact
                                      with .xlsx files.

  flask                               Lightweight web framework that
                                      powers the dashboard server.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

5. Input File — candidates.xlsx

The automation reads from candidates.xlsx. The file must contain the
following columns:

  Column Name       Description                      Example Value
  ----------------- -------------------------------- ------------------
  Candidate_ID      Unique ID for each candidate     001
  Name              Full name of the candidate       Amal Perera
  Email             Candidate’s email address        amal@example.com
  Position          Job role applied for             Data Analyst
  Status            Current state of the candidate   Interview
  Email_Sent        Tracks if email was sent         No
  Interview_Score   Score used for decision logic    85

Important: This module specifically processes candidates with
Status = 'Interview'.

------------------------------------------------------------------------

6. File Descriptions

6.1 main.py — CLI Automation Controller

The core command-line script. It performs the following steps: 1. Loads
candidates.xlsx. 2. Filters for candidates currently in the Interview
status. 3. Iterates through each candidate and prompts the user to enter
an Interview Score (0–100). 4. Applies Logic: - Score ≥ 75 → Updates
Status to Offer. - Score < 75 → Updates Status to Rejected. 5. Resets
Email_Sent to No to trigger the next module. 6. Saves the updates back
to candidates.xlsx.

6.2 app.py — Flask Web Dashboard Server

A Flask application that serves a modern web dashboard. It exposes two
REST API endpoints:

  -------------------------------------------------------------------------
  Endpoint                Method                  Description
  ----------------------- ----------------------- -------------------------
  /                       GET                     Serves the index.html
                                                  dashboard UI

  /api/candidates         GET                     Returns all candidate
                                                  records as JSON

  /api/update             POST                    Accepts
                                                  { candidate_id, score }
                                                  and updates status in
                                                  Excel
  -------------------------------------------------------------------------

6.3 templates/index.html — Web Dashboard UI

A single-page dashboard with a dark, modern design built with vanilla
HTML, CSS, and JavaScript. Features include: - Live statistics: Total,
Interview, Offer, and Rejected counts. - Candidate cards: Display name,
position, email, current status, and interview score. - Filter tabs:
View candidates by status (Interview / Offer / Rejected / All). - Score
input: Enter a score per candidate and submit to update status in real
time. - Toast notifications: Non-intrusive feedback on successful
updates or errors.

6.4 generate_mock_data.py

A helper script to create a fresh candidates.xlsx file with dummy data
for testing purposes.

6.5 verify_data.py

A helper script that prints the contents of the Excel file to the
terminal to verify that updates were applied correctly.

------------------------------------------------------------------------

7. How to Run the Automation

Option A — CLI Script (main.py)

Step 1 — Open Terminal

Navigate to the project folder:

    cd candidate_status_automation

Step 2 — Verify Input Data

Ensure candidates.xlsx exists. If not, generate it:

    python generate_mock_data.py

Step 3 — Run the Script

    python main.py

Step 4 — Interactive Execution

The script will prompt you for scores:

    [2026-02-20 10:52:17] Starting Candidate Status Update Automation...
    Found 3 candidates in 'Interview' status.
    Enter Interview Score for Amal Perera (ID: 001): 88
    Updated Amal Perera: Status -> Offer
    ...
    Successfully updated 3 records in 'candidates.xlsx'.

------------------------------------------------------------------------

Option B — Web Dashboard (app.py)

Step 1 — Start the Flask Server

    python app.py

Step 2 — Open Dashboard in Browser

Navigate to:

    http://127.0.0.1:5000

Step 3 — Update Candidates via UI

-   The dashboard loads all candidates automatically.
-   Use the filter tabs to view candidates at the Interview stage.
-   Enter a score in the input field on each candidate card and click
    Update.
-   The status badge, score, and stats update instantly without a page
    refresh.

------------------------------------------------------------------------

8. Automation Flow

  -----------------------------------------------------------------------
  Step                    Action                  Output
  ----------------------- ----------------------- -----------------------
  1                       Read candidates.xlsx    DataFrame with all
                                                  records

  2                       Filter                  List of candidates
                          Status = 'Interview'    pending review

  3                       Input Interview Score   User enters score
                                                  (e.g., 88)

  4                       Apply Threshold Logic   Determine Offer or
                                                  Rejected

  5                       Update Status & Reset   Status='Offer',
                          Flag                    Email_Sent='No'

  6                       Save to Excel           Updated candidates.xlsx
  -----------------------------------------------------------------------

------------------------------------------------------------------------

9. Time Saving Analysis

  -----------------------------------------------------------------------
  Task              Manual Time       Automated Time    Time Saved
  ----------------- ----------------- ----------------- -----------------
  Review Interview  5 mins            < 10 seconds      ~4.5 mins
  Score                                                 

  Update Excel      2 mins            Instant           ~2 mins
  Status                                                

  Reset Email       1 min             Instant           ~1 min
  Trigger                                               

  Total per         ~8 mins           ~10 seconds       ~7+ mins
  Candidate                                             
  -----------------------------------------------------------------------

------------------------------------------------------------------------

10. Common Errors & Troubleshooting

  ----------------------------------------------------------------------------
  Error                        Likely Cause            Solution
  ---------------------------- ----------------------- -----------------------
  FileNotFoundError            candidates.xlsx missing Run
                                                       generate_mock_data.py
                                                       first.

  ValueError                   Non-numeric input for   Enter a number between
                               score                   0–100.

  PermissionError              Excel file is open      Close candidates.xlsx
                                                       in Excel before
                                                       running.

  ModuleNotFoundError: flask   Flask not installed     Run pip install flask.

  Port 5000 already in use     Another process on port Kill the process or
                               5000                    change the port in
                                                       app.py.
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

11. Deliverables

-   main.py: Interactive CLI automation script.
-   app.py: Flask web server with REST API.
-   templates/index.html: Web dashboard UI.
-   candidates.xlsx: Shared data file.
-   generate_mock_data.py: Test data generator.
-   verify_data.py: Data verification utility.
-   README.md: Documentation.

------------------------------------------------------------------------

12. Author Information

  Field        Details
  ------------ ----------------------------------------------
  Module       Update Candidate Status Automation
  Project      Process Automation Opportunities Analysis
  Tools Used   Python, pandas, openpyxl, Flask, HTML/CSS/JS



Offer / Rejection Email Automation

Process Automation Opportunities Analysis — Staffing & Recruitment Field

Data Science Internship Group Project | February 2026

------------------------------------------------------------------------

1. Module Overview

This module automates the Offer and Rejection email communication step
in the Staffing and Recruitment workflow. Instead of HR staff manually
drafting and sending individual emails to each candidate, this
automation reads candidate data from an Excel file, generates
personalized emails based on each candidate’s status, attaches a
professional PDF offer letter for selected candidates, and updates the
tracking sheet automatically.

This module is one of six automated tasks in the group project: - Screen
CVs - Contact Candidates - Schedule Interviews - Update Candidate
Status - Send Offer / Rejection Email ← This Module - Generate
Recruitment Reports

------------------------------------------------------------------------

2. Objectives

-   Eliminate manual effort in sending offer and rejection emails to
    candidates
-   Ensure each candidate receives a personalized, professional email
-   Auto-generate and attach a PDF offer letter for selected candidates
-   Automatically update the Excel tracking sheet after each email is
    sent
-   Generate a summary report of all emails processed

------------------------------------------------------------------------

3. Project Folder Structure

    offer_rejection_automation/
    │
    ├── candidates.xlsx              # Input file - Candidate data
    ├── main.py                      # Main controller
    ├── email_sender.py              # Email sending logic
    ├── pdf_generator.py             # PDF offer letter generator
    ├── report_generator.py          # Summary report generator
    │
    └── templates/
        ├── offer_template.html      # HTML email template for offer
        └── rejection_template.html  # HTML email template for rejection

4. Prerequisites

4.1 Python Version

Python 3.8 or above is required. Check your version:

Check:

    python --version

4.2 Required Libraries

Install all required libraries by running:

    pip install pandas openpyxl yagmail jinja2 fpdf2

  Library    Purpose
  ---------- -------------------------------------------
  pandas     Read and update candidate data from Excel
  openpyxl   Read/write .xlsx Excel files
  yagmail    Simplified Gmail email sending
  jinja2     HTML email template rendering
  fpdf2      PDF offer letter generation

------------------------------------------------------------------------

5. Input File — candidates.xlsx

The automation reads from candidates.xlsx placed in the project root
folder. The file must contain the following columns:

  --------------------------------------------------------------------------------
  Column Name    Description                            Example Value
  -------------- -------------------------------------- --------------------------
  Candidate_ID   Unique ID for each candidate           001

  Name           Full name of the candidate             Amal Perera

  Email          Candidate’s email address              amal111.perera@gmail.com

  Position       Job role applied for                   Data Analyst

  Status         Must be exactly ‘Offer’ or ‘Rejected’  Offer

  Email_Sent     Tracks if email was sent. Start as     No
                 ‘No’                                   
  --------------------------------------------------------------------------------

  Important: The Status column must contain exactly “Offer” or
  “Rejected” (capital first letter). Any other value will be skipped by
  the script.

------------------------------------------------------------------------

6. File Descriptions

6.1 main.py — Main Controller

This is the entry point of the automation. It performs the following
steps: - Loads candidates.xlsx using pandas - Filters candidates where
Email_Sent is ‘No’ - Loops through each pending candidate - Calls
send_offer_email() or send_rejection_email() based on status - Updates
Email_Sent to ‘Yes’ in the Excel file after each successful send - Calls
generate_report() to display and save the final summary

Before running, update these two lines in main.py:

    SENDER_EMAIL    = "your_email@gmail.com"
    SENDER_PASSWORD = "your_16_char_app_password"

6.2 email_sender.py — Email Sending Logic

Contains two functions: - send_offer_email() — Renders offer HTML
template, generates PDF offer letter, and sends email with PDF
attached - send_rejection_email() — Renders rejection HTML template and
sends email without an attachment

Both functions use yagmail to send emails and Jinja2 to fill in the
candidate name and position inside the email templates.

6.3 pdf_generator.py — PDF Offer Letter

Automatically creates a professional PDF offer letter for each candidate
who receives an offer. The letter includes the company header, candidate
name, job title, position details, and a formal closing. The PDF is
named offer_letter_[CandidateName].pdf and is attached to the offer
email, then deleted after sending to keep the folder clean.

6.4 report_generator.py — Summary Report

After all emails are processed, this module prints a summary to the
terminal. The report includes: - Total candidates processed - Number of
offer emails sent - Number of rejection emails sent - Number of
successfully sent emails - Number of failed emails with reasons

6.5 Email Templates (templates/ folder)

Both are HTML files that use Jinja2 placeholder syntax: - {{ name }} —
Replaced with the candidate’s full name - {{ position }} — Replaced with
the job position they applied for

------------------------------------------------------------------------

7. Gmail App Password Setup

Gmail blocks direct password logins from scripts. You must generate an
App Password. Follow these steps:

1.  Go to your Google Account at myaccount.google.com
2.  Click on Security from the left panel
3.  Enable 2-Step Verification if not already enabled
4.  Search for “App Passwords” in the search bar
5.  Select Mail as the app and your device, then click Generate
6.  Copy the 16-character password and paste it into main.py as
    SENDER_PASSWORD

  Note: Never share your App Password.

------------------------------------------------------------------------

8. How to Run the Automation

Step 1 — Open Terminal

Navigate to your project folder:

    cd offer_rejection_automation

Step 2 — Verify Excel File

Make sure candidates.xlsx is in the folder and: - Status column contains
either “Offer” or “Rejected” for each candidate - Email_Sent column is
set to “No” for all pending candidates

Step 3 — Run the Script

    python main.py

Step 4 — Expected Terminal Output

    ================================================
    OFFER / REJECTION EMAIL AUTOMATION
    Loaded 30 candidates from candidates.xlsx
    Pending emails to send: 30
    Processing: Amal Perera -- Offer
    PDF generated: offer_letter_Amal_Perera.pdf
    Offer email sent to Amal Perera (amal111.perera@gmail.com)
    Processing: Nimal Silva -- Rejected
    Rejection email sent to Nimal Silva (ni2222mal.silva@gmail.com)
    ...
    Excel file updated -- candidates.xlsx
    Report saved as: email_report_20260219_103000.xlsx

    ---

9. Automation Flow

  ------------------------------------------------------------------------
  Step   Action                        Output
  ------ ----------------------------- -----------------------------------
  1      Read candidates.xlsx          DataFrame with all candidate
                                       records

  2      Filter Email_Sent = ‘No’      List of pending candidates only

  3      Check Status column           ‘Offer’ or ‘Rejected’ per candidate

  4a     If Offer → Generate PDF       offer_letter_[Name].pdf created

  4b     Send offer email + PDF        Email delivered with attachment

  5a     If Rejected → Send email      Rejection email delivered

  6      Update Excel                  Email_Sent changed to ‘Yes’

  7      Generate Report               Summary printed + saved as .xlsx
  ------------------------------------------------------------------------

------------------------------------------------------------------------

10. Time Saving Analysis

  ------------------------------------------------------------------------
  Task                          Manual Time     Automated Time Time Saved
  ----------------------------- --------------- -------------- -----------
  Draft & send 1 offer email    10 minutes      < 5 seconds    ~10 minutes

  Draft & send 1 rejection      7 minutes       < 5 seconds    ~7 minutes
  email                                                        

  Generate PDF offer letter     15 minutes      < 3 seconds    ~15 minutes

  Update Excel tracking sheet   2 min per row   Automatic      ~2 minutes

  Process 30 candidates total   ~7 to 8 hours   < 2 minutes    ~7+ hours
  ------------------------------------------------------------------------

For a recruitment cycle with 30 candidates, this automation saves
approximately 7 to 8 hours of manual HR work.

------------------------------------------------------------------------

11. Common Errors & Troubleshooting

  -----------------------------------------------------------------------------
  Error                     Likely Cause          Solution
  ------------------------- --------------------- -----------------------------
  SMTPAuthenticationError   Wrong email or        Use Gmail App Password, not
                            password              normal password

  FileNotFoundError:        Excel file missing or Make sure candidates.xlsx is
  candidates                wrong folder          in same folder

  ModuleNotFoundError       Library not installed Run: pip install pandas
                                                  openpyxl yagmail …

  TemplateNotFound          templates/ folder     Create templates/ folder with
                            missing               HTML files

  Status not recognized     Typo in Status column Check values are exactly
                                                  ‘Offer’ or ‘Rejected’
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

12. Deliverables for This Module

  ------------------------------------------------------------------------
  File                      Description
  ------------------------- ----------------------------------------------
  main.py                   Main automation controller script

  email_sender.py           Email sending logic for offer and rejection

  pdf_generator.py          Automated PDF offer letter generator

  report_generator.py       Post-run summary report generator

  offer_template.html       HTML email template for offer emails

  rejection_template.html   HTML email template for rejection emails

  candidates.xlsx           Sample input file with 30 candidates

                   This documentation file
  ------------------------------------------------------------------------

------------------------------------------------------------------------

13. Author Information

  -----------------------------------------------------------------------
  Field       Details
  ----------- -----------------------------------------------------------
  Module      Send Offer / Rejection Email Automation

  Project     Process Automation Opportunities Analysis — Staffing &
              Recruitment

  Field       Data Science Internship Group Project

  Tools Used  Python, pandas, yagmail, Jinja2, fpdf2, openpyxl
  -----------------------------------------------------------------------

------------------------------------------------------------------------

This module is part of a 6-task recruitment automation pipeline
developed as a Data Science Internship project.



Automated Report Generation Feature

Overview

The Candidate Recommendation System now includes automated PDF report
generation to help you document and analyze your candidate matching
process. Reports are generated automatically after each recommendation
cycle and can also be generated manually on-demand.

Features

🤖 Automatic Report Generation

-   Auto-generated after matching: Every time you run the recommendation
    engine, a comprehensive PDF report is automatically created and
    saved
-   Timestamped files: Reports are named with timestamps (e.g.,
    auto_report_20260224_153045.pdf)
-   Stored in reports/ folder: All reports are saved in the reports/
    directory for easy access

📊 Report Contents

Each PDF report includes:

1.  Executive Summary
    -   Total CVs processed
    -   Total job positions
    -   Total matches generated
    -   Average matches per job
2.  Statistics Overview
    -   Visual charts showing system statistics
    -   Match quality distribution (Excellent, Good, Moderate, Low)
3.  Job Positions Summary
    -   List of all job positions with details
    -   Required skills and qualifications
4.  Detailed Recommendations
    -   Complete ranking of candidates for each job
    -   Top 10 candidates per position
    -   Match percentages and similarity scores
    -   Skills preview for each candidate
5.  Visual Analytics
    -   Bar charts showing upload statistics
    -   Pie charts showing match quality distribution

How to Use

Method 1: Automatic Generation

Reports are automatically generated when you click “Generate Rankings”
in the dashboard.

1.  Upload CVs
2.  Add job descriptions
3.  Click “Generate Rankings”
4.  ✅ Report is automatically created in reports/ folder

Method 2: Manual Generation

Click the “📊 Generate Report” button in the dashboard to create a
report on-demand.

1.  Upload CVs and jobs
2.  Click “📊 Generate Report”
3.  Report will download automatically to your browser

Method 3: API Access

You can also generate reports programmatically using the API:

    # Generate a new report
    curl -X POST http://localhost:5000/api/generate-report \
      -H "Content-Type: application/json" \
      -d '{"include_recommendations": true}'

    # List all generated reports
    curl http://localhost:5000/api/reports

    # Download a specific report
    curl http://localhost:5000/api/download-report/auto_report_20260224_153045.pdf -o report.pdf

API Endpoints

Generate Report

-   Endpoint: POST /api/generate-report

-   Payload:

        {
          "include_recommendations": true  // Set to false for summary only
        }

-   Response:

        {
          "success": true,
          "message": "Report generated successfully",
          "filename": "candidate_recommendation_report_20260224_153045.pdf",
          "download_url": "/api/download-report/candidate_recommendation_report_20260224_153045.pdf"
        }

List All Reports

-   Endpoint: GET /api/reports

-   Response:

        {
          "reports": [
            {
              "filename": "auto_report_20260224_153045.pdf",
              "size": "245.67 KB",
              "created": "2026-02-24 15:30:45",
              "download_url": "/api/download-report/auto_report_20260224_153045.pdf"
            }
          ],
          "total": 1
        }

Download Report

-   Endpoint: GET /api/download-report/<filename>
-   Returns: PDF file download

Storage Location

All reports are saved in:

    Process-Automation-Opportunities-Analysis/
    └── reports/
        ├── auto_report_20260224_153045.pdf
        ├── candidate_recommendation_report_20260224_160215.pdf
        └── ...

Requirements

The following Python packages are required for report generation: -
reportlab: For PDF creation - matplotlib: For charts and visualizations

Install them using:

    pip install reportlab matplotlib

Report Customization

The report generator supports: - Color-coded rankings: Gold, Silver,
Bronze for top 3 candidates - Match quality highlighting: Different
colors for match percentages - Professional formatting: Headers,
footers, page numbers - Comprehensive data: All candidate information
included

Benefits for Automation

1.  Documentation: Automatic record of all matching processes
2.  Compliance: Maintain audit trails of hiring decisions
3.  Analysis: Review historical matching results
4.  Sharing: Easy to share PDF reports with stakeholders
5.  Archiving: Timestamped reports for record-keeping

Troubleshooting

Report not generating?

-   Ensure you have uploaded both CVs and job descriptions
-   Check that the recommendation engine has been run at least once
-   Verify that reportlab and matplotlib are installed

Can’t find reports?

-   Check the reports/ folder in the project directory
-   Use the /api/reports endpoint to list all available reports

Download not working?

-   Ensure the Flask server is running
-   Check that the report file exists in the reports/ folder
-   Try accessing the download URL directly in your browser

Future Enhancements

Potential additions: - Email delivery of reports - Scheduled report
generation - Excel format reports - Custom report templates - Report
comparison features - Dashboard analytics view
