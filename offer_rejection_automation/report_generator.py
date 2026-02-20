import pandas as pd
from datetime import datetime

def generate_report(results):
    """
    Generates a summary report of all emails sent.
    results: list of dicts with candidate info and send status
    """
    if not results:
        print("No emails were sent.")
        return

    df = pd.DataFrame(results)

    # Summary counts
    total = len(df)
    offers_sent = len(df[df['Status'] == 'Offer'])
    rejections_sent = len(df[df['Status'] == 'Rejected'])
    successful = len(df[df['Email_Status'] == 'Sent'])
    failed = len(df[df['Email_Status'] == 'Failed'])

    print("\n" + "="*50)
    print("       EMAIL AUTOMATION REPORT")
    print("="*50)
    print(f"  Report Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Total Processed  : {total}")
    print(f"  Offer Emails     : {offers_sent}")
    print(f"  Rejection Emails : {rejections_sent}")
    print(f"  Successfully Sent: {successful}")
    print(f"  Failed           : {failed}")
    print("="*50)

    # Detailed table
    print("\nDetailed Log:")
    print(df[['Name', 'Position', 'Status', 'Email_Status']].to_string(index=False))

    # Save report to Excel
    report_filename = f"email_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(report_filename, index=False)
    print(f"\n  Report saved as: {report_filename}")