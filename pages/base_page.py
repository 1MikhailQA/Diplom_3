from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element_with_retry(self, element):
        try:
            element.click()
        except ElementClickInterceptedException:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 5000);")

    def open_url(self, url):
        self.driver.get(url)