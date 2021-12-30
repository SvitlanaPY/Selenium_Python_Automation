# $pytest -v -s -m smoke <file name>.py   - run tests with 'smoke' mark
# $pytest -v -s -m regression <file name>.py   - run tests with 'regression' mark

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    def test_guest_should_see_login_link1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    def test_guest_should_see_login_link2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# $pytest -v -s -m smoke <file name>.py   - run tests with 'smoke' mark
# $pytest -v -s -m regression <file name>.py   - run tests with 'regression' mark
