from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeed
import allure

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на заказ в "Ленте заказов"')
    def click_order(self):
        self.click_element_with_retry(*OrderFeed.ORDER_OBJECT)

    @allure.step('Проверяем открытие окно с деталями')
    def check_order_ready_title(self):
        element = self.wait_and_find_element(*OrderFeed.TITLE_ORDER_READY)
        return element.is_displayed()

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def found_order_at_feed(self, order_id):
        elements = self.find_until_all_elements_located(*OrderFeed.ORDERS_AT_FEED)
        for element in elements:
            print(f"Checking order ID in feed: {element.text}")
            if order_id == element.text:
                return True
        return False

    @allure.step('Получение кол-ва заказов за сегодня')
    def get_total_count_today(self):
        return self.get_text(*OrderFeed.TOTAL_COUNT_TODAY)

