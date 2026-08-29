# ==========================================
# Day 21 - CSV Data Analyzer
# 30 Days Python GitHub Project Challenge
# ==========================================

import pandas as pd


print("======================================")
print("          CSV DATA ANALYZER")
print("======================================")


# Get CSV file path
file_path = input("\nEnter CSV file path: ").strip()


# Read CSV file
try:
    data = pd.read_csv(file_path)

except FileNotFoundError:
    print("\n❌ CSV file not found.")
    exit()

except Exception as e:
    print(f"\n❌ Error reading CSV file: {e}")
    exit()


# Display menu
while True:

    print("\n======================================")
    print("            ANALYZER MENU")
    print("======================================")
    print("1. View Data")
    print("2. View First 5 Rows")
    print("3. View Last 5 Rows")
    print("4. Dataset Information")
    print("5. Statistical Summary")
    print("6. Check Missing Values")
    print("7. View Column Names")
    print("8. Analyze a Column")
    print("9. Exit")
    print("======================================")

    choice = input("Enter your choice (1-9): ")


    # View complete data
    if choice == "1":

        print("\n======================================")
        print("              DATA")
        print("======================================")

        print(data)


    # First 5 rows
    elif choice == "2":

        print("\n======================================")
        print("          FIRST 5 ROWS")
        print("======================================")

        print(data.head())


    # Last 5 rows
    elif choice == "3":

        print("\n======================================")
        print("           LAST 5 ROWS")
        print("======================================")

        print(data.tail())


    # Dataset information
    elif choice == "4":

        print("\n======================================")
        print("        DATASET INFORMATION")
        print("======================================")

        print(f"Rows    : {data.shape[0]}")
        print(f"Columns : {data.shape[1]}")

        print("\nColumn Information:")
        data.info()


    # Statistical summary
    elif choice == "5":

        print("\n======================================")
        print("         STATISTICAL SUMMARY")
        print("======================================")

        print(data.describe())


    # Missing values
    elif choice == "6":

        print("\n======================================")
        print("           MISSING VALUES")
        print("======================================")

        missing = data.isnull().sum()

        print(missing)


    # Column names
    elif choice == "7":

        print("\n======================================")
        print("           COLUMN NAMES")
        print("======================================")

        for number, column in enumerate(data.columns, start=1):
            print(f"{number}. {column}")


    # Analyze column
    elif choice == "8":

        column = input("\nEnter column name: ")

        if column not in data.columns:

            print("❌ Column not found.")

        else:

            print("\n======================================")
            print(f"        ANALYSIS: {column}")
            print("======================================")

            print("\nData Type:")
            print(data[column].dtype)

            print("\nMissing Values:")
            print(data[column].isnull().sum())

            print("\nUnique Values:")
            print(data[column].nunique())

            print("\nTop Values:")
            print(data[column].value_counts().head())

            # Numeric analysis
            if pd.api.types.is_numeric_dtype(data[column]):

                print("\nMinimum:")
                print(data[column].min())

                print("\nMaximum:")
                print(data[column].max())

                print("\nAverage:")
                print(data[column].mean())


    # Exit
    elif choice == "9":

        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")

        break


    else:

        print("\n❌ Invalid choice! Please select 1-9.")