# Import functions from task_utils
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            try:
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            view_pending_tasks()
            if tasks:
                try:
                    index = int(input("Enter task number to mark as complete: ")) - 1
                    pending_tasks = [task for task in tasks if not task["completed"]]
                    if 0 <= index < len(pending_tasks):
                        task_to_complete = pending_tasks[index]
                        actual_index = tasks.index(task_to_complete)
                        mark_task_as_complete(actual_index)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            calculate_progress()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
