import pytest
from selenium import webdriver
from pages.main_page import MainPage
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='function')
def driver():
    path_driver = Service('V:/WebDriver/bin/geckodriver.exe')
    driver = webdriver.Firefox(service=path_driver)
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def preconditions(driver):
    main_page = MainPage(driver)
    main_page.wait_main_page()
    main_page.click_cookie_button()
    main_page.scroll_to_last_head()


