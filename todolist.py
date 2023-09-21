import os

# Define the file name to store the to-do list
TODO_FILE = "todo.txt"

def load_todo_list():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        file.write("\n".join(todo_list))

def display_todo_list(todo_list):
    if not todo_list:
        print("\n\nYour to-do list is empty!")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    save_todo_list(todo_list)
    print(f"\nTask '{task}' added to the to-do list.")

def complete_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        completed_task = todo_list.pop(task_index - 1)
        save_todo_list(todo_list)
        print(f"\nTask '{completed_task}' marked as completed.")
    else:
        print("\nInvalid task index. Please enter a valid task number.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n\n<><><><><><><><><><><><><><><><><><><><><>\n")
        print("             TO-DO LIST")
        print("\n<><><><><><><><><><><><><><><><><><><><><>\n")
        print("\nOPTIONS:   \n")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit\n\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("\nEnter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            display_todo_list(todo_list)
            task_index = int(input("\n\nEnter the task number to mark as completed: "))
            complete_task(todo_list, task_index)
        elif choice == "4":
            print("\n\nGOODBYE!")
            break
        else:
            print("\n\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
