link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


# Если вы теперь запустите тесты без параметра, то получите ошибку:
# $ pytest -s -v test_parser.py
# ERROR test_parser.py::test_guest_should_see_login_link - _pytest.config.exceptions.UsageError: --browser_name should be chrome or firefox


# Если в conftest.py задать значение параметра по умолчанию,
# чтобы в командной строке не обязательно было указывать параметр --browser_name,
# например, так:
# parser.addoption('--browser_name', action='store', default="chrome",
#                  help="Choose browser: chrome or firefox")
#
#
# И теперь при запуске тестов НЕ укажем параметр --browser_name:
# pytest -s -v test_parser.py
# то увидим увидеть, как тесты запустятся в браузере Chrome
#
# Но если теперь при запуске тестов укажем параметр --browser_name,
# сначала укажем firefox: --browser_name=firefox:
# pytest -s -v --browser_name=firefox test_parser.py
# должны увидеть, как тесты запустятся в браузере Firefox

# А теперь запустим тесты на Chrome, но укажем браузер Chrome в параметре: --browser_name=chrome:
# pytest -s -v --browser_name=chrome test_parser.py
# должны увидеть, как тесты запустятся в браузере Chrome.
