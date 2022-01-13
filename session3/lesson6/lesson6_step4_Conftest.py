"""
Conftest.py — конфигурация тестов

Ранее мы добавили фикстуру browser, которая создает нам экземпляр браузера для тестов в данном файле.
Когда файлов с тестами становится больше одного, приходится в каждом файле с тестами описывать данную фикстуру.
Это очень неудобно.
Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл conftest.py,
который должен лежать в директории верхнего уровня в вашем проекте с тестами.

Можно создавать дополнительные файлы conftest.py в других директориях,
но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.

Создадим файл conftest.py в корневом каталоге нашего тестового проекта и перенесем туда фикстуру browser.
Заметьте, насколько лаконичнее стал выглядеть файл с тестами.

conftest.py:

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser.
Фикстура передается в тестовый метод в качестве аргумента.
Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.

test_conftest.py:

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

ОЧЕНЬ ВАЖНО! 
Есть одна важная особенность поведения конфигурационных файлов, о которой вы обязательно должны знать.
PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами.

Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите,
чтобы не возникало ситуации, когда вы запускаете тесты из папки tests:

tests/
├── conftest.py
├── subfolder
│   └── conftest.py
│   └── test_abs.py

следует избегать!

В таком случае применяется ОБА файла conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.  

Таким образом можно переопределять разные фикстуры,
но мы в рамках курса рекомендуем придерживаться одного файла на проект/задачу и держать их горизонтально, как-нибудь так:

selenium_course_solutions/
├── section3
│   └── conftest.py
│   └── test_languages.py
├── section4 
│   └── conftest.py
│   └── test_main_page.py

правильно!

Будьте внимательны и следите, чтобы не было разных conftest во вложенных друг в друга директориях,
особенно, когда будете скачивать и проверять задания сокурсников.
"""