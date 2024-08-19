import allure
from selenium.webdriver.common.by import By

from helpers import not_visible_element
from locators.ui_locators import Locators
from pages.page_basic_functionality import base_page


@allure.suite('Проверка основного функционала')
class TestBasicFunctionality:
    @allure.title('Проверка Конструктора')
    def test_constructor(self, driver, web_url):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Лист заказов"'):
            base_page.click_list_orders(driver)
        with allure.step('Клик по кнопке "Конструктор"'):
            base_page.click_on_constructor(driver)

        assert driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).is_displayed()

    @allure.title('Проверка перехода на Ленты Заказов')
    def test_list_orders(self, driver, web_url):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Лист заказов"'):
            base_page.click_list_orders(driver)

        assert driver.current_url == web_url + "feed"

    @allure.title('Проверка ингредиента')
    def test_ingredients_cart(self, driver, web_url):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Клик по ингредиенту'):
            base_page.click_on_ingredients(driver)

        assert driver.find_element(By.XPATH, Locators.INGREDIENT_DETAILS).is_displayed()

    @allure.title('Проверка закрытия модального окна')
    def test_close_modal_window(self, driver, web_url):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Клик по ингредиенту'):
            base_page.click_on_ingredients(driver)
        with allure.step('Клик по кнопке "Закрытие модального окна"'):
            base_page.close_modal_window(driver)

        assert not_visible_element(driver, (By.XPATH, Locators.CALORIES_INGREDIENT))

    @allure.title('Проверка добавления ингредиента в заказ')
    def test_count_ingredients(self, driver, web_url):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Добавление ингредиента в заказ'):
            base_page.add_ingredients(driver)

        assert driver.find_element(By.XPATH, Locators.COUNT_INGREDIENT).text != 0

    @allure.title('Проверка авторизованный пользователь может оформить заказ')
    def test_auth_orders(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            base_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            base_page.authorization(driver, create_user)

        assert driver.find_element(By.XPATH, Locators.CREATE_ORDER_BUTTON).text == "Оформить заказ"
