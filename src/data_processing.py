import csv

def save_study_session(data, file_path='data/study_sessions.csv'):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def load_study_sessions(file_path='data/study_sessions.csv'):
    sessions = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        sessions = list(reader)
    return sessions
