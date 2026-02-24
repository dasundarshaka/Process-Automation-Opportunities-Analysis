"""
Automated Report Generator for Candidate Recommendation System
Generates comprehensive PDF reports with analytics and visualizations
"""

from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import pandas as pd
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend
import matplotlib.pyplot as plt


class ReportGenerator:
    """Generate comprehensive PDF reports for the recommendation system"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        # Title style
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#06b6d4'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        # Heading style
        self.heading_style = ParagraphStyle(
            'CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#1e40af'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        
        # Subheading style
        self.subheading_style = ParagraphStyle(
            'CustomSubHeading',
            parent=self.styles['Heading3'],
            fontSize=12,
            textColor=colors.HexColor('#374151'),
            spaceAfter=8,
            fontName='Helvetica-Bold'
        )
        
        # Normal text style
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#1f2937'),
            alignment=TA_JUSTIFY
        )
    
    def _create_header_footer(self, canvas, doc):
        """Add header and footer to each page"""
        canvas.saveState()
        
        # Header
        canvas.setFont('Helvetica-Bold', 10)
        canvas.setFillColor(colors.HexColor('#06b6d4'))
        canvas.drawString(inch, A4[1] - 0.5*inch, "Candidate Recommendation System Report")
        
        # Footer
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#6b7280'))
        canvas.drawString(inch, 0.5*inch, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        canvas.drawRightString(A4[0] - inch, 0.5*inch, f"Page {doc.page}")
        
        canvas.restoreState()
    
    def _create_statistics_chart(self, cvs_count, jobs_count, total_matches):
        """Create a bar chart for statistics"""
        fig, ax = plt.subplots(figsize=(6, 4))
        
        categories = ['CVs\nUploaded', 'Jobs\nPosted', 'Total\nMatches']
        values = [cvs_count, jobs_count, total_matches]
        colors_list = ['#06b6d4', '#8b5cf6', '#f97316']
        
        bars = ax.bar(categories, values, color=colors_list, alpha=0.8, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        ax.set_ylabel('Count', fontweight='bold', fontsize=11)
        ax.set_title('System Statistics Overview', fontweight='bold', fontsize=14, pad=20)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        
        plt.tight_layout()
        
        # Save to BytesIO
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def _create_match_distribution_chart(self, recommendations_data):
        """Create a pie chart showing match quality distribution"""
        match_levels = {'Excellent (>70%)': 0, 'Good (50-70%)': 0, 'Moderate (30-50%)': 0, 'Low (<30%)': 0}
        
        for job_rec in recommendations_data:
            for candidate in job_rec['candidates']:
                match_pct = candidate['match_percentage']
                if match_pct >= 70:
                    match_levels['Excellent (>70%)'] += 1
                elif match_pct >= 50:
                    match_levels['Good (50-70%)'] += 1
                elif match_pct >= 30:
                    match_levels['Moderate (30-50%)'] += 1
                else:
                    match_levels['Low (<30%)'] += 1
        
        fig, ax = plt.subplots(figsize=(6, 4))
        
        labels = [k for k, v in match_levels.items() if v > 0]
        sizes = [v for v in match_levels.values() if v > 0]
        colors_list = ['#10b981', '#06b6d4', '#f59e0b', '#ef4444'][:len(labels)]
        
        if sizes:
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors_list,
                                              autopct='%1.1f%%', startangle=90,
                                              textprops={'fontsize': 9, 'fontweight': 'bold'})
            
            ax.set_title('Match Quality Distribution', fontweight='bold', fontsize=14, pad=20)
            
            plt.tight_layout()
        
        # Save to BytesIO
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def generate_report(self, cvs_data, jobs_data, recommendations_data, output_path):
        """
        Generate comprehensive PDF report
        
        Args:
            cvs_data: List of CV dictionaries
            jobs_data: List of job dictionaries
            recommendations_data: List of recommendation results
            output_path: Path where PDF should be saved
        """
        # Create PDF document
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=inch,
            leftMargin=inch,
            topMargin=inch,
            bottomMargin=inch
        )
        
        # Container for the 'Flowable' objects
        elements = []
        
        # Title
        title = Paragraph("Candidate Recommendation System", self.title_style)
        elements.append(title)
        
        subtitle = Paragraph(
            f"<b>Automated Analysis Report</b><br/>Generated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}",
            self.normal_style
        )
        elements.append(subtitle)
        elements.append(Spacer(1, 0.3*inch))
        
        # Executive Summary
        elements.append(Paragraph("Executive Summary", self.heading_style))
        
        summary_text = f"""
        This report provides a comprehensive analysis of the candidate recommendation process.
        The system has processed <b>{len(cvs_data)} CVs</b> and matched them against <b>{len(jobs_data)} job positions</b>,
        generating a total of <b>{sum(len(job['candidates']) for job in recommendations_data)} candidate-job matches</b>.
        """
        elements.append(Paragraph(summary_text, self.normal_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Statistics Overview
        elements.append(Paragraph("Statistics Overview", self.heading_style))
        
        total_matches = sum(len(job['candidates']) for job in recommendations_data)
        
        stats_data = [
            ['Metric', 'Count'],
            ['Total CVs Uploaded', str(len(cvs_data))],
            ['Total Job Positions', str(len(jobs_data))],
            ['Total Matches Generated', str(total_matches)],
            ['Average Matches per Job', f"{total_matches / len(jobs_data):.1f}" if jobs_data else "0"],
        ]
        
        stats_table = Table(stats_data, colWidths=[3.5*inch, 1.5*inch])
        stats_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f3f4f6')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#d1d5db')),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')])
        ]))
        elements.append(stats_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Add statistics chart
        try:
            chart_buffer = self._create_statistics_chart(len(cvs_data), len(jobs_data), total_matches)
            chart_image = Image(chart_buffer, width=5*inch, height=3.33*inch)
            elements.append(chart_image)
            elements.append(Spacer(1, 0.2*inch))
        except Exception as e:
            print(f"Warning: Could not create statistics chart: {e}")
        
        # Page break before detailed sections
        elements.append(PageBreak())
        
        # Job Positions Summary
        elements.append(Paragraph("Job Positions Summary", self.heading_style))
        
        for idx, job in enumerate(jobs_data, 1):
            job_title = Paragraph(f"<b>{idx}. {job['title']}</b> (ID: {job['job_id']})", self.subheading_style)
            elements.append(job_title)
            
            job_info = f"""
            <b>Source:</b> {job.get('source', 'file')}<br/>
            <b>Upload Date:</b> {job['timestamp'][:10]}<br/>
            <b>Required Skills:</b> {job['required_skills'][:200] if job['required_skills'] else 'N/A'}...
            """
            elements.append(Paragraph(job_info, self.normal_style))
            elements.append(Spacer(1, 0.15*inch))
        
        elements.append(PageBreak())
        
        # Match Quality Distribution
        elements.append(Paragraph("Match Quality Distribution", self.heading_style))
        
        try:
            match_chart_buffer = self._create_match_distribution_chart(recommendations_data)
            match_chart_image = Image(match_chart_buffer, width=5*inch, height=3.33*inch)
            elements.append(match_chart_image)
            elements.append(Spacer(1, 0.2*inch))
        except Exception as e:
            print(f"Warning: Could not create match distribution chart: {e}")
        
        elements.append(PageBreak())
        
        # Detailed Recommendations
        elements.append(Paragraph("Detailed Recommendations by Job", self.heading_style))
        
        for job_rec in recommendations_data:
            # Job header
            job_header = Paragraph(
                f"<b>Job: {job_rec['job_title']}</b> (ID: {job_rec['job_id']})",
                self.heading_style
            )
            elements.append(job_header)
            
            elements.append(Paragraph(
                f"Total Candidates Matched: <b>{job_rec['total_matches']}</b>",
                self.normal_style
            ))
            elements.append(Spacer(1, 0.1*inch))
            
            # Top candidates table (show top 10)
            candidates_data = [['Rank', 'Candidate Name', 'Match %', 'Skills Preview']]
            
            for candidate in job_rec['candidates'][:10]:  # Show top 10
                skills_preview = candidate['skills'][:80] if candidate['skills'] else 'N/A'
                candidates_data.append([
                    str(candidate['rank']),
                    candidate['name'][:25],
                    f"{candidate['match_percentage']:.1f}%",
                    skills_preview + '...' if len(candidate.get('skills', '')) > 80 else skills_preview
                ])
            
            candidates_table = Table(candidates_data, colWidths=[0.6*inch, 1.8*inch, 0.8*inch, 2.8*inch])
            candidates_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#06b6d4')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                ('ALIGN', (2, 0), (2, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 9),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#d1d5db')),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')]),
                # Highlight top 3
                ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#fef3c7')),  # Gold
                ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#e5e7eb')) if len(candidates_data) > 2 else ('BACKGROUND', (0, 0), (0, 0), colors.white),  # Silver
                ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#fed7aa')) if len(candidates_data) > 3 else ('BACKGROUND', (0, 0), (0, 0), colors.white),  # Bronze
            ]))
            elements.append(candidates_table)
            elements.append(Spacer(1, 0.3*inch))
            
            # If there are more candidates, add note
            if job_rec['total_matches'] > 10:
                note = Paragraph(
                    f"<i>* Showing top 10 of {job_rec['total_matches']} total matches</i>",
                    self.normal_style
                )
                elements.append(note)
                elements.append(Spacer(1, 0.2*inch))
        
        # Build PDF
        doc.build(elements, onFirstPage=self._create_header_footer, onLaterPages=self._create_header_footer)
        
        return output_path
    
    def generate_summary_report(self, cvs_data, jobs_data, output_path):
        """
        Generate a quick summary report without recommendations
        Used when no matching has been done yet
        """
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=inch,
            leftMargin=inch,
            topMargin=inch,
            bottomMargin=inch
        )
        
        elements = []
        
        # Title
        title = Paragraph("System Status Report", self.title_style)
        elements.append(title)
        
        subtitle = Paragraph(
            f"Generated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}",
            self.normal_style
        )
        elements.append(subtitle)
        elements.append(Spacer(1, 0.3*inch))
        
        # Current Status
        elements.append(Paragraph("Current System Status", self.heading_style))
        
        status_text = f"""
        The system currently has <b>{len(cvs_data)} CVs</b> uploaded and <b>{len(jobs_data)} job positions</b> registered.
        Run the recommendation engine to generate candidate matches.
        """
        elements.append(Paragraph(status_text, self.normal_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Statistics
        stats_data = [
            ['Metric', 'Count'],
            ['Total CVs Uploaded', str(len(cvs_data))],
            ['Total Job Positions', str(len(jobs_data))],
        ]
        
        stats_table = Table(stats_data, colWidths=[3.5*inch, 1.5*inch])
        stats_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#d1d5db')),
        ]))
        elements.append(stats_table)
        
        doc.build(elements, onFirstPage=self._create_header_footer, onLaterPages=self._create_header_footer)
        
        return output_path
