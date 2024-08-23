import allure

from data import Urls
from pages.page_main_functionality import PageMainFunctionality
from pages.page_personal_account import PagePersonalAccount


@allure.suite('Проверка "Личный кабинет"')
class TestPersonalAccount:
    @allure.title('Авторизация и проверка "Личный кабинет"')
    def test_personal_account_check(self, driver, create_user):
        page = PagePersonalAccount(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.personal_account_check()

        assert page.text_logout() == True

    @allure.title('Проверка "История заказов"')
    def test_history_order(self, driver, create_user):
        page = PagePersonalAccount(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.personal_account_check()
        page.history_order()

        assert driver.current_url == Urls.URL_ORDER

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, create_user):
        page = PagePersonalAccount(driver)
        main_page = PageMainFunctionality(driver)
        main_page.authorization(driver, create_user)
        page.personal_account_check()
        page.logout_button()

        assert page.text_login() == True
