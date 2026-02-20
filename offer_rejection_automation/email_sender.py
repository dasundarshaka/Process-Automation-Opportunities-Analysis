import yagmail
import os
from jinja2 import Environment, FileSystemLoader

# Load Jinja2 templates from the templates folder
env = Environment(loader=FileSystemLoader('templates'))

def send_offer_email(sender_email, sender_password, candidate):
    """
    Sends an offer email with PDF offer letter attached.
    """
    # Load and render the offer email template
    template = env.get_template('offer_template.html')
    email_body = template.render(
        name=candidate['Name'],
        position=candidate['Position']
    )

    # Generate the PDF offer letter
    from pdf_generator import generate_offer_letter
    pdf_file = generate_offer_letter(candidate['Name'], candidate['Position'])

    # Send email with attachment
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=candidate['Email'],
        subject=f"Job Offer – {candidate['Position']} | Unknown Company",
        contents=email_body,
        attachments=pdf_file
    )

    # Delete the PDF after sending to keep folder clean
    if os.path.exists(pdf_file):
        os.remove(pdf_file)

    print(f"  Offer email sent to {candidate['Name']} ({candidate['Email']})")


def send_rejection_email(sender_email, sender_password, candidate):
    """
    Sends a rejection email to the candidate.
    """
    # Load and render the rejection email template
    template = env.get_template('rejection_template.html')
    email_body = template.render(
        name=candidate['Name'],
        position=candidate['Position']
    )

    # Send email
    yag = yagmail.SMTP(sender_email, sender_password)
    yag.send(
        to=candidate['Email'],
        subject=f"Application Update – {candidate['Position']} | Unknown Company",
        contents=email_body
    )

    print(f"  Rejection email sent to {candidate['Name']} ({candidate['Email']})")