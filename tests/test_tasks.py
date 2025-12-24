import pytest

from pages.tasks_page import TasksPage

class TestTasks:

    @pytest.mark.tasks
    @pytest.mark.positive
    def test_create_task_positive(self, logged_in_driver):
        tasks_page = TasksPage(logged_in_driver)
        tasks_page.open()
        tasks_page.create_task(data_key="default")
        from utils.test_data import get_task_data
        task_data = get_task_data("default")
        task_name = task_data["name"]
        assert tasks_page.is_task_at_top(task_name), f"Task '{task_name}' should be at the top of the list"
    
    @pytest.mark.tasks
    @pytest.mark.positive
    @pytest.mark.debug
    def test_mark_task_as_completed(self, logged_in_driver):
        tasks_page = TasksPage(logged_in_driver)
        tasks_page.open()
        tasks_page.create_task(data_key="with_description")
        from utils.test_data import get_task_data
        task_data = get_task_data("default")
        task_name = task_data["name"]
        assert tasks_page.is_task_at_top(task_name), f"Task '{task_name}' should be at the top of the list"
        tasks_page.mark_first_task_as_completed()
        tasks_page.filter_by_completed()
        first_task_name = tasks_page.get_first_task_name()
        assert first_task_name == task_name, f"Task '{task_name}' should be at the top of the completed tasks list, but found '{first_task_name}'"
    
    