import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def show_menu():
    print("\n--- Daily Task Tracker ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append({"task": task, "done": False})
    save_tasks()
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks for today 🎉")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to mark completed: "))
        tasks[task_no - 1]["done"] = True
        save_tasks()
        print("Task marked as completed 👍")
    except (ValueError, IndexError):
        print("Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Tasks saved. Goodbye! 👋")
        break
    else:
        print("Please choose a valid option!")
