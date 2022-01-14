import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# або з використання ф-ії pytest_addoption та фікстури request
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name",
#         action="store",
#         # default=None,
#         default="chrome",
#         help="Choose browser: chrome or firefox"
#     )
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     # Логика обработки командной строки.
#     # Для запроса значения параметра мы можем вызвать команду:
#     browser_name = request.config.getoption("--browser_name")
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
