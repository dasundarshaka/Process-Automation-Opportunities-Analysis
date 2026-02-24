from flask import Flask, render_template, jsonify, request
import pandas as pd
import os

app = Flask(__name__)

FILE_PATH = os.path.join(os.path.dirname(__file__), 'candidates.xlsx')
PASSING_SCORE = 75

def load_data():
    if not os.path.exists(FILE_PATH):
        return None
    return pd.read_excel(FILE_PATH, dtype={'Candidate_ID': str})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    df = load_data()
    if df is None:
        return jsonify({'error': 'candidates.xlsx not found'}), 404

    # Return all candidates with their full details
    records = df.fillna('').to_dict(orient='records')
    return jsonify(records)

@app.route('/api/update', methods=['POST'])
def update_status():
    data = request.get_json()
    candidate_id = str(data.get('candidate_id'))
    score = float(data.get('score'))

    if not (0 <= score <= 100):
        return jsonify({'error': 'Score must be between 0 and 100'}), 400

    df = load_data()
    if df is None:
        return jsonify({'error': 'candidates.xlsx not found'}), 404

    mask = df['Candidate_ID'].astype(str) == candidate_id
    if not mask.any():
        return jsonify({'error': f'Candidate ID {candidate_id} not found'}), 404

    new_status = 'Offer' if score >= PASSING_SCORE else 'Rejected'

    df.loc[mask, 'Status'] = new_status
    df.loc[mask, 'Email_Sent'] = 'No'
    if 'Interview_Score' in df.columns:
        df.loc[mask, 'Interview_Score'] = score

    df.to_excel(FILE_PATH, index=False)

    name = df.loc[mask, 'Name'].values[0]
    return jsonify({'success': True, 'name': name, 'status': new_status, 'score': score})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
