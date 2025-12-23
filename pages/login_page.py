from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage

class LoginPage(BasePage):
    __url = "https://account.simplepractice.com/"
    __username_input = (By.ID, "user_email")
    __password_input = (By.ID, "user_password")
    __login_button = (By.ID, "submitBtn")
    __error_message = (By.CLASS_NAME, "error-message")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time=3)