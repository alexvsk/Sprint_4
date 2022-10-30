from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as MPL
import time

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    # Клик по кнопке принятия куки "Да все привыкли"
    def click_cookie_button(self):
        if self.driver.find_element(*MPL.COOKIE_BUTTON):
            self.driver.find_element(*MPL.COOKIE_BUTTON).click()

    # Клик по кнопке "Заказать" вверху страницы
    def click_order_button_up(self):
        self.driver.find_element(*MPL.ORDER_BUTTON_UP).click()

    # Скролл до кнопки "Заказать" внизу страницы
    def scroll_to_order_button_down(self):
        elem1 = self.driver.find_element(*MPL.ORDER_BUTTON_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem1)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MPL.ORDER_BUTTON_DOWN))

    # Клик по кнопке "Заказать" внизу страницы
    def click_order_button_down(self):
        self.driver.find_element(*MPL.ORDER_BUTTON_DOWN).click()

    # Клик по первому заголовку сверху списка "Вопросы о важном"
    def click_head_first(self):
        self.driver.find_element(*MPL.HEAD_0).click()

    # Клик по второму заголовку сверху списка "Вопросы о важном"
    def click_head_second(self):
        self.driver.find_element(*MPL.HEAD_1).click()

    # Клик по третьему заголовку сверху списка "Вопросы о важном"
    def click_head_third(self):
        self.driver.find_element(*MPL.HEAD_2).click()

    # Клик по четвертому заголовку сверху списка "Вопросы о важном"
    def click_head_fourth(self):
        self.driver.find_element(*MPL.HEAD_3).click()

    # Клик по пятому заголовку сверху списка "Вопросы о важном"
    def click_head_fifth(self):
        self.driver.find_element(*MPL.HEAD_4).click()

    # Клик по шестому заголовку сверху списка "Вопросы о важном"
    def click_head_sixth(self):
        self.driver.find_element(*MPL.HEAD_5).click()

    # Клик по седьмому заголовку сверху списка "Вопросы о важном"
    def click_head_seventh(self):
        self.driver.find_element(*MPL.HEAD_6).click()

    # Клик по возьмому заголовку сверху списка "Вопросы о важном"
    def click_head_eighth(self):
        self.driver.find_element(*MPL.HEAD_7).click()

    # Текст при клике на первый заголовок списка "Вопросы о важном"
    def text_first(self):
        return self.driver.find_element(*MPL.TEXT_0).text

    # Текст при клике на второй заголовок списка "Вопросы о важном"
    def text_second(self):
        return self.driver.find_element(*MPL.TEXT_1).text

    # Текст при клике на третий заголовок списка "Вопросы о важном"
    def text_third(self):
        return self.driver.find_element(*MPL.TEXT_2).text

    # Текст при клике на четвертый заголовок списка "Вопросы о важном"
    def text_fourth(self):
        return self.driver.find_element(*MPL.TEXT_3).text

    # Текст при клике на пятый заголовок списка "Вопросы о важном"
    def text_fifth(self):
        return self.driver.find_element(*MPL.TEXT_4).text

    # Текст при клике на шестой заголовок списка "Вопросы о важном"
    def text_sixth(self):
        return self.driver.find_element(*MPL.TEXT_5).text

    # Текст при клике на седьмой заголовок списка "Вопросы о важном"
    def text_seventh(self):
        return self.driver.find_element(*MPL.TEXT_6).text

    # Текст при клике на восьмой заголовок списка "Вопросы о важном"
    def text_eighth(self):
        return self.driver.find_element(*MPL.TEXT_7).text


    # Ожидание загрузки главной страницы
    def wait_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPL.SCOOTER_IMG))


    # Скролл до последнего заголовка списка "Вопросы о важном"
    def scroll_to_last_head(self):
        elem = self.driver.find_element(*MPL.HEAD_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(MPL.HEAD_7))

    # Получение адреса страницы
    def get_url(self):
        return self.driver.current_url


    # Клик на лого скутера
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(MPL.SCOOTER_LOGO))
        self.driver.find_element(*MPL.SCOOTER_LOGO).click()


    # Клик на лого яндекса
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MPL.YANDEX_LOGO))
        self.driver.find_element(*MPL.YANDEX_LOGO).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(1)




