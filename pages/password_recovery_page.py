from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
from data import UserData
from data import Urls
import allure

class PasswordRecovery(BasePage):

    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_password_recovery_button(self):
        self.click_element_with_retry(*PasswordRecoveryLocators.LOGIN_BUTTON_RECOVERY_PASSWORD)

    @allure.step('Проверяем наличие заголовка "Восстановление пароля"')
    def is_check_name_page(self):
        element = self.wait_and_find_element(*PasswordRecoveryLocators.NAME_PAGE_RECOVERY_PASSWORD)
        return element.is_displayed()

    @allure.step('Открытие страницы "Восстановление пароля"')
    def open_page_recovery_password(self):
        self.open_url(f'{Urls.MAIN_PAGE}{Urls.RECOVERY_PASSWORD_PAGE}')

    @allure.step('Ввод email для восстановления')
    def input_email(self):
        email_input = self.wait_and_find_element(*PasswordRecoveryLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(UserData.AUTH_EMAIL)

    @allure.step('Клик кнопки "Восстановить"')
    def click_recovery_button(self):
        self.click_element_with_retry(*PasswordRecoveryLocators.RECOVERY_BUTTON)

    @allure.step('Проверяем наличие кнопки показать/скрыть пароль')
    def is_check_button_show_hide(self):
        element = self.wait_and_find_element(*PasswordRecoveryLocators.BUTTON_SHOW_HIDE)
        return element.is_displayed()

    @allure.step('Ввод нового пароля')
    def input_new_password(self):
        password_input = self.wait_and_find_element(*PasswordRecoveryLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(UserData.AUTH_PASSWORD)

    @allure.step('Клик кнопки показать/скрыть пароль')
    def click_click_show_hide(self):
        self.click_element_with_retry(*PasswordRecoveryLocators.BUTTON_SHOW_HIDE)

    @allure.step('Проверяем активность поля для ввода пароля')
    def is_check_field_active_password(self):
        element = self.wait_and_find_element(*PasswordRecoveryLocators.ACTIVE_FIELD_PASSWORD)
        return element.is_displayed()

    @allure.step('Предусловие для клика по кнопке показать/скрыть пароль')
    def precondition_for_click_show_hide(self):
        self.open_page_recovery_password()
        self.input_email()
        self.click_recovery_button()
