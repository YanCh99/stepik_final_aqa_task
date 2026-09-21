
# Реализовать логику запуска браузера с указанным языком пользователя.
# Добавить фикстуру, которая открывает браузер и передается в тест как параметр.
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Обработчик, который считает из командной строки параметр language
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="choose language: ru, en, es, etc."
    )
# Реализовать логику запуска браузера с указанным языком пользователя.
# Добавить фикстуру, которая открывает браузер и передается в тест как параметр.
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("/nquit browser..")
    browser.quit()
