from pathlib import Path
import pandas as pd
from functions import analyze_students, show_summary

BASE = Path(__file__).resolve().parent

def main():
    students = pd.read_csv(BASE / 'students.csv')
    print('DATASET:', len(students), 'records')
    print('COLUMNS:', ', '.join(students.columns))
    print('\nFIRST FIVE RECORDS')
    print(students.head().to_string(index=False))
    results = analyze_students(students)
    print('\nSTUDENT RESULTS')
    print(results[['Student ID','Name','Total','Average','Grade','Result']].to_string(index=False))
    show_summary(results)
    results.to_csv(BASE / 'student_results.csv', index=False)
    print('\nSaved student_results.csv')

if __name__ == '__main__':
    main()
