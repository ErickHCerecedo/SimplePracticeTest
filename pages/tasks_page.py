from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage

# TasksPage demonstrates data-driven testing by accepting data_key parameter.
# This approach centralizes test data in utils/test_data.py, making tests cleaner
# and enabling easy maintenance of test scenarios without modifying test code.
class TasksPage(BasePage):

    __task_add_button_locator = (By.XPATH, "//a[@href='/tasks/new']")
    __task_name_input_locator = (By.ID, "title")
    __task_description_input_locator = (By.ID, "description")
    __task_save_button_locator = (By.XPATH, "//button[contains(@class, 'button') and contains(@class, 'primary') and contains(text(), 'Save')]")
    
    __task_list_container_locator = (By.XPATH, "//div[contains(@class, 'list-items') and contains(@class, 'top')]")
    __task_list_first_item_locator = (By.XPATH, "//div[contains(@class, 'list-items')]//div[@class='I26t1' and @role='button'][1]")
    __task_item_name_button_locator = (By.XPATH, ".//button[@aria-label='Edit task']")
    __task_checkbox_input_locator = (By.XPATH, ".//label[@class='IX6yi']//input[@type='checkbox']")
    
    __filter_button_locator = (By.XPATH, "//*[@id='ember159']/button")
    __dropdown_menu_locator = (By.XPATH, "//div[contains(@class, 'ember-basic-dropdown-content') and contains(@class, 'menu')]")
    __completed_button_locator = (By.XPATH, "//button[contains(@class, 'utility-selected-option')]//span[text()='Completed']/ancestor::button | //button//span[text()='Completed']/ancestor::button")
    
    __url = "https://secure.simplepractice.com/tasks"
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def open(self):
        super()._open_url(self.__url)
    
    def create_task(self, name: str = None, description: str = None, data_key: str = None):
        if data_key:
            from utils.test_data import get_task_data
            task_data = get_task_data(data_key)
            name = name or task_data.get("name")
            description = description if description is not None else task_data.get("description")
        
        if not name:
            raise ValueError("Task name is required. Provide 'name' parameter or use 'data_key' with predefined data.")
        
        super()._click(self.__task_add_button_locator)
        super()._type(self.__task_name_input_locator, name)
        if description:
            super()._type(self.__task_description_input_locator, description)
        super()._click(self.__task_save_button_locator)
    
    def get_first_task_name(self) -> str:
        super()._wait_until_element_is_visible(self.__task_list_container_locator, time=5)
        first_task = super()._find(self.__task_list_first_item_locator)
        name_button = first_task.find_element(*self.__task_item_name_button_locator)
        return name_button.text.strip()
    
    def is_task_at_top(self, task_name: str, timeout: int = 10) -> bool:
        try:
            wait = WebDriverWait(self._driver, timeout)
            wait.until(lambda driver: self.get_first_task_name() == task_name)
            return True
        except:
            return False
    
    # JavaScript click fallback handles cases where elements are intercepted by overlays
    # or animations, which is common in modern web applications with dynamic UI frameworks.
    def mark_first_task_as_completed(self):
        super()._wait_until_element_is_visible(self.__task_list_first_item_locator, time=5)
        first_task = super()._find(self.__task_list_first_item_locator)
        checkbox = first_task.find_element(*self.__task_checkbox_input_locator)
        
        if not checkbox.is_selected():
            try:
                checkbox.click()
            except:
                self._driver.execute_script("arguments[0].click();", checkbox)
    
    # Multiple explicit waits ensure dropdown menu is fully rendered before interaction.
    # JavaScript click fallback prevents ElementClickInterceptedException from dynamic overlays.
    def filter_by_completed(self):
        super()._click(self.__filter_button_locator, time=10)
        super()._wait_until_element_is_visible(self.__dropdown_menu_locator, time=10)
        super()._wait_until_element_is_clickable(self.__completed_button_locator, time=10)
        
        completed_button = super()._find(self.__completed_button_locator)
        try:
            completed_button.click()
        except:
            self._driver.execute_script("arguments[0].click();", completed_button)
    
