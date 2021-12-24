# @pytest.mark.skip - метка, которая позволяет пропустить тест при сборе тестов для запуска
# (то есть не запускать тест) или запустить, но отметить особенным статусом тот тест,
# который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов.
# Эта метка не требует дополнительного объявления в pytest.ini.

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

    @pytest.mark.skip
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


# (venv) svitlana@svitlana-HP-ProBook-455-G1:~/Projects/Automation-Testing-Course/session3/lesson5$
# $ pytest -v -s lesson5_marks_Skipped.py
# ======================== test session starts ==========================
# platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/svitlana/Projects/Automation-Testing-Course/venv/bin/python
# cachedir: .pytest_cache
# rootdir: /home/svitlana/Projects/Automation-Testing-Course, configfile: pytest.ini
# collected 4 items
#
# lesson5_marks_Skipped.py::TestMainPage1::test_guest_should_see_login_link1 SKIPPED (unconditional skip)
# lesson5_marks_Skipped.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page1
# start browser for test..
# PASSED
# quit browser..
#
# lesson5_marks_Skipped.py::TestMainPage1::test_guest_should_see_login_link2
# start browser for test..
# PASSED
# quit browser..
#
# lesson5_marks_Skipped.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page2
# start browser for test..
# PASSED
# quit browser..
#
#
# =================== 3 passed, 1 skipped in 21.48s =====================
