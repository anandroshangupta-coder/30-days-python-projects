# ==========================================
# Day 27 - Personal Finance Dashboard
# 30 Days Python GitHub Project Challenge
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt


print("======================================")
print("       PERSONAL FINANCE DASHBOARD")
print("======================================")


# ==========================================
# Load CSV File
# ==========================================

file_path = input("\nEnter CSV file path: ").strip()

try:
    data = pd.read_csv(file_path)

except FileNotFoundError:
    print("❌ File not found.")
    exit()

except Exception as error:
    print("❌ Error:", error)
    exit()


print("\n✅ Finance data loaded successfully!")


# ==========================================
# Check Required Columns
# ==========================================

required_columns = [
    "Category",
    "Amount"
]

for column in required_columns:

    if column not in data.columns:

        print(f"❌ Missing column: {column}")
        exit()


# ==========================================
# Convert Amount to Number
# ==========================================

data["Amount"] = pd.to_numeric(
    data["Amount"],
    errors="coerce"
)

data = data.dropna(
    subset=["Amount"]
)


# ==========================================
# Main Dashboard
# ==========================================

while True:

    print("\n======================================")
    print("          FINANCE DASHBOARD")
    print("======================================")
    print("1. View Transactions")
    print("2. Total Expenses")
    print("3. Average Expense")
    print("4. Highest Expense")
    print("5. Category Summary")
    print("6. Expense Bar Chart")
    print("7. Expense Pie Chart")
    print("8. Expense Line Chart")
    print("9. Exit")
    print("======================================")

    choice = input("Enter your choice (1-9): ")


    # ======================================
    # View Transactions
    # ======================================

    if choice == "1":

        print("\n======================================")
        print("          TRANSACTIONS")
        print("======================================")

        print(data)


    # ======================================
    # Total Expenses
    # ======================================

    elif choice == "2":

        total = data["Amount"].sum()

        print("\n======================================")
        print("          TOTAL EXPENSES")
        print("======================================")

        print(f"Total Expenses: ₹{total:.2f}")


    # ======================================
    # Average Expense
    # ======================================

    elif choice == "3":

        average = data["Amount"].mean()

        print("\n======================================")
        print("          AVERAGE EXPENSE")
        print("======================================")

        print(f"Average Expense: ₹{average:.2f}")


    # ======================================
    # Highest Expense
    # ======================================

    elif choice == "4":

        highest = data.loc[
            data["Amount"].idxmax()
        ]

        print("\n======================================")
        print("          HIGHEST EXPENSE")
        print("======================================")

        print(f"Category : {highest['Category']}")
        print(f"Amount   : ₹{highest['Amount']:.2f}")


    # ======================================
    # Category Summary
    # ======================================

    elif choice == "5":

        summary = (
            data
            .groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\n======================================")
        print("          CATEGORY SUMMARY")
        print("======================================")

        print(summary)

    # ======================================
    # Bar Chart
    # ======================================

    elif choice == "6":

        summary = (
            data
            .groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        plt.figure(figsize=(8, 5))

        plt.bar(
            summary.index,
            summary.values
        )

        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.title("Expenses by Category")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


    # ======================================
    # Pie Chart
    # ======================================

    elif choice == "7":

        summary = (
            data
            .groupby("Category")["Amount"]
            .sum()
        )

        plt.figure(figsize=(7, 7))

        plt.pie(
            summary.values,
            labels=summary.index,
            autopct="%1.1f%%"
        )

        plt.title("Expense Distribution")

        plt.show()


    # ======================================
    # Line Chart
    # ======================================

    elif choice == "8":

        if "Date" not in data.columns:

            print("❌ Date column not found.")
            print("Add a 'Date' column to use the line chart.")
            continue

        data["Date"] = pd.to_datetime(
            data["Date"],
            errors="coerce"
        )

        daily_expenses = (
            data
            .dropna(subset=["Date"])
            .groupby("Date")["Amount"]
            .sum()
        )

        plt.figure(figsize=(9, 5))

        plt.plot(
            daily_expenses.index,
            daily_expenses.values,
            marker="o"
        )

        plt.xlabel("Date")
        plt.ylabel("Amount (₹)")
        plt.title("Daily Expenses")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


    # ======================================
    # Exit
    # ======================================

    elif choice == "9":

        print("\n======================================")
        print("       Dashboard Closed 👋")
        print("======================================")

        break


    else:

        print("❌ Invalid choice! Please select 1-9.")