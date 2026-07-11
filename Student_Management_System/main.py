"""
Student Management System
--------------------------
A simple console-based Student Management System built for a
BBA Summer Internship project.

This program collects a student's personal details and marks
in 5 subjects, then calculates:
    - Total Marks
    - Percentage
    - Pass / Fail status
    - Grade (A, B, C, D, F)

It then displays everything in a neatly formatted report.

Author : Rohit Kumar
Python Version : 3.13 compatible
No external libraries used.
"""

# ---------------------------------------------------------------
# CONSTANT VALUES USED THROUGHOUT THE PROGRAM
# ---------------------------------------------------------------
NUMBER_OF_SUBJECTS = 5      # We are recording marks for 5 subjects
MAX_MARKS_PER_SUBJECT = 100 # Each subject is out of 100 marks
PASSING_MARKS = 33          # Minimum marks required to pass a subject


# ---------------------------------------------------------------
# FUNCTION: get_non_empty_string
# ---------------------------------------------------------------
def get_non_empty_string(prompt_message):
    """
    Keeps asking the user for input until they type something
    that is not empty (i.e., not just blank spaces).

    Parameters:
        prompt_message (str): The message shown to the user.

    Returns:
        str: A valid, non-empty string typed by the user.
    """
    while True:
        user_input = input(prompt_message).strip()
        if user_input == "":
            print("This field cannot be empty. Please try again.\n")
        else:
            return user_input


