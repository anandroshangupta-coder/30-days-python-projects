# ==========================================
# Day 13 - Quiz Game
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("             QUIZ GAME")
print("======================================")

# Quiz questions
questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A. .py", "B. .python", "C. .pt", "D. .p"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. create"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store multiple items in a sequence?",
        "options": ["A. int", "B. float", "C. list", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. <!--", "D. #"],
        "answer": "D"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. input()", "B. get()", "C. scan()", "D. read()"],
        "answer": "A"
    }
]


# Score
score = 0


# Start quiz
print("\nAnswer the following questions.")
print("Enter A, B, C, or D.\n")


for number, quiz in enumerate(questions, start=1):

    print("--------------------------------------")
    print(f"Question {number}:")
    print(quiz["question"])

    # Display options
    for option in quiz["options"]:
        print(option)

    # Get answer
    user_answer = input("\nYour answer: ").upper()

    # Check answer
    if user_answer == quiz["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {quiz['answer']}")


# Calculate percentage
total_questions = len(questions)
percentage = (score / total_questions) * 100


# Display final result
print("\n======================================")
print("             QUIZ RESULT")
print("======================================")

print(f"Total Questions : {total_questions}")
print(f"Correct Answers : {score}")
print(f"Wrong Answers   : {total_questions - score}")
print(f"Score           : {score}/{total_questions}")
print(f"Percentage      : {percentage:.2f}%")

# Performance message
if percentage == 100:
    print("Performance     : Excellent! 🏆")

elif percentage >= 80:
    print("Performance     : Very Good! 🎉")

elif percentage >= 60:
    print("Performance     : Good! 👍")

elif percentage >= 40:
    print("Performance     : Keep Practicing! 💪")

else:
    print("Performance     : Need More Practice! 📚")

print("======================================")
print("          QUIZ COMPLETED! 🎉")
print("======================================")