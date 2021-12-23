# параметр autouse=True, укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser_():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:
    def test_guest_should_see_login_link1(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    def test_guest_should_see_login_link2(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson4$
# $ pytest -s -v test_fixture_autouse.py
# ======================== test session starts ==========================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course/session3/lesson4
# collected 4 items
#
# test_fixture_autouse.py::TestMainPage1::test_guest_should_see_login_link1
# preparing some critical data for every test
#
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture_autouse.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page1
# preparing some critical data for every test
#
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture_autouse.py::TestMainPage1::test_guest_should_see_login_link2
# preparing some critical data for every test
#
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture_autouse.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page2
# preparing some critical data for every test
#
# start browser for test..
# PASSED
# quit browser..
#
#
# ============================ 4 passed in 19.42s ============================
