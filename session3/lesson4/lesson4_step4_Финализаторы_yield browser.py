"""
Финализаторы — закрываем браузер.

Вероятно, вы заметили, что мы не использовали в этом примере команду browser.quit().
Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов,
а закрылись только после завершения всех тестов.
Закрытие браузеров произошло благодаря встроенной фикстуре — сборщику мусора.
Но если бы количество тестов насчитывало больше нескольких десятков, то открытые окна браузеров могли привести к тому,
что оперативная память закончилась бы очень быстро.
Поэтому надо явно закрывать браузеры после каждого теста.

Для этого мы можем воспользоваться финализаторами.
Один из вариантов финализатора — использование ключевого слова Python: yield.

После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки,
следующей за строкой со словом yield:

s3_lesson4_step4__fixture1_4.py

import pytest
from selenium import webdriver

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
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer.
Можете изучить его сами по документации PyTest:
https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly.

Рекомендуем также выносить очистку данных и памяти в фикстуру, вместо того чтобы писать это в шагах теста:
финализатор выполнится даже в ситуации, когда тест упал с ошибкой.

"""