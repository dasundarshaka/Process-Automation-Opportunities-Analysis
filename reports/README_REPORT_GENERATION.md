# 📊 Automated Report Generation System

## Overview

The Candidate Recommendation System now features **automated PDF report generation** that creates comprehensive, professional reports after each candidate-job matching process. This ensures complete documentation and provides stakeholders with detailed analytics.

---

## 🎯 What We've Built

### 1. **PDF Report Generator Module**
- **File**: `src/report_generator.py`
- **Purpose**: Generate professional PDF reports with charts, tables, and analytics
- **Technology**: ReportLab (PDF generation) + Matplotlib (charts)

### 2. **API Endpoints**
Added to `app.py`:
- `POST /api/generate-report` - Generate a report on-demand
- `GET /api/reports` - List all generated reports
- `GET /api/download-report/<filename>` - Download specific report

### 3. **Dashboard Integration**
Updated `templates/index.html`:
- Added **"📊 Generate Report"** button to the dashboard
- Automatic download functionality
- Button enabled/disabled based on data availability

### 4. **Automatic Report Generation**
- Reports are **automatically created** after each recommendation cycle
- No manual intervention required
- Timestamped filenames for easy tracking

---

## 📝 Report Contents

Each generated PDF report includes:

### 📄 Executive Summary
- Total CVs processed
- Total job positions
- Total candidate-job matches
- Average matches per job

### 📊 Visual Analytics
1. **Statistics Overview Chart** (Bar Chart)
   - CVs uploaded
   - Jobs posted
   - Total matches generated

2. **Match Quality Distribution** (Pie Chart)
   - Excellent matches (>70%)
   - Good matches (50-70%)
   - Moderate matches (30-50%)
   - Low matches (<30%)

### 💼 Job Positions Summary
- Job ID and title
- Source (file upload or text input)
- Upload date
- Required skills preview

### 🏆 Detailed Candidate Rankings
For each job position:
- **Rank** (with color coding: Gold 🥇, Silver 🥈, Bronze 🥉 for top 3)
- **Candidate Name**
- **Match Percentage**
- **Similarity Score**
- **Skills** (preview)
- **Experience** (preview)
- **Education** (preview)

### 📑 Professional Formatting
- Header and footer on each page
- Color-coded tables
- Highlighted top performers
- Timestamp and page numbers

---

## 🚀 How to Use

### Method 1: Automatic Generation (Recommended)
1. Upload CVs through the dashboard
2. Add job descriptions (file or text)
3. Click **"Generate Rankings"**
4. 📝 Report is **automatically generated** in `reports/` folder

**File naming**: `auto_report_YYYYMMDD_HHMMSS.pdf`

### Method 2: Manual Generation
1. Ensure you have CVs and jobs uploaded
2. Click **"📊 Generate Report"** button on dashboard
3. Report will **download automatically** to your browser

### Method 3: API Call
```bash
# Generate report
curl -X POST http://localhost:5000/api/generate-report \
  -H "Content-Type: application/json" \
  -d '{"include_recommendations": true}'

# List all reports
curl http://localhost:5000/api/reports

# Download specific report
curl http://localhost:5000/api/download-report/auto_report_20260224_153045.pdf \
  --output report.pdf
```

---

## 📁 File Structure

```
Process-Automation-Opportunities-Analysis/
├── src/
│   └── report_generator.py          # Report generation engine (NEW)
├── reports/                          # Generated PDF reports (NEW)
│   ├── auto_report_20260224_153045.pdf
│   └── candidate_recommendation_report_20260224_160215.pdf
├── database/                         # Excel databases
│   ├── cvs_database.xlsx
│   ├── jobs_database.xlsx
│   └── recommendations_database.xlsx
├── app.py                           # Updated with report endpoints
└── templates/
    └── index.html                   # Updated with report button
```

---

## 🔧 Technical Implementation

### Dependencies Added
```bash
pip install reportlab matplotlib
```

### Core Functions

#### `ReportGenerator` Class
```python
from src.report_generator import ReportGenerator

report_generator = ReportGenerator()

# Generate full report with recommendations
report_generator.generate_report(
    cvs_data, 
    jobs_data, 
    recommendations_data, 
    output_path
)

# Generate summary report (no recommendations)
report_generator.generate_summary_report(
    cvs_data, 
    jobs_data, 
    output_path
)
```

#### Auto-generation in Recommendation Pipeline
```python
# In app.py - /api/recommend endpoint
# After generating recommendations...
try:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_filename = f'auto_report_{timestamp}.pdf'
    report_path = os.path.join(app.config['REPORTS_FOLDER'], report_filename)
    report_generator.generate_report(cvs_data, jobs_data, job_recommendations, report_path)
    print(f"✓ Auto-generated report: {report_filename}")
except Exception as e:
    print(f"✗ Failed to auto-generate report: {str(e)}")
```

---

## 📊 Report Features

### 1. **Professional Layout**
- A4 page size
- Proper margins (1 inch all sides)
- Header and footer on every page
- Page numbers

