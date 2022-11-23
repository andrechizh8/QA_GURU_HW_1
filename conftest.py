import pytest
from selene.support.shared import browser
from selene import by, be, have


@pytest.fixture()
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://google.com").driver.maximize_window()




