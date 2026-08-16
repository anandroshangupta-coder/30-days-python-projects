# ==========================================
# Day 3 - Temperature Converter
# 30 Days Python GitHub Project Challenge
# ==========================================


print("===================================")
print("      TEMPERATURE CONVERTER")
print("===================================")


# Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Display menu
print("\nChoose an option:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")


# Get user input
choice = input("\nEnter your choice (1 or 2): ")
temperature = float(input("Enter temperature: "))


# Perform conversion
if choice == "1":

    result = celsius_to_fahrenheit(temperature)

    print("\n-----------------------------------")
    print(f"Temperature: {temperature}°C")
    print(f"Converted:   {result:.2f}°F")
    print("-----------------------------------")

elif choice == "2":

    result = fahrenheit_to_celsius(temperature)

    print("\n-----------------------------------")
    print(f"Temperature: {temperature}°F")
    print(f"Converted:   {result:.2f}°C")
    print("-----------------------------------")

else:

    print("\n❌ Invalid choice!")
    print("Please choose 1 or 2.")


print("\n===================================")
print("       Thank You! Goodbye 👋")
print("===================================")