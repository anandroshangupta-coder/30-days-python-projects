# ==========================================
# Day 11 - To-Do List CLI
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("             TO-DO LIST")
print("======================================")

# Store tasks
tasks = []


# Show tasks
def show_tasks():
    print("\n======================================")
    print("              YOUR TASKS")
    print("======================================")

    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    print("======================================")


# Add task
def add_task():
    task = input("\nEnter a new task: ")

    if task.strip() == "":
        print("❌ Task cannot be empty.")
    else:
        tasks.append(task)
        print("✅ Task added successfully!")


# Remove task
def remove_task():
    show_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"✅ Removed: {removed_task}")
        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# Main menu
while True:

    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("\n======================================")
        print("      Thank You! Goodbye 👋")
        print("======================================")
        break

    else:
        print("❌ Invalid choice! Please select 1-4.")