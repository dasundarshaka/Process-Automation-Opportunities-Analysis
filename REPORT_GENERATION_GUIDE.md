# Automated Report Generation Feature

## Overview
The Candidate Recommendation System now includes **automated PDF report generation** to help you document and analyze your candidate matching process. Reports are generated automatically after each recommendation cycle and can also be generated manually on-demand.

## Features

### 🤖 Automatic Report Generation
- **Auto-generated after matching**: Every time you run the recommendation engine, a comprehensive PDF report is automatically created and saved
- **Timestamped files**: Reports are named with timestamps (e.g., `auto_report_20260224_153045.pdf`)
- **Stored in reports/ folder**: All reports are saved in the `reports/` directory for easy access

### 📊 Report Contents
Each PDF report includes:

1. **Executive Summary**
   - Total CVs processed
   - Total job positions
   - Total matches generated
   - Average matches per job

2. **Statistics Overview**
   - Visual charts showing system statistics
   - Match quality distribution (Excellent, Good, Moderate, Low)

3. **Job Positions Summary**
   - List of all job positions with details
   - Required skills and qualifications

4. **Detailed Recommendations**
   - Complete ranking of candidates for each job
   - Top 10 candidates per position
   - Match percentages and similarity scores
   - Skills preview for each candidate

5. **Visual Analytics**
   - Bar charts showing upload statistics
   - Pie charts showing match quality distribution

## How to Use

### Method 1: Automatic Generation
Reports are **automatically generated** when you click "Generate Rankings" in the dashboard.

1. Upload CVs
2. Add job descriptions
3. Click "**Generate Rankings**"
4. ✅ Report is automatically created in `reports/` folder

### Method 2: Manual Generation
Click the "**📊 Generate Report**" button in the dashboard to create a report on-demand.

1. Upload CVs and jobs
2. Click "**📊 Generate Report**"
3. Report will download automatically to your browser

### Method 3: API Access
You can also generate reports programmatically using the API:

```bash
# Generate a new report
curl -X POST http://localhost:5000/api/generate-report \
  -H "Content-Type: application/json" \
  -d '{"include_recommendations": true}'

# List all generated reports
curl http://localhost:5000/api/reports

# Download a specific report
curl http://localhost:5000/api/download-report/auto_report_20260224_153045.pdf -o report.pdf
```

## API Endpoints

### Generate Report
- **Endpoint**: `POST /api/generate-report`
- **Payload**: 
  ```json
  {
    "include_recommendations": true  // Set to false for summary only
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "message": "Report generated successfully",
    "filename": "candidate_recommendation_report_20260224_153045.pdf",
    "download_url": "/api/download-report/candidate_recommendation_report_20260224_153045.pdf"
  }
  ```

### List All Reports
- **Endpoint**: `GET /api/reports`
- **Response**:
  ```json
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
  ```

### Download Report
- **Endpoint**: `GET /api/download-report/<filename>`
- **Returns**: PDF file download

## Storage Location

All reports are saved in:
```
Process-Automation-Opportunities-Analysis/
└── reports/
    ├── auto_report_20260224_153045.pdf
    ├── candidate_recommendation_report_20260224_160215.pdf
    └── ...
```

## Requirements

The following Python packages are required for report generation:
- `reportlab`: For PDF creation
- `matplotlib`: For charts and visualizations

Install them using:
```bash
pip install reportlab matplotlib
```

## Report Customization

The report generator supports:
- **Color-coded rankings**: Gold, Silver, Bronze for top 3 candidates
- **Match quality highlighting**: Different colors for match percentages
- **Professional formatting**: Headers, footers, page numbers
- **Comprehensive data**: All candidate information included

## Benefits for Automation

1. **Documentation**: Automatic record of all matching processes
2. **Compliance**: Maintain audit trails of hiring decisions
3. **Analysis**: Review historical matching results
4. **Sharing**: Easy to share PDF reports with stakeholders
5. **Archiving**: Timestamped reports for record-keeping

## Troubleshooting

### Report not generating?
- Ensure you have uploaded both CVs and job descriptions
- Check that the recommendation engine has been run at least once
- Verify that reportlab and matplotlib are installed

### Can't find reports?
- Check the `reports/` folder in the project directory
- Use the `/api/reports` endpoint to list all available reports

### Download not working?
- Ensure the Flask server is running
- Check that the report file exists in the `reports/` folder
- Try accessing the download URL directly in your browser

## Future Enhancements

Potential additions:
- Email delivery of reports
- Scheduled report generation
- Excel format reports
- Custom report templates
- Report comparison features
- Dashboard analytics view

---

**Last Updated**: February 24, 2026  
**Version**: 1.0
