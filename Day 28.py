# ==========================================
# Day 28 - Attendance Management System
# 30 Days Python GitHub Project Challenge
# ==========================================

import csv
import os
from datetime import date


FILE_NAME = "attendance.csv"


print("======================================")
print("      ATTENDANCE MANAGEMENT SYSTEM")
print("======================================")


# ==========================================
# Create CSV File
# ==========================================

def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Roll No",
                "Name",
                "Status"
            ])


# ==========================================
# Mark Attendance
# ==========================================

def mark_attendance():

    roll_no = input("\nEnter roll number: ").strip()
    name = input("Enter student name: ").strip()

    print("\n1. Present")
    print("2. Absent")

    choice = input("Enter attendance status: ")

    if choice == "1":
        status = "Present"

    elif choice == "2":
        status = "Absent"

    else:
        print("❌ Invalid choice.")
        return

    today = date.today()

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            today,
            roll_no,
            name,
            status
        ])

    print("\n✅ Attendance marked successfully!")


# ==========================================
# View Attendance
# ==========================================

def view_attendance():

    print("\n======================================")
    print("          ATTENDANCE RECORDS")
    print("======================================")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        records = list(reader)

    if not records:

        print("❌ No attendance records found.")
        return

    for record in records:

        print(
            f"\nDate     : {record['Date']}"
        )

        print(
            f"Roll No  : {record['Roll No']}"
        )

        print(
            f"Name     : {record['Name']}"
        )

        print(
            f"Status   : {record['Status']}"
        )

        print("--------------------------------------")


# ==========================================
# Search Student
# ==========================================

def search_student():

    roll_no = input(
        "\nEnter student roll number: "
    ).strip()

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        records = list(reader)

    student_records = [
        record
        for record in records
        if record["Roll No"] == roll_no
    ]

    if not student_records:

        print("\n❌ Student record not found.")
        return

    print("\n======================================")
    print("         STUDENT ATTENDANCE")
    print("======================================")

    name = student_records[0]["Name"]

    present = sum(
        1
        for record in student_records
        if record["Status"] == "Present"
    )

    absent = sum(
        1
        for record in student_records
        if record["Status"] == "Absent"
    )

    total = present + absent

    percentage = (
        present / total * 100
        if total > 0
        else 0
    )

    print(f"Roll No          : {roll_no}")
    print(f"Name             : {name}")
    print(f"Total Classes    : {total}")
    print(f"Present          : {present}")
    print(f"Absent           : {absent}")
    print(f"Attendance       : {percentage:.2f}%")

    print("======================================")


# ==========================================
# Attendance Summary
# ==========================================

def attendance_summary():

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        records = list(reader)

    if not records:

        print("\n❌ No attendance records available.")
        return

    total_classes = len(records)

    present = sum(
        1
        for record in records
        if record["Status"] == "Present"
    )

    absent = sum(
        1
        for record in records
        if record["Status"] == "Absent"
    )

    percentage = present / total_classes * 100

    print("\n======================================")
    print("        ATTENDANCE SUMMARY")
    print("======================================")

    print(f"Total Records : {total_classes}")
    print(f"Present       : {present}")
    print(f"Absent        : {absent}")
    print(f"Attendance    : {percentage:.2f}%")

    print("======================================")


# ==========================================
# Main Program
# ==========================================

create_file()


while True:

    print("\n======================================")
    print("          ATTENDANCE MENU")
    print("======================================")

    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Search Student")
    print("4. Attendance Summary")
    print("5. Exit")

    print("======================================")

    choice = input(
        "Enter your choice (1-5): "
    )

    if choice == "1":

        mark_attendance()

    elif choice == "2":

        view_attendance()

    elif choice == "3":

        search_student()

    elif choice == "4":

        attendance_summary()

    elif choice == "5":

        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")

        break

    else:

        print(
            "\n❌ Invalid choice! "
            "Please select 1-5."
        )