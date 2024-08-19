import allure
from selenium.webdriver.common.by import By

from locators.ui_locators import Locators
from pages.page_password_recovery import web_page


@allure.suite('Восстановление пароля')
class TestRecoveryUsers:
    @allure.title('Кнопка "Восстановить пароль"')
    def test_recovery_button(self, driver, web_url):
        with allure.step('Открытие браузера'):
            web_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Восстановить пароль"'):
            web_page.lk_bottom_and_recovery(driver)

        assert driver.find_element(By.XPATH, Locators.TEXT_RECOVERY).is_displayed()

    @allure.title('Отправка почты и клик по кнопке "Сохранить"')
    def test_send_email_and_click_button(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            web_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Восстановить пароль"'):
            web_page.lk_bottom_and_recovery(driver)
        with allure.step('Отправка почты и клик по кнопке "Сохранить"'):
            web_page.send_email_and_click_button(driver, create_user)

        assert driver.find_element(By.XPATH, Locators.SAVE_BUTTON).is_displayed()

    @allure.title('Новый пароль')
    def test_new_password(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            web_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Восстановить пароль"'):
            web_page.lk_bottom_and_recovery(driver)
        with allure.step('Отправка почты и клик по кнопке "Сохранить"'):
            web_page.send_email_and_click_button(driver, create_user)
        with allure.step('Новый пароль'):
            web_page.new_password(driver)
        with allure.step('Клик по кнопке "Показать пароль"'):
            web_page.eye_button(driver)

        assert driver.find_element(By.XPATH, Locators.TEXT_PASSWORD_RECOVERY).is_displayed()
