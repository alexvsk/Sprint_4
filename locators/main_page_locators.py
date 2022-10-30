from selenium.webdriver.common.by import By


class MainPageLocators:
    HEAD_0 = (By.XPATH, ".//div[@id='accordion__heading-0']")  # Заголовок списка «Вопросы о важном» 1 сверху
    HEAD_1 = (By.XPATH, ".//div[@id='accordion__heading-1']")  # Заголовок списка «Вопросы о важном» 2 сверху
    HEAD_2 = (By.XPATH, ".//div[@id='accordion__heading-2']")  # Заголовок списка «Вопросы о важном» 3 сверху
    HEAD_3 = (By.XPATH, ".//div[@id='accordion__heading-3']")  # Заголовок списка «Вопросы о важном» 4 сверху
    HEAD_4 = (By.XPATH, ".//div[@id='accordion__heading-4']")  # Заголовок списка «Вопросы о важном» 5 сверху
    HEAD_5 = (By.XPATH, ".//div[@id='accordion__heading-5']")  # Заголовок списка «Вопросы о важном» 6 сверху
    HEAD_6 = (By.XPATH, ".//div[@id='accordion__heading-6']")  # Заголовок списка «Вопросы о важном» 7 сверху
    HEAD_7 = (By.XPATH, ".//div[@id='accordion__heading-7']")  # Заголовок списка «Вопросы о важном» 8 сверху
    TEXT_0 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")  # Текст при открытии заголовка 1 списка «Вопросы о важном»
    TEXT_1 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")  # Текст при открытии заголовка 2 списка «Вопросы о важном»
    TEXT_2 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")  # Текст при открытии заголовка 3 списка «Вопросы о важном»
    TEXT_3 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")  # Текст при открытии заголовка 4 списка «Вопросы о важном»
    TEXT_4 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")  # Текст при открытии заголовка 5 списка «Вопросы о важном»
    TEXT_5 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")  # Текст при открытии заголовка 6 списка «Вопросы о важном»
    TEXT_6 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")  # Текст при открытии заголовка 7 списка «Вопросы о важном»
    TEXT_7 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")  # Текст при открытии заголовка 8 списка «Вопросы о важном»
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка куки "да все привыкли"
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")  # Логотип "Самокат"
    SCOOTER_IMG = (By.XPATH, ".//img[@alt='Scooter blueprint']")  # Изображение самоката
    ORDER_BUTTON_UP = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[1]")  # Кнопка "Заказать" вверху страницы
    ORDER_BUTTON_DOWN = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button")  # Кнопка "Заказать" внизу страницы
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")  # Логотип "Яндекс"


