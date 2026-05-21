from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME  = (By.ID, "username")
    PASSWORD  = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button")
    FLASH     = (By.ID, "flash")

    def open(self):
        super().open(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_flash_text(self):
        return self.find(self.FLASH).text
