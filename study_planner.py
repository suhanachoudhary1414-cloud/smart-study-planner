tasks = []

while True:
    print("\n" + "=" * 40)
    print("      SMART STUDY PLANNER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

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
        print("\nGoodbye! 👋")
        break

    else:
        print("\n❌ Invalid choice.")