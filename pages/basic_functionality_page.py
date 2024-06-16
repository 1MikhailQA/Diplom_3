from pages.base_page import BasePage
from locators.basic_functionality_locators import BasicFunctionalityPages
import allure

class BasicFunctionality(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.basic_functionality_page = None

    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_login_account_button_top(self):
        self.click_element_with_retry(*BasicFunctionalityPages.LOGIN_BUTTON_MAIN)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element_with_retry(*BasicFunctionalityPages.BUTTON_CONSTRUCTOR_MAIN)

    @allure.step('Проверка наличия заголовка "Соберите бургер"')
    def check_assemble_the_burger(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.TITLE_ASSEMBLE_THE_BURGER)
        return element.is_displayed()

    @allure.step('Клик кнопки "Лента заказов"')
    def click_order_feed_button(self):
        self.click_element_with_retry(*BasicFunctionalityPages.BUTTON_ORDER_FEED)

    @allure.step('Проверка наличия заголовка "Готовы"')
    def check_title_ready(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.TITLE_READY)
        return element.is_displayed()

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_element_with_retry(*BasicFunctionalityPages.BUTTON_INGREDIENT_R2_D3)

    @allure.step('Проверка наличия заголовка "Детали ингредиента"')
    def check_title_ingredient_details(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.TITLE_INGREDIENT_DETAILS)
        return element.is_displayed()

    @allure.step('Получение id заказа')
    def get_order_id(self):
        self.wait_and_find_element(*BasicFunctionalityPages.ID_ORDER_TEXT)
        order_id = self.get_text(*BasicFunctionalityPages.ID_ORDER)
        while order_id == '9999':
            order_id = self.get_text(*BasicFunctionalityPages.ID_ORDER)
        return f"{order_id}"

    @allure.step('Окно закрывается кликом по крестику')
    def click_close_button(self):
        self.click_element_with_retry(*BasicFunctionalityPages.CLOSE_BUTTON_LOCATOR)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_text(BasicFunctionalityPages.INGREDIENT_COUNTER)

    @allure.step('Перетаскивание ингредиента')
    def add_filling_to_order(self):
        self.drag_and_drop_on_element(BasicFunctionalityPages.BUTTON_INGREDIENT_R2_D3,
                                      BasicFunctionalityPages.BASKET_ORDER)

    @allure.step('Клик "Оформить заказ"')
    def click_order_button(self):
        self.click_element_with_retry(*BasicFunctionalityPages.BUTTON_ORDER)
    @allure.step('Получение текста "идентификатор заказа"')
    def check_placing_order(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.ID_ORDER_TEXT)
        return element.is_displayed()

