# Excel Database Feature

## Overview
The system now automatically stores all uploaded data in Excel files for easy reporting and record-keeping.

## Database Location
All Excel files are stored in the `database/` folder:

### 1. **cvs_database.xlsx**
Stores all uploaded CV information:
- Candidate ID
- Name
- Skills
- Experience
- Education
- Filename
- Upload Date
- Text Length

### 2. **jobs_database.xlsx**
Stores all job descriptions:
- Job ID
- Title
- Required Skills
- Experience Required
- Education Required
- Source (file/text)
- Filename
- Upload Date
- Description Length

### 3. **recommendations_database.xlsx**
Stores all candidate-job matches:
- Job ID
- Job Title
- Rank (1, 2, 3, etc.)
- Candidate ID
- Candidate Name
- Match Percentage
- Similarity Score
- Summary
- Skills Match
- Generated Date

## Automatic Updates

### When CVs are Uploaded
✓ Data is automatically saved to `cvs_database.xlsx`
✓ File is created/updated with formatted headers
✓ Blue professional styling applied

### When Jobs are Added
✓ Data is automatically saved to `jobs_database.xlsx`
✓ Works for both file uploads and text input
✓ Professional formatting applied

### When Recommendations are Generated
✓ All matches are saved to `recommendations_database.xlsx`
✓ Historical record of all recommendations
✓ Data is appended (not overwritten) for tracking over time

## API Endpoint

### Check Database Status
**GET** `/api/database-status`

Returns information about all Excel database files:
```json
{
  "databases": [
    {
      "name": "CVs Database",
      "filename": "cvs_database.xlsx",
      "size": "25.34 KB",
      "last_modified": "2026-02-21 23:45:12",
      "exists": true
    },
    ...
  ],
  "database_folder": "database"
}
```

## Features

### Professional Formatting
- **Blue Headers**: Professional blue background (#1E40AF) with white text
- **Auto-sized Columns**: Columns automatically sized for readability
- **Clean Layout**: Organized data structure for easy analysis

### Data Persistence
- Files are updated after every upload/recommendation
- Data is preserved between server restarts
- Historical tracking of all recommendations

### Clear Data
When using `/api/clear` endpoint:
- All Excel database files are deleted
- Uploaded files are removed
- System is reset to clean state

## Benefits

1. **Easy Reporting**: Open Excel files directly for analysis
2. **Data Backup**: Automatic backup of all system data
3. **Historical Tracking**: Keep records of all recommendations over time
4. **Export Ready**: Use Excel files for reports, presentations, or further analysis
5. **No Manual Work**: Everything is automatic - just upload and the system handles the rest

## Usage Example

1. Upload CVs → `cvs_database.xlsx` is created/updated
2. Add Job Descriptions → `jobs_database.xlsx` is created/updated
3. Generate Recommendations → `recommendations_database.xlsx` is created/updated
4. Open Excel files in `database/` folder to view reports
5. Use data for analysis, presentations, or record-keeping

## Technical Details

- Uses `openpyxl` library for Excel operations
- Pandas DataFrame integration for data handling
- Professional styling with colored headers
- Automatic column width adjustment
- UTF-8 encoding support for international characters
