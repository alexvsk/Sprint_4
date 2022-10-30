from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME = (By.XPATH, ".//input[@placeholder='* Имя']")  # Поле "Имя" в форме заказа
    SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")  # Поле "Фамилия" в форме заказа
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")  # "Адрес"
    STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")  # "Станция метро"
    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")  # "Телефон"
    NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")   # Кнопка "далее" в форме заказа
    ORDER_FORM = (By.CLASS_NAME, "Order_Form__17u6u")  # Форма заказа

    DELIVERY_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  #  Поле "Когда привезти самокат" в форме заказа
    CALENDAR = (By.XPATH, ".//div[contains(@class, 'day--selected')]")   # Дата в календаре
    RENTAL_DAYS_LIST = (By.XPATH, ".//span[@class='Dropdown-arrow']")    # Выпадающий список количества дней аренды
    ONE_DAY_RENT = (By.XPATH, ".//div[@class='Dropdown-menu']/div[1]")   # Один день аренды
    SEVEN_DAYS_RENT = (By.XPATH, ".//div[@class='Dropdown-menu']/div[last()]")   # Семь дней аренды
    BLACK_SCOOTER = (By.ID, "black")   # Черный цвет самоката
    GREY_SCOOTER = (By.ID, "grey")  # Серый цвет самоката
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")  #  Комментарий для курьера
    ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[2]")
    ORDER_CONFIRM_FORM = (By.CLASS_NAME, "Order_Modal__YZ-d3")  # Окно подтверждение заказа
    ORDER_CONFIRM_YES = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")  # Кнопка "Да"

    ORDER_DONE = (By.CLASS_NAME, "Order_Modal__YZ-d3")   # Окно об успешном заказе
    ORDER_TEXT = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']")  # Текст сообщения об успешном заказе
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")  # Кнопка "Проверить статус"






