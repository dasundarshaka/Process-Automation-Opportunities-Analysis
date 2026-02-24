import pandas as pd
import os

# Define the file path
file_path = 'candidates.xlsx'

# Define the data with the agreed schema
data = {
    'Candidate_ID': ['001', '002', '003', '004', '005'],
    'Name': ['Amal Perera', 'Nimal Silva', 'Kamal Dias', 'Sunil Fernando', 'Chathura Rao'],
    'Email': ['amal.perera@example.com', 'nimal.silva@example.com', 'kamal.dias@example.com', 'sunil.fernando@example.com', 'chathura.rao@example.com'],
    'Position': ['Data Analyst', 'Software Engineer', 'QA Engineer', 'Data Scientist', 'DevOps Engineer'],
    'Status': ['Interview', 'Interview', 'Interview', 'Screening', 'Offer'],  # Mix of statuses
    'Email_Sent': ['No', 'No', 'No', 'No', 'Yes'],
    'Interview_Score': [80, 65, 85, None, 90]  # Scores to drive the logic
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel(file_path, index=False)

print(f"Mock '{file_path}' created successfully with {len(df)} records.")
print(df)
