from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    PERSONAL_ACCOUNT_BUTTON_MAIN = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    PROFILE_HEADER = (By.XPATH, "//a[text() = 'Профиль']")
    HISTORY_ORDERS_BUTTON = (By.XPATH, '//*[@href="/account/order-history"]')
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    LOGIN_NAME = (By.XPATH, "//h2[text() = 'Вход']")
