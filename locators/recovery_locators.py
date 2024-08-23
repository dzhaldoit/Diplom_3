from selenium.webdriver.common.by import By


class RecoveryLocators:
    TEXT_RECOVERY = By.XPATH, './/h2[text()="Восстановление пароля"]'
    RECOVERY_PASSWORD_BUTTON = By.XPATH, './/a[text() ="Восстановить пароль"]'
    RECOVERY_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'
    EYE_BUTTON = By.XPATH, '//div[contains(@class, "input_status_active")]'
    PASSWORD_INPUT_ACTIVE = By.XPATH, '//div[contains(@class, "input_status_active")]'
