import pytest
import requests
from selenium import webdriver

import helpers
from data import Endpoints


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
def web_url():
    return "https://stellarburgers.nomoreparties.site/"


@pytest.fixture
def create_user(web_url):
    data = helpers.RandomUsers().generate_random_data()
    response_post = requests.post(web_url + Endpoints.REGISTER, data=data)
    token = response_post.json()['accessToken']

    headers = {
        "Content-type": "application/json",
        "Authorization": f'{token}'
    }

    yield response_post, data

    requests.delete(web_url + Endpoints.DELETE_USER, headers=headers)
