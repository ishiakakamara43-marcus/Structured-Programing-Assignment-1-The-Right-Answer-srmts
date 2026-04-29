# ============================================================
# PROG103 - PRINCIPLES OF STRUCTURED PROGRAMMING
# Assignment 1: Attendance Tracking System (ATS)
# Student: [Your Name] | ID: [Your Student ID]
# Limkokwing University of Creative Technology - Sierra Leone
# Semester 02 | March 2026 - July 2026
# SDG Alignment: SDG 4 - Quality Education
# ============================================================

# ---------- CONSTANTS ----------
SCHOOL_NAME = "Limkokwing University - Sierra Leone"
SYSTEM_NAME = "Attendance Tracking System (ATS)"
PASS_THRESHOLD = 75.0   # Minimum attendance % to avoid warning

# ---------- GLOBAL STORAGE ----------
students = []   # List of student attendance records


# ============================================================
# FUNCTION 1: Display the main menu
# ============================================================
def display_menu():
    print("\n" + "=" * 55)
    print(f"   {SCHOOL_NAME}")
    print(f"   {SYSTEM_NAME}")
    print("=" * 55)
    print("  1. Add Student Record")
    print("  2. Mark Attendance")
    print("  3. View Student Attendance Report")
    print("  4. View All Students Summary")
    print("  5. Search Student by ID")
    print("  6. Exit")
    print("=" * 55)


# ============================================================
# FUNCTION 2: Add a new student
# ============================================================
def add_student():
    print("\n--- ADD STUDENT RECORD ---")
    student_id = input("Enter Student ID   : ").strip().upper()

    # Check for duplicate ID
    for s in students:
        if s["id"] == student_id:
            print(f"[!] Student ID '{student_id}' already exists.")
            return

    name = input("Enter Student Name : ").strip().title()
    course = input("Enter Course Name  : ").strip().title()

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "total_classes": 0,
        "attended": 0,
        "attendance_log": []   # List of ("date", "status") tuples
    }

    students.append(student)
    print(f"\n[✓] Student '{name}' (ID: {student_id}) added successfully.")


# ============================================================
# FUNCTION 3: Mark attendance for a student
# ============================================================
def mark_attendance():
    if len(students) == 0:
        print("\n[!] No students found. Please add students first.")
        return

    print("\n--- MARK ATTENDANCE ---")
    student_id = input("Enter Student ID : ").strip().upper()
    student = find_student(student_id)

    if student is None:
        print(f"[!] Student ID '{student_id}' not found.")
        return

    date = input("Enter Date (DD/MM/YYYY) : ").strip()

    # Check for duplicate date entry
    for log in student["attendance_log"]:
        if log[0] == date:
            print(f"[!] Attendance for {date} already recorded.")
            return

    print("Mark Status - Enter 'P' for Present, 'A' for Absent: ", end="")
    status_input = input().strip().upper()

    if status_input == "P":
        status = "Present"
        student["attended"] += 1
    elif status_input == "A":
        status = "Absent"
    else:
        print("[!] Invalid input. Please enter 'P' or 'A'.")
        return

    student["total_classes"] += 1
    student["attendance_log"].append((date, status))

    print(f"\n[✓] Attendance marked: {student['name']} | {date} | {status}")


# ============================================================
# FUNCTION 4: Calculate attendance percentage
# ============================================================
def calculate_percentage(attended, total):
    if total == 0:
        return 0.0
    return (attended / total) * 100


# ============================================================
# FUNCTION 5: View detailed attendance report for one student
# ============================================================
def view_student_report():
    if len(students) == 0:
        print("\n[!] No student records available.")
        return

    print("\n--- STUDENT ATTENDANCE REPORT ---")
    student_id = input("Enter Student ID : ").strip().upper()
    student = find_student(student_id)

    if student is None:
        print(f"[!] Student ID '{student_id}' not found.")
        return

    percentage = calculate_percentage(student["attended"], student["total_classes"])

    print("\n" + "-" * 45)
    print(f"  Name    : {student['name']}")
    print(f"  ID      : {student['id']}")
    print(f"  Course  : {student['course']}")
    print("-" * 45)
    print(f"  {'Date':<15} {'Status':<10}")
    print("-" * 45)

    if len(student["attendance_log"]) == 0:
        print("  No attendance records yet.")
    else:
        for log in student["attendance_log"]:
            print(f"  {log[0]:<15} {log[1]:<10}")

    print("-" * 45)
    print(f"  Total Classes : {student['total_classes']}")
    print(f"  Attended      : {student['attended']}")
    print(f"  Attendance %  : {percentage:.2f}%")

    # Decision structure: attendance warning
    if student["total_classes"] == 0:
        print("  Status        : No data yet")
    elif percentage >= PASS_THRESHOLD:
        print(f"  Status        : [✓] GOOD STANDING")
    elif percentage >= 50:
        print(f"  Status        : [⚠] AT RISK - Attendance below {PASS_THRESHOLD}%")
    else:
        print(f"  Status        : [✗] CRITICAL - Risk of academic penalty")

    print("-" * 45)


# ============================================================
# FUNCTION 6: View summary of ALL students
# ============================================================
def view_all_students():
    if len(students) == 0:
        print("\n[!] No student records available.")
        return

    print("\n--- ALL STUDENTS SUMMARY ---")
    print("-" * 70)
    print(f"  {'ID':<10} {'Name':<20} {'Course':<18} {'%':<8} {'Status'}")
    print("-" * 70)

    for s in students:
        pct = calculate_percentage(s["attended"], s["total_classes"])

        if s["total_classes"] == 0:
            status = "No Data"
        elif pct >= PASS_THRESHOLD:
            status = "Good"
        elif pct >= 50:
            status = "At Risk"
        else:
            status = "Critical"

        print(f"  {s['id']:<10} {s['name']:<20} {s['course']:<18} {pct:<8.1f} {status}")

    print("-" * 70)
    print(f"  Total Students: {len(students)}")
    print("-" * 70)


# ============================================================
# FUNCTION 7: Search student by ID (helper)
# ============================================================
def find_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None


# ============================================================
# FUNCTION 8: Search student by ID (user-facing)
# ============================================================
def search_student():
    print("\n--- SEARCH STUDENT ---")
    student_id = input("Enter Student ID to search : ").strip().upper()
    student = find_student(student_id)

    if student is None:
        print(f"[!] No student found with ID '{student_id}'.")
    else:
        pct = calculate_percentage(student["attended"], student["total_classes"])
        print("\n[✓] Student Found:")
        print(f"  Name    : {student['name']}")
        print(f"  ID      : {student['id']}")
        print(f"  Course  : {student['course']}")
        print(f"  Classes : {student['total_classes']} | Attended: {student['attended']}")
        print(f"  Attendance: {pct:.2f}%")


# ============================================================
# MAIN PROGRAM - Entry Point
# ============================================================
def main():
    print(f"\nWelcome to the {SYSTEM_NAME}")
    print(f"Powered by {SCHOOL_NAME}")
    print("SDG 4 - Quality Education: Promoting accountability in education.\n")

    running = True

    while running:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            view_all_students()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("\n[✓] Thank you for using ATS. Goodbye!\n")
            running = False
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()