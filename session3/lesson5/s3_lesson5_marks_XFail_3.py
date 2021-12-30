# Добавим символ x в параметр -r, чтобы получить подробную информацию по XPASS-тестам:
# pytest -v -rx s3_lesson5_marks_XFail_3.py
# Когда баг починят, мы это узнаем, так как теперь,
# наш падавший тест с маркировкой @pytest.mark.xfail(reason="fixing this bug right now")
# будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")   # кнопка есть



# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson5$
# $ pytest -v -rx s3_lesson5_marks_XFail_3.py
# ======================== test session starts ========================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course, configfile: pytest.ini
# collected 3 items
#
# s3_lesson5_marks_XFail_3.py::TestMainPage1::test_guest_should_see_login_link PASSED                                                                               [ 33%]
# s3_lesson5_marks_XFail_3.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page PASSED                                                             [ 66%]
# s3_lesson5_marks_XFail_3.py::TestMainPage1::test_guest_should_see_search_button_on_the_main_page XPASS (fixing this bug right now)                                [100%]
#
#
# ====================== 2 passed, 1 xpassed in 14.22s ======================
