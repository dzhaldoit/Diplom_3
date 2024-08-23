import allure

from data import Urls
from pages.page_list_order import PageListOrder
from pages.page_main_functionality import PageMainFunctionality


@allure.suite('Проверка раздела "Ленты заказов"')
class TestListOrder:
    @allure.title('Проверка списка заказов')
    def test_list_orders(self, driver):
        page = PageListOrder(driver)
        page.open(Urls.URL_LIST_ORDER)
        page.click_order_in_list_orders()

        assert page.check_order_on_screen() == True

    @allure.title('Проверка заказа пользователя')
    def test_order_user(self, driver, create_user):
        page = PageListOrder(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.add_ingredients()
        page.click_create_order()
        number_user_order = page.number_order()
        page.close_modal_window()
        page.click_list_orders()

        assert '#0' + number_user_order in page.should_order_in_order_list()

    @allure.title('Проверка количества заказов за все время')
    def test_count_orders_all_time(self, driver, create_user):
        page = PageListOrder(driver)
        main_page = PageMainFunctionality(driver)
        page.open(Urls.URL_LIST_ORDER)
        main_page.authorization(driver, create_user)
        page.click_list_orders()
        all_time_order = page.should_be_count_all_time()
        page.click_constructor()
        page.add_ingredients()
        page.click_create_order()
        number_user_order = page.number_order()
        page.close_modal_window()

        assert str(number_user_order) <= str(all_time_order)

    @allure.title('Проверка количества заказов за сегодня')
    def test_count_orders_today(self, driver, create_user):
        page = PageListOrder(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.click_list_orders()
        previous_value = page.should_be_count_today()
        page.click_constructor()
        page.add_ingredients()
        page.click_create_order()
        page.close_modal_window()
        page.click_list_orders()
        current_value = page.should_be_count_today()

        assert int(previous_value) < int(current_value)

    @allure.title('Проверка "В процессе" заказа')
    def test_order_in_progress(self, driver, create_user):
        page = PageListOrder(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.add_ingredients()
        page.click_create_order()
        page.close_modal_window()
        number_user_order = page.number_order()
        page.click_list_orders()
        element = page.should_complete_order_list()

        assert '0' + number_user_order in element
