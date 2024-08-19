import allure
from selenium.webdriver.common.by import By

from pages.page_personal_account import personal_page
from locators.ui_locators import Locators
from data import Urls


@allure.suite('Проверка "Личный кабинет"')
class TestPersonalAccount:
    @allure.title('Авторизация и проверка "Личный кабинет"')
    def test_personal_account_check(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            personal_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            personal_page.authorization(driver, create_user)
        with allure.step('Проверка "Личного кабинета"'):
            personal_page.personal_account_check(driver)

        assert driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).is_displayed()

    @allure.title('Проверка "История заказов"')
    def test_history_order(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            personal_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            personal_page.authorization(driver, create_user)
        with allure.step('Проверка "Личного кабинета"'):
            personal_page.personal_account_check(driver)
        with allure.step('Проверка "Истории заказов"'):
            personal_page.history_order(driver)

        assert driver.current_url == Urls.LIST_ORDER

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            personal_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            personal_page.authorization(driver, create_user)
        with allure.step('Проверка "Личного кабинета"'):
            personal_page.personal_account_check(driver)
        with allure.step('Выход из аккаунта'):
            personal_page.logout(driver)

        assert driver.find_element(By.XPATH, Locators.TEXT_LOGOUT).is_displayed()