### 2. **Color Coding**
- **Headers**: Blue gradient (#1e40af, #06b6d4)
- **Top 3 Rankings**:
  - 🥇 Gold: #fef3c7 (Rank 1)
  - 🥈 Silver: #e5e7eb (Rank 2)
  - 🥉 Bronze: #fed7aa (Rank 3)
- **Match Quality**:
  - Excellent: Green (#10b981)
  - Good: Cyan (#06b6d4)
  - Moderate: Orange (#f59e0b)
  - Low: Red (#ef4444)

### 3. **Data Tables**
- Clean grid layout
- Alternating row colors for readability
- Bold headers
- Centered alignment where appropriate

### 4. **Charts & Visualizations**
- High-resolution (150 DPI)
- Professional styling
- Value labels on charts
- Legends and titles

---

## 💡 Use Cases

### 1. **Audit Trail**
- Maintain historical records of all matching processes
- Track changes over time
- Compliance documentation

### 2. **Stakeholder Reports**
- Share results with hiring managers
- Present to executives
- Client deliverables

### 3. **Process Automation**
- No manual report creation needed
- Consistent formatting
- Immediate availability

### 4. **Performance Analysis**
- Compare match quality across jobs
- Identify trends
- Optimize recruitment strategy

---

## 🎨 Customization Options

### Modify Report Styling
Edit `src/report_generator.py`:

```python
# Change title color
self.title_style = ParagraphStyle(
    'CustomTitle',
    fontSize=24,
    textColor=colors.HexColor('#YOUR_COLOR'),
    ...
)

# Adjust chart colors
colors_list = ['#COLOR1', '#COLOR2', '#COLOR3']
```

### Change Report Content
Edit `generate_report()` method to:
- Add/remove sections
- Modify table columns
- Include additional analytics

---

## 🔐 Best Practices

### 1. **Storage Management**
```python
# Clean old reports periodically
import os
from datetime import datetime, timedelta

def cleanup_old_reports(days=30):
    reports_folder = 'reports/'
    cutoff_date = datetime.now() - timedelta(days=days)
    
    for filename in os.listdir(reports_folder):
        file_path = os.path.join(reports_folder, filename)
        file_time = datetime.fromtimestamp(os.path.getctime(file_path))
        
        if file_time < cutoff_date:
            os.remove(file_path)
```

### 2. **Error Handling**
Reports are generated with try-except blocks to prevent application crashes:
```python
try:
    report_generator.generate_report(...)
    print("✓ Report generated")
except Exception as e:
    print(f"✗ Report generation failed: {str(e)}")
    # Application continues running
```

### 3. **Naming Conventions**
- Auto-generated: `auto_report_YYYYMMDD_HHMMSS.pdf`
- Manual: `candidate_recommendation_report_YYYYMMDD_HHMMSS.pdf`
- Custom: Can be configured in API request

---

## 📈 Future Enhancements

Potential improvements for the report system:

1. **Email Integration**
   - Automatically email reports to stakeholders
   - Schedule periodic report generation

2. **Multi-format Export**
   - Excel format
   - CSV export
   - HTML reports

3. **Advanced Analytics**
   - Trend analysis over time
   - Predictive insights
   - Comparison reports

4. **Customizable Templates**
   - Company branding
   - Multiple report styles
   - Configurable sections

5. **Interactive Reports**
   - HTML with JavaScript charts
   - Drill-down capabilities
   - Real-time updates

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'reportlab'"
**Solution**: Install required packages
```bash
pip install reportlab matplotlib
```

### Issue: Report generation fails
**Solution**: Check the following:
1. Ensure `reports/` folder exists and is writable
2. Verify CVs and jobs data are loaded
3. Check application logs for specific errors

### Issue: Charts not appearing in PDF
**Solution**: 
1. Verify matplotlib is installed: `pip install matplotlib`
2. Check matplotlib backend: Should use 'Agg' (non-GUI)
3. Ensure sufficient memory for chart generation

### Issue: Report download not working
**Solution**:
1. Check file permissions on `reports/` folder
2. Verify file exists: `GET /api/reports`
3. Check browser download settings

---

## 📞 Support & Contribution

### Questions?
- Review code documentation in `src/report_generator.py`
- Check API endpoint responses for error messages
- Review Flask application logs

### Contributing
To enhance the report generation system:
1. Modify `src/report_generator.py` for PDF changes
2. Update `app.py` for API functionality
3. Edit `templates/index.html` for UI improvements

---

## 📄 License & Credits

**Report Generation Module**: Built using
- [ReportLab](https://www.reportlab.com/) - PDF generation
- [Matplotlib](https://matplotlib.org/) - Chart creation
- Flask - Web framework

**Created**: February 24, 2026
**Version**: 1.0.0

---

## ✅ Summary

The automated report generation system provides:
- ✅ **Automated** PDF creation after each matching process
- ✅ **Professional** formatting with charts and tables
- ✅ **Comprehensive** analytics and statistics
- ✅ **Easy integration** with existing dashboard
- ✅ **Scalable** architecture for future enhancements

Reports are automatically saved and ready for distribution, providing complete documentation of the candidate recommendation process without any manual effort.

---

**For more information**, refer to the main [README.md](README.md) or check the application documentation at `http://localhost:5000` when the server is running.
