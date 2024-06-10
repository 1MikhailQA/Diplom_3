from pages.personal_account_page import PersonalAccount
import allure


class TestPersonalAccount:
    @allure.step('Переход по клику на «Личный кабинет» после авторизации')
    def test_click_personal_account_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        personal_account_page.click_login_account_button_top()
        personal_account_page.input_email()
        personal_account_page.input_password()
        personal_account_page.click_login_button()
        personal_account_page.click_personal_account_button()
        assert personal_account_page.check_profile_header()

    def test_click_history_orders_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        personal_account_page.personal_account_login()
        assert personal_account_page.click_history_orders() is True

    def test_click_exit_button(self, driver):
        personal_account_page = PersonalAccount(driver)
        personal_account_page.personal_account_login()
        personal_account_page.click_exit_button()
        assert personal_account_page.check_login_title()

