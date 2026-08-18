# ==========================================
# Day 09 - Password Generator
# 30 Days Python GitHub Project Challenge
# ==========================================

import random
import string

print("======================================")
print("          PASSWORD GENERATOR")
print("======================================")

# Get password length
length = int(input("\nEnter password length: "))

# Check minimum length
if length < 4:
    print("\n❌ Password length should be at least 4 characters.")

else:
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_characters = "!@#$%^&*"

    # Make sure the password contains different character types
    password_characters = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Remaining characters
    all_characters = lowercase + uppercase + numbers + special_characters

    for i in range(length - 4):
        password_characters.append(random.choice(all_characters))

    # Shuffle password
    random.shuffle(password_characters)

    # Convert list to string
    password = "".join(password_characters)

    # Display password
    print("\n======================================")
    print("        GENERATED PASSWORD")
    print("======================================")
    print(password)
    print("======================================")

    print("\n✅ Password generated successfully!")