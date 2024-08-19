

import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import wait_for_page_load, should_be_visible_elements, invisible_element

from locators.ui_locators import Locators


@allure.title('Проверка "Ленты Заказов"')
class PageListOrder:
    @allure.step('Открытие браузера')
    def open_browser(self, driver, web_url):
        driver.get(web_url)
        return self

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_list_orders(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.LIST_ORDER_BUTTON)))
        element = driver.find_element(By.XPATH, Locators.LIST_ORDER_BUTTON)
        driver.execute_script("arguments[0].click()", element)
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

    @allure.step('Клик по заказу в "Ленте заказов"')
    def click_order_in_list_orders(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CLICK_ORDER_IN_LIST_ORDER)))
        driver.find_element(By.XPATH, Locators.CLICK_ORDER_IN_LIST_ORDER).click()
        return self

    @allure.step("Получение количества заказов за все время")
    def number_orders_all_time(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.TEXT_COMPLETED_ALL_TIME)))
        element = driver.find_element(By.XPATH, Locators.TEXT_COMPLETED_ALL_TIME)
        return element

    @allure.step("Получение количества заказов за сегодня")
    def number_orders_today(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.TEXT_COMPLETED_TODAY)))
        element = driver.find_element(By.XPATH, Locators.TEXT_COMPLETED_TODAY)
        return element.text

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR_BUTTON)))
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        return self

    @allure.step('Оформление заказа и клик по кнопке "Оформить заказ"')
    def click_create_order(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.BUN_INGREDIENT)))
        element = driver.find_element(By.XPATH, Locators.BUN_INGREDIENT)
        basket = driver.find_element(By.XPATH, Locators.BASKET_ORDER)
        ActionChains(driver).move_to_element(element).click_and_hold().move_to_element(basket).release().perform()
        driver.find_element(By.XPATH, Locators.CREATE_ORDER_BUTTON).click()
        return self

    @allure.step('Закрытие модального окна и получение номера заказа')
    def close_modal_window(self, driver):
        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, Locators.NUMBER_ORDER_INVISIBLE)))
        should_be_visible_elements(driver, (By.CSS_SELECTOR, Locators.TEXT_NUMBER_ORDER_IN_MODAL_WINDOW))
        number_order = driver.find_element(By.CSS_SELECTOR, Locators.TEXT_NUMBER_ORDER_IN_MODAL_WINDOW)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.CLOSE_MODAL_WINDOW_BUTTON)))
        element = driver.find_element(By.XPATH, Locators.CLOSE_MODAL_WINDOW_BUTTON)
        if element.is_displayed():
            driver.execute_script("arguments[0].click()", element)
        return number_order.text

    @allure.step('Проверка количество выполненных заказов за все время')
    def should_be_count_all_time(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.TEXT_COMPLETED_ALL_TIME)))
        element_all_time_count = driver.find_element(By.XPATH, Locators.TEXT_COMPLETED_ALL_TIME)
        return element_all_time_count

    @allure.step('Проверка списка "В процессе" выполненных заказов')
    def should_be_count_today(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.TEXT_COMPLETED_TODAY)))
        element_in_progress = driver.find_element(By.XPATH, Locators.TEXT_COMPLETED_TODAY)
        return element_in_progress.text

    @allure.step('Проверка списка "Готовы" выполненных заказов')
    def should_complete_order_list(self, driver):
        invisible_element(driver, (By.XPATH, Locators.COMLETED_INVISIBLE))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.COMPLETED_ORDER_LIST)))

        element = driver.find_element(By.XPATH, Locators.COMPLETED_ORDER_LIST)
        wait_for_page_load(driver, 10, (By.XPATH, Locators.COMPLETED_ORDER_LIST))
        return element

    @allure.step('Проверка списка выполненных заказов в "Ленте заказов"')
    def should_order_in_order_list(self, driver):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.WINDOW_LIST_ORDER)))

        element = driver.find_element(By.XPATH, Locators.WINDOW_LIST_ORDER)
        wait_for_page_load(driver, 10, (By.XPATH, Locators.WINDOW_LIST_ORDER))
        return element


order_page = PageListOrder()
