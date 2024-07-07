tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def edit_task(index, new_task):
    if index >= 0 and index < len(tasks):
        tasks[index] = new_task
        print(f"Task {index+1} updated to '{new_task}'.")
    else:
        print("Invalid task index.")

def delete_task(index):
    if index >= 0 and index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task {index+1} '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

def show_tasks():
    if tasks:
        print("To-Do List:")
        for idx, task in enumerate(tasks):
            print(f"{idx+1}. {task}")
    else:
        print("To-Do List is empty.")


def todo_list_app():
    while True:
        print("\nTo-Do List App Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            add_task(task)
        elif choice == '2':
            index = int(input("Enter task index to edit (1, 2, ...): ")) - 1
            new_task = input(f"Enter new task for index {index+1}: ")
            edit_task(index, new_task)
        elif choice == '3':
            index = int(input("Enter task index to delete (1, 2, ...): ")) - 1
            delete_task(index)
        elif choice == '4':
            show_tasks()
        elif choice == '5':
            print("Exiting To-Do List App.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    todo_list_app()
