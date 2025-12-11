import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent = 2)

def show_tasks(tasks):
    if not tasks:
        print("/nNo tasks yet.")
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}, {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print(f"added: {task}")
    else:
        print("Task cannot be empty.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: View | Add | Delete | Quit")
        action = input("What do you want to do?").lower().strip()

        if action == "view":
            show_tasks(tasks)
        elif action == "add":
            add_task(tasks)
            save_tasks(tasks)
        elif action == "delete":
            delete_task(tasks)
            add_task(tasks)
        elif action == "quit":
            save_tasks(tasks)
            print("Bye for now!")
            break
        else:
            print("Unknown command.")

main()
