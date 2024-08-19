import time

import allure
from selenium.webdriver.common.by import By

from helpers import should_be_visible_elements
from pages.page_list_order import order_page
from locators.ui_locators import Locators


@allure.suite('Проверка раздела "Ленты заказов"')
class TestListOrder:
    @allure.title('Проверка списка заказов')
    def test_list_orders(self, driver, web_url):
        with allure.step('Открытие браузера'):
            order_page.open_browser(driver, web_url)
        with allure.step('Клик по кнопке "Лента Заказов"'):
            order_page.click_list_orders(driver)
        with allure.step('Клик по заказу в списке "Лента Заказов"'):
            order_page.click_order_in_list_orders(driver)

        assert should_be_visible_elements(driver, (By.XPATH, Locators.ORDER_IN_LIST_ORDERS))

    @allure.title('Проверка заказа пользователя')
    def test_order_user(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            order_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            order_page.authorization(driver, create_user)
        with allure.step('Клик по кнопке "Оформить заказ"'):
            order_page.click_create_order(driver)
        with allure.step('Закрытие модального окна'):
            time.sleep(3) # Тут поставил слип потому что тест иногда не ждет когда исчезнет номер
            number_user_order = order_page.close_modal_window(driver)
        with allure.step('Переход в "Лента Заказов"'):
            order_page.click_list_orders(driver)

        assert '#0' + number_user_order in order_page.should_order_in_order_list(driver).text

    @allure.title('Проверка количества заказов за все время')
    def test_count_orders_all_time(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            order_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            order_page.authorization(driver, create_user)
        with allure.step('Клик по кнопке "Лента Заказов"'):
            order_page.click_list_orders(driver)
        with allure.step('Проверка списка выполненных заказов'):
            order_page.should_be_count_all_time(driver)
        with allure.step('Клик по кнопке "Конструктор"'):
            order_page.click_constructor(driver)
        with allure.step('Клик по кнопке "Оформить заказ"'):
            order_page.click_create_order(driver)
            time.sleep(5)
        with allure.step('Закрытие модального окна и получение номера заказа'):
            number_user_order = order_page.close_modal_window(driver)
        with allure.step('Переход в "Лента Заказов"'):
            order_page.click_list_orders(driver)

        assert number_user_order <= order_page.should_be_count_all_time(driver).text

    @allure.title('Проверка количества заказов за сегодня')
    def test_count_orders_today(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            order_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            order_page.authorization(driver, create_user)
        with allure.step('Клик по кнопке "Лента Заказов"'):
            order_page.click_list_orders(driver)
        with allure.step('Просматриваем количества заказов за сегодня'):
            previous_value = order_page.should_be_count_today(driver)
        with allure.step('Клик по кнопке "Конструктор"'):
            order_page.click_constructor(driver)
        with allure.step('Клик по кнопке "Оформить заказ"'):
            order_page.click_create_order(driver)
        with allure.step("Закрытие модального окна"):
            order_page.close_modal_window(driver)
        with allure.step('Переход в "Лента Заказов"'):
            order_page.click_list_orders(driver)
        with allure.step('Просматриваем количества заказов за сегодня'):
            current_value = order_page.should_be_count_today(driver)

        assert int(previous_value) < int(current_value)

    @allure.title('Проверка "В процессе" заказа')
    def test_order_in_progress(self, driver, web_url, create_user):
        with allure.step('Открытие браузера'):
            order_page.open_browser(driver, web_url)
        with allure.step('Авторизация'):
            order_page.authorization(driver, create_user)
        with allure.step('Клик по кнопке "Оформить заказ"'):
            order_page.click_create_order(driver)
        with allure.step('Закрытие модального окна и получение номера заказа'):
            number_user_order = order_page.close_modal_window(driver)
        with allure.step('Переход в "Лента Заказов"'):
            order_page.click_list_orders(driver)
        with allure.step('Проверка заказа "В процессе"'):
            element = order_page.should_complete_order_list(driver)

        assert '0' + number_user_order in element.text
