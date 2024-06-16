from pages.basic_functionality_page import BasicFunctionality
from pages.personal_account_page import PersonalAccount
import allure

class TestBasicFunctionality:
    @allure.title('Клик по кнопке "Конструктор"')
    def test_click_constructor_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.click_constructor_button()
        assert basic_functionality_page.check_assemble_the_burger()

    @allure.title('Клик по кнопке "Лента заказов"')
    def test_click_order_feed_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.click_order_feed_button()
        assert basic_functionality_page.check_title_ready()

    @allure.title('Клик по ингредиенту бургера')
    def test_click_ingredient_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.click_ingredient()
        assert basic_functionality_page.check_title_ingredient_details()

    @allure.title('Клик крестику')
    def test_click_close_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.click_ingredient()
        basic_functionality_page.click_close_button()
        assert basic_functionality_page.check_assemble_the_burger()

    @allure.title('Перетаскивание ингредиента в заказ и проверка увеличения счетчика')
    def test_drag_and_drop_ingredient_increases_counter(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        assert basic_functionality_page.get_count_value() == "2"

    @allure.title('Заказ авторизованным пользователем')
    def test_order_authorized_user(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        assert basic_functionality_page.check_placing_order()


