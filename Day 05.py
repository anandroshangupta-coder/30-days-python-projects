# ==========================================
# Day 05 - Even/Odd & Number Analyzer
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("       EVEN/ODD & NUMBER ANALYZER")
print("======================================")

# Get number from user
number = int(input("\nEnter a number: "))


# Check Even or Odd
if number % 2 == 0:
    even_odd = "Even"
else:
    even_odd = "Odd"


# Check Positive, Negative or Zero
if number > 0:
    number_type = "Positive"
elif number < 0:
    number_type = "Negative"
else:
    number_type = "Zero"


# Check Divisibility
if number % 5 == 0:
    divisible_by_5 = "Yes"
else:
    divisible_by_5 = "No"


if number % 10 == 0:
    divisible_by_10 = "Yes"
else:
    divisible_by_10 = "No"


# Display results
print("\n======================================")
print("           ANALYSIS RESULT")
print("======================================")

print(f"Number          : {number}")
print(f"Even/Odd        : {even_odd}")
print(f"Number Type     : {number_type}")
print(f"Divisible by 5  : {divisible_by_5}")
print(f"Divisible by 10 : {divisible_by_10}")

print("======================================")
print("       Analysis Completed! 🎉")
print("======================================")