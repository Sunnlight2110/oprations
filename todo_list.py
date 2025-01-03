import sys
import time  # Import the time module

def display_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    time.sleep(1)  

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
            time.sleep(0.5)  

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    time.sleep(1)  

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    time.sleep(1)  

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application.")
            break  
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)  

if __name__ == "__main__":
    main()