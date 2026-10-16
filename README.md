# Student Performance Analytics System

## Objective
Analyze student academic performance using Python, NumPy, and Pandas.

## Dataset
20 fictional student records with ID, name, department, four subject marks (out of 100), and attendance percentage. Replace sample data with your own permitted records if needed.

## Features
- CSV loading and validation with Pandas
- NumPy totals and student averages
- Pass/fail: **Pass only if every subject mark is at least 40**
- Grades based on average for passing students: A+ >=90, A >=80, B >=70, C >=60, D >=50, E otherwise; F for failed students
- Highest, lowest, and class average
- Subject-wise average and top five students
- Export detailed results to `student_results.csv`

Attendance is displayed as dataset information; it is not part of the pass/fail rule in this implementation.

## Run locally
```bash
python -m pip install -r requirements.txt
python main.py
```

## Project files
- `main.py`: program entry point
- `functions.py`: analysis and summary functions
- `students.csv`: example dataset
- `requirements.txt`: dependencies
- `Project_Documentation.md`: assignment documentation

## Technologies and concepts
Python, NumPy, Pandas, variables, conditions, loops, functions, and data analysis.

## GitHub submission
Create a repository, push the source files, and submit its URL using the course's Google Form. Verify the repository contents before submission.
