# ==========================================
# Day 07 - Number Guessing Game
# 30 Days Python GitHub Project Challenge
# ==========================================

import random

print("======================================")
print("         NUMBER GUESSING GAME")
print("======================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Try to guess it! 🎯")

# Game loop
while True:

    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("📈 Too low! Try a higher number.")

        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")

        else:
            print("\n======================================")
            print("           🎉 YOU WON! 🎉")
            print("======================================")
            print(f"Correct number : {secret_number}")
            print(f"Your attempts  : {attempts}")
            print("======================================")
            break

    except ValueError:
        print("❌ Invalid input! Please enter a number.")

print("\nThanks for playing! 👋")