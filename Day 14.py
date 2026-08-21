# ==========================================
# Day 14 - Expense Tracker
# 30 Days Python GitHub Project Challenge
# ==========================================

import csv
import os

FILE_NAME = "expenses.csv"

print("======================================")
print("           EXPENSE TRACKER")
print("======================================")


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add expense
def add_expense():
    date = input("\nEnter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: ₹"))

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                date,
                category,
                description,
                amount
            ])

        print("\n✅ Expense added successfully!")

    except ValueError:
        print("\n❌ Please enter a valid amount.")


# View expenses
def view_expenses():
    print("\n======================================")
    print("             ALL EXPENSES")
    print("======================================")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        total = 0

        for number, expense in enumerate(expenses, start=1):
            amount = float(expense["Amount"])
            total += amount

            print(f"\n{number}.")
            print(f"Date        : {expense['Date']}")
            print(f"Category    : {expense['Category']}")
            print(f"Description : {expense['Description']}")
            print(f"Amount      : ₹{amount:.2f}")

        print("\n--------------------------------------")
        print(f"Total Expense: ₹{total:.2f}")
        print("======================================")


# Search expenses by category
def search_category():
    category = input("\nEnter category to search: ").lower()

    found = False
    total = 0

    print("\n======================================")
    print("         CATEGORY EXPENSES")
    print("======================================")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:

            if expense["Category"].lower() == category:
                amount = float(expense["Amount"])
                total += amount
                found = True

                print(f"\nDate        : {expense['Date']}")
                print(f"Description : {expense['Description']}")
                print(f"Amount      : ₹{amount:.2f}")

    if found:
        print("\n--------------------------------------")
        print(f"Category Total: ₹{total:.2f}")
    else:
        print("\n❌ No expenses found for this category.")

    print("======================================")


# Main program
create_file()

while True:

    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")
        break

    else:
        print("❌ Invalid choice! Please select 1-4.")