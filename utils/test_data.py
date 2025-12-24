# Centralized test data enables data-driven testing and easy maintenance.
# Test data is separated from test logic, making it simple to add new test scenarios
# without modifying test code, improving scalability and maintainability.
TASK_TEST_DATA = {
    "default": {
        "name": "Test Task",
        "description": "This is a default test task"
    },
    "with_description": {
        "name": "Task with Description",
        "description": "This task has a detailed description"
    },
    "simple": {
        "name": "Simple Task",
        "description": None
    }
}

def get_task_data(data_key: str = "default") -> dict:
    if data_key not in TASK_TEST_DATA:
        available_keys = ", ".join(TASK_TEST_DATA.keys())
        raise KeyError(f"Invalid data_key: '{data_key}'. Available keys: {available_keys}")
    
    return TASK_TEST_DATA[data_key].copy()

