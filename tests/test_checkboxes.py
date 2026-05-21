from pages.checkboxes_page import CheckboxesPage

def test_checkboxes(driver):
    page = CheckboxesPage(driver)
    page.open()
    page.select_all()
    assert not page.all_selected()
