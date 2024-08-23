import pytest
import requests
from selenium import webdriver

import helpers
from data import Endpoints, Urls


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError(f"Скорее всего вы передали неверное имя браузера: {request.param}")

    yield driver

    driver.quit()


@pytest.fixture
def create_user():
    data = helpers.RandomUsers().generate_random_data()
    response_post = requests.post(Urls.URL_HOME + Endpoints.REGISTER, data=data)
    token = response_post.json()['accessToken']

    headers = {
        "Content-type": "application/json",
        "Authorization": f'{token}'
    }

    yield response_post, data

    requests.delete(Urls.URL_HOME + Endpoints.DELETE_USER, headers=headers)
