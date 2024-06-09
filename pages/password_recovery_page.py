import data
from locators.main_locators import MainPage
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage
from data import UserData
from data import Urls
import allure




class PasswordRecovery(BasePage):
    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_login_button_top(self):
        button = self.wait_and_find_element(*MainPage.LOGIN_BUTTON_MAIN)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Кликаем на кнопку "Восстановить пароль"')
    def click_password_recovery_button(self):
        button = self.wait_and_find_element(*PasswordRecoveryLocators.LOGIN_BUTTON_RECOVERY_PASSWORD)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

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
        self.driver.execute_script("arguments[0].scrollIntoView();", email_input)
        self.click_element_with_retry(email_input)
        email_input.clear()
        email_input.send_keys(UserData.AUTH_EMAIL)

    @allure.step('Клик кнопки "Восстановить"')
    def click_recovery_button(self):
        button = self.wait_and_find_element(*PasswordRecoveryLocators.RECOVERY_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Проверяем наличие кнопки показать/скрыть пароль')
    def is_check_button_show_hide(self):
        element = self.wait_and_find_element(*PasswordRecoveryLocators.BUTTON_SHOW_HIDE)
        return element.is_displayed()

    @allure.step('Ввод нового пароля')
    def input_new_password(self):
        new_password_input = self.wait_and_find_element(*PasswordRecoveryLocators.PASSWORD_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView();", new_password_input)
        self.click_element_with_retry(new_password_input)
        new_password_input.clear()
        new_password_input.send_keys(UserData.AUTH_PASSWORD)

    @allure.step('Клик кнопки показать/скрыть пароль')
    def click_click_show_hide(self):
        button = self.wait_and_find_element(*PasswordRecoveryLocators.BUTTON_SHOW_HIDE)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.click_element_with_retry(button)

    @allure.step('Проверяем активность поля для ввода пароля')
    def is_check_field_active_password(self):
        element = self.wait_and_find_element(*PasswordRecoveryLocators.ACTIVE_FIELD_PASSWORD)
        return element.is_displayed()

    @allure.step('Предусловие для клика по кнопке показать/скрыть пароль')
    def precondition_for_click_show_hide(self):
        self.open_page_recovery_password()
        self.input_email()
        self.click_recovery_button()


