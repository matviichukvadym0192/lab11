from pages.alerts_page import AlertsPage

def test_js_alert(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_alert()
    page.accept()
    assert "You successfully clicked an alert" in page.get_result_text()

def test_js_confirm(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_confirm()
    page.accept()
    assert "You clicked: Ok" in page.get_result_text()
    page.click_confirm()
    page.dismiss()
    assert "You clicked: Cancel" in page.get_result_text()

def test_js_prompt(driver):
    page = AlertsPage(driver)
    page.open()
    page.click_prompt()
    page.send_text_to_alert("Hello Selenium!")
    page.accept()
    assert "You entered: Hello Selenium!" in page.get_result_text()
