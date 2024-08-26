import allure

from locators.account_locators import AccountLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


@allure.title('Проверка "Личный Кабинет"')
class PagePersonalAccount(BasePage):
    @allure.step('Проверка что авторизация прошла успешно')
    def personal_account_check(self):
        self.click_element(AccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке "История заказов"')
    def history_order(self):
        self.click_element(OrderLocators.HISTORY_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Выход"')
    def logout_button(self):
        self.click_element(AccountLocators.LOGOUT_BUTTON)

    @allure.step('Текст кнопки в лк "Выход"')
    def text_logout(self):
        return self.presence_element(AccountLocators.LOGOUT_BUTTON).is_displayed()

    @allure.step('Текст кнопки "Вход"')
    def text_login(self):
        return self.presence_element(AccountLocators.TEXT_LOGIN).is_displayed()
