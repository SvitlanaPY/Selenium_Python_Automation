link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")



# Если вы запустите тесты без параметра, то получите ОШИБКУ:
# $ pytest -s -v test_parser.py
# ERROR test_parser.py::test_guest_should_see_login_link - _pytest.config.exceptions.UsageError: --browser_name should be chrome or firefox
#
#
# Запустим тесты на Firefox.
# Для етого при запуске тестов нужно указать параметр --browser_name=firefox,
# pytest -s -v --browser_name=firefox test_parser.py
# и мы должны увидеть, как тесты запустятся в браузере Firefox
#
# А теперь запустим тесты на Chrome.
# Для етого при запуске тестов нужно указать параметр --browser_name=chrome:
# pytest -s -v --browser_name=chrome test_parser.py
# мы должны увидеть, как тесты запустятся в браузере Chrome.
