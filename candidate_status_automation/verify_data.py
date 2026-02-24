import pandas as pd

file_path = 'candidates.xlsx'

try:
    df = pd.read_excel(file_path)
    print(f"Contents of {file_path}:")
    print(df.to_string())
    
    # Simple assertions
    # 001: 80 -> Offer
    # 002: 65 -> Rejected
    # 003: 85 -> Offer
    # 005: 90 -> Offer (but was already Offer, so script should have ignored it if filter worked correctly, wait script filters by Status='Interview')
    # Let's check 005. In generate_mock_data.py, 005 was 'Offer'. So it should remain 'Offer' and not be processed/printed.
    
    print("\nVerification Checks:")
    row_001 = df[df['Candidate_ID'] == '001'].iloc[0]
    print(f"001 Status: {row_001['Status']} (Expected: Offer)")
    
    row_002 = df[df['Candidate_ID'] == '002'].iloc[0]
    print(f"002 Status: {row_002['Status']} (Expected: Rejected)")

    row_003 = df[df['Candidate_ID'] == '003'].iloc[0]
    print(f"003 Status: {row_003['Status']} (Expected: Offer)")
    
    row_005 = df[df['Candidate_ID'] == '005'].iloc[0]
    print(f"005 Status: {row_005['Status']} (Expected: Offer - unchanged)")

except Exception as e:
    print(f"Error verification failed: {e}")
