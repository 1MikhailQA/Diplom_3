from pages.password_recovery_page import PasswordRecovery
from pages.basic_functionality_page import BasicFunctionality
import allure


class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_page(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.click_login_account_button_top()
        password_recovery_page.click_password_recovery_button()
        assert password_recovery_page.is_check_name_page()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_page(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        password_recovery_page.open_page_recovery_password()
        password_recovery_page.input_email()
        password_recovery_page.click_recovery_button()
        assert password_recovery_page.is_check_button_show_hide()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_check_click_show_hide(self, driver):
        password_recovery_page = PasswordRecovery(driver)
        password_recovery_page.precondition_for_click_show_hide()
        password_recovery_page.input_new_password()
        password_recovery_page.click_click_show_hide()
        assert password_recovery_page.is_check_field_active_password
