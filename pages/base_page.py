from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element_with_retry(self, element):
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            self.close_modal_if_present()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def close_modal_if_present(self):
        try:
            modal_overlay = self.driver.find_element(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            if modal_overlay.is_displayed():
                self.driver.execute_script("arguments[0].style.display = 'none';", modal_overlay)
        except NoSuchElementException:
            pass

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 5000);")

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url