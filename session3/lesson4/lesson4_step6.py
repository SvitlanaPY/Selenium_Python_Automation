"""
Автоиспользование фикстур

При описании фикстуры можно указать дополнительный параметр autouse=True,
который укажет, что фикстуру нужно запустить для каждого теста даже без явного вызова:

test_fixture1_6_autouse.py


import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
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
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


session3_lesson4_step6_fixture1.png

Попробуйте запустить этот код и увидите,
что для каждого теста фикстура подготовки данных выполнилась без явного вызова.
Нужно быть аккуратнее с этим параметром, потому что фикстура выполняется для всех тестов.
Без явной необходимости автоиспользованием фикстур лучше не пользоваться.

Итог:
Вспомогательные функции — это очень мощная штука, которая решает много проблем при работе с автотестами.
Основной плюс в том, что их удобно использовать в любых тестах без дублирования лишнего кода.

Дополнительные материалы про фикстуры, которые мы настоятельно советуем почитать, приведены ниже:
https://habr.com/ru/company/yandex/blog/242795/
https://docs.pytest.org/en/stable/fixture.html

# scope="class":
# фікстура @pytest.fixture(scope="class") викликається ОДИН раз,
# її результат зберігається і використовується для ВСІХ методів класу.
# Якщо буде два класи, то фікстура викликається ДВА рази - по разу на кожен клас.

# scope="function":
# якщо область видимості function, то фікстура @pytest.fixture(scope="function")
# викликається на КОЖНУ функцію / метод.

# scope="module":
# module - це один файл з тестами

# scope="session":
# це один прогон ВСІХ тестів (може бути кілька файлів)

"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
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
