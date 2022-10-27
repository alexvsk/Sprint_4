from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators as OPL
from selenium.webdriver.common.keys import Keys

class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    # Ожидание формы заказа
    def wait_order_form_for_whom(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OPL.ORDER_FORM))

    # Название формы заказа
    def name_order_form(self):
        return self.driver.find_element(*OPL.ORDER_FORM_TEXT).text

    # Заполнение поля "Имя" в форме заказа
    def input_name(self, name):
        self.driver.find_element(*OPL.NAME).send_keys(name)

    # Заполнение поля "Фамилия" в форме заказа
    def input_surname(self, surname):
        self.driver.find_element(*OPL.SURNAME).send_keys(surname)

    # Заполнение поля "Адрес" в форме заказа
    def input_address(self, address):
        self.driver.find_element(*OPL.ADDRESS).send_keys(address)

    # Выбор станции метро в форме заказа
    def input_station(self, station):
        self.driver.find_element(*OPL.STATION).send_keys(station)
        self.driver.implicitly_wait(1)
        self.driver.find_element(*OPL.STATION).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*OPL.STATION).send_keys(Keys.ENTER)

    # Ввод номера телефона в форме заказа
    def input_phone(self, phone):
        self.driver.find_element(*OPL.PHONE).send_keys(phone)

    # Заполнение формы заказа "Для кого самокат"
    def input_order_form_for_whom(self, name, surname, address, station, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_station(station)
        self.input_phone(phone)

    # Клик по кнопке "Далее" в форме заказа
    def click_next_button(self):
        self.driver.find_element(*OPL.NEXT_BUTTON).click()

    # Ожидание формы заказа
    def wait_order_form_rent(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OPL.ORDER_FORM))

    def choice_delivery_date(self, date):
        self.driver.find_element(*OPL.DELIVERY_DATE).send_keys(date)
        self.driver.find_element(*OPL.CALENDAR).click()

    # Выбор срока аренды 7 дней в форме заказа
    def choice_seven_days_rent(self):
        self.driver.find_element(*OPL.RENTAL_DAYS_LIST).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*OPL.SEVEN_DAYS_RENT).click()
        self.driver.implicitly_wait(1)

    # Выбор цвета самоката "черный" в форме заказа
    def choice_black_scooter(self):
        self.driver.find_element(*OPL.BLACK_SCOOTER).click()
        self.driver.implicitly_wait(1)

    # Выбор срока аренды 1 день в форме заказа
    def choice_one_day_rent(self):
        self.driver.find_element(*OPL.RENTAL_DAYS_LIST).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*OPL.ONE_DAY_RENT).click()
        self.driver.implicitly_wait(1)

    # Выбор цвета цвета самоката "серый" в форме заказа
    def choice_grey_scooter(self):
        self.driver.find_element(*OPL.GREY_SCOOTER).click()
        self.driver.implicitly_wait(1)

    # Ввод комментария для курьера в форме заказа
    def input_comment(self, comment):
        self.driver.find_element(*OPL.COMMENT).send_keys(comment)

    # Клик по кнопке "Заказать" в форме заказа
    def click_order_button(self):
        self.driver.find_element(*OPL.ORDER_BUTTON).click()

    # Ожидание окна подтверждение заказа
    def wait_order_confirm_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OPL.ORDER_CONFIRM_FORM))

    # Клик по кнопке "Да" в окне подтверждения заказа
    def click_order_confirm_yes(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OPL.ORDER_CONFIRM_YES))
        self.driver.find_element(*OPL.ORDER_CONFIRM_YES).click()

    # Ожидание окна об успешном заказе
    def wait_order_done_window(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OPL.ORDER_DONE))

    # Текст сообщения об успешном заказе
    def message_order_done_window(self):
        span = self.driver.find_element(*OPL.ORDER_TEXT)
        text = self.driver.execute_script('return arguments[0].childNodes[0].nodeValue.trim()', span)
        return text

    # Клик по кнопке "Проверить статус" после совершения заказа
    def click_order_status_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OPL.ORDER_STATUS_BUTTON))
        self.driver.find_element(*OPL.ORDER_STATUS_BUTTON).click()

