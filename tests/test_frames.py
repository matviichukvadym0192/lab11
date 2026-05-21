from pages.nested_frames_page import NestedFramesPage

def test_nested_frames(driver):
    page = NestedFramesPage(driver)
    page.open()
    page.switch_to_top()
    page.switch_to_middle()
    assert page.get_content_text() == "MIDDLE"
