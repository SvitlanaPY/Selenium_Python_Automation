# $ pytest -v -s s3_lesson6_param_1_2.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        print(f"!!! test_guest_should_see_navbar_element: {language}!!!")
    #     # этот тест тоже запустится дважды



# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson6$
# $ pytest -v -s s3_lesson6_param_1_2.py
# ======================= test session starts =======================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course, configfile: pytest.ini
# collected 4 items
#
# s3_lesson6_param_1_2.py::TestLogin::test_guest_should_see_login_link[ru]
# start browser for test..
# PASSED
# quit browser..
#
# s3_lesson6_param_1_2.py::TestLogin::test_guest_should_see_login_link[en-gb]
# start browser for test..
# PASSED
# quit browser..
#
# s3_lesson6_param_1_2.py::TestLogin::test_guest_should_see_navbar_element[ru]
# start browser for test..
# !!! test_guest_should_see_navbar_element: ru!!!
# PASSED
# quit browser..
#
# s3_lesson6_param_1_2.py::TestLogin::test_guest_should_see_navbar_element[en-gb]
# start browser for test..
# !!! test_guest_should_see_navbar_element: en-gb!!!
# PASSED
# quit browser..
#
#
# =================== 4 passed in 12.90s =====================
