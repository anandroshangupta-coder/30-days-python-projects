# ==========================================
# Day 29 - Job Application Tracker
# 30 Days Python GitHub Project Challenge
# ==========================================

import sqlite3
from datetime import date


DATABASE = "job_applications.db"


# ==========================================
# Database Connection
# ==========================================

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()


# ==========================================
# Create Table
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    location TEXT,
    status TEXT NOT NULL,
    applied_date TEXT NOT NULL,
    notes TEXT
)
""")

connection.commit()


# ==========================================
# Add Application
# ==========================================

def add_application():

    print("\n======================================")
    print("        ADD JOB APPLICATION")
    print("======================================")

    company = input("Company name: ").strip()
    position = input("Job position: ").strip()
    location = input("Location: ").strip()

    print("\nStatus:")
    print("1. Applied")
    print("2. Interview")
    print("3. Selected")
    print("4. Rejected")

    choice = input("Choose status: ")

    status_list = {
        "1": "Applied",
        "2": "Interview",
        "3": "Selected",
        "4": "Rejected"
    }

    if choice not in status_list:
        print("❌ Invalid status.")
        return

    status = status_list[choice]

    notes = input("Notes: ").strip()

    applied_date = str(date.today())

    cursor.execute("""
    INSERT INTO applications
    (company, position, location, status, applied_date, notes)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        company,
        position,
        location,
        status,
        applied_date,
        notes
    ))

    connection.commit()

    print("\n✅ Job application added successfully!")


# ==========================================
# View Applications
# ==========================================

def view_applications():

    print("\n======================================")
    print("        ALL JOB APPLICATIONS")
    print("======================================")

    cursor.execute("""
    SELECT * FROM applications
    ORDER BY id DESC
    """)

    applications = cursor.fetchall()

    if not applications:
        print("❌ No applications found.")
        return

    for app in applications:

        print(f"""
ID           : {app[0]}
Company      : {app[1]}
Position     : {app[2]}
Location     : {app[3]}
Status       : {app[4]}
Applied Date : {app[5]}
Notes        : {app[6]}
--------------------------------------
""")


# ==========================================
# Search Application
# ==========================================

def search_application():

    keyword = input(
        "\nEnter company or position: "
    ).strip()

    cursor.execute("""
    SELECT * FROM applications
    WHERE company LIKE ?
       OR position LIKE ?
    """, (
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    applications = cursor.fetchall()

    if not applications:

        print("\n❌ No matching applications found.")
        return

    print("\n======================================")
    print("          SEARCH RESULTS")
    print("======================================")

    for app in applications:

        print(
            f"ID: {app[0]} | "
            f"Company: {app[1]} | "
            f"Position: {app[2]} | "
            f"Status: {app[4]}"
        )


# ==========================================
# Update Status
# ==========================================

def update_status():

    try:
        application_id = int(
            input("\nEnter application ID: ")
        )
    except ValueError:
        print("❌ Enter a valid ID.")
        return

    print("\n1. Applied")
    print("2. Interview")
    print("3. Selected")
    print("4. Rejected")

    choice = input("Choose new status: ")

    status_list = {
        "1": "Applied",
        "2": "Interview",
        "3": "Selected",
        "4": "Rejected"
    }

    if choice not in status_list:
        print("❌ Invalid status.")
        return

    new_status = status_list[choice]

    cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?
    """, (
        new_status,
        application_id
    ))

    connection.commit()

    if cursor.rowcount == 0:
        print("❌ Application not found.")
    else:
        print("✅ Status updated successfully!")


# ==========================================
# Delete Application
# ==========================================

def delete_application():

    try:
        application_id = int(
            input("\nEnter application ID: ")
        )
    except ValueError:
        print("❌ Enter a valid ID.")
        return

    cursor.execute("""
    DELETE FROM applications
    WHERE id = ?
    """, (application_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("❌ Application not found.")
    else:
        print("✅ Application deleted successfully!")


# ==========================================
# Application Statistics
# ==========================================

def show_statistics():

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM applications
    GROUP BY status
    """)

    statistics = cursor.fetchall()

    print("\n======================================")
    print("       APPLICATION STATISTICS")
    print("======================================")

    if not statistics:
        print("No application data available.")
        return

    total = 0

    for status, count in statistics:

        print(f"{status:<12}: {count}")
        total += count

    print("--------------------------------------")
    print(f"Total        : {total}")
    print("======================================")


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n======================================")
    print("       JOB APPLICATION TRACKER")
    print("======================================")

    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Application")
    print("4. Update Status")
    print("5. Delete Application")
    print("6. Application Statistics")
    print("7. Exit")

    print("======================================")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_application()

    elif choice == "2":
        view_applications()

    elif choice == "3":
        search_application()

    elif choice == "4":
        update_status()

    elif choice == "5":
        delete_application()

    elif choice == "6":
        show_statistics()

    elif choice == "7":

        connection.close()

        print("\n======================================")
        print("       Tracker Closed 👋")
        print("======================================")

        break

    else:

        print(
            "\n❌ Invalid choice! "
            "Please select 1-7."
        )