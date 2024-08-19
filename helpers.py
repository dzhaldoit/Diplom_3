import random
import string

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RandomUsers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_data():
        email = RandomUsers.generate_random_string(5) + "@gmail.com"
        password = RandomUsers.generate_random_string(10)
        name = RandomUsers.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name}

        return payload


def js_click(driver, element):
    element = driver.find_element(element)
    driver.execute_script("arguments[0].click();", element)


def should_be_visible_elements(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        return True
    except TimeoutException:
        return False


def not_visible_element(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(EC.invisibility_of_element(locator))
        return True
    except TimeoutException:
        return False


def invisible_element(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    except TimeoutException:
        print(f"Элемент {locator} не стал невидимым в течение {timeout} секунд")


def wait_for_page_load(driver, timeout=10, element=None):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(element))
