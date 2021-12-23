# создадим фикстуру browser, которая будет создавать объект WebDriver.
# Этот объект мы можем использовать в тестах для взаимодействия с браузером.
# Для этого мы напишем метод browser и укажем, что он является фикстурой с помощью декоратора @pytest.fixture.
# После этого мы можем вызывать фикстуру в тестах, передав ее как параметр.
#
# По умолчанию фикстура будет создаваться для каждого тестового метода,
# то есть для каждого теста запустится свой экземпляр браузера.

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser_():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link1(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    def test_guest_should_see_login_link2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
