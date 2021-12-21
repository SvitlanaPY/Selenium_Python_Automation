# базовый подход к созданию фикстур, когда тестовые данные задаются и очищаются в setup и teardown методах.
# создание экземпляра браузера и его закрытие только один раз для всех тестов первого тест-сьюта
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:

    @classmethod
    def setup(self):   # def setup_class(self): .... (name should start with setup)
        print("\nstart browser for test suite..")
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        # (открытие браузера)
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown(self):   # def teardown_class(self): .... (name should start with teardown)
        print("quit browser for test suite..")
        # закрываем браузер после всех манипуляций
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    def test_guest_should_see_login_link2(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page2(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# создание экземпляра браузера и его закрытие только ОДИН раз для ВСЕХ тестов тест-сьюта TestMainPage1
# ЗАПУСКАЕМ ТЕСТ В ТЕРМИНАЛЕ СЛЕЖУЮЩЕЙ КОМАНДОЙ:
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson4$ pytest -s -v test_fixture1_1.py
# ============================================== test session starts ============================================
# platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/svitlana/PyTest/environments/selenium_course/session3/lesson4
# collected 4 items
#
# test_fixture1_1.py::TestMainPage1::test_guest_should_see_login_link
# start browser for test suite..
# PASSED
# test_fixture1_1.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page PASSED
# test_fixture1_1.py::TestMainPage1::test_guest_should_see_login_link2 PASSED
# test_fixture1_1.py::TestMainPage1::test_guest_should_see_basket_link_on_the_main_page2 PASSED
# quit browser for test suite..
#
#
# ========================================== 4 passed in 8.22s =================================================
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson4$