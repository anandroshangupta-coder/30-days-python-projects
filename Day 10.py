# ==========================================
# Day 10 - Password Strength Checker
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("        PASSWORD STRENGTH CHECKER")
print("======================================")

# Get password
password = input("\nEnter your password: ")

# Check password conditions
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

# Check every character
for character in password:

    if character.isupper():
        has_uppercase = True

    elif character.islower():
        has_lowercase = True

    elif character.isdigit():
        has_number = True

    elif character in special_characters:
        has_special = True


# Calculate password score
score = 0

if len(password) >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1


# Determine strength
if score == 5:
    strength = "Very Strong 💪"

elif score >= 4:
    strength = "Strong 🔒"

elif score >= 3:
    strength = "Medium ⚠️"

elif score >= 2:
    strength = "Weak ❌"

else:
    strength = "Very Weak ❌"


# Display result
print("\n======================================")
print("          PASSWORD ANALYSIS")
print("======================================")

print(f"Password Length : {len(password)}")
print(f"Uppercase       : {'Yes' if has_uppercase else 'No'}")
print(f"Lowercase       : {'Yes' if has_lowercase else 'No'}")
print(f"Number          : {'Yes' if has_number else 'No'}")
print(f"Special Symbol  : {'Yes' if has_special else 'No'}")

print("--------------------------------------")
print(f"Score            : {score}/5")
print(f"Strength         : {strength}")

print("======================================")
print("         Analysis Completed! 🎉")
print("======================================")