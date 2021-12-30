# базовый подход к созданию фикстур, когда тестовые данные задаются и очищаются в setup и teardown методах.
# создание экземпляра браузера и его закрытие для каждого теста
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage2:

    def setup_method(self):    # def setup(self): .... (name should start with setup)
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):   # def teardown(self): .... (name should start with teardown)
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link1(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link1")

    def test_guest_should_see_basket_link_on_the_main_page1(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    def test_guest_should_see_login_link2(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link2")

    def test_guest_should_see_basket_link_on_the_main_page2(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# создание экземпляра браузера и его закрытие для КАЖДОГО теста
# ЗАПУСКАЕМ ТЕСТ В ТЕРМИНАЛЕ СЛЕЖУЮЩЕЙ КОМАНДОЙ:
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson4$ pytest -s -v s3_lesson4_step2_fixture1_2.py
# ======================================= test session starts ===============================================
# platform linux -- Python 3.8.10, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# rootdir: /home/svitlana/PyTest/environments/selenium_course/session3/lesson4
# collected 4 items
#
# s3_lesson4_step2_fixture1_2.py::TestMainPage2::test_guest_should_see_login_link1
# start browser for test..
# PASSED
# quit browser for test..
#
# s3_lesson4_step2_fixture1_2.py::TestMainPage2::test_guest_should_see_basket_link_on_the_main_page1
# start browser for test..
# PASSED
# quit browser for test..
#
# s3_lesson4_step2_fixture1_2.py::TestMainPage2::test_guest_should_see_login_link2
# start browser for test..
# PASSED
# quit browser for test..
#
# s3_lesson4_step2_fixture1_2.py::TestMainPage2::test_guest_should_see_basket_link_on_the_main_page2
# start browser for test..
# PASSED
# quit browser for test..
#
#
# ================================== 4 passed in 20.42s ============================================
# svitlana@svitlana-HP-ProBook-455-G1:~/PyTest/environments/selenium_course/session3/lesson4$





