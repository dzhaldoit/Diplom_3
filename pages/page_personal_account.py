import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.ui_locators import Locators


@allure.title('Проверка "Личный Кабинет"')
class PagePersonalAccount:

    @allure.step('Открытие браузера')
    def open_browser(self, driver, web_url):
        driver.get(web_url)
        return self

    @allure.step('Авторизация')
    def authorization(self, driver, create_user):
        response_post, data = create_user
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["password"])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        return self

    @allure.step('Проверка что авторизация прошла успешно')
    def personal_account_check(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.LOGOUT_BUTTON)))
        return self

    @allure.step('Клик по кнопке "История заказов"')
    def history_order(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.HISTORY_ORDER_BUTTON)))
        driver.find_element(By.XPATH, Locators.HISTORY_ORDER_BUTTON).click()
        return self

    @allure.step('Клик по кнопке "Выход"')
    def logout(self, driver):
        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.TEXT_LOGOUT)))
        return self


personal_page = PagePersonalAccount()
