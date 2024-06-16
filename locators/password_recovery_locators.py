from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    LOGIN_BUTTON_RECOVERY_PASSWORD = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    NAME_PAGE_RECOVERY_PASSWORD = (By.XPATH, "//div[@class='Auth_login__3hAey']//h2[text()='Восстановление пароля']")
    EMAIL_INPUT = (By.XPATH, '//*[@name = "name"]')
    RECOVERY_BUTTON = (By.XPATH, '//*[text() = "Восстановить"]')
    BUTTON_SHOW_HIDE = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")
    PASSWORD_INPUT = (By.XPATH, '//*[@name="Введите новый пароль"]')
    ACTIVE_FIELD_PASSWORD = (By.XPATH, ".//div[contains(@class,'input_status_active')]")