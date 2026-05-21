from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxesPage(BasePage):
    URL        = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        super().open(self.URL)

    def select_all(self):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        for cb in checkboxes:
            if not cb.is_selected():
                cb.click()

    def all_selected(self):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return all(cb.is_selected() for cb in checkboxes)
