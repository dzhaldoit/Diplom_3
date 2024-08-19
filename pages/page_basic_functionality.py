import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators.ui_locators import Locators


@allure.title('Проверка раздела «Лента заказов»')
class PageBasicFunctionality:
    @allure.step('Открытие браузера')
    def open_browser(self, driver, web_url):
        driver.get(web_url)
        return self

    @allure.step('Авторизация')
    def authorization(self, driver, create_user):
        response_post, data = create_user
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, Locators.EMAIL_INPUT).send_keys(data["email"])
        driver.find_element(By.XPATH, Locators.PASSWORD_INPUT).send_keys(data["password"])
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)))
        return self

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR_BUTTON)))
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        return self

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_list_orders(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.LIST_ORDER_BUTTON)))
        driver.find_element(By.XPATH, Locators.LIST_ORDER_BUTTON).click()
        return self

    @allure.step('Клик по кнопке "Ингредиенту"')
    def click_on_ingredients(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.BUN_INGREDIENT)))
        driver.find_element(By.XPATH, Locators.BUN_INGREDIENT).click()
        return self

    @allure.step('Клик по кнопке "Закрытие модального окна"')
    def close_modal_window(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CLOSE_MODAL_WINDOW_BUTTON)))
        element = driver.find_element(By.XPATH, Locators.CLOSE_MODAL_WINDOW_BUTTON)
        element.click()
        return self

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredients(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.BUN_INGREDIENT)))
        element = driver.find_element(By.XPATH, Locators.BUN_INGREDIENT)
        basket = driver.find_element(By.XPATH, Locators.BASKET_ORDER)
        ActionChains(driver).move_to_element(element).click_and_hold().move_to_element(basket).release().perform()
        return self

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_create_order(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CREATE_ORDER_BUTTON)))
        driver.find_element(By.XPATH, Locators.CREATE_ORDER_BUTTON).click()
        return self


base_page = PageBasicFunctionality()
