import allure

from helpers import RandomUsers
from locators.account_locators import AccountLocators
from locators.recovery_locators import RecoveryLocators
from pages.base_page import BasePage


@allure.title('Проверка "Восстановление пароля"')
class PasswordRecoveryPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def button_recovery(self):
        self.click_element(RecoveryLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Проверка текста "Восстановление пароля"')
    def text_recovery_password(self):
        return self.wait_element_appear(RecoveryLocators.TEXT_RECOVERY).is_displayed()

    @allure.step('Текст кнопки "Сохранить"')
    def text_save(self):
        return self.wait_element_appear(RecoveryLocators.SAVE_BUTTON).is_displayed()

    @allure.step('Ввод email')
    def send_email(self, create_user):
        response_post, data = create_user
        self.send_input(AccountLocators.EMAIL_INPUT, data["email"])

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save(self):
        self.click_element(RecoveryLocators.SAVE_BUTTON)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_button_recovery(self):
        self.click_element(RecoveryLocators.RECOVERY_BUTTON)

    @allure.step('Ввод нового пароля')
    def new_password(self):
        self.send_input(AccountLocators.PASSWORD_INPUT, RandomUsers.generate_random_data().get("password"))

    @allure.step('Клик по кнопке "Показать пароль"')
    def eye_button(self):
        self.click_element(RecoveryLocators.EYE_BUTTON)

    @allure.step('Проверяем активность поля "Пароль"')
    def check_password_field_status(self):
        return self.find_element(RecoveryLocators.PASSWORD_INPUT_ACTIVE)
