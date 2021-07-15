import time

import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    # Initializing the Chrome browser
    driver = webdriver.Chrome()

    # Maximizing the browser window and hitting the target Url
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    # Assigning local driver to the class driver so that we use this local driver in the desired class also
    request.cls.driver = driver

    yield

    time.sleep(2)
    driver.quit()