# ==========================================
# Day 30 - Student Productivity Dashboard
# 30 Days Python GitHub Project Challenge
# ==========================================

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


DATABASE = "productivity.db"


# ==========================================
# Database Connection
# ==========================================

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


# ==========================================
# Create Table
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS productivity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    subject TEXT NOT NULL,
    study_hours REAL NOT NULL,
    tasks_completed INTEGER NOT NULL,
    productivity_score REAL NOT NULL
)
""")

connection.commit()


# ==========================================
# Add Productivity Record
# ==========================================

def add_record():

    print("\n======================================")
    print("       ADD PRODUCTIVITY RECORD")
    print("======================================")

    date = input("Enter date (YYYY-MM-DD): ").strip()
    subject = input("Enter subject: ").strip()

    try:

        study_hours = float(
            input("Enter study hours: ")
        )

        tasks_completed = int(
            input("Enter tasks completed: ")
        )

        productivity_score = float(
            input("Enter productivity score (0-100): ")
        )

    except ValueError:

        print("\n❌ Please enter valid numbers.")
        return

    if study_hours < 0:
        print("❌ Study hours cannot be negative.")
        return

    if tasks_completed < 0:
        print("❌ Tasks cannot be negative.")
        return

    if not 0 <= productivity_score <= 100:
        print("❌ Score must be between 0 and 100.")
        return

    cursor.execute("""
    INSERT INTO productivity
    (date, subject, study_hours, tasks_completed, productivity_score)
    VALUES (?, ?, ?, ?, ?)
    """, (
        date,
        subject,
        study_hours,
        tasks_completed,
        productivity_score
    ))

    connection.commit()

    print("\n✅ Productivity record added!")


# ==========================================
# Load Data
# ==========================================

def load_data():

    query = """
    SELECT
        date,
        subject,
        study_hours,
        tasks_completed,
        productivity_score
    FROM productivity
    """

    return pd.read_sql_query(
        query,
        connection
    )


# ==========================================
# View Records
# ==========================================

def view_records():

    data = load_data()

    print("\n======================================")
    print("       PRODUCTIVITY RECORDS")
    print("======================================")

    if data.empty:

        print("❌ No records available.")
        return

    print(data.to_string(index=False))


# ==========================================
# Productivity Summary
# ==========================================

def productivity_summary():

    data = load_data()

    if data.empty:

        print("\n❌ No data available.")
        return

    total_hours = data["study_hours"].sum()

    total_tasks = data["tasks_completed"].sum()

    average_score = data[
        "productivity_score"
    ].mean()

    best_score = data[
        "productivity_score"
    ].max()

    average_hours = data[
        "study_hours"
    ].mean()

    print("\n======================================")
    print("       PRODUCTIVITY SUMMARY")
    print("======================================")

    print(f"Total Study Hours : {total_hours:.2f}")
    print(f"Average Study Hours: {average_hours:.2f}")
    print(f"Tasks Completed   : {total_tasks}")
    print(f"Average Score     : {average_score:.2f}")
    print(f"Best Score        : {best_score:.2f}")

    print("======================================")


# ==========================================
# Subject Analysis
# ==========================================

def subject_analysis():

    data = load_data()

    if data.empty:

        print("\n❌ No data available.")
        return

    summary = (
        data
        .groupby("subject")
        .agg(
            study_hours=("study_hours", "sum"),
            tasks_completed=("tasks_completed", "sum"),
            average_score=("productivity_score", "mean")
        )
        .sort_values(
            "study_hours",
            ascending=False
        )
    )

    print("\n======================================")
    print("         SUBJECT ANALYSIS")
    print("======================================")

    print(summary)


# ==========================================
# Study Hours Chart
# ==========================================

def study_hours_chart():

    data = load_data()

    if data.empty:

        print("\n❌ No data available.")
        return

    summary = (
        data
        .groupby("subject")["study_hours"]
        .sum()
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        summary.index,
        summary.values,
        color="skyblue"
    )

    plt.xlabel("Subject")
    plt.ylabel("Study Hours")
    plt.title("Study Hours by Subject")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


# ==========================================
# Productivity Score Chart
# ==========================================

def productivity_chart():

    data = load_data()

    if data.empty:

        print("\n❌ No data available.")
        return

    plt.figure(figsize=(9, 5))

    plt.plot(
        range(len(data)),
        data["productivity_score"],
        marker="o"
    )

    plt.xlabel("Date")
    plt.ylabel("Productivity Score")
    plt.title("Productivity Score Trend")

    plt.xticks(range(len(data)), data["date"], rotation=45)

    plt.tight_layout()
    plt.show()


# ==========================================
# Tasks Chart
# ==========================================

def tasks_chart():

    data = load_data()

    if data.empty:

        print("\n❌ No data available.")
        return

    summary = (
        data
        .groupby("subject")["tasks_completed"]
        .sum()
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        summary.index,
        summary.values,
        color="lightcoral"
    )

    plt.xlabel("Subject")
    plt.ylabel("Tasks Completed")
    plt.title("Tasks Completed by Subject")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


# ==========================================
# Dashboard
# ==========================================

def dashboard():

    data = load_data()

    if data.empty:

        print("\n❌ No productivity data available.")
        return

    total_hours = data["study_hours"].sum()

    total_tasks = data["tasks_completed"].sum()

    average_score = data[
        "productivity_score"
    ].mean()

    print("\n")
    print("╔══════════════════════════════════════╗")
    print("║      STUDENT PRODUCTIVITY DASHBOARD ║")
    print("╠══════════════════════════════════════╣")

    print(
        f"║ Total Study Hours : "
        f"{total_hours:<15.2f} ║"
    )

    print(
        f"║ Tasks Completed   : "
        f"{total_tasks:<15} ║"
    )

    print(
        f"║ Average Score     : "
        f"{average_score:<15.2f} ║"
    )

    print("╚══════════════════════════════════════╝")

    print("\n📚 Subject Performance:")

    subject_data = (
        data
        .groupby("subject")
        .agg(
            Hours=("study_hours", "sum"),
            Tasks=("tasks_completed", "sum"),
            Score=("productivity_score", "mean")
        )
    )

    print(subject_data)


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n======================================")
    print("     STUDENT PRODUCTIVITY SYSTEM")
    print("======================================")

    print("1. Add Productivity Record")
    print("2. View Records")
    print("3. Productivity Summary")
    print("4. Subject Analysis")
    print("5. Study Hours Chart")
    print("6. Productivity Score Chart")
    print("7. Tasks Chart")
    print("8. Dashboard")
    print("9. Exit")

    print("======================================")

    choice = input(
        "Enter your choice (1-9): "
    )

    if choice == "1":

        add_record()

    elif choice == "2":

        view_records()

    elif choice == "3":

        productivity_summary()

    elif choice == "4":

        subject_analysis()

    elif choice == "5":

        study_hours_chart()

    elif choice == "6":

        productivity_chart()

    elif choice == "7":

        tasks_chart()

    elif choice == "8":

        dashboard()

    elif choice == "9":

        connection.close()

        print("\n======================================")
        print("    🎉 CHALLENGE COMPLETED! 🎉")
        print("======================================")
        print("Congratulations on completing")
        print("30 Days of Python Projects!")
        print("======================================")

        break

    else:

        print("\n❌ Invalid choice! Please select 1-9.")