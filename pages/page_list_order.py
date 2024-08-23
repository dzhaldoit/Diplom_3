import time

import allure

from locators.order_locators import OrderLocators
from pages.base_page import BasePage


@allure.title('Проверка "Ленты Заказов"')
class PageListOrder(BasePage):
    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_list_orders(self):
        self.wait_element_appear(OrderLocators.LIST_ORDER_BUTTON)
        self.click_element(OrderLocators.LIST_ORDER_BUTTON)

    @allure.step('Клик по заказу в "Ленте заказов"')
    def click_order_in_list_orders(self):
        self.click_element(OrderLocators.CLICK_ORDER_IN_LIST_ORDER)

    @allure.step('Проверить заказа в "Ленте заказов"')
    def check_order_on_screen(self):
        return self.presence_element(OrderLocators.ORDER_IN_LIST_ORDERS).is_displayed()

    @allure.step("Получение количества заказов за все время")
    def number_orders_all_time(self):
        self.get_text(OrderLocators.TEXT_COMPLETED_ALL_TIME)

    @allure.step("Получение количества заказов за сегодня")
    def number_orders_today(self):
        self.get_text(OrderLocators.TEXT_COMPLETED_TODAY)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor(self):
        self.click_element(OrderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_order(self):
        self.click_element(OrderLocators.CREATE_ORDER_BUTTON)
        time.sleep(2)

    def number_order(self):
        self.wait_element_disappear(OrderLocators.NUMBER_ORDER_INVISIBLE)
        return self.get_text(OrderLocators.TEXT_NUMBER_ORDER_IN_MODAL_WINDOW)

    @allure.step('Закрытие модального окна и получение номера заказа')
    def close_modal_window(self):
        self.wait_element_appear(OrderLocators.CLOSE_MODAL_WINDOW_BUTTON)
        self.click_element(OrderLocators.CLOSE_MODAL_WINDOW_BUTTON)
        self.wait_element_disappear(OrderLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Проверка количество выполненных заказов за все время')
    def should_be_count_all_time(self):
        self.get_text(OrderLocators.TEXT_COMPLETED_ALL_TIME)

    @allure.step('Проверка списка "В процессе" выполненных заказов')
    def should_be_count_today(self):
        return self.get_text(OrderLocators.TEXT_COMPLETED_TODAY)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredients(self):
        self.drag_and_drop(self.find_element(OrderLocators.BUN_INGREDIENT),
                           self.find_element(OrderLocators.BASKET_ORDER))

    @allure.step('Проверка списка "Готовы" выполненных заказов')
    def should_complete_order_list(self):
        self.wait_element_disappear(OrderLocators.COMLETED_INVISIBLE)
        self.wait_element_appear(OrderLocators.COMPLETED_ORDER_LIST)
        return self.get_text(OrderLocators.COMPLETED_ORDER_LIST)

    @allure.step('Проверка списка выполненных заказов в "Ленте заказов"')
    def should_order_in_order_list(self):
        self.wait_element_appear(OrderLocators.WINDOW_LIST_ORDER)
        return self.get_text(OrderLocators.WINDOW_LIST_ORDER)
