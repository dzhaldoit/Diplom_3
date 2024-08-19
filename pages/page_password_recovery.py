import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import RandomUsers
from locators.ui_locators import Locators


@allure.title('Проверка "Восстановление пароля"')
class PasswordRecoveryPage:

    @allure.step('Открытие браузера')
    def open_browser(self, driver, web_url):
        driver.get(web_url)
        return self

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def lk_bottom_and_recovery(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.RECOVERY_PASSWORD_BUTTON)))
        driver.find_element(By.XPATH, Locators.RECOVERY_PASSWORD_BUTTON).click()
        return self

    @allure.step('Ввод email и нажатие кнопки "Восстановить"')
    def send_email_and_click_button(self, driver, create_user):
        response_post, data = create_user
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.RECOVERY_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.SAVE_BUTTON)))
        return self

    @allure.step('Ввод нового пароля')
    def new_password(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.PASSWORD_INPUT)))
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(
            RandomUsers.generate_random_data().get("password"))
        return self

    @allure.step('Клик по кнопке "Показать пароль"')
    def eye_button(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.EYE_BUTTON)))
        driver.find_element(By.XPATH, Locators.EYE_BUTTON).click()
        return self


web_page = PasswordRecoveryPage()
