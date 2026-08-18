# ==========================================
# Day 08 - Rock Paper Scissors
# 30 Days Python GitHub Project Challenge
# ==========================================

import random

print("======================================")
print("       ROCK PAPER SCISSORS")
print("======================================")

# Choices
choices = ["rock", "paper", "scissors"]

# Display menu
print("\nChoose your move:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

# User input
choice = input("\nEnter your choice (1-3): ")

# Convert number to choice
if choice == "1":
    player = "rock"

elif choice == "2":
    player = "paper"

elif choice == "3":
    player = "scissors"

else:
    print("\n❌ Invalid choice!")
    print("Please choose 1, 2, or 3.")
    exit()


# Computer choice
computer = random.choice(choices)


# Display choices
print("\n--------------------------------------")
print(f"You chose      : {player.capitalize()}")
print(f"Computer chose : {computer.capitalize()}")
print("--------------------------------------")


# Decide winner
if player == computer:
    result = "It's a Draw! 🤝"

elif (
    (player == "rock" and computer == "scissors")
    or
    (player == "paper" and computer == "rock")
    or
    (player == "scissors" and computer == "paper")
):
    result = "You Win! 🎉"

else:
    result = "Computer Wins! 🤖"


# Display result
print(f"\nResult: {result}")

print("\n======================================")
print("          GAME OVER 👋")
print("======================================")