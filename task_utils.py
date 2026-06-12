from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return False
    tasks[index]["completed"] = True
    print("Task marked as complete!")
    return True
    
# Implement view_pending_tasks function
def view_pending_tasks():
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks!")
        return []
    print("Pending Tasks:")
    for i, task in enumerate(pending_tasks):
        print(f"{i + 1}. {task['title']} (Due: {task['due_date']})")
        print(f"   Description: {task['description']}")
    return pending_tasks

# Implement calculate_progress function
def calculate_progress():
    if len(tasks) == 0:
        progress = {
            "total_tasks": 0,
            "completed_tasks": 0,
            "progress_percentage": 0.0
        }
        print("No tasks to calculate progress.")
        return progress
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress_percentage = (completed_tasks / total_tasks) * 100
    
    progress = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "progress_percentage": progress_percentage
    }
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Progress: {progress_percentage:.2f}%")
    return progress
