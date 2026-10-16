import numpy as np
import pandas as pd

SUBJECTS = ['Python', 'Mathematics', 'Statistics', 'English']

def grade(average, passed):
    if not passed:
        return 'F'
    if average >= 90: return 'A+'
    if average >= 80: return 'A'
    if average >= 70: return 'B'
    if average >= 60: return 'C'
    if average >= 50: return 'D'
    return 'E'

def analyze_students(df):
    required = ['Student ID', 'Name', 'Department', 'Attendance'] + SUBJECTS
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {missing}')
    if df['Student ID'].duplicated().any():
        raise ValueError('Student IDs must be unique')
    df = df.copy()
    for col in SUBJECTS + ['Attendance']:
        df[col] = pd.to_numeric(df[col], errors='raise')
        if not df[col].between(0, 100).all():
            raise ValueError(f'{col} must be between 0 and 100')
    marks = df[SUBJECTS].to_numpy(dtype=float)
    df['Total'] = np.sum(marks, axis=1)
    df['Average'] = np.mean(marks, axis=1).round(2)
    df['Result'] = np.where((marks >= 40).all(axis=1), 'Pass', 'Fail')
    df['Grade'] = [grade(avg, result == 'Pass') for avg, result in zip(df['Average'], df['Result'])]
    return df

def show_summary(df):
    print('\nCLASS SUMMARY')
    print('Students:', len(df))
    print('Passed:', int((df['Result'] == 'Pass').sum()))
    print('Failed:', int((df['Result'] == 'Fail').sum()))
    print('Class average:', round(float(np.mean(df['Average'])), 2))
    print('Highest student average:', df['Average'].max())
    print('Lowest student average:', df['Average'].min())
    print('\nSUBJECT-WISE AVERAGES')
    print(df[SUBJECTS].mean().round(2).to_string())
    print('\nTOP 5 STUDENTS')
    print(df.nlargest(5, 'Average')[['Student ID','Name','Average','Grade','Result']].to_string(index=False))
