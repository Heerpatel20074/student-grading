students = {}

def add_student():
    name = input("Enter student's name: ").strip().title()
    try:
        marks = float(input("Enter marks out of 100: "))
        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid numeric marks.")
        return

    grade = assign_grade(marks)
    students[name] = {'marks': marks, 'grade': grade}
    print(f"Student {name} added with Grade '{grade}'.")

def assign_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def view_all_students():
    if not students:
        print("No students found.")
        return

    print("\nReport Card:")
    print(f"{'Name':<20}{'Marks':<10}{'Grade'}")
    print("-" * 35)
    for name, info in students.items():
        print(f"{name:<20}{info['marks']:<10}{info['grade']}")



while True:
    print("\nStudent Grading System Menu:")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid option (1-3).")
        continue

    if choice == 1:
        add_student()
    elif choice == 2:
        view_all_students()
    elif choice == 3:
        print("Exiting... Bye!")
        break
    else:
        print("Invalid option. Choose from 1 to 3.")
