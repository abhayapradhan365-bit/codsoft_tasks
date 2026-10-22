tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")

        if task.strip():
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print("Removed task:", removed_task)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please select 1-4.")