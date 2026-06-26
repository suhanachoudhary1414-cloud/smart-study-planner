tasks = []

print("=" * 40)
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
    print(tasks)

elif choice == "3":
    print("\nGoodbye!")

else:
    print("\nInvalid choice!")