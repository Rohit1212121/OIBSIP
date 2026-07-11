# Student Management System

A simple console-based **Student Management System** built in Python, created
as a BBA Summer Internship project.

## 📌 Overview
This program allows a user to enter a student's personal details and marks
in 5 subjects. It then automatically calculates the **Total Marks**,
**Percentage**, **Pass/Fail status**, and **Grade**, and displays everything
in a neatly formatted report card.

## 🛠️ Requirements
- Python 3.13 (also works on Python 3.8+)
- No external libraries — uses only Python's built-in features.

## 📂 Project Structure
```
student_management_system/
│
├── main.py            # The complete program (all functions + main logic)
├── README.md           # Project documentation (this file)
└── sample_output.txt   # A sample run showing input and output
```

## ▶️ How to Run
1. Make sure Python 3 is installed on your computer.
2. Open a terminal / command prompt in the project folder.
3. Run the command:
   ```
   python main.py
   ```
4. Follow the on-screen prompts to enter student details and marks.

## 📋 Features
- Collects Student Name, Age, College Name, Course, and Roll Number.
- Collects marks for 5 subjects (out of 100 each).
- Validates all numeric input (rejects text, out-of-range numbers, etc.).
- Calculates:
  - **Total Marks** (sum of all 5 subjects)
  - **Percentage** (total marks out of the maximum possible)
  - **Pass/Fail** (a student must score 33 or more in *every* subject to pass)
  - **Grade**:
    | Percentage Range | Grade |
    |-------------------|-------|
    | 90 and above      | A     |
    | 75 – 89.99         | B     |
    | 60 – 74.99         | C     |
    | 33 – 59.99         | D     |
    | Below 33 or any Fail | F  |
- Displays a clean, formatted report card.
- Lets the user enter records for multiple students in one run.

## 🧩 Functions Used
| Function | Purpose |
|----------|---------|
| `get_non_empty_string()` | Makes sure the user doesn't leave a text field blank. |
| `get_valid_integer()` | Makes sure the user enters a proper whole number within a valid range. |
| `get_student_details()` | Collects all personal details of the student. |
| `get_marks()` | Collects marks for all 5 subjects. |
| `calculate_total_marks()` | Adds up all subject marks. |
| `calculate_percentage()` | Works out the percentage score. |
| `check_pass_fail()` | Decides whether the student passed or failed. |
| `calculate_grade()` | Assigns a letter grade based on percentage. |
| `display_report()` | Prints the final formatted report card. |
| `main()` | Controls the overall flow of the program. |

## 📄 License
This project is created for educational/internship purposes.
