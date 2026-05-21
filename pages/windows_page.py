from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class WindowsPage(BasePage):
    URL            = "https://the-internet.herokuapp.com/windows"
    CLICK_HERE_BTN = (By.LINK_TEXT, "Click Here")

    def open(self):
        super().open(self.URL)

    def click_here(self):
        self.click(self.CLICK_HERE_BTN)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def wait_for_number_of_windows(self, expected_count):
        self.wait.until(EC.number_of_windows_to_be(expected_count))

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def switch_to_new_window(self, original_window):
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                return

    def close_window(self):
        self.driver.close()

    def is_click_here_clickable(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.CLICK_HERE_BTN))
            return True
        except Exception:
            return False

    def get_page_source(self):
        return self.driver.page_source
