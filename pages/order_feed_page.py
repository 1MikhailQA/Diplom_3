from locators.main_locators import MainPage
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from locators.basic_functionality_locators import BasicFunctionalityPages
from locators.order_feed_locators import OrderFeed
from data import UserData
import allure

class OrderFeedPage(BasePage):
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

    @allure.step('Окно закрывается кликом по крестику')
    def click_close_button(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.CLOSE_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Клик кнопки "Лента заказов"')
    def click_order_feed_button(self):
        button = self.wait_and_find_element(*BasicFunctionalityPages.BUTTON_ORDER_FEED)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Предусловие оформления заказа и переход в ленту заказов')
    def placing_an_order(self):
        self.click_login_account_button_top()
        self.input_email()
        self.input_password()
        self.click_login_button()
        self.add_filling_to_order()
        self.click_order_button()
        self.click_close_button()
        self.click_order_feed_button()

    @allure.step('Клик на заказ в "Ленте заказов"')
    def click_order(self):
        button = self.wait_and_find_element(*OrderFeed.ORDER_OBJECT)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Проверяем открытие окно с деталями')
    def check_order_ready_title(self):
        element = self.wait_and_find_element(*OrderFeed.TITLE_ORDER_READY)
        return element.is_displayed()

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def found_order_at_feed(self, order_id):
        elements = self.find_until_all_elements_located(OrderFeed.ORDERS_AT_FEED)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Получение кол-ва заказов за сегодня')
    def get_total_count_today(self):
        self.find_element_visibility(OrderFeed.TOTAL_COUNT_TODAY)
        return self.get_text(OrderFeed.TOTAL_COUNT_TODAY)

