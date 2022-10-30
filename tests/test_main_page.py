from pages.main_page import MainPage
import allure

class TestHeaders:

    @allure.title('Проверка первого вопроса в списке "Вопросы важном"')
    def test_first_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_first()
        driver.implicitly_wait(2)
        exp_result = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        act_result = main_page.text_first()
        assert act_result == exp_result

    @allure.title('Проверка второго вопроса в списке "Вопросы важном"')
    def test_second_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_second()
        driver.implicitly_wait(2)
        exp_result = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями," \
                     " можете просто сделать несколько заказов — один за другим."
        act_result = main_page.text_second()
        assert act_result == exp_result

    @allure.title('Проверка третьего вопроса в списке "Вопросы важном"')
    def test_third_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_third()
        driver.implicitly_wait(2)
        exp_result = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня." \
                     " Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру." \
                     " Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        act_result = main_page.text_third()
        assert act_result == exp_result

    @allure.title('Проверка четвертого вопроса в списке "Вопросы важном"')
    def test_fourth_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_fourth()
        driver.implicitly_wait(2)
        exp_result = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        act_result = main_page.text_fourth()
        assert act_result == exp_result

    @allure.title('Проверка пятого вопроса в списке "Вопросы важном"')
    def test_fifth_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_fifth()
        driver.implicitly_wait(2)
        exp_result = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку" \
                     " по красивому номеру 1010."
        act_result = main_page.text_fifth()
        assert act_result == exp_result

    @allure.title('Проверка шестого вопроса в списке "Вопросы важном"')
    def test_sixth_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_sixth()
        driver.implicitly_wait(2)
        exp_result = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если" \
                     " будете кататься без передышек и во сне. Зарядка не понадобится."
        act_result = main_page.text_sixth()
        assert act_result == exp_result

    @allure.title('Проверка седьмого вопроса в списке "Вопросы важном"')
    def test_seventh_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_seventh()
        driver.implicitly_wait(2)
        exp_result = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим." \
                     " Все же свои."
        act_result = main_page.text_seventh()
        assert act_result == exp_result

    @allure.title('Проверка восьмого вопроса в списке "Вопросы важном"')
    def test_eighth_head(self, driver, preconditions):
        main_page = MainPage(driver)
        main_page.click_head_eighth()
        driver.implicitly_wait(2)
        exp_result = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        act_result = main_page.text_eighth()
        assert act_result == exp_result






