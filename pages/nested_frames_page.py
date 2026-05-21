from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class NestedFramesPage(BasePage):
    URL     = "https://the-internet.herokuapp.com/nested_frames"
    CONTENT = (By.ID, "content")

    def open(self):
        super().open(self.URL)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def switch_to_top(self):
        self.switch_to_default()
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it("frame-top"))

    def switch_to_middle(self):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it("frame-middle"))

    def switch_to_right(self):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it("frame-right"))

    def switch_to_bottom(self):
        self.switch_to_default()
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it("frame-bottom"))

    def get_content_text(self):
        return self.get_text(self.CONTENT)
