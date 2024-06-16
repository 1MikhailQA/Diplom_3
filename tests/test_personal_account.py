from pages.personal_account_page import PersonalAccount
from pages.basic_functionality_page import BasicFunctionality
import allure


class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет» после авторизации')
    def test_click_personal_account_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        basic_functionality_page = BasicFunctionality(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.input_email()
        personal_account_page.input_password()
        personal_account_page.click_login_button()
        personal_account_page.click_personal_account_button()
        assert personal_account_page.check_profile_header()

    @allure.title('Переход по клику на «История заказов» после авторизации')
    def test_click_history_orders_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        basic_functionality_page = BasicFunctionality(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        personal_account_page.click_personal_account_button()
        assert personal_account_page.click_history_orders() is True

    @allure.title('Переход по клику на «Выход» после авторизации')
    def test_click_exit_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        basic_functionality_page = BasicFunctionality(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        personal_account_page.click_personal_account_button()
        personal_account_page.click_exit_button()
        assert personal_account_page.check_login_title()

