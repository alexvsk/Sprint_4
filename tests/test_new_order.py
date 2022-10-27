from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
import allure

class TestNewOrder:

    @allure.title('Проверка сценария создания нового заказа через кнопку "Заказать" вверху страницы')
    def test_new_order_by_button_up(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
        main_page.wait_main_page()
        main_page.click_cookie_button()
        main_page.click_order_button_up()
        order_page.wait_order_form_for_whom()

        name = "Эдвард"
        surname = "Сноуден"
        address = "ул. Безопасная"
        station = "Выхино"
        phone = "89992230102"

        order_page.input_order_form_for_whom(name, surname, address, station, phone)
        order_page.click_next_button()
        order_page.wait_order_form_rent()

        date = "11.11.2022"
        comment = "Оставьте около двери"

        order_page.choice_delivery_date(date)
        order_page.choice_seven_days_rent()
        order_page.choice_black_scooter()
        order_page.input_comment(comment)
        order_page.click_order_button()

        order_page.wait_order_confirm_window()
        order_page.click_order_confirm_yes()
        order_page.wait_order_done_window()

        assert order_page.message_order_done_window() == "Заказ оформлен"

    @allure.title('Проверка сценария создания нового заказа через кнопку "Заказать" внизу страницы')
    def test_new_order_by_button_down(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
        main_page.wait_main_page()
        main_page.click_cookie_button()
        main_page.scroll_to_order_button_down()
        main_page.click_order_button_down()
        order_page.wait_order_form_for_whom()

        name = "Петр"
        surname = "Иванов"
        address = "ул. Большая Семеновская"
        station = "Электрозаводская"
        phone = "89775567711"

        order_page.input_order_form_for_whom(name, surname, address, station, phone)
        order_page.click_next_button()
        order_page.wait_order_form_rent()

        date = "12.12.2022"
        comment = "Если не будет дома - оставьте соседям"

        order_page.choice_delivery_date(date)
        order_page.choice_seven_days_rent()
        order_page.choice_grey_scooter()
        order_page.input_comment(comment)
        order_page.click_order_button()

        order_page.wait_order_confirm_window()
        order_page.click_order_confirm_yes()
        order_page.wait_order_done_window()

        assert order_page.message_order_done_window() == "Заказ оформлен"

    @allure.title('Проверка открытия нового окна в браузере (вкладки) при нажатии на логотип Яндекса на странице статуса заказа')
    def test_click_yandex_logo(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
        main_page.wait_main_page()
        main_page.click_cookie_button()
        main_page.click_order_button_up()
        order_page.wait_order_form_for_whom()

        name = "Эдвард"
        surname = "Сноуден"
        address = "ул. Безопасная"
        station = "Выхино"
        phone = "89992230102"

        order_page.input_order_form_for_whom(name, surname, address, station, phone)
        order_page.click_next_button()
        order_page.wait_order_form_rent()

        date = "11.11.2022"
        comment = "Оставьте около двери"

        order_page.choice_delivery_date(date)
        order_page.choice_seven_days_rent()
        order_page.choice_black_scooter()
        order_page.input_comment(comment)
        order_page.click_order_button()

        order_page.wait_order_confirm_window()
        order_page.click_order_confirm_yes()
        order_page.wait_order_done_window()
        order_page.click_order_status_button()

        main_page.click_yandex_logo()

        assert main_page.get_url() == "https://dzen.ru/?yredirect=true"


    @allure.title('Проверка перехода на главнуюю страницу при нажатии на логотип "Самоката" на странице статуса заказа')
    def test_click_scooter(self, driver):
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
        main_page.wait_main_page()
        main_page.click_cookie_button()
        main_page.click_order_button_up()
        order_page.wait_order_form_for_whom()

        name = "Петр"
        surname = "Иванов"
        address = "ул. Большая Семеновская"
        station = "Электрозаводская"
        phone = "89775567711"

        order_page.input_order_form_for_whom(name, surname, address, station, phone)
        order_page.click_next_button()
        order_page.wait_order_form_rent()

        date = "12.12.2022"
        comment = "Если не будет дома - оставьте соседям"

        order_page.choice_delivery_date(date)
        order_page.choice_seven_days_rent()
        order_page.choice_black_scooter()
        order_page.input_comment(comment)
        order_page.click_order_button()

        order_page.wait_order_confirm_window()
        order_page.click_order_confirm_yes()
        order_page.wait_order_done_window()
        order_page.click_order_status_button()

        main_page.click_scooter_logo()
        main_page.wait_main_page()

        assert main_page.get_url() == "https://qa-scooter.praktikum-services.ru/"







