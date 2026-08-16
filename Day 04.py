# ==========================================
# Day 04 - Age & Personal Information Calculator
# 30 Days Python GitHub Project Challenge
# ==========================================

from datetime import date


print("==========================================")
print("    AGE & PERSONAL INFORMATION CALCULATOR")
print("==========================================")


# Get personal information
name = input("Enter your name: ")
city = input("Enter your city: ")

# Get date of birth
print("\nEnter your Date of Birth")

birth_day = int(input("Day   : "))
birth_month = int(input("Month : "))
birth_year = int(input("Year  : "))


# Get today's date
today = date.today()

# Create date of birth
birth_date = date(birth_year, birth_month, birth_day)


# Calculate age
age = today.year - birth_date.year

# Check if birthday has occurred this year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1


# Calculate approximate days lived
days_lived = (today - birth_date).days


# Display information
print("\n==========================================")
print("          PERSONAL INFORMATION")
print("==========================================")

print(f"Name       : {name}")
print(f"City       : {city}")
print(f"Date of Birth : {birth_day:02d}-{birth_month:02d}-{birth_year}")
print(f"Current Date  : {today.strftime('%d-%m-%Y')}")
print(f"Age          : {age} years")
print(f"Days Lived   : {days_lived} days")

print("==========================================")
print("       Calculation Completed! 🎉")
print("==========================================")