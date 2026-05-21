from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AlertsPage(BasePage):
    URL         = "https://the-internet.herokuapp.com/javascript_alerts"
    ALERT_BTN   = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_BTN  = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT      = (By.ID, "result")

    def open(self):
        super().open(self.URL)

    def click_alert(self):
        self.click(self.ALERT_BTN)

    def click_confirm(self):
        self.click(self.CONFIRM_BTN)

    def click_prompt(self):
        self.click(self.PROMPT_BTN)

    def _wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())

    def accept(self):
        self._wait_for_alert().accept()

    def dismiss(self):
        self._wait_for_alert().dismiss()

    def send_text_to_alert(self, text):
        self._wait_for_alert().send_keys(text)

    def get_result_text(self):
        return self.get_text(self.RESULT)