from fpdf import FPDF
from datetime import date

def generate_offer_letter(name, position):
    """
    Generates a PDF offer letter for the candidate.
    Returns the filename of the generated PDF.
    """
    pdf = FPDF()
    pdf.add_page()

    # Company Header
    pdf.set_font("Arial", style='B', size=16)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(200, 10, txt="Unknown COMPANY", ln=True, align='C')

    pdf.set_font("Arial", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(200, 6, txt="Hello Business Street, Colombo, Sri Lanka", ln=True, align='C')
    pdf.cell(200, 6, txt="hr@unknowncompany.com | +94 11 234 5678", ln=True, align='C')

    # Divider line
    pdf.set_draw_color(0, 102, 204)
    pdf.line(10, 35, 200, 35)
    pdf.ln(15)

    # Title
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt="OFFICIAL OFFER LETTER", ln=True, align='C')
    pdf.ln(5)

    # Date
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt=f"Date: {date.today().strftime('%B %d, %Y')}", ln=True)
    pdf.ln(5)

    # Greeting
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt=f"Dear {name},", ln=True)
    pdf.ln(3)

    # Body
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(190, 8, txt=(
        f"We are pleased to offer you the position of {position} at Unknown Company. "
        f"After a thorough review of your application and interviews, we are confident "
        f"that your skills and experience will be a great asset to our team."
    ))
    pdf.ln(5)

    pdf.multi_cell(190, 8, txt=(
        "This offer is contingent upon successful completion of background verification. "
        "Please review the terms and confirm your acceptance within 5 business days "
        "by signing and returning a copy of this letter."
    ))
    pdf.ln(8)

    # Terms Section
    pdf.set_font("Arial", style='B', size=11)
    pdf.cell(200, 8, txt="Position Details:", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt=f"   - Job Title     : {position}", ln=True)
    pdf.cell(200, 8, txt=f"   - Start Date    : To be confirmed", ln=True)
    pdf.cell(200, 8, txt=f"   - Employment    : Full Time", ln=True)
    pdf.cell(200, 8, txt=f"   - Location      : Colombo, Sri Lanka", ln=True)
    pdf.ln(8)

    # Closing
    pdf.multi_cell(190, 8, txt=(
        "We look forward to having you on board and are excited about the "
        "contributions you will make to our team."
    ))
    pdf.ln(8)

    pdf.cell(200, 8, txt="Sincerely,", ln=True)
    pdf.ln(10)
    pdf.set_font("Arial", style='B', size=11)
    pdf.cell(200, 8, txt="HR Recruitment Team", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 8, txt="Unknown Company", ln=True)

    # Save PDF
    filename = f"offer_letter_{name.replace(' ', '_')}.pdf"
    pdf.output(filename)
    print(f"  PDF generated: {filename}")
    return filename