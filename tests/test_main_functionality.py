import allure

from data import Urls
from locators.order_locators import OrderLocators
from pages.page_main_functionality import PageMainFunctionality


@allure.suite('Проверка основного функционала')
class TestBasicFunctionality:
    @allure.title('Проверка Конструктора')
    def test_constructor(self, driver):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_LIST_ORDER)
        page.click_on_constructor()

        assert page.get_url() == Urls.URL_HOME

    @allure.title('Проверка перехода на Ленты Заказов')
    def test_list_orders(self, driver):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_HOME)
        page.click_list_orders()

        assert page.get_url() == Urls.URL_LIST_ORDER

    @allure.title('Проверка ингредиента')
    def test_ingredients_cart(self, driver):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_HOME)
        page.click_on_ingredients()

        assert page.get_text(OrderLocators.INGREDIENT_DETAILS) == 'Детали ингредиента'

    @allure.title('Проверка закрытия модального окна')
    def test_close_modal_window(self, driver):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_HOME)
        page.click_on_ingredients()
        page.close_modal_window()
        page.wait_for_order_details_disappear()

        assert page.check_ingredients_details_on_screen() == False

    @allure.title('Проверка добавления ингредиента в заказ')
    def test_count_ingredients(self, driver):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_HOME)
        page.add_ingredients()

        assert page.get_text(OrderLocators.COUNT_INGREDIENT) == "2"

    @allure.title('Проверка авторизованный пользователь может оформить заказ')
    def test_auth_orders(self, driver, create_user):
        page = PageMainFunctionality(driver)
        page.open(Urls.URL_LOGIN)
        page.authorization(driver, create_user)

        assert page.get_text(OrderLocators.CREATE_ORDER_BUTTON) == "Оформить заказ"
