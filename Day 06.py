# ==========================================
# Day 06 - Simple Calculator
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("          SIMPLE CALCULATOR")
print("======================================")


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


# Menu
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")


# User input
choice = input("\nEnter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Perform calculation
if choice == "1":

    result = add(num1, num2)
    operator = "+"

elif choice == "2":

    result = subtract(num1, num2)
    operator = "-"

elif choice == "3":

    result = multiply(num1, num2)
    operator = "*"

elif choice == "4":

    result = divide(num1, num2)
    operator = "/"

else:

    result = "Invalid choice!"
    operator = "?"


# Display result
print("\n======================================")
print("             RESULT")
print("======================================")

if isinstance(result, (int, float)):
    print(f"{num1} {operator} {num2} = {result:.2f}")
else:
    print(result)

print("======================================")
print("       Calculation Completed! 🎉")
print("======================================")