import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        logging.info(f"Відкриття сторінки: {url}")
        self.driver.get(url)

    def find(self, locator):
        logging.info(f"Пошук елемента: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        logging.info(f"Клік по елементу: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        logging.info(f"Введення тексту в елемент: {locator}")
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        text = self.find(locator).text
        logging.info(f"Отримано текст: '{text}'")
        return text

    def get_text_from_frame(self, frame_name, locator):
        logging.info(f"Отримання тексту з фрейму '{frame_name}'")
        self.driver.switch_to.default_content()
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(frame_name))
        text = self.get_text(locator)
        self.driver.switch_to.default_content()
        return text
