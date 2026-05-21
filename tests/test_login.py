import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_message", [
    ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
    ("wrong",    "wrong",                "Your username is invalid!"),
    ("",         "",                     "Your username is invalid!"),
])
def test_login(driver, username, password, expected_message):
    page = LoginPage(driver)
    page.open()
    page.login(username, password)
    assert expected_message in page.get_flash_text()
