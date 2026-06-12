from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    return True
    
def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    return True
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Due date must be in format YYYY-MM-DD.")
