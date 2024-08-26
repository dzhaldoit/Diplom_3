import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем браузер')
    def open(self, url):
        return self.driver.get(url)

    @allure.step('Собираем текущий урл')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Проверяем присутсвие элемента')
    def presence_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Проверяем видимость элемента')
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Дожидаемся появления элемента')
    def wait_element_appear(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step('Дождаться пропажи элемента')
    def wait_element_disappear(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element(locator))

    @allure.step('Собираем текст с элемента')
    def get_text(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).text

    @allure.step('Ожидаем элемент и вводим данные')
    def send_input(self, locator, data, time=15):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).send_keys(data)

    @allure.step('Клик по элементу')
    def click_element(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Перенос элемента')
    def drag_and_drop(self, element, target):
        return ActionChains(self.driver).drag_and_drop(element, target).perform()
