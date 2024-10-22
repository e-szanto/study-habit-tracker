import matplotlib.pyplot as plt
import pandas as pd

def plot_weekly_study_hours(file_path='data/study_sessions.csv'):
    # Load study session data from CSV
    df = pd.read_csv(file_path, header=None, names=['date', 'subject', 'duration', 'notes'])
    df['date'] = pd.to_datetime(df['date'])
    
    # Ensure the 'duration' column is numeric (set errors='coerce' to handle non-numeric values)
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    
    # Drop rows where duration is NaN (caused by non-numeric values)
    df = df.dropna(subset=['duration'])
    
    # Group by week and sum up study hours
    df['week'] = df['date'].dt.strftime('%Y-%U')  # Year and week number
    weekly_hours = df.groupby('week')['duration'].sum()
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    weekly_hours.plot(kind='line', marker='o')
    plt.title('Weekly Study Hours')
    plt.xlabel('Week')
    plt.ylabel('Total Hours')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def plot_study_time_by_subject(file_path='data/study_sessions.csv'):
    # Load study session data from CSV
    df = pd.read_csv(file_path, header=None, names=['date', 'subject', 'duration', 'notes'])
    
    # Ensure the 'duration' column is numeric (set errors='coerce' to handle non-numeric values)
    df['duration'] = pd.to_numeric(df['duration'], errors='coerce')
    
    # Drop rows where duration is NaN (caused by non-numeric values)
    df = df.dropna(subset=['duration'])
    
    # Group by subject and sum up study hours
    subject_hours = df.groupby('subject')['duration'].sum()
    
    # Plot the data
    plt.figure(figsize=(10, 5))
    subject_hours.plot(kind='bar', color='skyblue')
    plt.title('Study Time by Subject')
    plt.xlabel('Subject')
    plt.ylabel('Total Hours')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

