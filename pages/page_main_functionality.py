import allure

from data import Urls
from locators.account_locators import AccountLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


@allure.title('Проверка раздела «Лента заказов»')
class PageMainFunctionality(BasePage):
    @allure.step('Авторизация')
    def authorization(self, driver, create_user):
        response_post, data = create_user
        driver.get(Urls.URL_LOGIN)
        self.send_input(AccountLocators.EMAIL_INPUT, data["email"])
        self.send_input(AccountLocators.PASSWORD_INPUT, data["password"])
        self.click_element(AccountLocators.LOGIN_BUTTON)
        self.wait_element_appear(OrderLocators.CREATE_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor(self):
        self.click_element(OrderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_list_orders(self):
        self.click_element(OrderLocators.LIST_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Ингредиенту"')
    def click_on_ingredients(self):
        self.click_element(OrderLocators.BUN_INGREDIENT)

    @allure.step('Клик по кнопке "Закрытие модального окна"')
    def close_modal_window(self):
        self.click_element(OrderLocators.INGRADIENT_CLOSE_BUTTON)

    @allure.step('Дождаться исчезновения деталей заказа')
    def wait_for_order_details_disappear(self):
        self.wait_element_disappear(OrderLocators.INGREDIENT_DETAILS)

    @allure.step('Проверить наличие элемента на экране')
    def check_ingredients_details_on_screen(self):
        return self.presence_element(OrderLocators.INGREDIENT_DETAILS).is_displayed()

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredients(self):
        self.drag_and_drop(self.find_element(OrderLocators.BUN_INGREDIENT),
                           self.find_element(OrderLocators.BASKET_ORDER))

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_order(self):
        self.click_element(OrderLocators.CREATE_ORDER_BUTTON)
