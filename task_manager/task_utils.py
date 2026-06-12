from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    """
    Adds a new task to the task list.
    
    Args:
        title (str): Task title
        description (str): Task description
        due_date (str): Due date in format YYYY-MM-DD
        
    Returns:
        bool: True if task was added successfully
        
    Raises:
        ValueError: If any of the inputs are invalid
    """
    # Validate inputs
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    
    # Create task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    
    # Add task to list
    tasks.append(task)
    print("Task added successfully!")
    return True

    
def mark_task_as_complete(index):
    """
    Marks a task as complete.
    
    Args:
        index (int): The index of the task to mark as complete
        
    Returns:
        bool: True if task was marked as complete, False otherwise
    """
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return False
    
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True

    
def view_pending_tasks():
    """
    Displays all pending (incomplete) tasks.
    
    Returns:
        list: List of pending tasks
    """
    pending_tasks = [task for task in tasks if not task["completed"]]
    
    if not pending_tasks:
        print("No pending tasks!")
        return []
    
    print("\n--- Pending Tasks ---")
    for i, task in enumerate(pending_tasks):
        print(f"{i + 1}. {task['title']} (Due: {task['due_date']})")
        print(f"   Description: {task['description']}")
    print()
    
    return pending_tasks

def calculate_progress(tasks_list=None):
    """
    Calculates the progress of tasks completed.
    
    Args:
        tasks_list (list, optional): List of tasks. If None, uses the global tasks list
        
    Returns:
        dict: Dictionary containing total tasks, completed tasks, and progress percentage
    """
    if tasks_list is None:
        tasks_list = tasks
    
    if len(tasks_list) == 0:
        progress = {
            "total_tasks": 0,
            "completed_tasks": 0,
            "progress_percentage": 0.0
        }
        print("No tasks to calculate progress.")
        return progress
    
    total_tasks = len(tasks_list)
    completed_tasks = sum(1 for task in tasks_list if task["completed"])
    progress_percentage = (completed_tasks / total_tasks) * 100
    
    progress = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress_percentage": progress_percentage
    }
    
    print(f"\n--- Progress ---")
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Progress: {progress_percentage:.2f}%\n")
    
    return progress
