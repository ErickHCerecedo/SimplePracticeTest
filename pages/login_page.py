from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage

class LoginPage(BasePage):
    __url = "https://account.simplepractice.com/"
    __expected_url = "https://secure.simplepractice.com/calendar/appointments"
    __username_input = (By.ID, "user_email")
    __password_input = (By.ID, "user_password")
    __login_button = (By.ID, "submitBtn")
    __error_message = (By.CLASS_NAME, "banner-message")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_input, username)
        super()._type(self.__password_input, password)
        super()._click(self.__login_button)
    
    def wait_for_login_success(self, timeout: int = 15):
        super()._wait_for_url_update(self.__expected_url, timeout)
    
    def wait_for_error_message(self, timeout: int = 5):
        super()._wait_until_element_is_visible(self.__error_message, timeout)

    def get_error_message(self, normalize: bool = True) -> str:
        error_text = super()._get_text(self.__error_message, time=3)
        return super()._normalize_text(error_text) if normalize else error_text
    
    def is_error_message_visible(self) -> bool:
        return super()._is_displayed(self.__error_message)
    
    def normalize_text(self, text: str) -> str:
        """Normaliza el texto usando el método de BasePage. 
        Útil para normalizar mensajes esperados en los tests."""
        return super()._normalize_text(text)

    @property
    def expected_url(self) -> str:
        return self.__expected_url
    
    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)
