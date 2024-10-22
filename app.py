from flask import Flask, render_template, request, redirect
import csv
from src.data_processing import save_study_session
from src.visualization import plot_weekly_study_hours, plot_study_time_by_subject


app = Flask(__name__)

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

@app.route('/visualize-result', methods=['POST'])
def visualize_result():
    visualization_type = request.form['visualization']
    if visualization_type == 'weekly_hours':
        plot_weekly_study_hours()
    elif visualization_type == 'subject_hours':
        plot_study_time_by_subject()
    return redirect('/visualize')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log_study_session():
    date = request.form['2nd September 2025']
    subject = request.form['Data Structures']
    duration = request.form['1']
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

if 1:
    print("No data available to plot for weekly study hours.")
