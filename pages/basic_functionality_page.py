from locators.main_locators import MainPage
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.basic_functionality_locators import BasicFunctionalityPages
from data import UserData
import allure

class BasicFunctionality(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.basic_functionality_page = None

    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_login_account_button_top(self):
        button = self.wait_and_find_element(*MainPage.LOGIN_BUTTON_MAIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Ввод email')
    def input_email(self):
        email_input = self.wait_and_find_element(*PersonalAccountLocators.EMAIL_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", email_input)
        self.click_element_with_retry(email_input)
        email_input.clear()
        email_input.send_keys(UserData.AUTH_EMAIL)

    @allure.step('Ввод пароля')
    def input_password(self):
        password_input = self.wait_and_find_element(*PersonalAccountLocators.PASSWORD_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", password_input)
        self.click_element_with_retry(password_input)
        password_input.clear()
        password_input.send_keys(UserData.AUTH_PASSWORD)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_button(self):
        button = self.wait_and_find_element(*PersonalAccountLocators.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Клик на кнопку "Конструктор"')
    def click_constructor_button(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.BUTTON_CONSTRUCTOR_MAIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Проверка наличия заголовка "Соберите бургер"')
    def check_assemble_the_burger(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.TITLE_ASSEMBLE_THE_BURGER)
        return element.is_displayed()

    @allure.step('Клик кнопки "Лента заказов"')
    def click_order_feed_button(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.BUTTON_ORDER_FEED)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Проверка наличия заголовка "Готовы"')
    def check_title_ready(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.TITLE_READY)
        return element.is_displayed()

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.BUTTON_INGREDIENT_R2_D3)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

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
        button = self.wait_and_find_element(*BasicFunctionalityPages.CLOSE_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_text(BasicFunctionalityPages.INGREDIENT_COUNTER)

    @allure.step('Перетаскивание ингредиента')
    def add_filling_to_order(self):
        self.find_element_clickable(BasicFunctionalityPages.BUTTON_INGREDIENT_R2_D3)
        self.drag_and_drop_on_element(BasicFunctionalityPages.BUTTON_INGREDIENT_R2_D3,
                                      BasicFunctionalityPages.BASKET_ORDER)

    @allure.step('Клик "Оформить заказ"')
    def click_order_button(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.BUTTON_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Получение текста "идентификатор заказа"')
    def check_placing_order(self):
        element = self.wait_and_find_element(*BasicFunctionalityPages.ID_ORDER_TEXT)
        return element.is_displayed()

    @allure.step('Предусловие входа в аккаунт')
    def personal_account_login(self):
        self.click_login_account_button_top()
        self.input_email()
        self.input_password()
        self.click_login_button()




