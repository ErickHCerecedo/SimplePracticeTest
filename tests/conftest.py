import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv

from pages.login_page import LoginPage

# Loading .env file at module level ensures credentials are available before any test runs.
# Environment variables provide security by keeping sensitive data out of source code.
load_dotenv()

ENV_USERNAME = "SP_USERNAME"
ENV_PASSWORD = "SP_PASSWORD"

def get_username() -> str:
    username = os.getenv(ENV_USERNAME)
    if not username:
        raise ValueError(f"Environment variable '{ENV_USERNAME}' is not set. Please set it in .env file or as environment variable.")
    return username

def get_password() -> str:
    password = os.getenv(ENV_PASSWORD)
    if not password:
        raise ValueError(f"Environment variable '{ENV_PASSWORD}' is not set. Please set it in .env file or as environment variable.")
    return password

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Invalid browser: {browser}")
    
    yield my_driver

    my_driver.quit()

# logged_in_driver fixture encapsulates authentication, reducing test setup code
# and ensuring consistent login state across all tests that require authentication.
@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.execute_login(get_username(), get_password())
    login_page.wait_for_login_success()
    yield driver

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )

