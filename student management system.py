"""
========================================================
  Student Result Management Terminal System (SRMTS)
  Course: PROG103 - Principles of Structured Programming
  Limkokwing University of Creative Technology - Sierra Leone
  Semester: 02 | March 2026 - July 2026
========================================================
"""

# ──────────────────────────────────────────
#  CONSTANTS
# ──────────────────────────────────────────
GRADE_BOUNDARIES = {
    "A": (80, 100),
    "B": (70, 79),
    "C": (60, 69),
    "D": (50, 59),
    "F": (0,  49),
}

PASSING_SCORE = 50
APP_NAME = "Student Result Management Terminal System (SRMTS)"

# ──────────────────────────────────────────
#  FUNCTION: Display banner
# ──────────────────────────────────────────
def display_banner():
    """Displays the application header banner."""
    print("=" * 60)
    print(f"  {APP_NAME}")
    print("  Limkokwing University - Sierra Leone")
    print("=" * 60)


# ──────────────────────────────────────────
#  FUNCTION: Calculate grade from score
# ──────────────────────────────────────────
def calculate_grade(score):
    """
    Determines the letter grade based on a numeric score.
    Uses if/elif/else decision structures.
    Returns the grade letter as a string.
    """
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade


# ──────────────────────────────────────────
#  FUNCTION: Calculate average of scores
# ──────────────────────────────────────────
def calculate_average(scores):
    """
    Calculates the average of a list of numeric scores.
    Uses iteration (loop) to sum all values.
    Returns the average as a float.
    """
    total = 0.0
    for score in scores:
        total += score
    if len(scores) == 0:
        return 0.0
    return total / len(scores)


# ──────────────────────────────────────────
#  FUNCTION: Input student record
# ──────────────────────────────────────────
def input_student():
    """
    Prompts the user to enter one student's details.
    Accepts name and scores for 3 subjects.
    Returns a dictionary containing the student record.
    """
    print("\n" + "-" * 40)
    print("  ENTER STUDENT DETAILS")
    print("-" * 40)

    name = input("  Student Name   : ").strip()
    student_id = input("  Student ID     : ").strip()

    subjects = ["Mathematics", "English", "ICT"]
    scores = []

    for subject in subjects:
        while True:
            try:
                score = float(input(f"  Score for {subject} (0-100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("  ⚠  Score must be between 0 and 100. Try again.")
            except ValueError:
                print("  ⚠  Invalid input. Please enter a number.")

    # Build student record dictionary
    student = {
        "name": name,
        "id": student_id,
        "subjects": subjects,
        "scores": scores,
    }
    return student


# ──────────────────────────────────────────
#  FUNCTION: Process and display one result
# ──────────────────────────────────────────
def display_result(student):
    """
    Processes a student record: computes average, grade, pass/fail.
    Displays a formatted result card in the terminal.
    """
    avg = calculate_average(student["scores"])
    grade = calculate_grade(avg)

    if avg >= PASSING_SCORE:
        status = "PASS ✓"
    else:
        status = "FAIL  ✗"

    print("\n" + "=" * 45)
    print("         STUDENT RESULT CARD")
    print("=" * 45)
    print(f"  Name       : {student['name']}")
    print(f"  Student ID : {student['id']}")
    print("-" * 45)
    print(f"  {'Subject':<18}  {'Score':>6}  {'Grade':>6}")
    print("-" * 45)

    # Loop through each subject and display per-subject grade
    for i in range(len(student["subjects"])):
        subj = student["subjects"][i]
        sc = student["scores"][i]
        gr = calculate_grade(sc)
        print(f"  {subj:<18}  {sc:>6.1f}  {gr:>6}")

    print("-" * 45)
    print(f"  {'Average':<18}  {avg:>6.1f}  {grade:>6}")
    print("=" * 45)
    print(f"  Overall Status : {status}")
    print("=" * 45)


# ──────────────────────────────────────────
#  FUNCTION: Display class summary
# ──────────────────────────────────────────
def display_summary(all_students):
    """
    Iterates over all entered students and displays a summary table.
    Also reports class average, highest, and lowest scores.
    """
    if len(all_students) == 0:
        print("\n  No student records found.")
        return

    print("\n" + "=" * 60)
    print("              CLASS SUMMARY REPORT")
    print("=" * 60)
    print(f"  {'#':<4} {'Name':<20} {'Average':>8}  {'Grade':>6}  {'Status':>6}")
    print("-" * 60)

    averages = []
    pass_count = 0
    fail_count = 0

    for idx, student in enumerate(all_students):
        avg = calculate_average(student["scores"])
        grade = calculate_grade(avg)
        averages.append(avg)

        if avg >= PASSING_SCORE:
            status = "PASS"
            pass_count += 1
        else:
            status = "FAIL"
            fail_count += 1

        print(f"  {idx+1:<4} {student['name']:<20} {avg:>8.1f}  {grade:>6}  {status:>6}")

    print("-" * 60)
    class_avg = calculate_average(averages)
    highest = max(averages)
    lowest = min(averages)

    print(f"\n  Total Students   : {len(all_students)}")
    print(f"  Passed           : {pass_count}")
    print(f"  Failed           : {fail_count}")
    print(f"  Class Average    : {class_avg:.1f}")
    print(f"  Highest Average  : {highest:.1f}")
    print(f"  Lowest Average   : {lowest:.1f}")
    print("=" * 60)


# ──────────────────────────────────────────
#  FUNCTION: Main menu
# ──────────────────────────────────────────
def main_menu():
    """Displays the main menu and returns the user's choice."""
    print("\n" + "-" * 40)
    print("  MAIN MENU")
    print("-" * 40)
    print("  1. Add Student Record")
    print("  2. View All Results")
    print("  3. View Class Summary")
    print("  4. Exit")
    print("-" * 40)
    choice = input("  Enter your choice (1-4): ").strip()
    return choice


# ──────────────────────────────────────────
#  MAIN PROGRAM ENTRY POINT
# ──────────────────────────────────────────
def main():
    """
    Main function: controls program flow using a loop and menu.
    Stores all student records in a list (all_students).
    """
    display_banner()
    all_students = []  # List to hold all student records (data structure)

    running = True  # Boolean constant for loop control

    while running:
        choice = main_menu()

        if choice == "1":
            student = input_student()
            all_students.append(student)
            display_result(student)
            print("\n  ✓ Record saved successfully.")

        elif choice == "2":
            if len(all_students) == 0:
                print("\n  ⚠  No records yet. Please add a student first.")
            else:
                print(f"\n  Showing results for {len(all_students)} student(s)...\n")
                for student in all_students:
                    display_result(student)

        elif choice == "3":
            display_summary(all_students)

        elif choice == "4":
            print("\n  Thank you for using SRMTS. Goodbye!\n")
            running = False

        else:
            print("\n  ⚠  Invalid choice. Please enter 1, 2, 3, or 4.")


# ──────────────────────────────────────────
#  Run the program
# ──────────────────────────────────────────
if __name__ == "__main__":
    main()