from selenium.webdriver.common.by import By

class OrderFeed:
    ORDER_OBJECT = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    TITLE_ORDER_READY = (By.CSS_SELECTOR, "p.text.text_type_main-default.mb-15")
    ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")
    TOTAL_COUNT_TODAY = (By.XPATH, '//*[text() = "Выполнено за сегодня:"]/following::*[@class][1]')