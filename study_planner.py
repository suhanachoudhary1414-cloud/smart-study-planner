import json

tasks = []

def show_tasks():

    if len(tasks) == 0:
        print("\nNo tasks yet.")

    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):

            status = "✓" if task["completed"] else " "

            print(f"{i}. [{status}] {task['name']}")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []


load_tasks()

while True:
    print("\n" + "=" * 40)
    print("📚 SMART STUDY PLANNER")
    print("=" * 40)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Clear Completed Tasks")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        task = input("Enter your task: ").strip()

        if task == "":
            print("\n❌ Task cannot be empty!")

        else:
            new_task = {
                "name": task,
                "completed": False
            }

            tasks.append(new_task)
            save_tasks()

            print("\n✅ Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":

        if len(tasks) == 0:
            print("\nNo tasks to delete.")

        else:
            show_tasks()

            try:
                delete = int(input("\nEnter task number to delete: "))

                if 1 <= delete <= len(tasks):
                    removed = tasks.pop(delete - 1)
                    save_tasks()
                    print(f"\n✅ '{removed['name']}' deleted successfully!")

                else:
                    print("\n❌ Invalid task number.")

            except ValueError:
                print("\n❌ Please enter a valid number.")

    elif choice == "4":

        if len(tasks) == 0:
            print("\nNo tasks available.")

        else:
            show_tasks()
            
            try:
                complete = int(input("\nEnter task number to mark as completed: "))

                if 1 <= complete <= len(tasks):
                    tasks[complete - 1]["completed"] = True
                    save_tasks()
                    print("\n✅ Task marked as completed!")

                else:
                    print("\n❌ Invalid task number.")

            except ValueError:
                print("\n❌ Please enter a valid number.")

    elif choice == "5":

        before = len(tasks)

        tasks = [task for task in tasks if not task["completed"]]

        removed = before - len(tasks)

        save_tasks()

        print(f"\n✅ Removed {removed} completed task(s).")

    elif choice == "6":

        print("\nGoodbye! 👋")
        break

    else:
        print("\n❌ Invalid choice.")