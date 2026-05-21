import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Forgot password basic test")
def test_forgot_password(driver):
    driver.get("https://the-internet.herokuapp.com/forgot_password")
    email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    assert driver.find_element(By.TAG_NAME, "h2").text == "Forgot Password"
    email.send_keys("test@test.com")
    assert email.get_attribute("value") == "test@test.com"
    submit = driver.find_element(By.ID, "form_submit")
    assert submit.is_displayed() and submit.is_enabled()


