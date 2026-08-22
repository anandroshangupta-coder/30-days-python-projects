# ==========================================
# Day 15 - Student Grade Management System
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("     STUDENT GRADE MANAGEMENT SYSTEM")
print("======================================")

# Store students
students = {}


# Add student
def add_student():
    name = input("\nEnter student name: ")
    
    try:
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("❌ Marks must be between 0 and 100.")
            return

        students[name] = {
            "marks": marks,
            "grade": calculate_grade(marks)
        }

        print("✅ Student added successfully!")

    except ValueError:
        print("❌ Please enter valid marks.")


# Calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 50:
        return "D"

    elif marks >= 40:
        return "E"

    else:
        return "F"


# View students
def view_students():

    print("\n======================================")
    print("          STUDENT RECORDS")
    print("======================================")

    if not students:
        print("No student records found.")
        return

    for number, (name, details) in enumerate(students.items(), start=1):

        print(f"\n{number}. Student")
        print(f"Name  : {name}")
        print(f"Marks : {details['marks']:.2f}")
        print(f"Grade : {details['grade']}")

    print("======================================")


# Search student
def search_student():

    name = input("\nEnter student name: ")

    if name in students:

        student = students[name]

        print("\n======================================")
        print("          STUDENT FOUND")
        print("======================================")
        print(f"Name  : {name}")
        print(f"Marks : {student['marks']:.2f}")
        print(f"Grade : {student['grade']}")
        print("======================================")

    else:
        print("❌ Student not found.")


# Update student
def update_student():

    name = input("\nEnter student name to update: ")

    if name not in students:
        print("❌ Student not found.")
        return

    try:
        marks = float(input("Enter new marks (0-100): "))

        if marks < 0 or marks > 100:
            print("❌ Marks must be between 0 and 100.")
            return

        students[name]["marks"] = marks
        students[name]["grade"] = calculate_grade(marks)

        print("✅ Student record updated successfully!")

    except ValueError:
        print("❌ Please enter valid marks.")


# Delete student
def delete_student():

    name = input("\nEnter student name to delete: ")

    if name in students:

        del students[name]

        print("✅ Student deleted successfully!")

    else:
        print("❌ Student not found.")


# Display class statistics
def show_statistics():

    if not students:
        print("\n❌ No student records available.")
        return

    marks_list = []

    for student in students.values():
        marks_list.append(student["marks"])

    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)

    print("\n======================================")
    print("          CLASS STATISTICS")
    print("======================================")
    print(f"Total Students : {len(students)}")
    print(f"Average Marks  : {average:.2f}")
    print(f"Highest Marks  : {highest:.2f}")
    print(f"Lowest Marks   : {lowest:.2f}")
    print("======================================")


# Main menu
while True:

    print("\nChoose an option:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")
        break

    else:
        print("❌ Invalid choice! Please select 1-7.")