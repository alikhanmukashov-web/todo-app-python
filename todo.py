tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def add_task():
    task = input("Enter new task: ").strip()
    if task == "":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        print("Task added")
def delete_task():
    show_tasks()
    if not tasks:
        return
    user_input = input("Enter task numbers to delete (e.g., 1 or 2,3): ").strip()
    try:
        numbers = [int(x) for x in user_input.split(",")]
        for num in sorted(numbers, reverse=True):
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print(f"Invalid number: {num}")
    except ValueError:
        print("Please enter numbers separated by commas")
def get_choice(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["1", "show", "show tasks"]:
        return "show"
    elif user_input in ["2", "add", "add task"]:
        return "add"
    elif user_input in ["3", "delete", "delete task", "remove"]:
        return "delete"
    elif user_input in ["4", "exit", "quit"]:
        return "exit"
    else:
        return None

while True:
    print("\n==== TO-DO APP ====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    user_input = input("Choose option: ")
    choice = get_choice(user_input)

    if choice == "show":
        show_tasks()
    elif choice == "add":
        add_task()
    elif choice == "delete":
        delete_task()
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid input (try 'add', 'show', 'delete', or number)")