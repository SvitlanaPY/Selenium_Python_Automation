# Надо явно закрывать браузеры после каждого теста
#
# Для этого мы можем воспользоваться финализаторами.
# Один из вариантов финализатора — использование ключевого слова Python: yield.
# После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки,
# следующей за строкой со словом yield

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    def test_guest_should_see_login_link2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")



# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson4$ pytest -s -v test_fixture1_4.py
# ============= test session starts =========================
# platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/svitlana/PyTest/environments/selenium_course/session3/lesson4
# collected 4 items
#
# test_fixture1_4.py::TestMainPage1::test_guest_should_see_login_link1
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture1_4.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page1
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture1_4.py::TestMainPage1::test_guest_should_see_login_link2
# start browser for test..
# PASSED
# quit browser..
#
# test_fixture1_4.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page2
# start browser for test..
# PASSED
# quit browser..
#
#
# ========= 4 passed in 22.99s ================
#