import allure

from data import Urls
from pages.page_password_recovery import PasswordRecoveryPage


@allure.suite('Восстановление пароля')
class TestRecoveryUsers:
    @allure.title('Тест кнопки "Восстановить пароль"')
    def test_recovery_button(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open(Urls.URL_LOGIN)
        page.button_recovery()

        assert page.text_recovery_password() == True

    @allure.title('Тест кнопки "Сохранить"')
    def test_send_email_and_click_button(self, driver, create_user):
        page = PasswordRecoveryPage(driver)
        page.open(Urls.URL_LOGIN)
        page.button_recovery()
        page.send_email(create_user)
        page.click_button_recovery()

        assert page.text_save() == True

    @allure.title('Новый пароль')
    def test_new_password(self, driver, create_user):
        page = PasswordRecoveryPage(driver)
        page.open(Urls.URL_LOGIN)
        page.button_recovery()
        page.send_email(create_user)
        page.click_button_recovery()
        page.new_password()
        page.eye_button()

        assert page.check_password_field_status()
