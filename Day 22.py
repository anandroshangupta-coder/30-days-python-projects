# ==========================================
# Day 22 - Data Visualization
# 30 Days Python GitHub Project Challenge
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt


print("======================================")
print("          DATA VISUALIZATION")
print("======================================")


# Enter CSV file
file_path = input("\nEnter CSV file path: ").strip()


# Read CSV
try:
    data = pd.read_csv(file_path)

except FileNotFoundError:
    print("❌ CSV file not found.")
    exit()

except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit()


print("\n✅ Dataset loaded successfully!")

print("\nColumns available:")
for number, column in enumerate(data.columns, start=1):
    print(f"{number}. {column}")


# Main menu
while True:

    print("\n======================================")
    print("       VISUALIZATION MENU")
    print("======================================")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Histogram")
    print("4. Scatter Plot")
    print("5. Exit")
    print("======================================")

    choice = input("Enter your choice (1-5): ")


    # --------------------------------------
    # Bar Chart
    # --------------------------------------

    if choice == "1":

        x_column = input("Enter X-axis column: ")
        y_column = input("Enter Y-axis column: ")

        if x_column not in data.columns or y_column not in data.columns:
            print("❌ Invalid column name.")
            continue

        plt.figure(figsize=(8, 5))

        plt.bar(
            data[x_column].astype(str),
            data[y_column]
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} by {x_column}")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


    # --------------------------------------
    # Line Chart
    # --------------------------------------

    elif choice == "2":

        x_column = input("Enter X-axis column: ")
        y_column = input("Enter Y-axis column: ")

        if x_column not in data.columns or y_column not in data.columns:
            print("❌ Invalid column name.")
            continue

        plt.figure(figsize=(8, 5))

        plt.plot(
            data[x_column],
            data[y_column],
            marker="o"
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} Trend")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


    # --------------------------------------
    # Histogram
    # --------------------------------------

    elif choice == "3":

        column = input("Enter numeric column: ")

        if column not in data.columns:
            print("❌ Column not found.")
            continue

        if not pd.api.types.is_numeric_dtype(data[column]):
            print("❌ Please select a numeric column.")
            continue

        plt.figure(figsize=(8, 5))

        plt.hist(
            data[column].dropna(),
            bins=10
        )

        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {column}")

        plt.tight_layout()
        plt.show()


    # --------------------------------------
    # Scatter Plot
    # --------------------------------------

    elif choice == "4":

        x_column = input("Enter X-axis column: ")
        y_column = input("Enter Y-axis column: ")

        if x_column not in data.columns or y_column not in data.columns:
            print("❌ Invalid column name.")
            continue

        plt.figure(figsize=(8, 5))

        plt.scatter(
            data[x_column],
            data[y_column]
        )

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{x_column} vs {y_column}")

        plt.tight_layout()
        plt.show()


    # --------------------------------------
    # Exit
    # --------------------------------------

    elif choice == "5":

        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")

        break


    else:

        print("❌ Invalid choice! Please select 1-5.")