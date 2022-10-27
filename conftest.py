import pytest
from selenium import webdriver
from pages.main_page import MainPageScooter

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox(executable_path=r'V:\WebDriver\bin\geckodriver.exe')
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def preconditions(driver):
    main_page = MainPageScooter(driver)
    main_page.wait_main_page()
    main_page.click_cookie_button()
    main_page.scroll_to_last_head()


