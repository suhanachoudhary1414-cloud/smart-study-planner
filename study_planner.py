tasks = []

while True:
    print("\n" + "=" * 40)
    print("      SMART STUDY PLANNER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        task = input("Enter your task: ")

        new_task = {
            "name": task,
            "completed": False
        }

        tasks.append(new_task)
        print("\n✅ Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['name']}")

    elif choice == "3":

        if len(tasks) == 0:
            print("\nNo tasks to delete.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['name']}")

            delete = int(input("\nEnter task number to delete: "))

            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete - 1)
                print(f"\n✅ '{removed['name']}' deleted successfully!")

            else:
                print("\n❌ Invalid task number.")

    elif choice == "4":

        if len(tasks) == 0:
            print("\nNo tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['name']}")

            complete = int(input("\nEnter task number to mark as completed: "))

            if 1 <= complete <= len(tasks):
                tasks[complete - 1]["completed"] = True
                print("\n✅ Task marked as completed!")

            else:
                print("\n❌ Invalid task number.")

    elif choice == "5":
        print("\nGoodbye! 👋")
        break

    else:
        print("\n❌ Invalid choice.")