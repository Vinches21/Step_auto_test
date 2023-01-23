import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= 'en', help="language: --language=en' or '--language=ru'" )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nStart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(executable_path='C:\\Users\\Home\PycharmProjects\\resource\\chromedriver.exe', options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nQuit browser..")
    browser.quit()