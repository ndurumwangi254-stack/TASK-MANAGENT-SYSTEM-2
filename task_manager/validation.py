from datetime import datetime

def validate_task_title(title):
    """
    Validates the task title.
    
    Args:
        title (str): The title to validate
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If title is empty or not a string
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    return True

    
def validate_task_description(description):
    """
    Validates the task description.
    
    Args:
        description (str): The description to validate
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If description is not a string
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    return True

    
def validate_due_date(due_date):
    """
    Validates the due date.
    
    Args:
        due_date (str): The due date in format YYYY-MM-DD
        
    Returns:
        bool: True if valid, raises ValueError otherwise
        
    Raises:
        ValueError: If due date format is invalid or date is in the past
    """
    try:
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        if date_obj < datetime.now():
            raise ValueError("Due date cannot be in the past.")
        return True
    except ValueError as e:
        if "Due date cannot be in the past" in str(e):
            raise
        raise ValueError("Due date must be in format YYYY-MM-DD.")
