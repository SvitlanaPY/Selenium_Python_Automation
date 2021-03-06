link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")



# Если мы теперь запустим тесты БЕЗ параметра, то НЕ получим ошибку:
# $ pytest -s -v test_parser.py
# и наши тесты запустятся в браузере Chrome (который задан по умолчанию в conftest.py)
#
# если все же при запуске тестов укажем параметр --browser_name=chrome,
# pytest -s -v --browser_name=chrome test_parser.py
# то наши тесты также запустятся в браузере Chrome.
#
# теперь запустим тесты на firefox (--browser_name=firefox):
# pytest -s -v --browser_name=firefox test_parser.py
# мы должны увидеть, как тесты запустятся в браузере Firefox
