import pytest

from pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login_positive(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("erickcerecedo@gmail.com", "QwertyBeta777")
        login_page.wait_for_login_success()
        assert login_page.expected_url == login_page.current_url, "Actual URL is not the same as expected URL"

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [
        ("invalid@email.com", "GoodLuck777", "Couldn't sign in Enter the email associated with your account and double-check your password. If you're still having trouble, you can reset your password.")
    ])
    def test_login_negative(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        login_page.wait_for_error_message()
        assert login_page.is_error_message_visible(), "Error message is not visible on the page"
        error_msg = login_page.get_error_message() 
        expected_normalized = login_page.normalize_text(expected_error_message)
        assert error_msg == expected_normalized, f"Expected '{expected_normalized}' but got '{error_msg}'"

