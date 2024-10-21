from flask import Flask, render_template, request, redirect
import csv
from src.data_processing import save_study_session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_study_session():
    date = request.form['2nd September 2025']
    subject = request.form['Data Structures']
    duration = request.form['1 hour']
    notes = request.form['Focus on understading the whole picture.']
    
    # Create a data object
    data = [date, subject, duration, notes]


    # Save the data to a CSV file
    with open('data/study_sessions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, subject, duration, notes])
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
