from pages.login_page import LoginPage

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong", "wrong")
    assert "invalid" in page.get_flash_text()
