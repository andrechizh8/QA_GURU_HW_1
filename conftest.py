import pytest
from selene.support.shared import browser
from selene import by, be, have


@pytest.fixture()
def browser_open():
    browser.config.hold_browser_open = True  # Не закрывать браузер
    browser.config.window_width = 1920  # Выставить ширину окна браузера
    browser.config.window_height = 1080  # Выставить высоту окна браузера
    browser.open("https://google.com").driver.maximize_window()  # Открыть браузер в полноэкранном режиме
    print("Браузер открыт")


@pytest.fixture()
def page_search_1(browser_open):  # Позитивный сценарий
    browser.element(by.name("q")).should(be.blank).type("selene").press_enter()  # Поиск "selene"
    browser.element(by.id("search")).should(
        have.text("User-oriented Web UI browser tests in Python"))  # Страница содержит нужный текст
    return "Страница содержит текст 'User-oriented Web UI browser tests in Python' "


@pytest.fixture()
def page_search_2(browser_open):
    browser.element('[class="gLFyf"]').should(be.blank).type("asdghagsydgkaysgdyla").press_enter()
    browser.element('[class="s6JM6d"]').should(have.text("По запросу asdghagsydgkaysgdyla ничего не найдено. "))
    yield "Страница содержит текст 'По запросу asdghagsydgkaysgdyla ничего не найдено.' "
    browser.quit()
    print('Браузер закрыт')
