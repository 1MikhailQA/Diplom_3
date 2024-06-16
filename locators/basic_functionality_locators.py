from selenium.webdriver.common.by import By

class BasicFunctionalityPages:
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    BUTTON_CONSTRUCTOR_MAIN = (By.XPATH, "//p[text() = 'Конструктор']")
    TITLE_ASSEMBLE_THE_BURGER = (By.XPATH, '//*[text() = "Соберите бургер"]')
    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(.,"Лента Заказов")]')
    TITLE_READY = (By.XPATH, '//*[text() = "Готовы:"]')
    BUTTON_INGREDIENT_R2_D3 = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    TITLE_INGREDIENT_DETAILS = (By.XPATH, '//*[text() = "Детали ингредиента"]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//button[@type='button' and contains(@class, 'Modal_modal__close')]")
    BASKET_ORDER = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter")]')
    BUTTON_ORDER = (By.XPATH, '//*[text()="Оформить заказ"]')
    ID_ORDER_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ID_ORDER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
