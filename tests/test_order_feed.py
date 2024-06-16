from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccount
from pages.basic_functionality_page import BasicFunctionality
import allure

class TestOrderFeed:
    @allure.title('Клик по заказу в "Ленте заказов"')
    def test_click_order_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        basic_functionality_page.click_close_button()
        basic_functionality_page.click_order_feed_button()
        order_feed_page.click_order()
        assert order_feed_page.check_order_ready_title()

    @allure.title('Проверка совпадения id в ленте заказов и в истории заказов')
    def test_find_order_in_list(self, driver):
        personal_account_page = PersonalAccount(driver)
        basic_functionality_page = BasicFunctionality(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        order_id = basic_functionality_page.get_order_id()
        basic_functionality_page.click_close_button()
        personal_account_page.click_personal_account_button()
        personal_account_page.click_history_orders()
        assert personal_account_page.found_order_at_history(order_id) is False

    @allure.title('Проверка изменения счетчика заказов за сегодня')
    def test_today_orders_counter(self, driver):
        order_feed_page = OrderFeedPage(driver)
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.click_order_feed_button()
        pre_count = order_feed_page.get_total_count_today()
        basic_functionality_page.click_constructor_button()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        basic_functionality_page.click_close_button()
        basic_functionality_page.click_order_feed_button()
        post_count = order_feed_page.get_total_count_today()
        assert post_count > pre_count, 'Счетчик не изменился'

    @allure.title('Проверка появления только что созданного заказа в ленте заказов')
    def test_new_order_at_order_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        basic_functionality_page = BasicFunctionality(driver)
        personal_account_page = PersonalAccount(driver)

        basic_functionality_page.click_login_account_button_top()
        personal_account_page.personal_account_login()
        basic_functionality_page.add_filling_to_order()
        basic_functionality_page.click_order_button()
        order_id = basic_functionality_page.get_order_id()
        basic_functionality_page.click_close_button()
        basic_functionality_page.click_order_feed_button()
        assert order_feed_page.found_order_at_feed(order_id) is False

