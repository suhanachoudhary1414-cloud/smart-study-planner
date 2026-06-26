tasks = []

while True:
    print("\n" + "=" * 40)
    print("      SMART STUDY PLANNER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("\n✅ Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to delete.")
        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete = int(input("\nEnter task number to delete: "))

            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete - 1)
                print(f"\n✅ '{removed}' deleted successfully!")
            else:
                print("\n❌ Invalid task number.")

    elif choice == "4":
        print("\nGoodbye! 👋")
        break

    else:
        print("\n❌ Invalid choice.")