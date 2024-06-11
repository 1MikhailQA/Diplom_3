from pages.basic_functionality_page import BasicFunctionality
import allure

class TestBasicFunctionality:
    @allure.step('Клик по кнопке "Конструктор"')
    def test_click_constructor_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.click_constructor_button()
        assert basic_functionality_page.check_assemble_the_burger()

    @allure.step('Клик по кнопке "Лента заказов"')
    def test_click_order_feed_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.click_order_feed_button()
        assert basic_functionality_page.check_title_ready()

    @allure.step('Клик по ингредиенту бургера')
    def test_click_ingredient_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.click_ingredient()
        assert basic_functionality_page.check_title_ingredient_details()

    @allure.step('Клик крестику')
    def test_click_close_button(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.click_ingredient()
        basic_functionality_page.click_close_button()
        assert basic_functionality_page.check_assemble_the_burger()

    @allure.step('Перетаскивание ингредиента в заказ и проверка увеличения счетчика')
    def test_drag_and_drop_ingredient_increases_counter(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        assert basic_functionality_page.get_count_value() == "2"

    @allure.step('Заказ авторизованным пользователем')
    def test_order_authorized_user(self, driver):
        basic_functionality_page = BasicFunctionality(driver)
        basic_functionality_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        assert basic_functionality_page.check_placing_order()


