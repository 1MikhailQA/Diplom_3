from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from data import Urls
from data import UserData
import allure

class PersonalAccount(BasePage):

    @allure.step('Ввод email')
    def input_email(self):
        email_input = self.wait_and_find_element(*PersonalAccountLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(UserData.AUTH_EMAIL)

    @allure.step('Ввод пароля')
    def input_password(self):
        password_input = self.wait_and_find_element(*PersonalAccountLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(UserData.AUTH_PASSWORD)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_button(self):
        self.click_element_with_retry(*PersonalAccountLocators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку "Личный кабинет')
    def click_personal_account_button(self):
        self.click_element_with_retry(*PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON_MAIN)

    @allure.step('Проверка наличия кнопки "Профиль" в "Личном кабинете"')
    def check_profile_header(self):
        element = self.wait_and_find_element(*PersonalAccountLocators.PROFILE_HEADER)
        return element.is_displayed()

    @allure.step('Переход во вкладку "История заказов"')
    def click_history_orders(self):
        self.click_element_with_retry(*PersonalAccountLocators.HISTORY_ORDERS_BUTTON)
        return self.get_url() == Urls.MAIN_PAGE + Urls.HISTORY_PAGE

    @allure.step("Проверка нахождения идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.find_until_all_elements_located(*PersonalAccountLocators.ORDERS_AT_HISTORY)
        for element in elements:
            print(f"Checking order ID in history: {element.text}")
            if order_id == element.text:
                return True
        return False

    @allure.step('Клик по кнопке "Выход"')
    def click_exit_button(self):
        self.click_element_with_retry(*PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Проверка наличия заголовка "Вход", после выхода из личного кабинета')
    def check_login_title(self):
        element = self.wait_and_find_element(*PersonalAccountLocators.LOGIN_NAME)
        return element.is_displayed()

    @allure.step('Предусловие перехода в "Личный кабинет"')
    def personal_account_login(self):
        self.input_email()
        self.input_password()
        self.click_login_button()






