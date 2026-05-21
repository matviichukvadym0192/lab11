from pages.windows_page import WindowsPage

# Сценарій 1: відкрити нову вкладку, знайти без індексів 
def test_window_scenario_1(driver):
    page = WindowsPage(driver)
    page.open()
    original = page.get_current_window()
    page.click_here()
    page.wait_for_number_of_windows(2)
    page.switch_to_new_window(original)
    
    # Стабілізація: чекаємо завантаження елемента на новій сторінці
    page.wait_for_header()
    
    assert "New Window" in page.get_page_source()

# Сценарій 2: відкрити → закрити нову → повернутись → перевірити кнопку 
def test_window_scenario_2(driver):
    page = WindowsPage(driver)
    page.open()
    original = page.get_current_window()
    page.click_here()
    page.wait_for_number_of_windows(2)
    page.switch_to_new_window(original)
    page.close_window()
    page.switch_to_window(original)
    assert page.is_click_here_clickable()

# Сценарій 3: explicit wait замість прямого звернення до handles[1] 
def test_window_scenario_3(driver):
    page = WindowsPage(driver)
    page.open()
    original = page.get_current_window()
    page.click_here()
    page.wait_for_number_of_windows(2)   # чекаємо — не беремо одразу [1]
    page.switch_to_new_window(original)
    
    # Стабілізація: чекаємо завантаження елемента на новій сторінці
    page.wait_for_header()
    
    assert "New Window" in page.get_page_source()

# Сценарій 4: два кліки — три вкладки — перевірити кожну 
def test_window_scenario_4(driver):
    page = WindowsPage(driver)
    page.open()
    original = page.get_current_window()
    page.click_here()
    page.click_here()
    page.wait_for_number_of_windows(3)
    for window in page.get_all_windows():
        page.switch_to_window(window)
        if window == original:
            assert "Opening a new window" in page.get_page_source()
        else:
            # Стабілізація: перед перевіркою коду вкладки чекаємо її завантаження
            page.wait_for_header()
            assert "New Window" in page.get_page_source()