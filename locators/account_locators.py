from selenium.webdriver.common.by import By


class AccountLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'
    EMAIL_INPUT = By.XPATH, './/input[@type="text"]'
    PASSWORD_INPUT = By.XPATH, './/input[@type="password"]'
    LOGIN_BUTTON = By.XPATH, './/button[text()="Войти"]'
    LOGOUT_BUTTON = By.XPATH, './/button[text()="Выход"]'
    TEXT_LOGIN = By.XPATH, './/h2[text()="Вход"]'
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'