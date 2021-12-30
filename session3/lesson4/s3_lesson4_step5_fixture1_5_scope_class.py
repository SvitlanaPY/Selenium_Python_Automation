# scope="class":
# фікстура @pytest.fixture(scope="class") викликається ОДИН раз,
# її результат зберігається і використовується для ВСІХ методів класу.
# Якщо буде два класи, то фікстура викликається ДВА рази - по разу на кожен клас

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link1(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page1(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

    def test_guest_should_see_login_link2(self, browser):
        print("start test3")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test3")

    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        print("start test4")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test4")


# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson4$
# $ pytest -v -s s3_lesson4_step5_fixture1_5_scope_class.py
#
# ============================ test session starts ==========================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course/session3/lesson4
# collected 4 items
#
# s3_lesson4_step5_fixture1_5_scope_class.py::TestMainPage1::test_guest_should_see_login_link1
# start browser for test..
#
# start test1
# finish test1
# PASSED
#
# s3_lesson4_step5_fixture1_5_scope_class.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page1
# start test2
# finish test2
# PASSED
#
# s3_lesson4_step5_fixture1_5_scope_class.py::TestMainPage1::test_guest_should_see_login_link2
# start test3
# finish test3
# PASSED
#
# s3_lesson4_step5_fixture1_5_scope_class.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page2
# start test4
# finish test4
# PASSED
#
# quit browser..
#
#
# =================== 4 passed in 8.05s ====================
#