from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    ElementNotInteractableException, TimeoutException
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

    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f'Cant find element by locator {locator}')

    def close_modal_if_present(self):
        try:
            modal_overlay = self.driver.find_element(By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            if modal_overlay.is_displayed():
                self.driver.execute_script("arguments[0].style.display = 'none';", modal_overlay)
        except NoSuchElementException:
            pass

    def set_text(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    def check_exist_element(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def return_text_element(self, locator):
        self.wait_and_find_element(locator)
        text = self.driver.find_element(*locator).text
        return text

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 5000);")

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url


    def find_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def drag_and_drop_on_element(self, source_locator, target_locator):
        source_element = self.wait_and_find_element(*source_locator)
        target_element = self.wait_and_find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))