# ---------------------------------------------------------------
# FUNCTION: get_valid_integer
# ---------------------------------------------------------------
def get_valid_integer(prompt_message, min_value=None, max_value=None):
    """
    Asks the user to enter a whole number (integer) and keeps
    asking until a valid number is entered. Optionally checks
    that the number is within a given range.

    Parameters:
        prompt_message (str): The message shown to the user.
        min_value (int or None): Smallest acceptable value (optional).
        max_value (int or None): Largest acceptable value (optional).

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        user_input = input(prompt_message).strip()
        try:
            value = int(user_input)  # Try converting text to a number

            # Check the lower limit, if one was given
            if min_value is not None and value < min_value:
                print(f"Value must be {min_value} or more. Please try again.\n")
                continue

            # Check the upper limit, if one was given
            if max_value is not None and value > max_value:
                print(f"Value must be {max_value} or less. Please try again.\n")
                continue

            return value  # If all checks pass, return the number

        except ValueError:
            # This runs if the user typed something that is not a number
            print("Invalid input. Please enter a whole number (e.g., 18, 75).\n")


# ---------------------------------------------------------------
# FUNCTION: get_student_details
# ---------------------------------------------------------------
def get_student_details():
    """
    Collects the student's basic personal details from the user.

    Returns:
        dict: A dictionary containing name, age, college,
              course, and roll number.
    """
    print("\n----- ENTER STUDENT DETAILS -----")

    name = get_non_empty_string("Enter Student Name: ")
    age = get_valid_integer("Enter Age: ", min_value=1, max_value=100)
    college = get_non_empty_string("Enter College Name: ")
    course = get_non_empty_string("Enter Course Name: ")
    roll_number = get_non_empty_string("Enter Roll Number: ")

    # We store all details together in a dictionary for easy access later
    student_details = {
        "name": name,
        "age": age,
        "college": college,
        "course": course,
        "roll_number": roll_number
    }

    return student_details


# ---------------------------------------------------------------
# FUNCTION: get_marks
# ---------------------------------------------------------------
def get_marks(number_of_subjects):
    """
    Collects marks for each subject from the user, making sure
    each mark is a valid number between 0 and MAX_MARKS_PER_SUBJECT.

    Parameters:
        number_of_subjects (int): How many subjects to ask marks for.

    Returns:
        list: A list of integers representing marks in each subject.
    """
    print(f"\n----- ENTER MARKS (out of {MAX_MARKS_PER_SUBJECT}) -----")

    marks_list = []
    for subject_number in range(1, number_of_subjects + 1):
        prompt = f"Enter marks for Subject {subject_number}: "
        marks = get_valid_integer(prompt, min_value=0, max_value=MAX_MARKS_PER_SUBJECT)
        marks_list.append(marks)

    return marks_list


# ---------------------------------------------------------------
# FUNCTION: calculate_total_marks
# ---------------------------------------------------------------
def calculate_total_marks(marks_list):
    """
    Adds up all the marks in the list to get the total.

    Parameters:
        marks_list (list): List of marks for each subject.

    Returns:
        int: The sum of all marks.
    """
    return sum(marks_list)


# ---------------------------------------------------------------
# FUNCTION: calculate_percentage
# ---------------------------------------------------------------
def calculate_percentage(total_marks, number_of_subjects):
    """
    Calculates the percentage based on total marks obtained.

    Parameters:
        total_marks (int): Sum of marks in all subjects.
        number_of_subjects (int): Number of subjects.

    Returns:
        float: Percentage rounded to 2 decimal places.
    """
    maximum_possible_marks = number_of_subjects * MAX_MARKS_PER_SUBJECT
    percentage = (total_marks / maximum_possible_marks) * 100
    return round(percentage, 2)


# ---------------------------------------------------------------
# FUNCTION: check_pass_fail
# ---------------------------------------------------------------
def check_pass_fail(marks_list):
    """
    Checks whether the student has passed or failed.
    A student PASSES only if EVERY subject has marks
    greater than or equal to PASSING_MARKS.

    Parameters:
        marks_list (list): List of marks for each subject.

    Returns:
        str: "Pass" or "Fail"
    """
    for marks in marks_list:
        if marks < PASSING_MARKS:
            return "Fail"   # Even one failing subject means overall Fail
    return "Pass"


# ---------------------------------------------------------------
# FUNCTION: calculate_grade
# ---------------------------------------------------------------
def calculate_grade(percentage, result):
    """
    Assigns a grade based on the percentage scored.
    If the student has failed, the grade is automatically "F".

    Grading Scale:
        90 and above      -> A
        75 to below 90     -> B
        60 to below 75      -> C
        33 to below 60      -> D
        Below 33 or Fail    -> F

    Parameters:
        percentage (float): The student's percentage.
        result (str): "Pass" or "Fail".

    Returns:
        str: Grade letter (A, B, C, D, or F).
    """
    if result == "Fail":
        return "F"

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 33:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------
# FUNCTION: display_report
# ---------------------------------------------------------------
def display_report(student_details, marks_list, total_marks, percentage, result, grade):
    """
    Prints a neatly formatted final report card showing all
    student details and calculated results.

    Parameters:
        student_details (dict): Student's personal details.
        marks_list (list): Marks obtained in each subject.
        total_marks (int): Sum of all marks.
        percentage (float): Percentage scored.
        result (str): "Pass" or "Fail".
        grade (str): Final grade letter.

    Returns:
        None
    """
    print("\n" + "=" * 45)
    print("           STUDENT REPORT CARD")
    print("=" * 45)
    print(f"Name         : {student_details['name']}")
    print(f"Age          : {student_details['age']}")
    print(f"College      : {student_details['college']}")
    print(f"Course       : {student_details['course']}")
    print(f"Roll Number  : {student_details['roll_number']}")
    print("-" * 45)
    print("SUBJECT-WISE MARKS")
    for index, marks in enumerate(marks_list, start=1):
        print(f"  Subject {index} : {marks} / {MAX_MARKS_PER_SUBJECT}")
    print("-" * 45)
    print(f"Total Marks  : {total_marks} / {NUMBER_OF_SUBJECTS * MAX_MARKS_PER_SUBJECT}")
    print(f"Percentage   : {percentage}%")
    print(f"Result       : {result}")
    print(f"Grade        : {grade}")
    print("=" * 45)


# ---------------------------------------------------------------
# FUNCTION: main
# ---------------------------------------------------------------
def main():
    """
    The main function that controls the overall flow of the program:
        1. Welcome the user
        2. Collect student details
        3. Collect marks
        4. Perform calculations
        5. Display the final report
        6. Ask if the user wants to process another student

    Returns:
        None
    """
    print("=" * 45)
    print("   WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    # This loop allows processing multiple students in one run
    while True:
        # Step 1: Get student's personal details
        student_details = get_student_details()

        # Step 2: Get marks for all subjects
        marks_list = get_marks(NUMBER_OF_SUBJECTS)

        # Step 3: Perform all calculations
        total_marks = calculate_total_marks(marks_list)
        percentage = calculate_percentage(total_marks, NUMBER_OF_SUBJECTS)
        result = check_pass_fail(marks_list)
        grade = calculate_grade(percentage, result)

        # Step 4: Display the final report card
        display_report(student_details, marks_list, total_marks, percentage, result, grade)

        # Step 5: Ask if user wants to enter another student's data
        again = input("\nDo you want to enter another student's record? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using the Student Management System. Goodbye!")
            break


# ---------------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------------
# This ensures main() only runs when this file is executed directly,
# not when it is imported as a module into another program.
if __name__ == "__main__":
    main()
