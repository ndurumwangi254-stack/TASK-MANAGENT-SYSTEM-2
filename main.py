# Import functions from task_manager package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, tasks

# Define the main function
def main():
    """
    Main function that runs the task management system menu interface.
    """
    while True:
        print("\n" + "="*40)
        print("     Task Management System")
        print("="*40)
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. View All Tasks")
        print("6. Exit")
        print("="*40)
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            # Add Task
            try:
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                add_task(title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            # Mark Task as Complete
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
            # View Pending Tasks
            view_pending_tasks()
            
        elif choice == "4":
            # View Progress
            calculate_progress(tasks)
            
        elif choice == "5":
            # View All Tasks
            if not tasks:
                print("\nNo tasks yet!")
            else:
                print("\n--- All Tasks ---")
                for i, task in enumerate(tasks, 1):
                    status = "✓ Completed" if task["completed"] else "○ Pending"
                    print(f"{i}. [{status}] {task['title']}")
                    print(f"   Description: {task['description']}")
                    print(f"   Due Date: {task['due_date']}")
                print()
            
        elif choice == "6":
            print("\nExiting the program...")
            break
            
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
