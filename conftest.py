from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as Optionsf

# для корректного отображения кириллицы в параметризаторах


def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store',
                     default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: '--language=en/ru/es/ko/fr' etc.")

# Запуск браузера(для каждой функции)


# по умолчанию запускается для каждой функции
@pytest.fixture(scope="function")
def browser(request):
    # получаем параметр командной строки browser_name
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        user_language = request.config.getoption("language")
        options = Optionsf()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        # browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
